from django.shortcuts import render
def startpage(request):
	return render(request, "quiz/startpage.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")	

def results(request):
	return render(request, "quiz/results.html")		

# Create your views here.
