import os
import shutil
from bs4 import BeautifulSoup

# Path to the Streamlit package directory
streamlit_path = '/usr/local/lib/python3.9/site-packages/streamlit/static/index.html'

# Create a backup of the original index.html
shutil.copy2(streamlit_path, streamlit_path + '.bak')

# Read the original index.html
with open(streamlit_path, 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Create new meta tags
meta_tags = [
    # General SEO
    {'name': 'description', 'content': 'Damián Capdevila helps engineers unlock the freedom, flexibility, and high income of a software career. Expert guidance for your transition into software engineering.'},
    
    # Open Graph / Facebook
    {'property': 'og:type', 'content': 'website'},
    {'property': 'og:url', 'content': 'https://damiancapdevila.com'},
    {'property': 'og:title', 'content': 'Damián Capdevila - Software Engineer'},
    {'property': 'og:description', 'content': 'Unlock your potential in software engineering with expert guidance from Damián Capdevila.'},
    {'property': 'og:image', 'content': 'https://raw.githubusercontent.com/DamianCapdevila/damian-capdevila-personal-website-assets/main/Damian-sin%20fondo-gris.webp'},
    
    # Twitter
    {'name': 'twitter:card', 'content': 'summary_large_image'},
    {'name': 'twitter:url', 'content': 'https://damiancapdevila.com'},
    {'name': 'twitter:title', 'content': 'Damián Capdevila - Software Engineer'},
    {'name': 'twitter:description', 'content': 'Unlock your potential in software engineering with expert guidance from Damián Capdevila.'},
    {'name': 'twitter:image', 'content': 'https://raw.githubusercontent.com/DamianCapdevila/damian-capdevila-personal-website-assets/main/Damian-sin%20fondo-gris.webp'},
    
    # LinkedIn
    {'name': 'linkedin:title', 'content': 'Damián Capdevila - Software Engineer'},
    {'name': 'linkedin:description', 'content': 'Unlock your potential in software engineering with expert guidance from Damián Capdevila.'},
    {'name': 'linkedin:image', 'content': 'https://raw.githubusercontent.com/DamianCapdevila/damian-capdevila-personal-website-assets/main/Damian-sin%20fondo-gris.webp'},
    
    # Additional tags
    {'name': 'author', 'content': 'Damián Capdevila'},
    {'name': 'keywords', 'content': 'software engineering, career transition, engineering, consulting, mentorship'},
]

# Add new meta tags to the head
for tag in meta_tags:
    new_tag = soup.new_tag('meta')
    for key, value in tag.items():
        new_tag[key] = value
    soup.head.append(new_tag)

# Save the modified HTML
with open(streamlit_path, 'w') as file:
    file.write(str(soup))

print("Meta tags have been added to the Streamlit index.html file.")
