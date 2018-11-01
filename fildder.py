import urllib.request
# url='https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3369433747,1794263154&fm=26&gp=0.jpg'
# response=urllib.request.urlopen(url)
# print(response)
# print(response.read().decode('utf8'))
# with open('img1.jpg','wb') as fp:
#     fp.write(response.read())
# print(response.url)
# print(response.status)
url='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=146315145,2320894337&fm=26&gp=0.jpg'
urllib.request.urlretrieve(url,'img2.jpg')