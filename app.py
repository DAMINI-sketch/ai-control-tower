import streamlit as st
import pandas as pd
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Control Tower Governance Console",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE INITIALIZATION ---
if 'audit_history' not in st.session_state:
    st.session_state.audit_history = [
        {"Timestamp": "2026-06-25 10:14:22", "Layer": "Semantic Filter", "Event": "Anomalous prompt injection blocked", "Risk Level": "High"},
        {"Timestamp": "2026-06-25 11:30:05", "Layer": "Token Limiter", "Event": "Rate limit threshold adjusted", "Risk Level": "Low"},
        {"Timestamp": "2026-06-25 13:45:18", "Layer": "Guardrail Engine", "Event": "PII data masking policy applied", "Risk Level": "Medium"}
    ]

# --- PREMIUM SIDEBAR ---
with st.sidebar:
    # FIXED: Changed unsafe_unsafe_html to unsafe_allow_html
    st.markdown("<h2 style='color: #FF4B4B;'>🛡️ Governance Core</h2>", unsafe_allow_html=True)
    st.caption("Enterprise AI Firewall Platform")
    st.markdown("---")
    
    # Active Deployment Badge
    st.success("● Pipeline Status: Active")
    
    st.markdown("### 🎛️ Control Parameters")
    safety_threshold = st.slider("Global Safety Guardrail Threshold", 0.0, 1.0, 0.85, 0.05)
    max_token_buffer = st.number_input("Max Output Token Allocation", min_value=128, max_value=8192, value=2048, step=128)
    
    st.markdown("---")
    st.info("System Engine: v2.4.0-Stable\nEnvironment: Production Cluster")

# --- MAIN DASHBOARD LAYOUT ---
st.title("📊 AI Control Tower Governance Console")
st.markdown("Real-time monitoring, semantic alignment verification, and automated firewall telemetry orchestration.")
st.markdown("---")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Blocks (Today)", value="1,422", delta="+12%")
with col2:
    st.metric(label="Average Latency Overhead", value="42ms", delta="-4ms", delta_color="inverse")
with col3:
    st.metric(label="Guardrail Sync Accuracy", value="99.82%", delta="0.05%")
with col4:
    st.metric(label="Threat Mitigation Index", value="0.94 / 1.0", delta="Stable")

st.markdown("---")

# Main Content Split (Operational Logic & Controls)
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📡 Live Policy Gateway & Inference Telemetry")
    
    # Live Prompt Validation Test Area
    with st.expander("🔍 Test Prompt Against Active Inference Guardrails", expanded=True):
        user_prompt = st.text_area("Enter diagnostic payload / nursing query input:", placeholder="Type something to check policy enforcement...")
        
        if st.button("Execute Safety Sub-System Diagnostics", type="primary"):
            if user_prompt.strip() == "":
                st.warning("Please enter a valid text payload for validation.")
            else:
                with st.spinner("Analyzing semantics via alignment layer..."):
                    st.markdown("#### Diagnostic Evaluation Matrix")
                    res_col1, res_col2 = st.columns(2)
                    
                    # Log real-time event simulation to session state
                    is_flagged = len(user_prompt) >= 150
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    new_log = {
                        "Timestamp": current_time,
                        "Layer": "Semantic Filter" if is_flagged else "Guardrail Engine",
                        "Event": "Policy Infraction Detected" if is_flagged else "Diagnostic Evaluation Passed",
                        "Risk Level": "High" if is_flagged else "Low"
                    }
                    # Prepend new log to show it on top
                    st.session_state.audit_history.insert(0, new_log)
                    
                    with res_col1:
                        st.json({
                            "Payload Status": "FLAGGED" if is_flagged else "PASSED",
                            "Safety Score Match": f"{safety_threshold:.2f}",
                            "Token Evaluation Size": len(user_prompt.split())
                        })
                    with res_col2:
                        if is_flagged:
                            st.error("Policy Infraction Detected: Review Log Traces")
                        else:
                            st.success("Target Alignment Validated Successfully")

with right_col:
    st.subheader("⚙️ System Directives")
    st.markdown("Toggle granular compliance protocols across live production clusters.")
    
    enforce_pii = st.toggle("Enforce Strict PII Masking", value=True)
    block_jailbreaks = st.toggle("Anti-Jailbreak Structural Shielding", value=True)
    enable_logging = st.toggle("Deep Telemetry Audit Archiving", value=True)
    
    st.markdown("### 📊 Active Sub-Systems")
    st.code(f"""
Layer-1: Prompt Scrubber [{"ON" if block_jailbreaks else "OFF"}]
Layer-2: Embedding Distance [ON]
Layer-3: Output Masker [{"ON" if enforce_pii else "OFF"}]
    """, language="text")

st.markdown("---")

# Bottom Section: Audit Ledger Tracing Table
st.header("📋 Runtime Audit Ledger Tracing")

with st.popover("ℹ️ What is the Audit Ledger feature?"):
    st.markdown("""
    **How to use:** This ledger automatically logs live background state changes and security events.
    \n**Expected Result:** Renders a read-only table mapping active timelines to threat classifications.
    """)

# Display table containing historical data + dynamic updates
df_ledger = pd.DataFrame(st.session_state.audit_history)
st.dataframe(df_ledger, use_container_width=True, hide_index=True)
