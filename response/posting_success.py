import xml.etree.ElementTree as ET
import aiohttp

async def modify_html():
    # Load the HTML file
    tree = ET.parse('posting.html')
    root = tree.getroot()
    body = root.find('.//body')
    if body is not None:
        success_element = ET.Element('p')
        success_element.text = 'success'
        body.append(success_element)
    return ET.tostring(root, encoding='unicode', method='html')


async def posting_success():
    modified_html = await modify_html()
    return aiohttp.web.Response(text=modified_html, content_type='text/html')

# <!DOCTYPE html>
# <html>
# <head>
#     <title>Text Input</title>
# </head>
# <body>
#     <form action="/save-text" method="post">
#         <textarea name="text" rows="4" cols="50"></textarea><br>
#         <input type="submit" value="Save Text">
#     </form>
# </body>
# </html>
# 