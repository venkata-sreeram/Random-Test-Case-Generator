#!/usr/bin/python3

import os
import time

try:
    import numpy as np
except:
    print("You don't have numpy package, first install it.")
    os.system("sudo pip3 install numpy")

def print_array(arr: list, fh, f_flag: bool =False) -> None:
    if f_flag:
        for e in arr:
            fh.write(str(e)+" ")
        fh.write("\n")
    else:
        for e in arr:
            print(e, end=" ")
        print()

    return

def print_matrix(arr: list, r: int, c: int, fh, f_flag: bool) -> None:
    tmp = np.array(arr).reshape(r, c)
    for i in range(r):
        for j in range(c):
            if f_flag:
                fh.write(str(tmp[i][j])+" ")
            else:
                print(tmp[i][j], end=" ")
        if f_flag:
            fh.write("\n")
        else:
            print()

    return

def numbers(n: int, mini: int, maxi: int, fh, n_flag: bool =False, dis: bool =False, f_flag: bool =False) -> None:
    if dis and maxi - mini < n:
        print("With the given parameters generating randomness is not possible")
        print("Range of integers is less than n (maxi - mini < n)")
        finally_block(fh)
        os.remove(fh.name)
        quit()

    if n_flag:
        if f_flag:
            fh.write(str(n)+"\n")
        else:
            print(n)

    if dis:
        tmp = list()
        for i in range(n):
            val = np.random.randint(mini, maxi+1)
            while val in tmp:
                val = np.random.randint(mini, maxi+1)
            tmp.append(val)
            if f_flag:
                fh.write(str(val))
            else:
                print(val)
    else:
        for i in range(n):
            if f_flag:
                fh.write(str(np.random.randint(mini, maxi+1))+"\n")
            else:
                print(np.random.randint(mini, maxi+1))

    return

def array(n: int, size: int, mini: int, maxi: int, fh, n_flag: bool =False, size_flag: bool =False, dis: bool =False, f_flag: bool =False) -> None:
    if dis and maxi - mini < size:
        print("With the given parameters generating randomness is not possible")
        print("Range of integers is less than size of array (maxi-mini < size)")
        finally_block(fh)
        os.remove(fh.name)
        quit()

    if n_flag:
        if f_flag:
            fh.write(str(n)+"\n")
        else:
            print(n)

    for i in range(n):
        if size_flag:
            if f_flag:
                fh.write(str(size)+"\n")
            else:
                print(size)

        if dis:
            tmp = list()
            for j in range(size):
                val = np.random.randint(mini, maxi+1)
                while val in tmp:
                    val = np.random.randint(mini, maxi+1)
                tmp.append(val)
            print_array(tmp, fh, f_flag)
        else:
            for j in range(size):
                if f_flag:
                    fh.write(str(np.random.randint(mini, maxi+1))+" ")
                else:
                    print(np.random.randint(mini, maxi+1))
        print("\n")

    return

def matrix(n: int, r: int, c: int, mini: int, maxi: int, fh, n_flag: bool =False, nm_flag: bool =False, dis: bool =False, f_flag: bool =False) -> None:
    if dis and maxi - mini < r*c:
        print("With the given parameters generating randomness is not possible")
        print("Range of integers is less than the cells of array (maxi-mini < size)")
        finally_block(fh)
        os.remove(fh.name)
        quit()

    if n_flag:
        if f_flag:
            fh.write(str(n)+"\n")
        else:
            print(n)

    for i in range(n):
        if nm_flag:
            if f_flag:
                fh.write(str(r)+" "+str(c)+"\n")
            else:
                print(r, c)

        if dis:
            tmp = list()
            for j in range(r*c):
                val = np.random.randint(mini, maxi+1)
                while val in tmp:
                    val = np.random.randint(mini, maxi+1)
                tmp.append(val)
            print_matrix(tmp, r, c, fh, f_flag)
        else:
            print_matrix(np.random.randint(mini, maxi+1, size=r*c), r, c, fh, f_flag)

    return

def string(n: int, size: int, charset: str, fh, n_flag: bool =False, size_flag: bool =False, dis: bool =False, f_flag: bool =False) -> None:
    if dis and size > len(set(charset)):
        print("With the given parameters generating randomness is not possible")
        print("Size of string > character set(distinct)")
        finally_block(fh)
        os.remove(fh.name)
        quit()

    if n_flag:
        if f_flag:
            fh.write(str(n)+"\n")
        else:
            print(n)

    for i in range(n):
        if size_flag:
            if f_flag:
                fh.write(str(size)+"\n")
            else:
                print(size)

        rand_str = ""        
        if dis:
            for j in range(size):
                ind = np.random.randint(0, len(charset))
                while charset[ind] in rand_str:
                    ind = np.random.randint(0, len(charset))
                rand_str = rand_str + charset[ind]
        else:
            for j in range(size):
                ind = np.random.randint(0, len(charset))
                rand_str = rand_str + charset[ind]
        if f_flag:
            fh.write(rand_str+"\n")
        else:
            print(rand_str)

    return

def string_matrix(n: int, r: int, c: int, charset: str, fh, n_flag: bool =False, nm_flag: bool =False, dis: bool =False, f_flag: bool =False) -> None:
    if dis and r*c > len(set(charset)):
        print("With the given parameters generating randomness is not possible")
        print("Cells of array > character set(distinct)")
        finally_block(fh)
        os.remove(fh.name)
        quit()

    if n_flag:
        if f_flag:
            fh.write(str(n)+"\n")
        else:
            print(n)

    for i in range(n):
        if nm_flag:
            if f_flag:
                fh.write(str(r)+" "+str(c)+"\n")
            else:
                print(r, c)

        rand_str = ""
        if dis:
            for j in range(r*c):
                ind = np.random.randint(0, len(charset))
                while charset[ind] in rand_str:
                    ind = np.random.randint(0, len(charset))
                rand_str = rand_str + charset[ind]
        else:
            for j in range(r*c):
                ind = np.random.randint(0, len(charset))
                rand_str = rand_str + charset[ind]
        print_matrix(list(rand_str), r, c, fh, f_flag)

    return

