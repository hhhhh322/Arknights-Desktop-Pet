from PIL import Image,ImageTk
imgpath = './memo/Amiya.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)