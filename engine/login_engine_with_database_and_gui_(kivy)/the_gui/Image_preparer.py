from PIL import Image,ImageOps,ImageDraw,ImageChops


def crop_to_circle(image_name,size):
    im=Image.open(image_name).resize(size)
    big_size=tuple([i*3 for i in im.size])  #size #
    print(type(big_size))
    mask=Image.new('L',big_size,0)
    ImageDraw.Draw(mask).ellipse((0,0)+big_size,fill=255)
    mask=mask.resize(size)
    #mask=ImageChops.darker(mask,im.split()[-1])
    im.putalpha(mask)
    return im

def change_to_png(image_name_and_path,path_to_save):
    im=Image.open(image_name_and_path)
    image_name=image_name_and_path.split('/').pop()
    extentionless_name=image_name.split('.jpg')[0]
    im.save(path_to_save+extentionless_name+'.png')
    return path_to_save+extentionless_name+'.png'
if __name__=='__main__':
    path_name='david_photo.jpg'

    size=(100,100)
    #
    im=crop_to_circle(path_name,size)
    im.save(path_name.split('.jpg')[0]+'.png',mode='PNG')
    im.show()

