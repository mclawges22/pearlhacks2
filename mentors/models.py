from django.db import models

# Create your models here.

class Skill(models.Model):
	name = models.TextField()
	description = models.TextField()

	def __unicode__(self):
		return U'%s %s' %(self.name, self.description)

class Mentor(models.Model):
    nameFirst = models.TextField()
    nameLast = models.TextField()
    company = models.TextField()
    companyUrl = models.TextField()
    companyImgUrl = models.TextField()
    email = models.TextField()
    twitter = models.TextField()
    linkedIn = models.TextField()
    gitHub = models.TextField()
    website = models.TextField()
    linkOther = models.TextField()
    skills = models.ManyToManyField(Skill)
    skillsOther = models.TextField()
    language = models.TextField()
    languageUrl = models.TextField()
    almaMater = models.TextField()
    photoUrl = models.TextField()
    color = models.TextField()
    hexCode = models.TextField()
    highlight = models.TextField()
    allWomen = models.TextField()
    afraid = models.TextField()
    proud = models.TextField()
    about = models.TextField()
    hobbies = models.TextField()
    techTalk = models.BooleanField()
    judge = models.BooleanField()
    mentor = models.BooleanField()

    class Meta(object):
		ordering = ('nameFirst', 'nameLast', 'company')
