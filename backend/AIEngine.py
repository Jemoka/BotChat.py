# Natural Language Library, created by Houjun "Jack" Liu

# Numpy
import numpy as np

# Sklearn ML Libraries
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Django model libraries
from backend.models import QAPairEntry, TranslatorEntry
from django.db.models import Max
from django.db.models import Q

class DatabaseModule():
    def storeQAPair(self, question_entry, answer_entry):
        maxvalue = TranslatorEntry.objects.all().aggregate(Max('key'))['key__max']
        question_translation = TranslatorEntry(key=maxvalue+1, value=question_entry)
        question_translation.save()
        answer_translation = TranslatorEntry(key=maxvalue+2, value=answer_entry)
        answer_translation.save()
        entry = QAPairEntry(question=maxvalue+1, answer=maxvalue+2)
        entry.save()

    def getTranslation(self, searchKey):
        return TranslatorEntry.objects.filter(key=searchKey).values_list("value", flat=True)[0]

    def levenshtein(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1       # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def getDictionaryKey(self, searchString):
        print("Looking up user's question ",searchString)
        try:
            qset = Q()
            for term in searchString.split():
                qset |= Q(value__contains=term)
            query = list(TranslatorEntry.objects.filter(qset).values_list("value", flat=True))
            print("possible matches for: "+searchString, ": ", query)
            distances = []
            for i in query:
                distance = self.levenshtein(searchString, i)
                print("distance: "+str(distance))
                distances.append(distance)
            smallest = {}
            counter = -1
            for i in distances:
                counter += 1
                try:
                    if i<=10:
                        if smallest["value"] > i:
                            smallest["value"] = i
                            smallest["key"] = counter
                except:
                    if i<=10:
                        smallest["value"] = i
                        smallest["key"] = counter

            print("Using '"+TranslatorEntry.objects.filter(qset).values_list("value", flat=True)[smallest["key"]], "' to predict")
            return TranslatorEntry.objects.filter(qset).values_list("key", flat=True)[smallest["key"]]
        except KeyError:
            print("Match/near-match not found, giving up...")
            return 'NOT_FOUNT_DRES'


class AIEngine():
    def __init__(self, type):
        self.databaseHandler = DatabaseModule()
        if type == "SVM":
            self.clf = SVC()
        elif type == "GNB":
            self.clf = GaussianNB()
        elif type == "DTC":
            self.clf = DecisionTreeClassifier()
        elif type == "RFC":
            self.clf = RandomForestClassifier()
        else:
            self.clf = SVC()

        try:
            questionlist = np.asarray(list(QAPairEntry.objects.values_list('question', flat=True)))
            answerlist = np.asarray(list(QAPairEntry.objects.values_list('answer', flat=True)))
            self.clf.fit(questionlist, answerlist)
        except ValueError:
            temp_questionlist = np.asarray(list(QAPairEntry.objects.values_list('question', flat=True))).reshape(-1, 1)
            temp_answerlist = np.asarray(list(QAPairEntry.objects.values_list('answer', flat=True))).reshape(-1, 1)
            self.clf.fit(temp_questionlist, temp_answerlist)

    def predictAnswer(self, question):
        translation = self.databaseHandler.getDictionaryKey(question)
        if translation == 'NOT_FOUNT_DRES':
            return "NOT_FOUNT_DRES"
        result = self.clf.predict(translation)
        return self.databaseHandler.getTranslation(result)


