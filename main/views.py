from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406408602',
        'name': 'Muhammad Yufan Jonni',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

# Create your views here.
