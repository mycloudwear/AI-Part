import requests
import base64
import socket

# imgPath = r'12.png'
hostname = '192.168.0.67'
port = 8080


def encode_base64(string):
    encodestr = base64.b64encode(string.encode('utf-8'))
    encodestr = encodestr.decode('utf-8')
    return encodestr


def get_byte(Path):
    with open(Path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
        img_str = base64_data.decode('ascii')
        return img_str


# The first parameter is the local address of the uploaded image. (.png)
# The second parameter is the name of the image.
# The third parameter is the user's name. (phone number)
def upload_filename(match_results_filename, username):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((hostname, port))
    temp = username + ','

    for each in match_results_filename:
        temp = temp + each + ','
    data = {'list': temp[:-1]}
    res = requests.post(url='http://192.168.0.67:8080/WebPicStream/DeletePhoto', data=data)
    s.close()


def upload_image(imgPath, Uuid, username):
    img = get_byte(imgPath)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((hostname, port))
    info = username + ',' + Uuid + ',' + img
    data = {'list': info}
    if (data != None):
        res = requests.post(url='http://192.168.0.67:8080/WebPicStream/UpdateResult', data=data)
        print(Uuid + '.jpg---------uploaded successfully')
    s.close()
