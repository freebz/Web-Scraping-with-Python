# CHAPTER 11 이미지 처리와 텍스트 인식

# 11.1 라이브러리 개관

# 11.1.1 필로

from PIL import Image, ImageFilter
kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()
