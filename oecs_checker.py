from docx import Document
import sys



filename = sys.argv[1]

try:
    f = open(filename,'r')
    f.close()
except FileNotFoundError:
    print(filename,"not found, aborting")
    exit()


document = Document(filename)
correct_order = ["History","Core concepts","Questions, controversies, and new developments","Broader connections",
                 "Further reading","References","Keywords"]
acceptable_styles = ["title","subtitle","normal","heading 1","heading 2"]

heading_list = []
styles_list = []
waspara = False
empty_style_warning = False
nonstandard_warning = False
for p in document.paragraphs:
    style = p.style.name
    if style.lower().find('normal') == -1:

        if waspara:
            print()
            waspara = False

        if style.lower() not in acceptable_styles:
            nonstandard_warning = True
            print(style,": [!NONSTANDARD STYLE TEXT!]")
        else:
            text = p.text
            flag = ""
            if len(text)==0:
                flag = "[!EMPTY STYLE!]"
                empty_style_warning = True
            print(style,":",p.text,flag)
            styles_list.append(style)

    else:
        print("n",end="")
        waspara = True

    if style == "Heading 1":
        text = p.text
        text = text.rstrip(" ") #even template doesn't get this right
        if text != "Acknowledgements" and (len(text)!=0):
            heading_list.append(text)


print()
print()

if len(styles_list) == 0:
    print("ONLY NORMAL STYLES FOUND, FIX STYLES ON TITLES AND HEADERS")
    exit()

if nonstandard_warning:
    print("WARNING NONSTANDARD STYLES FOUND, SEE ABOVE")
if empty_style_warning:
    print("WARNING EMPTY STYLED LINES FOUND SEE ABOVE")
if styles_list.count("Title") < 0:
    print("MISSING TITLE STYLE")
elif styles_list.count("Title") > 1:
    print("MORE THAN ONE TITLE STYLE")
elif styles_list[0]!="Title":
    print("TITLE NOT FIRST")
else:
    print("-Title present and correctly located")

if styles_list.count("Subtitle") != 2:
    print("SHOULD HAVE 2 SUBTITLE STYLES,COUNT IS WRONG")
elif styles_list[1]!="Subtitle" or styles_list[2]!="Subtitle":
    print("SUBTITLES NOT IN CORRECT PLACE")
else:
    print("-Subtitles present and correctly located")




if heading_list == correct_order:
    print("-Top-level sections correct")
elif len(heading_list) == len(correct_order):
    for i,h in enumerate(heading_list):
        c  = correct_order[i]
        if c!=h:
            print("SECTION POSITION",i,"SHOULD READ","["+c+"]","ACTUALLY READS","["+h+"]")
elif len(heading_list) < len(correct_order):
    print("SECTION LIST IS TOO SHORT")
    print()
    print("SHOULD READ",correct_order)
    print()
    print("ACTUALLY READS",heading_list)
    print()
    missing = set(correct_order) - set(heading_list)
    print("APPEARS TO BE MISSING",missing)
else:
    print("SECTION LIST IS TOO LONG")
    print("SHOULD READ",correct_order)
    print("ACTUALLY READS",heading_list)
