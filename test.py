import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('eng.png', detail=0)
print(result)