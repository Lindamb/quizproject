from quiz.models import Quiz 
from django.shortcuts import render	
from django.shortcuts import redirect

def start(request):
	context = {
			"quizzes": Quiz.objects.all()
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)
	
def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[int(question_number) - 1]
	context = {
		"question_number": question_number,
	    "question": question.question,
		"answer1": question.answer1,
	   	"answer2": question.answer2,
	    "answer3": question.answer3,
	    "quiz": quiz,
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)
def answer(request, quiz_number, questions_number):
	saved_answers = request.session.get(quiz_number, {})
	saved_answers[question_number] = answer
	request.session[quiz_number] = saved_answers

	question_number = int(question_number)
	return redirect("question_page", quiz_number, question_number + 1)	
	
def results(request, quiz_number):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)
	
