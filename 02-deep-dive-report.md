# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
Chúng ta chọn bài toán: “Tự động phân loại và điều phối sự cố kỹ thuật từ phản ánh cư dân đến bộ phận xử lý đúng người tại Vinhomes”.

### Workflow hiện tại
1. Cư dân gửi phản ánh qua App Vinhomes Resident / hotline / email / chat.  
2. Nhân viên CSKH hoặc văn phòng nhận tin, đọc và tóm tắt nội dung.  
3. Nhân viên phân loại lỗi theo lĩnh vực: điện, nước, điều hòa, thẻ từ, thang máy, vệ sinh…  
4. Nhân viên kiểm tra vị trí tòa nhà / căn hộ / tầng / mã căn hộ để xác định đội xử lý phù hợp.  
5. Ticket được chuyển đến đội kỹ thuật hoặc Ban Quản Lý tòa nhà và cập nhật trạng thái bằng tay.  
6. Đội kỹ thuật xử lý sự cố và phản hồi lại cho cư dân.

### Handoff / Bottleneck
- 🔄 Handoff: từ cư dân -> CSKH -> Ban Quản Lý -> đội kỹ thuật -> cư dân.  
- 🔴 Bottleneck: Bước “phân loại và điều phối sự cố” tốn nhiều thời gian vì thông tin đầu vào là ngôn ngữ tự do, không chuẩn hóa, và nhiều lần chuyển sai bộ phận.  
- Tổng thời gian quy trình hiện tại trung bình: khoảng 25–35 phút/lượt, trong đó phân loại và gán đội chiếm 15–25 phút.

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên CSKH, văn phòng quản lý tòa nhà, đội kỹ thuật, Ban Quản Lý cư dân. |
| **2. Current Workflow** | Cư dân gửi phản ánh sự cố kỹ thuật; nhân viên đọc tin nhắn; phân loại theo loại sự cố; xác định khu vực và đội xử lý; đề xuất/tạo ticket; chuyển cho đội kỹ thuật; cập nhật tiến độ. Công cụ chủ yếu là App Vinhomes Resident, email, hotline, sheet Excel/ticket nội bộ và hệ thống quản lý tòa nhà. |
| **3. Bottleneck** | Bước đọc và hiểu tiếng tự do của cư dân, sau đó gán loại sự cố, mức độ ưu tiên và bộ phận xử lý phù hợp. Đây là bước nhiều sai lệch, mất thời gian và làm tăng thời gian phản hồi. |
| **4. Business Impact** | Mỗi ticket sai phân loại hoặc chuyển nhầm team làm tăng thời gian xử lý, tăng số vòng phản hồi, giảm SLA, khiến cư dân không hài lòng. Đối với 1.000 sự cố/tháng, nếu sai routing 10% thì cơ sở quản lý phải bổ sung thêm 150–250 lượt xử lý thủ công. |
| **5. Success Metric** | AI giúp đạt: 90% ticket được phân loại đúng loại sự cố và gán đúng bộ phận trong dưới 60 giây; giảm thời gian phân loại từ 15 phút xuống dưới 2 phút; tỷ lệ route sai giảm dưới 5%. |
| **6. Operational Boundary** | AI được phép: tóm tắt tiếng tự do của cư dân, trích xuất loại sự cố, vị trí, mức độ khẩn cấp, và đề xuất bộ phận/đội xử lý. AI tuyệt đối không được: tự động chốt sửa chữa, hứa hẹn thời gian xử lý hoặc quyết định bồi thường; AI không được tự động đóng ticket hay thay mặt con người phản hồi; mọi quyết định khẩn cấp cần nhân viên CSKH/BQL xác nhận. |

## 3.3. Future-State Flow & AI Fit (25 min)

### AI Fit
Chúng ta chọn mức AI Fit: **LLM Feature**.  
Vì bài toán là xử lý ngôn ngữ tự do của cư dân, cần suy diễn ngữ nghĩa và trích xuất dữ liệu không có cấu trúc. Tuy nhiên, quy định routing/policy và team assignment nên dùng **Rule/State-Machine** kết hợp với LLM.

