import streamlit as st
from src.adjustment_agent import AdjustmentAgent
import json

st.set_page_config(layout="wide")
st.title("📊 Manual Adjustments Validation Agent")

coa_file = st.file_uploader("Upload COA CSV", type=["csv"])
adj_file = st.file_uploader("Upload Adjustments JSON", type=["json"])

if coa_file and adj_file:

    if st.button("Run Validation 🚀"):

        agent = AdjustmentAgent(coa_file)
        results = agent.process(adj_file)

        st.success("Processing Complete")

        col1, col2, col3 = st.columns(3)
        col1.metric("Valid", len(results["valid"]))
        col2.metric("Rejected", len(results["rejected"]))
        col3.metric("Flagged", len(results["flagged"]))

        tab1, tab2, tab3 = st.tabs(["Valid", "Rejected", "Flagged"])

        with tab1:
            st.json(results["valid"])

        with tab2:
            for r in results["rejected"]:
                with st.expander(f"Entry {r['entry_id']}"):
                    st.error("Errors")
                    st.write(r["errors"])
                    st.info("Explanation")
                    st.write(r["explanation"])

        with tab3:
            st.json(results["flagged"])

        st.download_button(
            "Download Results",
            data=json.dumps(results, indent=2),
            file_name="results.json"
        )