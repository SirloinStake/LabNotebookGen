# The idea is to mirror the functionality of "Lab Journal Chem.pdf" which currently uses rich buttons for internal hyperlinking.

# In the "./templates/" folder, this pdf is broken into its fundamental parts

# This includes 1) a background template as required by the original script, 2) a cover page, 3) two constants pages, 4) TOC pages for sections 1-5,

# 5) 3 pages for Misc Notes, 6) Sections 1-5 each with 40 pages per section

# All pages should have hyperlinks on the book tabs redirecting to one of the first 9 pages (see "Lab Journal Chem.pdf")

# All TOCs should link to the correct page under the "DESC" heading

# All section pages have an arrow which links back to that sections respective TOC

from  notebook_builder import Doc,Page,LinearLinks
from datetime import date,timedelta
import sys

doc=Doc("templates/journalTemplate.pdf")

# links down notebook tabs
notebookTabs=LinearLinks(left=6,top=38,flowdirection="down",width=28,height=93)

# links down page numbers for TOC1
notebookTOC1=LinearLinks(right=-67,top=72,flowdirection="down",width=59,height=15.6)

# links down page numbers for TOC2
notebookTOC2=LinearLinks(right=-67,top=72,flowdirection="down",width=59,height=15.6)

# links down page numbers for TOC3
notebookTOC3=LinearLinks(right=-67,top=72,flowdirection="down",width=59,height=15.6)

# links down page numbers for TOC4
notebookTOC4=LinearLinks(right=-67,top=72,flowdirection="down",width=59,height=15.6)

# links down page numbers for TOC5
notebookTOC5=LinearLinks(right=-67,top=72,flowdirection="down",width=59,height=15.6)

# links back to TOC1
notebookTOC1Return=LinearLinks(left=67,top=54,width=24,height=22)

# links back to TOC2
notebookTOC2Return=LinearLinks(left=67,top=54,width=24,height=22)

# links back to TOC3
notebookTOC3Return=LinearLinks(left=67,top=54,width=24,height=22)

# links back to TOC4
notebookTOC4Return=LinearLinks(left=67,top=54,width=24,height=22)

# links back to TOC5
notebookTOC5Return=LinearLinks(left=67,top=54,width=24,height=22)


# Build top pages, with templates, and give them their outbound links

journalCover=doc.addPage(title=f"Cover",basepdfname="templates/journalCover.pdf",toclevel=1)
journalCover.addLinks(notebookTabs)

journalConstants=doc.addPage(title=f"Constants",basepdfname="templates/journalConstants.pdf",toclevel=1)
journalConstants.addLinks(notebookTabs)

# Build TOC pages, with templates, and give them their outbound links

journalTOC1=doc.addPage(title=f"TOC1",basepdfname="templates/journalTOC2.pdf",toclevel=1)
journalTOC1.addLinks(notebookTabs,notebookTOC2)

journalTOC2=doc.addPage(title=f"TOC2",basepdfname="templates/journalTOC2.pdf",toclevel=1)
journalTOC2.addLinks(notebookTabs,notebookTOC2)

journalTOC3=doc.addPage(title=f"TOC3",basepdfname="templates/journalTOC3.pdf",toclevel=1)
journalTOC3.addLinks(notebookTabs,notebookTOC3)

journalTOC4=doc.addPage(title=f"TOC4",basepdfname="templates/journalTOC4.pdf",toclevel=1)
journalTOC4.addLinks(notebookTabs,notebookTOC4)

journalTOC5=doc.addPage(title=f"TOC5",basepdfname="templates/journalTOC5.pdf",toclevel=1)
journalTOC5.addLinks(notebookTabs,notebookTOC5)

# Build Notes pages, with templates, and give them their outbound links

journalNotes=doc.addPage(title=f"Misc Notes",basepdfname="templates/journalNotes.pdf",toclevel=1)
journalNotes.addLinks(notebookTabs)

# Link top level pages to each other
notebookTabs.addLink(journalConstants,"C");
notebookTabs.addLink(journalTOC1,"1");
notebookTabs.addLink(journalTOC2,"2");
notebookTabs.addLink(journalTOC3,"3");
notebookTabs.addLink(journalTOC4,"4");
notebookTabs.addLink(journalTOC5,"5");
notebookTabs.addLink(journalNotes,"N");

doc.render(sys.argv[1])






