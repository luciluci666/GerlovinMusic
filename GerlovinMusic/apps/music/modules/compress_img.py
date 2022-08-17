from PIL import Image
import os


class Compress():
    def compress_img(self, path, quality=70):
        img = Image.open(path)

        if img.height > 300 or img.width > 300:
            img.save(path.path, format="JPEG", quality=quality)

    def folder_imgs_compress(self, folder, quality=70):
        filelist = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                #append the file name to the list
                filelist.append(os.path.join(root,file))

        #print all the file names
        for path in filelist:
            if not "png" or not "svg" in path :
                img = Image.open(path)
                if img.height > 300 or img.width > 300:
                    img.save(path, format="JPEG", quality=quality)
                    print(path + " - compressed!")
        

if __name__ == "__main__":
    Compress().folder_imgs_compress("GerlovinMusic\static\static_files\img", 20)