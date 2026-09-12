**🔍 Phase 1 — SCAN**

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
| --- | --- | --- | --- |
| **1** | Vinhomes | Lặp lại (Repetitive) | Tự động phân loại và điều phối ticket sự cố (mất nước, hỏng đèn, tiếng ồn) từ App Vinhomes Resident về đúng Ban Quản lý từng tòa nhà. |
| **2** | VinFast | Tốn thời gian (Time-consuming) | Tra cứu và tổng hợp phương án sửa chữa từ sổ tay kỹ thuật (Workshop Manual/TSB) dựa trên log mã lỗi OBD/CAN-bus tại xưởng dịch vụ. |
| **3** | Xanh SM | Tốn thời gian (Time-consuming) | Phân tích các đánh giá của khách hàng |
| **4** | Vinpearl | AI có thể tốt hơn (AI-upgrade) | Tự động bóc tách email/file Excel yêu cầu đặt phòng đoàn (Group Booking) từ các đại lý lữ hành để kiểm tra tồn kho PMS và tạo dự thảo báo giá. |
| **5** | Vinmec | Tốn thời gian (Time-consuming) | Tiền kiểm hồ sơ bệnh án xuất viện, đối chiếu chỉ định thuốc và thủ thuật với danh mục chi trả bảo hiểm theo mã chuẩn ICD-10 để tránh xuất toán. |

**Phase 2 — QUICK-ASSESS**

### QUICK PROBLEM CARD #01

* **Bài toán (1 câu):** Tự động phân loại và điều phối ticket sự cố kỹ thuật/đời sống từ App Vinhomes Resident đến đúng Ban Quản lý từng tòa nhà.
* **Công ty thành viên:**
  - [ ] VinFast
  - [ ] Xanh SM
  - [x] Vinhomes
  - [ ] Vinmec
  - [ ] Khác (Ghi rõ)
* **Ai đang đau (Actor)?** Điều phối viên CSKH trung tâm vận hành đại đô thị & Trực ban kỹ thuật BQL tòa nhà.
* **Workflow thủ công hiện tại:**
  1. Nhận ticket từ App
  2. Đọc text & soi ảnh đính kèm
  3. Tra cứu phân quyền tòa/cụm
  4. Gán và Dispatch
* **Bước nào tốn thời gian/lỗi nhất?** Bước 2 & 3 (⏱ 5–15 phút/vé)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2 & 3: Nhận diện đa phương thức (Text + Vision) để gắn nhãn danh mục, mức độ khẩn cấp và auto-dispatch qua API vào hệ thống BMS tòa nhà.
* **Đo thành công bằng gì (Metric có số)?**
  - Giảm thời gian phân loại & dispatch từ 15 phút xuống dưới 10 giây.
  - Tỷ lệ điều phối đúng tuyến ngay lần đầu đạt >= 90%.
  - Tỷ lệ tự động hóa hoàn toàn (Zero-touch) đạt >= 75%.
* **Quick Architecture:**
  - [ ] No AI
  - [ ] Rule
  - [ ] LLM
  - [x] Agent

---

### QUICK PROBLEM CARD #02

* **Bài toán (1 câu):** Tự động tổng hợp, bóc tách nguyên nhân phàn nàn từ đánh giá 1–3 sao của khách hàng Xanh SM để kích hoạt quy trình khắc phục dịch vụ (Service Recovery).
* **Công ty thành viên:**
  - [ ] VinFast
  - [x] Xanh SM
  - [ ] Vinhomes
  - [ ] Vinmec
  - [ ] Khác (Ghi rõ)
* **Ai đang đau (Actor)?** Chuyên viên Đảm bảo chất lượng (QA/QC) & Bộ phận Điều hành tài xế GSM.
* **Workflow thủ công hiện tại:**
  1. Xuất file đánh giá định kỳ
  2. Đọc và gán nhãn lỗi thủ công
  3. Lập báo cáo ca trực
  4. Gửi voucher / thông báo đào tạo tài xế
* **Bước nào tốn thời gian/lỗi nhất?** Bước 2 (⏱ 3–5 phút/review, ngốn 4–6 tiếng/ngày của nhân viên QA)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2 & 4: Phân tích Aspect-Based Sentiment, bóc tách lỗi cụ thể (mùi xe, thái độ, đón trễ), tự động kích hoạt gửi voucher xin lỗi khách và phân bổ bài đào tạo lại cho tài xế trên app.
* **Đo thành công bằng gì (Metric có số)?**
  - Giảm độ trễ gửi phản hồi/voucher xin lỗi: từ 24 giờ xuống dưới 5 phút.
  - Độ chính xác trích xuất đúng nhóm lỗi (F1-score) >= 88%.
  - Cắt giảm >= 80% thời gian phân loại thủ công của đội ngũ QA.
* **Quick Architecture:**
  - [ ] No AI
  - [ ] Rule
  - [ ] LLM
  - [x] Agent

---

### QUICK PROBLEM CARD #03

* **Bài toán (1 câu):** Tự động bóc tách yêu cầu đặt phòng đoàn (Group Booking) từ email/Excel của đại lý lữ hành để kiểm tra tồn kho Opera PMS và lập dự thảo báo giá.
* **Công ty thành viên:**
  - [ ] VinFast
  - [ ] Xanh SM
  - [ ] Vinhomes
  - [ ] Vinmec
  - [x] Khác (Vinpearl)
* **Ai đang đau (Actor)?** Chuyên viên Đặt phòng khách đoàn (Group Reservation Executive) & Sales MICE Vinpearl.
* **Workflow thủ công hiện tại:**
  1. Nhận email/file RFP
  2. Đọc và chuẩn hóa ngày/phòng/ăn
  3. Tra cứu tồn kho & mã giá trên PMS
  4. Soạn file báo giá PDF & email gửi đại lý
* **Bước nào tốn thời gian/lỗi nhất?** Bước 2 & 3 (⏱ 30–45 phút/yêu cầu do file Excel lộn xộn, phòng chia nhiều đợt)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2, 3 & 4: OCR và LLM trích xuất bảng biểu, Tool-calling gọi API check tồn kho phòng trống, tính phụ thu và tạo dự thảo báo giá tự động.
* **Đo thành công bằng gì (Metric có số)?**
  - Giảm thời gian tạo dự thảo báo giá từ 6–12 giờ xuống dưới 15 phút.
  - Độ chính xác bóc tách thông số (ngày, hạng phòng) >= 95%.
  - Tỷ lệ giữ phòng tạm thời (Tentative Hold) tự động đạt >= 60%.
* **Quick Architecture:**
  - [ ] No AI
  - [ ] Rule
  - [ ] LLM
  - [x] Agent
