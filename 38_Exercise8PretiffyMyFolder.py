import os


def readfiles(filename):
    ff = open(filename)
    l = ff.read()
    var = l.split("\n")
    ff.close()
    return var


def pmf(path, filen, extx):
    var = readfiles(filen)
    os.chdir(path)
    count = 0
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_last = f_ext.strip(".")
        if f_name not in var:
            newname = f"{f_name.title()}{f_ext}"
            os.rename(f, newname)
            pass

        if f_last == extx:
            count += 1
            nwname = f"{count}{f_ext}"
            os.rename(f, nwname)
            pass


if __name__ == '__main__':
    path = input("Enter your path : ")
    filen = input("Enter file name which include imp names : ")
    extx = input("Enter extension of your file : ")
    pmf(path, filen, extx)
