def Myfungsion(X):
    print(X)
Myfungsion(X = 2)

"""array"""
def nama():
    motor = ["supra", "vario", "beat" ]
    print("daftar motor",motor)

nama()
nama()
"""fungsion """
def MMM():
    nama = "ujang "
    alamat = "soul "
    print("alamat",alamat)
    print("nama",nama)

MMM()

def menu():
    makanan = "nasi goreng "
    minuman = "es teler"
    print("makanan",makanan)
    print("minuman",minuman)

menu()



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

