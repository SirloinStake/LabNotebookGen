from  labnotebook_builder import Doc,Page,LinearLinks
import sys

doc=Doc("templates/journalTemplate.pdf")

# links of tabs
tabLinks=LinearLinks(left=6,top=37.7,width=28,height=92.4,flowdirection="down")
  
# build cover page
bookCover=doc.addPage(title=f"Notebook Cover",basepdfname="templates/journalCover.pdf",toclevel=1)
bookCover.addLinks(tabLinks)

# build constants pages
# for i in range(2):
#     pdfConstants = {}
#     pdfConstants[i]:append{f"templates/journalConstants_{i+1}.pdf"}
# 
# # link top level pages to eachother
# tabLinks.addLink(bookConstants,"")

for i in range(1,3):
    journalConstants=doc.addPage(title=f"Constants {i}",basepdfname=f"templates/journalConstants_{i}.pdf",toclevel=1)
    journalConstants.addLinks(tabLinks)
    if i==1:
        tabLinks.addLink(journalConstants,"Constants A")
    else:
        continue


tocLinks = {}
journalTOC={}
sectLinks={}

for i in range(1,6):

    sectLinks[f"sectLinks{i}"] = LinearLinks(left=67.44,top=54.24,width=23.3,height=21.1,flowdirection="down")

    tocLinks[f"tocLinks{i}"] = LinearLinks(left=473.76,top=73.2,width=57.12,height=15.834,flowdirection="down")

    journalTOC[f"journalTOC{i}"]=doc.addPage(title=f"TOC {i}",basepdfname=f"templates/journalTOC{i}.pdf",toclevel=1)
    journalTOC[f"journalTOC{i}"].addLinks(tabLinks,tocLinks[f"tocLinks{i}"])

    tabLinks.addLink(journalTOC[f"journalTOC{i}"],"TOC {i}")

    sectLinks[f"sectLinks{i}"].addLink(journalTOC[f"journalTOC{i}"],"TOC {i}")

for i in range(1,4):
    journalNotes=doc.addPage(title=f"Notes {i}",basepdfname=f"templates/journalNotes_{i}.pdf",toclevel=1)
    journalNotes.addLinks(tabLinks)
    if i==1:
        tabLinks.addLink(journalNotes,"Notes A")
    else:
        continue



journalPages={}


sect = 1
while sect < 6:

    for i in range(1,41):
        journalPages[f"journalPage{i+40*(sect-1)}"]=doc.addPage(title=f"Page {sect}_{i}",basepdfname=f"templates/journalSec{sect}_{i}.pdf",toclevel=1)
        journalPages[f"journalPage{i+40*(sect-1)}"].addLinks(tabLinks,sectLinks[f"sectLinks{sect}"])

        tocLinks[f"tocLinks{sect}"].addLink(journalPages[f"journalPage{i+40*(sect-1)}"],"Page {sect}_{i}")
    
    sect=sect+1

doc.render(sys.argv[1])

# # links of TOC pages
# tocnum = 1
# toclinks=[""]
# while tocnum < 6:
#         toclinks.append(LinearLinks(right=-66.72,top=72.24,width=58.32,height=17.28,flowdirection="down"))






# journalTOC1=doc.addPage(title=f"TOC 1",basepdfname=f"templates/journalTOC1.pdf",toclevel=1)
# journalTOC1.addLinks(tabLinks,toc1Links)

# journalTOC2=doc.addPage(title=f"TOC 2",basepdfname=f"templates/journalTOC2.pdf",toclevel=1)
# journalTOC2.addLinks(tabLinks,toc2Links)

# journalTOC3=doc.addPage(title=f"TOC 3",basepdfname=f"templates/journalTOC3.pdf",toclevel=1)
# journalTOC3.addLinks(tabLinks,toc3Links)

# journalTOC4=doc.addPage(title=f"TOC 4",basepdfname=f"templates/journalTOC4.pdf",toclevel=1)
# journalTOC4.addLinks(tabLinks,toc4Links)

# journalTOC5=doc.addPage(title=f"TOC 5",basepdfname=f"templates/journalTOC5.pdf",toclevel=1)
# journalTOC5.addLinks(tabLinks,toc5Links)








