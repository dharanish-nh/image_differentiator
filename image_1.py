from IMAGE import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDialog
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys
from PIL import Image
from skimage.measure import compare_ssim
import imutils
import cv2
import webbrowser

image = Ui_Dialog()

class ui(QDialog):
    def __init__(self):
        super(ui, self).__init__()
        image.setupUi(self)
        image.pushButton.clicked.connect(self.file)
        image.pushButton_2.clicked.connect(self.convert)
        image.pushButton_3.clicked.connect(self.file1)
        image.pushButton_4.clicked.connect(self.save_file)
        image.pushButton_5.clicked.connect(self.info)
        self.show()
        self.s="\t\t****INSTRUCTIONS****\n\n1.UPLOAD IMAGE OF SAME SIZE \n\n2.PRESS CHECK TO COMPARE\n\n3.PRESS SAVE TO SAVE FILE" \
          " WITH EXT (.JPG)(.PNG)  "
        image.lineEdit_3.setText(self.s)
        self.img1=None
        self.temp=True
        self.img2 = None
        self.modified=None
        self.imageA=None
        self.imageB = None

    def file(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '../ ', "Image Files(*.png *.jpg *.bmp)")
        image.lineEdit.setText(self.fname[0])
        self.img1 = self.fname[0]
        image.lineEdit_3.setText("IMAGE1 LOADED:\n{0}".format(self.img1))



    def file1(self):
        self.fname1 = QFileDialog.getOpenFileName(self, 'Open file', '../ ', "Image Files(*.png *.jpg *.bmp)")
        image.lineEdit_2.setText(self.fname1[0])
        print(self.fname1[0])
        self.img2 = self.fname1[0]
        image.lineEdit_3.append("\n\nIMAGE2 LOADED:\n{0}".format(self.img2))

    def info(self):

        self.temp=not self.temp
        if self.temp== False:
           image.lineEdit_3.setText("\t\t ♥♥THANK YOU FOR SUPPORTING♥♥  \n"
                                 "\n\n DHARANISH N H"
                                 "\n\n UNDER GUIDANCE"
                                 "\n\n VIVIAN DAVIS")
           webbrowser.open("https://www.linkedin.com/in/dharanish-nh-27426115b")
        else:
            image.lineEdit_3.setText(self.s)

    def convert(self):
      try:
        self.imageA = cv2.imread(self.img1)
        self.imageB = cv2.imread(self.img2)

        # convert the images to grayscale
        grayA = cv2.cvtColor(self.imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(self.imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(self.imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(self.imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # show the output images
        cv2.imshow("Original", self.imageA)
        cv2.imshow("Modified", self.imageB)
        image.lineEdit_3.setText("SUCCESS")
        # cv2.imshow("Diff", diff)
        # cv2.imshow("Thresh", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

      except Exception as e:
          image.lineEdit_3.setText(str(e))

    def save_file(self):
        self.modified = QFileDialog.getSaveFileName(self,'Save File', "Image Files(*.png *.jpg *.bmp)")
        print(self.modified[0])
        try:
         img_save=Image.fromarray(self.imageB)
         img_save.save(self.modified[0])
         image.lineEdit_3.setText("SAVED")
        except Exception as e:
         image.lineEdit_3.setText(str(e))


if __name__ == '__main__':
    h =QApplication(sys.argv)
    n = ui()
    n.show()
    h.exec_()
