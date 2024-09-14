import streamlit as st
from forms.contact import contact_form
from utilities.footer import footer

HEADSHOT_URL = 'https://raw.githubusercontent.com/DamianCapdevila/damian-capdevila-personal-website-assets/main/Damian-sin%20fondo-gris.png'
UVP_TEXT = f"**I help engineers Unlock the Freedom, Flexibility, and Higher Income of a Software Career!**"
UVP_EXPLANATION = f"**Thrive in the digital age** by **transforming your engineering experience** into a Software Engineering Powerhouse, **without the fear or uncertainty.**"

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
    if st.button("📈 Career Mentoring", type="primary", help="Book a free initial consultation!"):
        st.switch_page("pages/services.py")
with col6:
    if st.button("📄 Resume Reviewing", type="primary", help="Get my free resume-building cheatsheet!"):
        st.switch_page("pages/services.py")
st.caption("""<p>Questions? See <a href="services#FAQ" target="_self">FAQ Section</a></p>""", unsafe_allow_html=True)

st.write("")
st.subheader("About Me", divider=True)
st.write("""*Over the last years, I [successfully transitioned from Automation Engineering into Software Development.](https://damiancapdevila.substack.com/p/from-automation-engineer-to-software) 
            Now, I want to share my experience with you!* 
         """)
if st.button("🤖 Ask my assistant about me!", use_container_width=False, type="primary"):
        st.switch_page("pages/chat.py")
st.write("")

with st.expander(label="**Skills**", icon="🛠"):
    st.write("")
    st.write("""
    - **Presales:** *Technical Consultancy, Conference Speaking, Professional English, Native Spanish*  
    - **Programming:** *C#, .NET, REST API, WPF, Blazor, MVVM, Unity Container, Nunit, Python, Streamlit*  
    - **Industrial Automation:** *PLC, HMI, Drives, Commissioning*  
    - **Tools:** *Docker, Git, Postman, Azure, Visual Studio, VSCode, Azure DevOps Platform*   
    - **Methodologies:** *Agile Software Development, Refactoring Legacy Systems, Code Reviewing* 
    """)

with st.expander(label="**Experience**", icon="👨‍🏭"):
    st.write("")
    with st.container(border=True):
        st.write("**📋 Summary**")
        st.write("""
                    - Greetings 👋🏻! I'm Damián Capdevila, an accomplished electronic engineer with **Seven years of experience spanning software development, 
                    solutions engineering, presales, automation engineering, and academic research**. 
                    
                    - My current focus is on **engineering enterprise-grade software, 
                    serving a global user base.**

                    - As an Italian and Argentinian dual citizen, **I offer versatility and can work in the EU, LATAM, or GLOBALLY REMOTE 🌎.** 
                    
                    - **Fluent in Spanish and English**, I've worked in English-Centric environments for over four years, 
                    including **hybrid/remote** roles at Siemens' International Hubs.
                """)
    
    with st.container(border=True):
        st.write("**🔎 Details**")
        st.write("- For further details, you can visit my [LinkedIn Profile](https://www.linkedin.com/in/damiancapdevila) 😎")
        st.write("")

with st.expander("**Education**", icon="👨‍🎓"):
    st.subheader("Formal Education", divider=True)
    st.write("""
    **Master of Engineering (Electronics) - National University of La Plata**  
    *La Plata, Argentina (03/2012 - 10/2017)*  
    - *[Thesis in Brain-Computer Interfaces](https://drive.google.com/file/d/1y4BDSVnrj8vulKdOlVp3ZUHFDBYpUJ_v/view?usp=drive_link) based on Stationary-state visually-evoked potentials.*
    """)

    st.subheader("Relevant Courses", divider=True)
    st.write("""
    - **Microsoft Applied Skills:** *Develop an ASP.NET Core web app that consumes an API* – [Credential](https://learn.microsoft.com/api/credentials/share/en-us/DamianCapdevila/D6A902CF0642B0D0?sharingId=975F76F04E9A23A5)
    - **University of Michigan:** *Web Application Technologies and Django* – [Credential](https://coursera.org/share/ba8303b333e48ccf6ee9b5a8a687329e)
    - **University of Michigan:** *Python for Everybody Specialization* – [Credential](https://coursera.org/share/42c74c2cf60501210dd5f0d1c214a541)
    """)

st.write("")
# Call to Action - Book an appointment
st.subheader("🗓️ Book an Appointment", divider=True)
st.write("Are you ready to start your transition into software engineering?")
if st.button("**BOOK AN APPOINTMENT**", type="primary"):
    st.switch_page("pages/services.py")

#Disclaimer
st.write("---")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

footer()