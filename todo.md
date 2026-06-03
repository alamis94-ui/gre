# Reviewing draft articles

- [ ] Check for any comments within the text
- [ ] Deal with empty stuff that is now commented out (by deleting) -- but keep headings in case maps/plans/images are added later!
- [ ] Fix all links that have [text](#) or [text](link) or [(worldcat)](WORLDCAT_LINK_URL)

# Random issues

- [ ] Bibliography first item actually two? https://roman-gardens.github.io/province/italia/rome/regio_x_palatium/domus_augustana/
- [ ] how to handle alternative names of a garden -- example https://roman-gardens.github.io/test-a/id/5c8aada6d5
- [ ] Can we show progress in number of gardens in each place?  ("23 out of 35 known gardens have been published")
- [ ]display metadata for place pages

# Images

- no spaces in filenames!  (fix in gre-images and in links from gre)
- some photos we want lower resolution (so copyright holder can control access to full resolution)
- link to reuse/take-down policy in image captions -- or link at bottom of every page?
- set permissions on image repo to prevent deletion, modification?
- images: remove alt unless it provides additional info
- handle links in captions/credits
- remove "Credit: " from display of image credit?  (Review credit values to see if they can stand on their own?)

# Cleanup

- [ ] move content from garden entries to the province _index.md
- [ ] add gre_id/aliases for places, update citation example
- [ ] id shortcode for people? (perseus authors like "Pliny the Elder")
- [ ] fix or remove empty links -- search for "(#)"
- [ ] update Leaflet from 1.6 to 1.9.4
- [ ] cleanup double/triple spaces (skip arabia-petragarden!) AFTER we have cleaned up spaces from image filenames
- should we rework the id shortcode to handle inline references?

# Keywords

- new meta page section showing UNLINKED keywords (literary gardens, etc.)
- keywords -- use glossary from GRE v.1
- keywords like lucus, nemus (recode as keyword "groves"?), oscilla, stagnum, textrina that are not proper AAT terms
- Search for any keywords mentioned in text that are not listed under the garden keywords
- public list of keywords as glossary (similiar to /meta page)

# from 2025 meetings

- [ ] people: Change Pleiades liaison from Gabriel to Tom Elliott
- [ ] maps: fix/remove blank maps
- [ ] garden list sort order (currently alphabetical, but most recent first?)
- [ ] browse by province -- only list most recent updates?

# Documentation

- [ ] use \" to escape any quotes within an image caption


# Article Guidelines

- images
    - guidelines for image filename, size, format
    - new images can be added to the gre-images repo via the GitHub website
    - upload images to the same place in the province hierarchy as the article is
    - to add the image to an article, type "image" and press CTRL-SPACE and select "GRE image shortcut"
    - check the hugo server preview to check if the image is linked correctly
    - file = filename and extension "my-image.jpg"
    - caption = caption text (should all figures be numbered for the article??)
    - credit = "Drawing by...", "Gauckler, P., 1904, pp.16-17", etc. -- standardize format?
    - alt = "" in most cases, unless we want to add additional description when the reader cannot see the image -- see https://webaim.org/techniques/alttext/ for guidance
- comment out headers of any empty sections

# Questions/Discussion

- People names -- when to include middle initial?
- People links/pages for everyone, or just prominent contributors?
- exedrae (AAT, indoor vs outdoor)
- linking words within paragraphs -- is this necessary?  too much?  consistent?
- translator in frontmatter (2 gardens)
- double angle quotes like « Pluton » -- can these be converted to normal " quotes?
- what is green highlighting for???
    - Example: https://roman-gardens.github.io/test-drafts/place/italia/pompeii/region_i/insula_ix/house_5/house_of_the_fruit_orchard/
- add area editors to province pages?
- standardize and document recommendations for entry titles
    - House name, or house number, or both? 2026: "House Name (IV.2)"
    - Roman or Arabic numerals? for region, insula, house (e.g. Pompeii VIII.4.30 vs VIII.iv.30)
- inline citations -- currently "(ALL CAPS 1895)" etc - what does AJA do?
- "Contribute" vs "Join" (Pleiades uses "Participate")
- Africa.PDF (in Box) has additional info for gardens in Mauretania (at least) -- is this an earlier or later draft???
- Should Machaerus be under Judaea or Arabia Petraea?
- Change "Places" heading to "Linked Places"?

# User forks

User forks of the old GRE repo that have updates that might not be in main GRE repo, as of 2025-03-26:
- [ ] [amartyashri](https://github.com/roman-gardens/gre-archive-2025-06-04/compare/main...amartyashri:gre-archive-2025-06-04:master) (Amartya Shri) - 28 files in Achaea, Pleaides links, removed empty sections


Stub records -- still need to check _index.md files for content or template in Italia
- Get coordinates from Pleiades records
- editorial style for including species names (hambach has two different styles)
- province boundaries
- via praenestina is the same road as via gabina
- move "tomb garden near rome" folder contents into regio_i_latium_et_campania/roma?
- 'jashemski-catalogue' exists in front matter for 86 gardens -- this could be useful for tracking progress compared to Jashemski's original list, but we would want to add these numbers to those gardens that came from ithe original documents
