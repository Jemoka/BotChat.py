# Natural Language Library

# Keep_Alive
import time

time.sleep(1)
# Numpy
import numpy as np

# Sklearn ML Libraries
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import tree
import sklearn.svm as svm
import sklearn.ensemble as ensemble

# Django modding libraries
from Chat.models import QAPairEntry, TranslatorEntry

# Classifiers
# clf = ensemble.RandomForestClassifier()
# clf = GaussianNB()
# clf = tree.DecisionTreeClassifier()
clf = svm.SVC()


# Module backend

def getResponceTranslation(searchKey):
    return TranslatorEntry.objects.filter(key=searchKey).values_list("value", flat=True)[0]


def getQuestionKey(searchString):
    return TranslatorEntry.objects.filter(key=searchString).values_list("key", flat=True)[0]


# HTML-Accessible Functions (see tag.py)
def trainCLF():
    try:
        clf.fit(list(QAPairEntry.objects.values_list('question', flat=True)), list(QAPairEntry.objects.values_list('answer', flat=True).ravel()))
    except ValueError:
        temp_q = list(QAPairEntry.objects.values_list('question', flat=True)).reshape(-1, 1)
        temp_a = list(QAPairEntry.objects.values_list('answer', flat=True)).reshape(-1, 1)
        clf.fit(temp_q, temp_a.ravel())


def predictAnswer(question_entry):
    result = clf.predict(getQuestionKey(question_entry))
    return getResponceTranslation(result)


def storeQAPair(question_entry, answer_entry):
    entry = QAPairEntry(question=question_entry, answer=answer_entry)
    entry.save()


def keep_alive():
    time.sleep(5)

if __name__ == '__main__':
    while True:
        try:
            keep_alive()
        except Exception as err:
            print(err)
            pass


