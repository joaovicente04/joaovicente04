#for A in range(10):
    #print(f"Contando: {A}")


from time import sleep
ct = 10
while True:
    if ct == -1:
        break
    print(f"Contagem: {ct}")
    sleep(1)
    ct= ct-1
