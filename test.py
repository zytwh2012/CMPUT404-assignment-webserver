from urllib import request
import unittest

BASEURL = "http://127.0.0.1:8080"
url = BASEURL+"/base.css"
req = request.urlopen(url, None, 3)
print(req,"req")
print(req.getcode(),"code")
print(req.info().get_content_type(),"info")