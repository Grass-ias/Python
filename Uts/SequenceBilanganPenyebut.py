# Program     : Sequence Bilangan Penyebut
# Deskripsi   : Menentukan apakah urutan angka x terulang tersebut sesuai dengan desimal hasil pembagian 1 dengan sebuah bilangan bulat.
# NIM/Nama    : 24060124140145/Ferdy Prasetya Putra
# Tanggal     : 18/09/2024
# ===========================================================================
def denumeratorSeq(x):
    if (10 ** len(x) - 1) % int(x) == 0:
        return f'Ada: {(10 ** len(x) - 1) // int(x)}'
    return 'Tidak ada'

print(denumeratorSeq('3'))
print(denumeratorSeq('142857'))
print(denumeratorSeq('7'))
