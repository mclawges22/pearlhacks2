#!/usr/bin/env python

from django.contrib import admin
from mentors.models import Mentor
from mentors.models import Skill


class MentorAdmin(admin.ModelAdmin):
	search_fields = ('firstName', 'lastName', 'company',)

admin.site.register(Mentor, MentorAdmin)
