from  labnotebook_builder import Doc,Page,LinearLinks
import sys

doc=Doc("templates/journalTemplate.pdf")

# links of tabs
tabLinks=LinearLinks(left=6,top=37.7,width=28,height=92.4,flowdirection="down")

# build cover page
bookCover=doc.addPage(title=f"Notebook Cover",basepdfname="templates/journalCover.pdf",toclevel=1)
bookCover.addLinks(tabLinks)

# build constants page

bookConstants=doc.addPages("templates/journalConstants.pdf")

# link top level pages to eachother
tabLinks.addLink(bookConstants,"")

doc.render(sys.argv[1])






