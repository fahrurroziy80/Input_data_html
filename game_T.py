Welcome = "Selamat datang di dalam game "
jawaban1 = 300
jawaban2 = 857
jawaban3 = 25

print("=================================")
print(f"=={Welcome}==")
print("=================================")

nama_player = input("masukan nama kamu : ")

print("--jawablah pertanyaan di bawah ini dengan benar--")
print(f'''(01).100 + 200 =''')
print(f'''(02).55-912 =''')
print(f'''(03). 5*5 =''')


pilihan_player1 = int(input("jawaban 01:"))
pilihan_player2 = int(input("jawaban 02:"))
pilihan_player3 = int(input('jawaban 03:'))

print(f"pilihan kamu adalah : ",pilihan_player1)


if pilihan_player1 == jawaban1:
    print("(01) jawaban kamu bener")
        
    
else:
    print("(01) salah ")
    
print(f"pilihan kamu adalah : ",pilihan_player2)

if pilihan_player2 == jawaban2:
    print('(02) jawaban kamu bener')
    
else:
    print("(02) jawaban kamu salah ")
    
    
print(f"pilihan kamu adalah : ",pilihan_player3)

if pilihan_player3 == jawaban3:
    print('(03) jawaban kamu bener')
    
else:
    print("(03) jawaban kamu salah ")
    


