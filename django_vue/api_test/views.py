from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse,HttpResponse,QueryDict,HttpRequest
import json
from django.http import StreamingHttpResponse
from contract.contract_py2 import *
from django.views.generic import View
from json import dumps
import os
from django.utils.encoding import escape_uri_path

class Contract(View):

    def post(self,request):
        json_dic = eval(request.body)
        getContract(json_dic)
        # file=open('./%s互联网专线合同.docx'%json_dic['party_name'],'rb')
        # response = StreamingHttpResponse(file)
        if not os.path.isfile('./src/file/contract/%s互联网专线合同.docx'%json_dic['party_name']):  # 判断下载文件是否存在
            return HttpResponse("Sorry but Not Found the File")
        def file_iterator(file_path):
            with open(file_path, mode='rb') as f:
                while True:
                    c = f.read()
                    if c:
                        yield c
                    else:
                        break
        try:
        # 设置响应头
        # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
            response = StreamingHttpResponse(open('./src/file/contract/%s互联网专线合同.docx'%json_dic['party_name'],'rb'))
        # 以流的形式下载文件,这样可以实现任意格式的文件下载
            response['Content-Type'] = 'application/octet-stream'
        # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
            response['Content-Disposition'] = "attachment; filename={0}".format(escape_uri_path(json_dic['party_name']))
        except:
            return HttpResponse("Sorry but Not Found the File")
        return response