#while문
hit =0
while hit<100:
    hit+=1
    print(f'나무를 {hit}번 찍었습니다.')
    if hit==10:
        print('나무가 넘어갑니다')
        break
    else:
        print('계속 찍으세요')
print('나무찍기를 마칩니다')