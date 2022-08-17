from PIL import Image
import os


class Compress():
    def compress_img(self, path, quality=70):
        if not "png" in path and not "svg" in path and not "mp3" in path:
                img = Image.open(path)
                img_size = os.stat(path).st_size / 1024
                print(f'File Size in Kb is {img_size}')
                if img_size > 300:
                    img.save(path, format="JPEG", quality=quality)
                    print(path + " - compressed!")


    def folder_imgs_compress(self, quality=70, folders=[], folder=""):
        filelist = []
        if folder == "" and not folders == []:
            try:
                for folder in folders:
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            #append the file name to the list
                            filelist.append(os.path.join(root,file))
            except:
                print("List is invalid!")
        else:
            try:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        #append the file name to the list
                        filelist.append(os.path.join(root,file))
            except:
                print("Folder is invalid!")

        #print all the file names
        for path in filelist:
            if not "png" in path and not "svg" in path and not "mp3" in path:
                img = Image.open(path)
                img_size = int(os.stat(path).st_size / 1024)
                if img_size > 300:
                    img.save(path, format="JPEG", quality=quality)
                    print(path + " - compressed! File Size is " + str(img_size) + "Kb")
        


if __name__ == "__main__":
    folders = [
        "GerlovinMusic\static\static_files\img",
        "GerlovinMusic\static\img",
        "GerlovinMusic\static\static_files\media",
        "GerlovinMusic\static\media",
    ]

    Compress().folder_imgs_compress(20, folders=folders)
    