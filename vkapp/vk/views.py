from django.shortcuts import render

# def init(request, api_url, api_settings, viewer_id, group_id, is_app_user):
#     return render(request, 'vk/index.html', context)

# api_url=https://api.vk.com/api.php
# &api_settings=0
# &viewer_id=123456
# &group_id=654321
# &is_app_user=0 \\
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def init(request, **request_params):
    param = list(request.GET.items()) #.get('viewer_id')
    context = {'data': param}
    return render(request, 'vk/index.html', context)

@xframe_options_exempt
def blogers(request):
    return render(request, 'vk/blogers.html')