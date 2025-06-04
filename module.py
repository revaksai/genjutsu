import streamlit as st
import time

st.set_page_config(page_title="Floating Modal UI", layout="centered")

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "GPT-4"
if "show_model_dropdown" not in st.session_state:
    st.session_state.show_model_dropdown = False
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False
if "just_selected_model" not in st.session_state:
    st.session_state.just_selected_model = False

st.session_state.query = ""

def open_modal():
    st.session_state.show_modal = True

def close_modal():
    st.session_state.show_modal = False
    st.rerun()

def toggle_model_dropdown():
    st.session_state.show_model_dropdown = not st.session_state.show_model_dropdown

def select_model_callback():
    st.session_state.selected_model = st.session_state.selected_model_dropdown
    st.session_state.just_selected_model = True

col1, col2, col3, col4 = st.columns([0.08, 0.16, 0.64, 0.12])
with col1:
    st.button("➕", on_click=open_modal, use_container_width=True)

with col2:
    st.button(f"{st.session_state.selected_model} ▼", on_click=toggle_model_dropdown, use_container_width=True)
with col3:
    user_input = st.text_input(" ", placeholder="Ask something...", label_visibility="collapsed",key="query")

with col4:
    submit = st.button("✈️", use_container_width=True)
    # query = st.session_state.query.strip()
    # if query:
    #     # Enabled submit button with styles
    #     submit = st.button("✈️", use_container_width=True)
    #     st.markdown("""
    #         <style>
    #         div.stButton > button {
    #             background-color: #0059f7 !important;
    #             color: white !important;
    #             border-radius: 8px;
    #             font-weight: 600;
    #             border: none;
    #             cursor: pointer !important;
    #             transition: background-color 0.2s ease;
    #         }
    #         div.stButton > button:hover {
    #             background-color: #0043c1 !important;
    #         }
    #         </style>
    #     """, unsafe_allow_html=True)
    # else:
    #     # Disabled-looking button as a non-clickable div
    #     st.markdown("""
    #         <div style="
    #             background-color: white;
    #             color: grey;
    #             border-radius: 8px;
    #             padding: 0.5em 0;
    #             border: 1px solid #ccc;
    #             cursor: not-allowed;
    #             text-align: center;
    #             font-weight: 600;
    #             width: 100%;
    #             user-select: none;
    #         ">✈️</div>
    #     """, unsafe_allow_html=True)
    #     submit = False
if st.session_state.show_modal:
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded.")
        for f in uploaded_files:
            st.write(f.name)
    if st.button("❌ Close"):
        close_modal()
    st.markdown("</div>", unsafe_allow_html=True)
if st.session_state.show_model_dropdown:
    model = st.selectbox(
        "Choose a model",
        ["GPT-4", "GPT-3.5", "Davinci", "Curie"],
        key="selected_model_dropdown",
        on_change=select_model_callback,
        label_visibility="collapsed"
    )
    st.write(f"✅ Selected Model: **{st.session_state.selected_model}**")
if st.session_state.just_selected_model:
    st.session_state.show_model_dropdown = False
    st.session_state.just_selected_model = False
    st.rerun()

if submit:
    if st.session_state.query == "":
        st.error("Empty query")
    else:
        st.write(f"🔍submitted")
        time.sleep(2)
    close_modal()