def input_N() -> (int, bool):
    try:
        n = int(input("Enter the value of N Test Cases: "))
    except:
        print("N value is set to 10")
        n = 10

    print("Include N Test Cases Flag")
    print("1) Yeah")
    print("2) Naah!")
    opt = int(input("Enter your choice: "))
    if opt == 1:
        n_flag = True
    else:
        n_flag = False

    return (n, n_flag)

def input_min_max() -> (int, int):
    try:
        mini = int(input("Enter Min Value: "))
    except:
        print("Min Value is set to 0")
        mini = 0
    try:
        maxi = int(input("Enter Max Value: "))
    except:
        print("Max Value is set to 1000")
        maxi = 1000

    return (mini, maxi)

def input_array_dimension() -> (int, int, bool):
    try:
        row = int(input("Enter number of rows of matrix: "))
    except:
        print("Num Rows Value is set to 5")
        row = 5
    try:
        col = int(input("Enter number of columns of matrix: "))
    except:
        print("Num Cols Value is set to 5")
        col = 5

    print("Include N M Flag")
    print("1) Yeah")
    print("2) Naah!")
    opt = int(input("Enter your choice: "))
    if opt == 1:
        nm_flag = True
    else:
        nm_flag = False

    return (row, col, nm_flag)

def input_array() -> (int, bool):
    try:
        size = int(input("Enter the size: "))
    except:
        print("Size set to 10")
        size = 10
    print("Include N Flag")
    print("1) Yeah")
    print("2) Naah!")
    opt = int(input("Enter your choice: "))
    if opt == 1:
        size_flag = True
    else:
        size_flag = False

    return (size, size_flag)

def input_charset() -> str:
    charset = input("Enter the chars without any separator: ")
    if len(charset) == 0:
        print("Charcter Set set to ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    return charset

def input_distinct() -> bool:
    print("Distinct Flag")
    print("1) Yeah")
    print("2) Naah!")
    opt = int(input("Enter your choice: "))
    if opt == 1:
        distinct = True
    else:
        distinct = False

    return distinct

def menu() -> (int, str):
    print("# Types of Test Cases #")
    print("1) Number")
    print("2) Array")
    print("3) Characters")
    print("Any-Key) Exit")
    opt1 = int(input("Enter your option: "))

    print("Should I Write it into a file?")
    print("1) Yeah!")
    print("2) Naah!")
    opt2 = int(input("Should I? "))
    if opt2 == 1:
        fname = input("Enter your file-name: ")
        if len(fname) == 0:
            epoch = "".join(str(time.time()).split("."))
            fname = "test-cases-"+epoch+".txt"
            print("File name set to default ->", fname)
    else:
        fname = None

    return opt1, fname

def input_data1() -> (int, int, bool):
    mini, maxi = input_min_max()
    dis = input_distinct()

    return (mini, maxi, dis)

def input_data2() -> (int, int, int, bool, bool):
    mini, maxi = input_min_max()
    size, size_flag = input_array()
    dis = input_distinct()

    return (size, mini, maxi, size_flag, dis)

def input_data3() -> (int, int, int, int, bool, bool):
    mini, maxi = input_min_max()
    r, c, nm_flag = input_array_dimension()
    dis = input_distinct()

    return (r, c, mini, maxi, nm_flag, dis)

def input_data4() -> (int, str, bool, bool):
    size, size_flag = input_array()
    charset = input_charset()
    dis = input_distinct()

    return (size, charset, size_flag, dis)

def input_data5() -> (int, int, str, bool, bool):
    r, c, nm_flag = input_array_dimension()
    charset = input_charset()
    dis = input_distinct()

    return (r, c, charset, nm_flag, dis)

def finally_block(fh) -> None:
    if fh != None:
        fh.close()

if __name__ == '__main__':
    opt, fname = menu()

    if fname != None:
        fh = open(fname, "w")
        f_flag = True
    else:
        fh = None
        f_flag = False

    n, n_flag = input_N()
    if opt == 1:
        mini, maxi, dis = input_data1()
        numbers(n, mini, maxi, fh, n_flag, dis, f_flag)
    elif opt == 2:
        print("! Type of Array !")
        print("1) One-dimensional")
        print("2) Multi-dimensional")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            size, mini, maxi, size_flag, dis = input_data2()
            array(n, size, mini, maxi, fh, n_flag, size_flag, dis, f_flag)
        elif choice == 2:
            r, c, mini, maxi, nm_flag, dis = input_data3()
            matrix(n, r, c, mini, maxi, fh, n_flag, nm_flag, dis, f_flag)
    elif opt == 3:
        print("! Type of Character Arrays !")
        print("1) Strings")
        print("2) Character Array(Multi-dimensional)")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            size, charset, size_flag, dis = input_data4()
            string(n, size, charset, fh, n_flag, size_flag, dis, f_flag)
        elif choice == 2:
            r, c, charset, nm_flag, dis = input_data5()
            string_matrix(n, r, c, charset, fh, n_flag, nm_flag, dis, f_flag)
    else:
        fh.close()
        print("Thank You, Hope to see you soon :-D")
        sys.quit()
