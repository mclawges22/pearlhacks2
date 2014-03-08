# FILE: mentors/views.py

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mentors.models import Mentor, Skill


def home(request):
	context = {
		'mentor_count': Mentor.objects.count(),
        'skill_count': Skill.objects.count(),
	}
	return render(request, 'mentors/home.html', context)

# how do I actually get this to be random?
def afraid(request):
    mentor = Mentor.objects.order_by('?')[0]
    # mentor = get_object_or_404(Mentor, id=pk)
    return render(request, "mentors/afraid.html", {'Mentor': mentor})

def proud(request):
    mentor = Mentor.objects.order_by('?')[0]
    # mentor = get_object_or_404(Mentor, id=pk)
    return render(request, "mentors/proud.html", {'Mentor': mentor})

def mentor(request, pk):
    # mentor = Mentor.objects.order_by('?')[0]
    mentor = get_object_or_404(Mentor, id=pk)
    return render(request, "mentors/mentor.html", {'Mentor': mentor})

def mentorList(request):
    mentor_list = Mentor.objects.all()
    # skill_list = Skill.objects.all()
    paginator = Paginator(mentor_list, 25)
    page = request.GET.get('page')
    try:
        mentors= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mentors = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mentors = paginator.page(paginator.num_pages)

    return render(request, 'mentors/mentor_list.html', {"mentors": mentors})

def skill(request, pk):
	# skill = Skill.objects.order_by('?')[0]
    skill = get_object_or_404(Skill, id=pk)
    return render(request, "mentors/skill.html", {'skill': skill})

def skillList(request):
    skill_list = Skill.objects.all()
    paginator = Paginator(skill_list, 25)
    page = request.GET.get('page')
    try:
        skills= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        skills = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        skills = paginator.page(paginator.num_pages)

    return render(request, 'mentors/skill_list.html', {"skills": skills})