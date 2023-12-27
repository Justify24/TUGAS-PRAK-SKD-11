from PyPDF2 import PdfWriter, PdfFileReader
  
# buat objek pdf writer
out = PdfWriter()
  
# buka file pdf asli
file = PdfFileReader("D:\materi\skd\enkripsiobjek\iya.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num): 
    
   
    page = file.getPage(idx)
      

    out.addPage(page)
  
  
# masukkan password enkripsi 
password = "pass"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("D:\materi\skd\enkripsiobjek\iya.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)