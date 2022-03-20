
abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = int(input('Masukkan cipher key yang anda inginkan (dalam angka, misal 9): '))  

def Caesar_cipher(kalimat,cipher_key): 
  kalimat = kalimat.lower()
  hasil_Caesar_cipher = '' 
  for karakter in kalimat: 
    if karakter in abjad:
      index_lama = abjad.index(karakter) 
      index_baru = (index_lama + cipher_key ) 
      abjad_baru = abjad[index_baru] 
      hasil_Caesar_cipher = hasil_Caesar_cipher + abjad_baru 
    else:
       hasil_Caesar_cipher = hasil_Caesar_cipher + karakter  
  return hasil_Caesar_cipher 

print("Masukkan pilihan")
print("1. Enkripsi")
print("2. Dekripsi")
pil = int(input()) 
if pil == 1:
  kalimat = input('Masukkan kalimat yang ingin dienkripsi : ') 
  kalimat_hasil = Caesar_cipher(kalimat,key) 
  print('Kalimat yang dimasukkan adalah:',kalimat)
  print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:',key, 'adalah', kalimat_hasil) 
  
elif pil == 2:
  kalimat_enkripsi = input('Masukkan kalimat yang ingin didekripsi : ') 
  kalimat_awal = Caesar_cipher(kalimat_enkripsi,-key) 
  print('Hasil Dekripsi Kalimat menggunakan Caesar chiper dengan key negatif adalah:',-key, 'adalah', kalimat_awal) 

else:
  print("Pilihan yang anda masukkan salah") 
