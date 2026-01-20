import streamlit as st
import pandas as pd

# Cấu hình giao diện hiện đại
st.set_page_config(page_title="PVU - Chấm điểm Đồ án", layout="wide")

# Hiển thị Logo và Tiêu đề
st.sidebar.image("https://pvu.edu.vn/logo.png", width=200) # Thầy thay link logo thật ở đây
st.title("🎓 HỆ THỐNG ĐÁNH GIÁ ĐỒ ÁN - KHOA DẦU KHÍ")
st.subheader("Trường Đại học Dầu khí Việt Nam")

# --- PHẦN BACKEND (Logic xử lý dữ liệu) ---
def calculate_score(rubric_answers, weights):
    # rubric_answers: danh sách các mức 1, 2, 3, 4
    # Chuyển đổi sang thang 10: (Trung bình mức / 4) * 10
    raw_score = sum(rubric_answers) / len(rubric_answers)
    return (raw_score / 4) * 10

# --- PHẦN FRONTEND (Giao diện người dùng) ---
role = st.selectbox("Bạn là ai?", ["Thư ký", "Giảng viên Hướng dẫn", "Giảng viên Phản biện", "Hội đồng"])

if role == "Giảng viên Hướng dẫn":
    st.write("### Danh sách sinh viên hướng dẫn")
    # Giả sử lấy dữ liệu từ file students.xlsx
    selected_student = st.selectbox("Chọn sinh viên chấm điểm", ["Lưu Thị Ngọc Nhi", "Nguyễn Nhựt Đăng Khoa"])
    
    st.info(f"Đang chấm điểm cho SV: {selected_student}")
    
    # Hiển thị Rubric mức 1-4
    score1 = st.radio("1. Apply basic science", [1, 2, 3, 4], horizontal=True)
    score2 = st.radio("2. Analyze and design", [1, 2, 3, 4], horizontal=True)
    
    if st.button("Lưu kết quả"):
        final_10 = calculate_score([score1, score2], None)
        st.success(f"Đã lưu! Điểm quy đổi thang 10: {final_10:.2f}")

elif role == "Thư ký":
    st.write("### Bảng điều khiển Quản trị")
    tab1, tab2 = st.tabs(["Cấu hình Khóa", "Xuất báo cáo"])
    with tab1:
        st.number_input("Trọng số HD (%)", value=25)
        st.number_input("Trọng số PB (%)", value=25)
        st.number_input("Trọng số Hội đồng (%)", value=50)
    with tab2:
        st.button("Tải file báo cáo tổng hợp (Excel)")