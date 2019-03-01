import sys

all_h = list()
all_v = list()
slides = list()



def main(arg):
    with open(arg) as read_file:
        all_pictures = read_file.readlines()
        i = 0
        for picture in all_pictures:
            picture = picture.rstrip()
            if picture[0] == "H":
                picture += " " + str(i)
                all_h.append(picture.split(" "))
            if picture[0] == "V":
                picture += " " + str(i)
                all_v.append(picture.split(" "))
            i += 1
        all_h.sort(key=lambda x: int(x[1]))
        all_v.sort(key=lambda x: int(x[1]))
        x = 0
        y = 0
        for item in all_v:
            slide = [all_v[x], all_v[y]]
            slides.append(slide)
            x += 1
            y += 1
        for slide in slides:
            slide_tag_total = 0
            count = 0
            for picture in slide:
                slide_tag_total += int(picture[1])
                count += 1
            slide.append(slide_tag_total)
       
        slides.sort(key=lambda x: int(x[len(slide)- 1]))
        print(len(slides))
        for slide in slides:
            for picture in slide:
                print(picture) 

main(sys.argv[1])