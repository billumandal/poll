from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
	return HttpResponse("<html>You're looking at the results of poll <strong>%s</strong>.</html>" % (poll_id,))

def vote(request, poll_id):
	return HttpResponse("You're voting at poll %s." % (poll_id,))