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

    def getDictionaryKey(self, searchString):
        try:
            return TranslatorEntry.objects.filter(value=searchString).values_list("key", flat=True)[0]
        except IndexError:
            return 0


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
        result = self.clf.predict(self.databaseHandler.getDictionaryKey(question))
        return self.databaseHandler.getTranslation(result)


