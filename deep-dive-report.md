# PHASE 3 & PHASE 5: DEEP-DIVE REPORT & EVALUATION
**Dự án:** Vinhomes Smart Resident Complaint Dispatcher & Response Generator  
**Đơn vị:** Vin Smart Future (Vingroup)  
**Tác giả / Nhóm thực hiện:** Nguyễn Đức Anh (nguyenducanhflm@gmail.com) — AI Product Engineer  

---

## 🏛️ 1. Giới thiệu dự án

Dự án **Vinhomes Smart Resident Complaint Dispatcher** được xây dựng nhằm phối hợp giữa khối công nghệ **Vin Smart Future** và **Khối Vận hành Vinhomes (Vingroup)**. Dự án tập trung giải quyết điểm nghẽn trong khâu tiếp nhận, phân loại và điều hướng phản ánh của cư dân trên ứng dụng **Vinhomes Resident App**, nhằm nâng cao trải nghiệm sống thông minh và tối ưu hóa thời gian xử lý của Ban quản lý (BQL) tòa nhà.

---

## 🏗️ Phase 3 — DEEP-DIVE (Báo cáo Phân tích sâu)

### 3.1. Current-State Workflow Mapping (Sơ đồ quy trình hiện tại)

Quy trình tiếp nhận & phản hồi khiếu nại cư dân thủ công của Ban quản lý Vinhomes:

```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Bước 1          │      │ Bước 2 🔴       │      │ Bước 3 🔴       │      │ Bước 4          │
│ Cư dân gửi      │ ───> │ Đọc & Phân loại │ ───> │ Chuyển ticket   │ ───> │ Bộ phận chuyên  │
│ ticket qua App  │      │ thủ công nhóm YC│      │ cho BQL/Kỹ thuật│      │ trách xử lý     │
│                 │      │                 │      │                 │      │                 │
│ Ai: Cư dân      │      │ Ai: Tiếp tân BQL│      │ Ai: Tiếp tân BQL│      │ Ai: Kỹ thuật/AN │
│ ⏱ 3 phút        │      │ ⏱ 4-6 giờ 🔴    │      │ ⏱ 2-4 giờ 🔴    │      │ ⏱ 2-6 giờ       │
│ In: App form    │      │ In: Text thô    │      │ In: Danh mục    │      │ In: Yêu cầu XL  │
│ Out: Ticket thô │      │ Out: Nhóm sự cố │      │ Out: Tag bộ phận│      │ Out: Kết quả XL │
└─────────────────┘      └─────────────────┘      └─────────────────┘      └─────────────────┘
                                                                                    │
                                                                                    ▼
                                                                           ┌─────────────────┐
                                                                           │ Bước 5 🔴       │
                                                                           │ Soạn phản hồi   │
                                                                           │ gửi cư dân      │
                                                                           │ Ai: Tiếp tân BQL│
                                                                           │ ⏱ 1-2 giờ 🔴    │
                                                                           │ Out: SMS/App msg│
                                                                           └─────────────────┘

🔴 = Bottleneck (Điểm tắc nghẽn chính: Mất 12-24 giờ delay ở khâu đọc, phân loại, chuyển tiếp & soạn phản hồi)
🔄 = Handoff (Chuyển giao thông tin từ App cư dân -> Tiếp tân BQL -> Trưởng bộ phận Kỹ thuật/An ninh -> Cư dân)
⏱ Tổng thời gian phản hồi thủ công hiện tại: 12 – 24 giờ / ticket.
```

---

### 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Tiếp tân & Cán bộ Điều phối thuộc Ban Quản lý (BQL) Tòa nhà Vinhomes. |
| **2. Current Workflow** | Cư dân gửi phản ánh (hỏng đèn, rò rỉ nước, tiếng ồn, thẻ xe...) qua App Vinhomes Resident. Tiếp tân BQL đọc thủ công từng văn bản tiếng Việt, tự phân loại nhóm sự cố, chuyển tiếp thủ công đến đúng trưởng bộ phận (Kỹ thuật/An ninh/Vệ sinh), và soạn phản hồi thủ công gửi lại cư dân. |
| **3. Bottleneck** | **Bước 2, 3 & 5 (mất 12–24 giờ SLA):** Tiếp tân bị ngợp trước lượng lớn ticket (>300 ticket/ngày/đại đô thị), dẫn đến phân loại trễ, chuyển nhầm bộ phận hoặc trả lời rập khuôn, gây bức xúc cho cư dân. |
| **4. Business Impact** | Làm giảm chỉ số hài lòng cư dân (CSAT), gây ra các cuộc tranh cãi trên các diễn đàn cư dân Vinhomes, lãng phí ~18 giờ làm việc/ngày của tiếp tân cho các tác vụ phân loại và soạn văn bản hành chính lặp đi lặp lại. |
| **5. Success Metric** | **1.** Giảm thời gian tiếp nhận, phân loại & phản hồi ban đầu từ **12 giờ xuống dưới 15 phút** (Hiệu suất).<br>**2.** Tỉ lệ phân loại đúng nhóm sự cố và bộ phận chuyên trách đạt **≥ 95%** (Chất lượng). |
| **6. Operational Boundary** | **ĐƯỢC PHÉP:** AI được phân tích nội dung tiếng Việt của ticket, gán tag danh mục (Kỹ thuật/Vệ sinh/An ninh/Thủ tục), đánh giá mức độ khẩn cấp (Thấp/Trung bình/Khẩn/Nguy hiểm), và soạn phản hồi nháp lịch sự có nhãn bắt buộc `[DRAFT_RESPONSE]`.<br>**TUYỆT ĐỐI CẤM:** <br>1. AI **tuyệt đối không được tự động gửi phản hồi** tới cư dân khi chưa được Tiếp tân BQL bấm duyệt (Bắt buộc HITL).<br>2. AI **tuyệt đối không được tự cam kết miễn giảm phí dịch vụ, bồi thường tài chính** hoặc đưa ra phát ngôn pháp lý đại diện cho Vinhomes.<br>3. Đối với sự cố **Nguy hiểm khẩn cấp (Rò rỉ khí gas, kẹt thang máy, cháy nổ, ngập nước nghiêm trọng)**, AI tuyệt đối không được đưa ra thời gian chờ 24h thông thường mà phải lập tức phát lệnh CẢNH BÁO ĐỎ cho Hotline An ninh/Kỹ thuật: `{"action": "trigger_emergency_alert", "priority": "CRITICAL", "department": "SECURITY_HOTLINE", "reason": "<lý_do>"}`. |

