# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('MediaCenter.html')

def menu(request):
	return render_to_response('menu.html')

