from io import StringIO
import streamlit as st
from backend import process


def _main():
    st.title('Simple Text Summary')

    st.write('You can get summary from texts either from input area or from uploaded file!')

    form = st.form('input_text_form')
    txt = form.text_area('Input text to get summary')
    uploaded_file = form.file_uploader('Or upload a file', type=['txt'])
    submitted = form.form_submit_button('Submit')

    model = process.Summarizer()

    if submitted:
        text = ''
        file_name = 'Summary.txt'
        if uploaded_file is not None:
            file_name = uploaded_file.name[:-len('.txt')] + ' summary.txt'
            text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        else:
            text = txt

        if text != '':
            st.download_button('Download summary', model.make_summary(text), file_name)
        else:
            st.error('Input is empty')


if __name__ == '__main__':
    _main()
