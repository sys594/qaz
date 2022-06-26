def funcA():
    print("in funcA")
    driver = 3
    a = 1
    print(a == 1)  # 1 == 4 ?
    print("in funcA", driver)
    return a

def funcB(driver):
    print("in funcB")
    print(driver)

if __name__ == '__main__':
    # driver2 = funcA()
    # funcB(driver2)
    a = 1
    if a == 4:
        print('if', a)
    else:
        a = a+1
        print('else', a)
    
