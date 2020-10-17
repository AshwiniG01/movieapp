from django.shortcuts import render,redirect


# Create your views here.
def home_page(request):
	return render(request=request, template_name="movieapp/homepage.html")


from movieapp.forms import MovieDataTable

def add_movie(request):
	form=MovieDataTable()
	

	if request.method=="POST":
		movie_data=MovieDataTable(request.POST)
		if movie_data.is_valid():
			movie_data.save(commit=True)

	if request.method=="POST":
		movie_data=MovieDataTable(request.POST)
		if movie_data.is_valid():
			print("Name of the movie:",movie_data.cleaned_data['movie_name'])
			print("Movie release date:",movie_data.cleaned_data['release_date'])
			print("Name of the Hero:",movie_data.cleaned_data['hero_name'])
			print("Name of the Heroin:",movie_data.cleaned_data['heroin_name'])
			print("Movie Language:",movie_data.cleaned_data['language'])
	my_dict={'form':form}
	return render(request=request, template_name='movieapp/addmovie.html',context=my_dict)


from movieapp.models import MovieTable


def list_movie(request):
	list_movie=MovieTable.objects.all()
	my_dict={'list_movie':list_movie}
	return render(request=request, template_name='movieapp/listmovie.html',context=my_dict)

def delete_view(request,id):
	MovieTable=MovieTable.objects.get(id=id)
	MovieTable.delete()
	return redirect('/listmovie/')




	
			