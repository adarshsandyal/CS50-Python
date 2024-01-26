def main():
    filename = input("What is the file name? ")
    extension(filename)

def extension(name):
    name= name.lower().strip().split('.') # split the string along the period/.
    if len(name) > 1: # if it splits length will be >1 , else 0
        if name[-1] == "gif":# -1 indicates last item in the list
            print("image/gif")
        elif name[-1] == "jpg" or name[-1]=="jpeg":
            print("image/jpeg")
        elif name[-1]=="png":
            print("image/png")
        elif name[-1]=="pdf":
            print("application/pdf")
        elif name[-1]=="txt":
            print("text/plain")
        elif name[-1]=="zip":
            print("application/zip")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

main()
#.gif .jpg .jpeg .png .pdf .txt .zip