from django.http import JsonResponse


def error_404(request, exception):
    message = ('The endpoint is not fuond')

    response = JsonResponse(data={'message': message, 'status_code': 404})
    response.status_code = 404
    return response


def error_500(request):
    message = ('somthing wrong with the server')

    response = JsonResponse(data={'message': message, 'status_code': 500})
    response.status_code = 500
    return response
