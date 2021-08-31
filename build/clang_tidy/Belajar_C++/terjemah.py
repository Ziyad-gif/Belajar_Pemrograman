from googletrans import Translator

translator = Translator()
texts = input("masukan yang mau diterjemahkan")

destination= input("masukan destinasi").lower()

translate  = transtalor.translate(texts,dest=destination)

print("terjemahan" + translate.text)