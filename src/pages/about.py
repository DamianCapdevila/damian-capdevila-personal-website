import streamlit as st
import time
from forms.contact import contact_form
import utilities.helper

HEADSHOT_URL = 'https://raw.githubusercontent.com/DamianCapdevila/damian-capdevila-personal-website-assets/main/Damian-sin%20fondo-gris.png'
UVP_TEXT = f"**I help Engineers Unlock the Freedom, Flexibility, and High Income of a Software Career!** 💻🌎"
UVP_EXPLANATION = f"**Thrive in the digital age** by **transforming your engineering experience** into a Software Engineering Powerhouse, **without the fear or uncertainty.**"
ACTIONABLE_STEPS_URL = 'https://damiancapdevila.substack.com/i/144652439/actionable-steps-if-you-want-to-make-the-transition'
col1, col2 = st.columns(2, gap='small', vertical_alignment="top")

with col1:
    st.image(HEADSHOT_URL, output_format="PNG", width=300)
with col2:
    st.title("Damián Capdevila", anchor=False)
    st.write(UVP_TEXT)
    st.write(f"*{UVP_EXPLANATION}*")
        
st.subheader("Providing Services", divider=True)
st.write("*Are you ready to start your transition into software engineering?*")
col5, col6, col7 = st.columns(3, gap='small', vertical_alignment="center")
with col5:
    if st.button("📈 FREE Initial Consultation!", type="primary", help="**Book a free initial consultation!**"):
        st.switch_page("pages/services.py")
with col6:
    st.link_button("💡 See Actionable Advice", url=ACTIONABLE_STEPS_URL, type="secondary", help="**See 8 steps to begin your transition!**")

utilities.helper.faq()

st.write("")
st.subheader("About Me", divider=True)
st.write("""*Over the last years, I [successfully transitioned from Automation Engineering into Software Development.](https://damiancapdevila.substack.com/p/from-automation-engineer-to-software) 
            Now, I want to share my experience with you!* 
         """)
st.write("")

with st.expander(label="**Experience**", icon="👨‍🏭"):
    st.write("")
    with st.container(border=False):
        st.write("""
                    - Greetings 👋🏻! I'm Damián Capdevila, an accomplished electronic engineer with **Seven years of experience** spanning **Software Engineering, 
                    Automation Engineering, Solutions Engineering, Pre-sales, and Academic Research**. 
                    
                    - My current focus is on **engineering enterprise-grade software, 
                    serving a global user base.**

                    - As an Italian and Argentinian dual citizen, **I offer versatility and can work in the EU, LATAM, or GLOBALLY REMOTE 🌎.** 
                    
                    - **Fluent in Spanish and English**, I've worked in English-Centric environments for over four years, 
                    including **hybrid/remote** roles at Siemens' International Hubs.
                """)
    
        st.write("- For further details, you can visit my [LinkedIn Profile](https://www.linkedin.com/in/damiancapdevila) 😎")
        st.write("")

with st.expander("**Education**", icon="👨‍🎓"):
    st.subheader("Formal Education", divider=True)
    st.write("""
    **Master of Engineering (Electronics) - National University of La Plata**  
    *La Plata, Argentina (03/2012 - 10/2017)*  
    - *[Thesis in Brain-Computer Interfaces 🧠](https://drive.google.com/file/d/1y4BDSVnrj8vulKdOlVp3ZUHFDBYpUJ_v/view?usp=drive_link) based on Stationary-state visually-evoked potentials.*
    """)

    st.subheader("Relevant Courses", divider=True)
    st.write("""
    - **Microsoft Applied Skills:** *Develop an ASP.NET Core web app that consumes an API* – [Credential](https://learn.microsoft.com/api/credentials/share/en-us/DamianCapdevila/D6A902CF0642B0D0?sharingId=975F76F04E9A23A5)
    - **University of Michigan:** *Web Application Technologies and Django* – [Credential](https://coursera.org/share/ba8303b333e48ccf6ee9b5a8a687329e)
    - **University of Michigan:** *Python for Everybody Specialization* – [Credential](https://coursera.org/share/42c74c2cf60501210dd5f0d1c214a541)
    - [Full list of courses here! 👨🏻‍🏫](https://www.linkedin.com/in/damiancapdevila/details/certifications/)
    """)

with st.expander(label="**Skills**", icon="🛠"):
    st.write("")
    st.write("""
    - 📣 **Presales:** *Technical Consultancy, Conference Speaking, Professional English, Native Spanish*  
    - 💻 **Programming:** *C#, .NET, REST API, WPF, Blazor, MVVM, Nunit, Python, Streamlit*  
    - 👷🏻‍♂️ **Industrial Automation:** *PLC, HMI, Drives, Commissioning, TIA Portal, RS Logix*  
    - 🔧 **Tools:** *Docker, Git, Postman, Azure, Visual Studio, VSCode, Azure DevOps Platform*   
    - 🥋 **Methodologies:** *Agile Software Development, Refactoring Legacy Systems, Code Reviewing* 
    """)
    st.write("")

st.write("")
utilities.helper.call_to_action()
utilities.helper.faq()

#Disclaimer
st.write("---")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

utilities.helper.footer()