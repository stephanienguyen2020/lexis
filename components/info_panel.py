import streamlit as st
import base64

def render_info_panel():
    st.markdown("""
        <style>
        .info-container {
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Wrap all content in settings container
    st.markdown('<div class="info-container">', unsafe_allow_html=True)
    
    st.markdown("### Information Panel")
    
    # Display the currently selected PDF
    if 'current_file' in st.session_state and st.session_state.get('current_file'):
        try:
            # Get the selected file from uploaded_files
            current_file = st.session_state.uploaded_files.get(st.session_state['current_file'])
            if current_file:
                st.markdown(f"**File name:** {st.session_state['current_file']}")
                # Convert PDF to base64
                base64_pdf = base64.b64encode(current_file.getvalue()).decode('utf-8')
                # Embed PDF viewer
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error displaying PDF: {str(e)}")
    else:
        st.markdown("Upload a PDF file to view its content here.")
    
    # Display search mode and selected files for search
    search_mode = st.session_state.get('search_mode')
    if search_mode == 'specific_files':
        selected_files = st.session_state.get('selected_files', [])
        if selected_files:
            st.markdown("**Selected for Search:**")
            for file in selected_files:
                st.markdown(f"- {file}")
    elif search_mode == 'all_files':
        st.markdown("**Searching in all files**")
    