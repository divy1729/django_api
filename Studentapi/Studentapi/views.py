from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    friends=[
        'ravi',
        'uttam',
        'prateek',

    ]
    return JsonResponse(friends,safe=False)