---

### 3.3. Future-State Flow & AI Fit

* **Đánh giá AI Fit:** Lựa chọn mô hình **LLM Feature (Intent Classification & Draft Copilot)** kết hợp Rule-based Router. Bài toán xử lý ngôn ngữ tự nhiên tiếng Việt có ngữ cảnh rõ ràng, kiểm soát rủi ro phát ngôn thông qua bước duyệt 1-click của Tiếp tân BQL.
* **Sơ đồ quy trình tương lai (Future-State Workflow):**

```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Bước 1          │      │ Bước 2          │      │ Bước 3          │      │ Bước 4          │
│ Cư dân gửi      │ ───> │ 🔵 AI phân loại │ ───> │ 🔵 AI Draft SMS │ ───> │ 🟢 Tiếp tân BQL │
│ ticket qua App  │      │ & gán tag bộ    │      │ phản hồi với thẻ│      │ 1-Click duyệt   │
│                 │      │ phận chuyên trách│     │ [DRAFT_RESPONSE]│      │ & phát hành     │
│ Ai: Cư dân      │      │ Ai: LLM Feature │      │ Ai: LLM Feature │      │ Ai: Human (HITL)│
│ ⏱ 3 phút        │      │ ⏱ 5 giây        │      │ ⏱ 5 giây        │      │ ⏱ 1 phút 🟢     │
└─────────────────┘      └─────────────────┘      └─────────────────┘      └─────────────────┘
                                                                                    │
                                                                                    ▼
                                                                           ↩️ Fallback:
                                                                           Nếu AI có độ tin cậy
                                                                           < 80% hoặc ý kiến mơ hồ,
                                                                           chuyển ticket về hòm thư
                                                                           xử lý thủ công của BQL.
```

* **Cấu trúc Ranh giới & Kiểm soát (Safety Control & HITL):**
  * 🔵 **AI Step:** Phân tích ý định (Intent Detection) $\rightarrow$ Gán tag bộ phận chuyên trách $\rightarrow$ Soạn phản hồi nháp lịch sự có thẻ `[DRAFT_RESPONSE]`. Nếu phát hiện sự cố khẩn cấp (Gas/Cháy/Kẹt thang), kích hoạt `trigger_emergency_alert`.
  * 🟢 **Human Step (HITL):** Tiếp tân BQL xem bản phân loại & phản hồi nháp trên Dashboard, kiểm tra thông tin và bấm "Phê duyệt & Chuyển tiếp" cho kỹ thuật/cư dân.
  * ↩️ **Fallback Plan:** Khi điểm tin cậy (Confidence score) $< 0.80$, hệ thống tự động đánh dấu `[MANUAL_REVIEW_REQUIRED]` để BQL xử lý thủ công.

---

## 🏁 Phase 5 — EVALUATE (Đánh giá độ sẵn sàng & Quyết định)

### AI Readiness Checklist:
1. [x] **Dữ liệu mẫu/logs sạch:** Hệ thống Vinhomes Resident App lưu trữ đầy đủ hàng vạn ticket phản ánh của cư dân cùng lịch sử phản hồi thực tế của BQL.
2. [x] **Kiểm soát rủi ro:** Rủi ro phát ngôn hoặc bồi thường tài chính được kiểm soát 100% nhờ bước duyệt con người **Human-in-the-loop (HITL)** và quy tắc cảnh báo đỏ khẩn cấp.
3. [x] **Sự sẵn sàng của Stakeholders:** Ban Quản lý Vinhomes rất mong muốn đưa hệ thống vào thử nghiệm để giảm tải 80% khối lượng công việc hành chính cho tiếp tân.

---

### 🏛️ Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

✅ **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển bản thử nghiệm cho Ban Quản lý Vinhomes Ocean Park và Vinhomes Smart City.

### Lý giải quyết định (Justification):
1. **Khả thi về Kỹ thuật:** Sử dụng công nghệ **LLM Feature** phân loại văn bản tiếng Việt và soạn nháp văn bản có chi phí vận hành thấp (Gemini 2.5 Flash), độ chính xác cao và dễ tích hợp vào hệ thống ticket có sẵn của Vinhomes.
2. **Giá trị Vận hành & ROI:** Giảm thời gian phản hồi cư dân từ 12 giờ xuống dưới 15 phút, tăng điểm CSAT đô thị, tiết kiệm hàng chục nghìn giờ làm việc hành chính mỗi năm cho tập đoàn.
3. **An toàn Pháp lý & Vận hành:** Ranh giới vận hành chặt chẽ ngăn chặn tuyệt đối việc AI hứa hẹn bồi thường tài chính hoặc tự động phát ngôn khi chưa qua kiểm duyệt.
