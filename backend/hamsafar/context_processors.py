from account.models import Client


def is_passenger(request):
    res = {'is_passenger': True}
    if request.user.is_authenticated:
        if Client.objects.filter(user=request.user).first() is None:
            res['is_passenger'] = False
    return res
