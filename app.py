import streamlit as st

from prompt_prototype import phan_tich_phan_anh



st.set_page_config(

    page_title=
    "Vinhomes AI Vận hành",

    page_icon=
    "🏙️",

    layout=
    "wide"

)



st.title(
    "🏙️ Vinhomes AI Resident Intelligence System"
)


st.subheader(
    "Trợ lý AI hỗ trợ vận hành đô thị thông minh"
)


st.write(
"""
Hệ thống AI giúp ban quản lý Vinhomes:
- Phân tích phản ánh cư dân
- Xác định mức độ ưu tiên
- Đề xuất bộ phận xử lý
- Hỗ trợ ra quyết định vận hành
"""
)



st.divider()



st.header(
    "📩 Nhập phản ánh cư dân"
)



col1,col2 = st.columns(2)


with col1:

    toa_nha = st.text_input(
        "Tòa nhà",
        "S2.08"
    )


with col2:

    can_ho = st.text_input(
        "Căn hộ",
        "A1205"
    )



noi_dung = st.text_area(

    "Nội dung phản ánh",

    placeholder=
    """
Ví dụ:

Nhà tôi bị rò nước từ trần phòng ngủ,
đã 2 ngày chưa xử lý.
"""

)



if st.button(
    "🤖 Phân tích bằng AI"
):


    ticket = {


        "toa_nha":
        toa_nha,


        "can_ho":
        can_ho,


        "noi_dung":
        noi_dung

    }



    with st.spinner(
        "AI đang phân tích..."
    ):


        ket_qua = phan_tich_phan_anh(
            ticket
        )



    st.success(
        "Phân tích hoàn tất"
    )



    st.divider()



    st.header(
        "📊 Kết quả phân tích"
    )


    c1,c2,c3 = st.columns(3)


    c1.metric(

        "Loại vấn đề",

        ket_qua.get(
            "loai_van_de"
        )

    )


    c2.metric(

        "Mức độ",

        ket_qua.get(
            "muc_do"
        )

    )


    c3.metric(

        "Độ tin cậy",

        str(
            ket_qua.get(
                "do_tin_cay"
            )
        )
        +"%"

    )



    st.info(

        "📍 Bộ phận xử lý: "
        +
        ket_qua.get(
            "bo_phan",
            ""
        )

    )



    st.write(

        "⏱️ SLA đề xuất:",

        ket_qua.get(
            "sla",
            ""
        )

    )



    if ket_qua.get(
        "can_duyet_nguoi"
    ):


        st.warning(

"""
⚠️ Cần nhân viên vận hành xác nhận trước khi xử lý.
"""

        )


    else:


        st.success(

"""
✅ Đề xuất AI đã sẵn sàng để vận hành kiểm tra.
"""

        )



    with st.expander(
        "Xem dữ liệu AI trả về"
    ):


        st.json(
            ket_qua
        )