"""
VINHOMES AI RESIDENT INTELLIGENCE SYSTEM

Vin Smart Future AI Product Prototype

Chức năng:
- Phân tích phản ánh cư dân
- Phân loại vấn đề
- Xác định mức độ ưu tiên
- Đề xuất bộ phận xử lý
- Đưa ra quyết định hỗ trợ vận hành

AI chỉ hỗ trợ quyết định.
Không thay thế con người.
"""


import os
import json

from google import genai



# ==============================
# KẾT NỐI GEMINI
# ==============================


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL = "gemini-3.6-flash"



# ==============================
# KNOWLEDGE BASE VẬN HÀNH VINHOMES
# ==============================


VINHOMES_ROUTING = {


    "Bảo trì kỹ thuật": {

        "bo_phan":
        "Đội kỹ thuật",

        "sla":
        "Trong vòng 2 giờ"

    },


    "An ninh": {

        "bo_phan":
        "Đội an ninh",

        "sla":
        "Trong vòng 15 phút"

    },


    "Vệ sinh": {

        "bo_phan":
        "Đội vệ sinh",

        "sla":
        "Trong vòng 4 giờ"

    },


    "Tiếng ồn": {

        "bo_phan":
        "Bộ phận chăm sóc cư dân",

        "sla":
        "Trong vòng 8 giờ"

    },


    "Gửi xe": {

        "bo_phan":
        "Bộ phận vận hành bãi xe",

        "sla":
        "Trong vòng 4 giờ"

    }

}




# ==============================
# RULE ENGINE AN TOÀN
# ==============================


def kiem_tra_khan_cap(noi_dung):


    tu_khoa = [

        "cháy",
        "rò điện",
        "kẹt thang máy",
        "ngập nước",
        "nguy hiểm"

    ]


    for tu in tu_khoa:

        if tu in noi_dung.lower():

            return True


    return False




# ==============================
# FALLBACK AI LOCAL
# ==============================


def local_ai(noi_dung, ticket):


    text = noi_dung.lower()



    if "nước" in text or "rò" in text:


        return {

            "loai_van_de":
            "Bảo trì kỹ thuật",

            "mo_ta":
            noi_dung,

            "muc_do":
            "Cao",

            "do_tin_cay":
            92,

            "ly_do":
            "Phát hiện phản ánh liên quan đến rò rỉ nước"

        }



    if "ồn" in text or "nhạc" in text:


        return {

            "loai_van_de":
            "Tiếng ồn",

            "mo_ta":
            noi_dung,

            "muc_do":
            "Trung bình",

            "do_tin_cay":
            90,

            "ly_do":
            "Phát hiện phản ánh tiếng ồn"

        }



    return {

        "loai_van_de":
        "Chăm sóc cư dân",

        "mo_ta":
        noi_dung,

        "muc_do":
        "Thấp",

        "do_tin_cay":
        70,

        "ly_do":
        "Cần nhân viên xác minh thêm"

    }




# ==============================
# AI ANALYSIS
# ==============================


def phan_tich_phan_anh(ticket):


    noi_dung = ticket["noi_dung"]



    # Kiểm tra sự cố nguy hiểm trước


    if kiem_tra_khan_cap(noi_dung):


        return {

            "loai_van_de":
            "Sự cố khẩn cấp",

            "muc_do":
            "Rất cao",

            "bo_phan":
            "Đội xử lý khẩn cấp",

            "sla":
            "Xử lý ngay",

            "do_tin_cay":
            100,

            "can_duyet_nguoi":
            True

        }



    prompt = """

Bạn là trợ lý AI vận hành đô thị Vinhomes.

Hãy phân tích phản ánh cư dân.

Trả về JSON:

{
"loai_van_de":"",
"muc_do":"",
"mo_ta":"",
"do_tin_cay":0
}

Không đưa ra quyết định cuối cùng.
Chỉ hỗ trợ nhân viên vận hành.

"""



    try:


        response = client.models.generate_content(

            model=MODEL,

            contents=[

                prompt,

                f"""

Tòa nhà:
{ticket['toa_nha']}


Căn hộ:
{ticket['can_ho']}


Phản ánh:

{noi_dung}

"""

            ]

        )



        result = json.loads(
            response.text
        )



    except Exception:


        result = local_ai(
            noi_dung,
            ticket
        )



    loai = result.get(
        "loai_van_de",
        "Bảo trì kỹ thuật"
    )


    routing = VINHOMES_ROUTING.get(

        loai,

        VINHOMES_ROUTING[
            "Bảo trì kỹ thuật"
        ]

    )



    result["bo_phan"] = (
        routing["bo_phan"]
    )


    result["sla"] = (
        routing["sla"]
    )



    result["can_duyet_nguoi"] = (

        result.get(
            "do_tin_cay",
            0
        )
        < 80

    )


    return result