### Future-State Flow
1. Cư dân gửi phản ánh thông qua App / hotline / email.  
2. 🔵 AI Step: LLM đọc và tóm tắt nội dung, trích xuất lĩnh vực, vị trí căn hộ/tòa nhà, mức độ ưu tiên, và gợi ý loại sự cố.  
3. 🔵 AI Step: LLM sinh draft ticket chuẩn hóa theo template nội bộ.  
4. 🟢 Human Step (HITL): Nhân viên CSKH/BQL review ticket và xác nhận loại sự cố / mức ưu tiên / đội xử lý.  
5. ↩️ Fallback: Nếu AI không đủ tự tin hoặc thông tin thiếu, hệ thống chuyển sang workflow manual: nhân viên tiếp nhận bằng tay và yêu cầu bổ sung thông tin.  
6. 🟢 Human Step (HITL): Đội kỹ thuật xử lý sự cố và cập nhật trạng thái.  
7. 🔵 AI Step: LLM có thể hỗ trợ tóm tắt tiến độ và viết phản hồi lại cho cư dân.

### AI Fit Matrix
- **LLM Feature**: tóm tắt hotline/app/phản ánh, trích xuất loại sự cố, mapping loại sự cố -> team, sinh draft ticket.  
- **Rule / State-Machine**: xác thực thông tin bắt buộc như căn hộ, tòa, khu vực; gán phân loại tiêu chuẩn và mức SLA.  
- **Human-in-the-loop**: quyết định cuối cùng về team dispatch và phản hồi chốt.

### Ranh giới vận hành
- AI được phép: phân loại ticket, đề xuất đội xử lý, chuẩn hóa nội dung, sinh draft phản hồi.  
- AI không được phép: tự động cập nhật lịch sửa chữa, tự động xác nhận tình trạng đã sửa, hay phản hồi với cam kết thời gian xử lý mà không có phê duyệt của người vận hành.  
- Cần có check: “AI confidence < 0.8 hoặc nội dung thiếu vị trí/tòa/căn hộ” thì đẩy sang fallback.

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.  
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.  
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Chúng tôi chọn quyết định **GO với scope hẹp** cho bài toán “tự động phân loại và điều phối sự cố kỹ thuật từ phản ánh cư dân trong Vinhomes”.  
> Lý do: bài toán có nguồn dữ liệu đầu vào là văn bản tự do từ các kênh như App Vinhomes Resident, hotline, email, chat, nên AI/LLM có khả năng tóm tắt, trích xuất loại sự cố, xác định mức độ khẩn cấp và đề xuất bộ phận xử lý nhanh hơn quy trình thủ công.  
> Bên cạnh đó, bài toán có thể kiểm soát được rủi ro bằng **Human-in-the-Loop (HITL)**: nhân viên CSKH/BQL xác nhận phân loại, ưu tiên và đội xử lý trước khi chuyển ticket.  
> Về kỹ thuật, AI không cần tự quyết định sửa chữa hay cập nhật lịch xử lý, nên rủi ro là ít hơn và dễ kiểm soát. Bài toán cũng có thể triển khai theo mô hình **LLM Feature + Rule/State-Machine** để tăng độ tin cậy: LLM làm tóm tắt và phân loại, rule engine xác thực thông tin bắt buộc và kiểm tra routing.  
> Về kinh tế, nếu quy trình hiện tại tốn 15–25 phút/lượt cho phân loại và gán sự cố, việc giảm xuống dưới 2 phút cho một phần lớn ticket sẽ mang lại hiệu quả trực tiếp thông qua giảm thời gian xử lý, giảm số vòng phản hồi, và cải thiện SLA.  
> Tuy nhiên, dự án này nên bắt đầu với scope hẹp: chỉ hỗ trợ tóm tắt, phân loại loại sự cố, xác định khu vực và đề xuất đội xử lý; tránh tự động hành động trong các trường hợp khẩn cấp hoặc bồi thường. Vì vậy, quyết định GO với prototype có ranh giới rõ ràng là phù hợp và có thể đo lường hiệu quả bằng tỷ lệ route đúng, thời gian xử lý, và tỷ lệ ticket thiếu thông tin.