# oecs_checker
This is a simple script to aid in validating OECS articles for template compliance. (If you don't know what that means, this repository is not for you.)



### Usage:

You may need to install python-docx (`pip install python-docx`).

To run: `python oecs_checker.py target_document.docx`.

This will output a list of styled headings (both the style and the content of the heading). Normal-styled paragraphs will appear as 'n'. This will give you a high-level overview of the document. Then it will flag common problems: missing sections, wrong section heading names, unusual styles, etc. If things are very wrong, it may not catch all errors. Run it again after editing until it passes.

*Important Note:* If you make changes while using track changes, this script doesn't seem to pick up on them until the changes are accepted. I would suggest getting template verified first without track changes.

The `test/` directory contains several example files that you can try the script on. `test/Good.docx` is correctly formatted as per the current template. Other files demonstrate a variety of errors.

This has been built using the OECS template of 15 June 2024. It will need to be updated if the template changes.

There are surely bugs. Feel free to fix them, or to email me about them. I also definitely haven't considered all the ways the template can go wrong, so be sure to double-check.  

Colin Klein  
colin.klein@anu.edu.au


Example run:
```
github/oecs_checker~ % python oecs_checker.py test/Incorrect_sections.docx   
Title : This article has incorrect sections  
Subtitle : Bad author (000000)   
Subtitle : Barish-Estranza Corporate R&D   
Heading 1 : The Distant Past  
nn  
Heading 1 : Core concepts
nnnn  
Heading 2 : Subheader 1   
nn  
Heading 1 : Questions, controversies, and awesome stuff   
nn  
Heading 1 : Broader connections   
n  
Heading 1 : Acknowledgements   
n  
Heading 1 : Key references   
nnn  
Heading 1 : Bibliography   
nn  
Heading 1 : Keywords    
n  

-Title present and correctly located  
-Subtitles present and correctly located  
SECTION POSITION 0 SHOULD READ [History] ACTUALLY READS [The Distant Past]  
SECTION POSITION 2 SHOULD READ [Questions, controversies, and new developments] ACTUALLY READS [Questions, controversies, and awesome stuff]  
SECTION POSITION 4 SHOULD READ [Further reading] ACTUALLY READS [Key references]  
SECTION POSITION 5 SHOULD READ [References] ACTUALLY READS [Bibliography]
```
