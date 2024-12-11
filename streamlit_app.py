import streamlit as st
import pandas as pd
from pathlib import Path
import os

# Resolve paths dynamically to handle bundled executables
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo_path = current_dir / "Logo1.jpg"

# The app begins here!
st.title('Desktop App')
st.caption('Made by Brian')

# Add the logo and image if the file exists
if logo_path.is_file():
    st.logo(str(logo_path))
    st.image(str(logo_path))
else:
    st.warning("Logo not found. Ensure 'Logo1.jpg' is in the correct directory.")


st.header("Directory File Lister")
# Input field for the directory path
dir_path = st.text_input("Enter the path of the directory:")

if dir_path:
    try:
        # Check if the path exists and is a directory
        if os.path.isdir(dir_path):
            # List files in the directory
            files = os.listdir(dir_path)
            if files:
                st.write(f"Files in `{dir_path}`:")
                for file in files:
                    st.write(f"- {file}")
            else:
                st.write("The directory is empty.")
        else:
            st.error("The provided path is not a valid directory.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter a directory path to list its files.")
