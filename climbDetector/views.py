from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from ImgTools import Predictor
import climbDetector.models as CD_models
import time

predictor = Predictor("./ImgTools/")  # 实例化一个预测类


@csrf_exempt    
def imgFunc(request):
    print(111)
    # 过滤直接访问的情况
    if 'python' not in request.META.get('HTTP_USER_AGENT', '') or \
            request.method == 'GET':
        return HttpResponse(404)
    res_ls = {}
    # POST方法
    imgs = request.FILES.get("img")  # 获取传输的图片
    for img_index in imgs:
        img = Image.open(imgs[img_index])
        res = predictor.detectImage(img)
        res_ls[img_index] = res

    CD_models.DetectDetails.objects.create(
        recode_time=time.strftime('%Y%m%d%H%M%S'),
        record_details=str(res_ls)
    )
    # fID = request.POST.get('time')  # 获取传输附带的数据
    # img.save(f"./static/img/{fID}.png")
    # print(time.time())
    print(str(res_ls))
    return HttpResponse(str(res_ls))

