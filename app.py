# Import Python packages
import streamlit as st
from faker import Faker

# Instantiates Faker
fake = Faker()

# Function: generate_sl_xml
# Description: generates single line XML documents
def generate_sl_xml(num_docs):
    xml = ''
    for i in range(num_docs):
        xml += f'<documents> <document id="{i+1}"> <title>{fake.sentence()}</title> <date>{fake.date()}</date> <content>{fake.paragraph()}</content> </document> </documents>\n'
    return xml

# Function: generate_ml_xml
# Description: generates multi-line XML documents
def generate_ml_xml(num_docs):
    xml = '<documents>\n'
    for i in range(num_docs):
        xml += f'  <document id="{i+1}">\n'
        xml += f'    <title>{fake.sentence()}</title>\n'
        xml += f'    <author>{fake.name()}</author>\n'
        xml += f'    <date>{fake.date()}</date>\n'
        xml += f'    <content>{fake.paragraph()}</content>\n'
        xml += '  </document>\n'
    xml += '</documents>'
    return xml

# Function: main
# Description: sets up the Streamlit application logic for generating single line or multi-line XML documents
def main():
    st.title('Fake XML Generator')
    doc_type = st.selectbox("Type of XML document: ", ["", "single line", "multi-line"])
    if doc_type == "single line":
        num_docs = st.number_input('Enter the number of documents you want to generate:', min_value=0, max_value=1000000, step=1000, format='%i', key=0)
        if num_docs:
            xml = generate_sl_xml(num_docs)
            st.code(xml, language='xml')
    if doc_type == "multi-line":
        num_docs = st.number_input('Enter the number of documents you want to generate:', min_value=0, max_value=1000000, step=1000, format='%i', key=1)
        if num_docs:
            xml = generate_ml_xml(num_docs)
            st.code(xml, language='xml')
    else:
        st.write("")

# Description: executes the Python program and calls the main() function
if __name__ == '__main__':
    main()