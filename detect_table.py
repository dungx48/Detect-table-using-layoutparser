from re import I
import layoutparser as lp
import cv2
import time
from PIL import Image

def detect_table(image):

    ## load image and convert BGR2RGB
    # image = cv2.imread(img_path)
    # image = image[..., ::-1]
    # image = Image.open(image)
    # print(type(image))

    # load model
    model = lp.models.Detectron2LayoutModel('lp://TableBank/faster_rcnn_R_50_FPN_3x/config')

    # Processing
    tik = time.time()
    layout = model.detect(image)
    print("Processing time: ", time.time() - tik)

    img_processed = lp.draw_box(image, layout)
    # print(type(img_processed))
    print("--------------------------")
    # img_processed.show()
    # img_processed.save("1.png")
    return img_processed

# detect_table('/home/vdungx/Pictures/1.png')   
