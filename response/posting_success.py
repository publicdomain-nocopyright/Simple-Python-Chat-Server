import xml.etree.ElementTree as ET
import aiohttp

import xml.etree.ElementTree as ET

async def modify_html(file):
    try:
        # Load the HTML file
        with open(file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Correct the HTML content
        html_content = html_content.replace('<br>', '<br/>').replace('&', '&amp;')

        # Wrap the HTML content in a single root element
        wrapped_html_content = f"<root>{html_content}</root>"

        # Parse the HTML content
        root = ET.fromstring(wrapped_html_content)

        # Find the body element
        body = root.find('.//body')
        if body is not None:
            # Create and append the success element
            success_element = ET.Element('p')
            success_element.text = 'success'
            body.append(success_element)
        
        # Get the inner content of the root
        body_content = ''.join(ET.tostring(e, encoding='unicode', method='html') for e in root)
        
        # Remove the wrapping root element tags
        body_content = body_content.replace('<root>', '').replace('</root>', '')

        return body_content

    except ET.ParseError as e:
        print(f"Error parsing HTML file: {e}")
        return None




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