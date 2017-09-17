from django.db import models


# A question and answer pair
class QAPairEntry(models.Model):
    question = models.IntegerField()
    answer = models.IntegerField()

    def __str__(self):
        return "Q: " + str(self.question) + "\t" + "A: " + str(self.answer)

    class Meta:
        verbose_name = "QA Pair Entry"
        verbose_name_plural = "QA Pairs"


# A translator entry to translate key to value
class TranslatorEntry(models.Model):
    key = models.IntegerField()
    value = models.CharField(max_length=1000)

    def __str__(self):
        return "Key: " + str(self.key) + "\t" + "Value: " + str(self.value)

    class Meta:
        verbose_name = "Translator Entry"
        verbose_name_plural = "Translator Entries"

# A list of classes who participated
class Class(models.Model):
    classKey = models.CharField(max_length=5)
    verboseName = models.CharField(max_length=1000)

    def __str__(self):
        return "Key: " + str(self.classKey) + "\t" + "Name: " + str(self.verboseName)

    class Meta:
        verbose_name = "Locked class"
        verbose_name_plural = "Locked classes"

# A list of keys who participated
class ExpiredKey(models.Model):
    key = models.CharField(max_length=8)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Expired key"
        verbose_name_plural = "Expired keys"
