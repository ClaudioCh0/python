hytti_luokka = input("Minkä tason hytti sinulla on (LUX, A, B, C)?: ")

LUX = print("LUX on parvekkeellinen hytti yläkannella.")
A = ("A on ikkunallinen hytti autokannen yläpuolella.")
B = ("B on ikkunaton hytti autokannen yläpuolella.")
C = ("C on ikkunaton hytti autokannen alapuolella.")

if hytti_luokka == LUX:
    print(LUX)
elif hytti_luokka == A:
    print(A)
elif hytti_luokka == B :
    print(B)
elif hytti_luokka == C:
    print(C)

print("Tervetuloa")
