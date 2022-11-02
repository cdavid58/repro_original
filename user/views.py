from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render, redirect
from .models import User
from music.models import Bar, Music

def Login(request):
	if request.method == 'POST':
		try:
			bar = Bar.objects.get(code = request.POST.get('code'))
		except Bar.DoesNotExist:
			bar = None
		if bar is not None:
			request.session['code'] = request.POST.get('code')
			try:
				user = User.objects.get(number_phone = request.POST.get('number_phone'))
			except User.DoesNotExist:
				User(
					number_phone = request.POST.get('number_phone'),
					lat = request.POST.get('lat'),
					lon = request.POST.get('lon')
				).save()
			request.session['number_phone'] = request.POST.get('number_phone')
			return redirect('Index')
		else:
			message = "El Codigo del bar es incorrecto"
	return render(request,'login.html')


def Index(request):
	music = Music.objects.filter(bar = Bar.objects.get(code = request.session['code']))
	return render(request,'index.html',{'music':music})

def Save_Music(request):
	if request.is_ajax():
		user = User.objects.get(number_phone = request.session['number_phone'])
		alert = False
		if user.count_music > 0:
			Music(
				name = request.GET['music'],
				artist = request.GET['artist'],
				user = user,
				bar = Bar.objects.get(code = request.session['code'])
			).save()
			n = user.count_music - 1
			user.count_music = n
			user.save()
			alert = True
		return HttpResponse(alert)


@api_view(['POST'])
def Get_List_Music(request):
	music = Music.objects.filter(bar = Bar.objects.get(code = request.data['code']))
	data = [
		{
			'pk':i.pk,
			'name':i.name,
			'artist':i.artist,
			'user':i.user.number_phone,
			'user_pk':i.user.pk
		}
		for i in music
	]
	return Response(data)

@api_view(['POST'])
def Delete_Music(request):
	data = request.data
	Music.objects.get(pk = data['pk']).delete()
	user = User.objects.get(pk = data['pk_user'])
	if user.count_music < 5:
		n = user.count_music + 1
		user.count_music = n
		user.save()
	return Response({})