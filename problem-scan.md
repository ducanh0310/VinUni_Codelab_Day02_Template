# PHASE 1 & PHASE 2: PROBLEM SCAN & QUICK-ASSESS REPORT
**Dự án:** AI Product Scoping — Vin Smart Future (Vingroup)  
**Tác giả:** Nguyễn Đức Anh (nguyenducanhflm@gmail.com)  
**Vai trò:** AI Product Engineer — Vin Smart Future  

---

## 🏛️ Bối cảnh & Định hướng

Với vai trò là **AI Product Engineer** tại **Vin Smart Future** (đơn vị công nghệ thuộc Tập đoàn Vingroup), tôi đã tiến hành khảo sát quy trình vận hành tại các công ty thành viên (VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl) nhằm nhận diện các điểm nghẽn (bottlenecks), rò rỉ hiệu suất, và đề xuất các bài toán AI tiềm năng mang lại giá trị thực tế cho tập đoàn.

---

## 🔍 Phase 1 — SCAN: Danh sách 5 bài toán vận hành (Cá nhân)

Sử dụng **4 Lenses** (*Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác*) để quét qua các mảng hoạt động kinh doanh:

| # | Subsidiary | Lens | Mô tả ngắn bài toán / Bottleneck thực tế |
|---|------------|------|------------------------------------------|
| 1 | **VinFast** | AI-upgrade | **Chẩn đoán ban đầu lỗi xe điện tại Xưởng dịch vụ:** Cố vấn dịch vụ mất 20–25 phút tra cứu thủ công sổ tay mã lỗi OBD-II & tài liệu kỹ thuật (TSB) từ triệu chứng tiếng Việt tự nhiên của chủ xe. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian | **Xử lý sự cố sạc pin / hết pin thực địa của tài xế taxi điện:** Điều phối viên mất 12–15 phút tra cứu thủ công vị trí GPS xe, kiểm tra trụ sạc VinFast trống, và viết tin nhắn chỉ dẫn đường hoặc liên hệ xe cứu hộ. |
| 3 | **Vinhomes** | Pain từ người khác | **Phân loại & tự động điều hướng phản ánh cư dân trên App Vinhomes Resident:** Ticket phản ánh (hỏng đèn, rò rỉ nước, tiếng ồn, thẻ xe) bị trễ trễ phân loại hoặc chuyển nhầm Ban quản lý (BQL) tòa nhà, gây trễ SLA phản hồi từ 12–24 giờ. |
| 4 | **VinFast** | Lặp lại | **Đối chiếu hóa đơn sạc điện hàng tuần với đối tác trạm sạc ngoài:** Nhân viên tài chính phải so khớp thủ công hàng vạn giao dịch sạc giữa dữ liệu telemetry VinFast và bảng kê hóa đơn từ đối tác sạc liên kết. |
| 5 | **Vinmec** | Tốn thời gian | **Tóm tắt hồ sơ xuất viện (Discharge Summary) cho bệnh nhân:** Bác sĩ mất 25–30 phút/bệnh nhân để tổng hợp lịch sử điều trị, xét nghiệm và viết hướng dẫn chăm sóc sau xuất viện bằng ngôn ngữ bình dân. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

### 🃏 Quick Problem Card #1

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Trợ lý AI chẩn đoán ban đầu lỗi xe điện tại Xưởng VinFast.   │
│ Công ty thành viên: [x] VinFast   [ ] Xanh SM   [ ] Vinhomes           │
│                                                                         │
│ Ai đang đau? Cố vấn dịch vụ (quá tải), Chủ xe (chờ tiếp nhận lâu).      │
│ Workflow thủ công: Nghe mô tả -> Ghi chép -> Tra cứu TSB -> Lập phiếu RO.│
│ Bước tốn nhất: Tra cứu TSB & mã lỗi OBD-II (⏱ 18-20 phút).               │
│ AI hỗ trợ ở đâu: Trích xuất triệu chứng ──> RAG tìm TSB ──> Draft báo cáo.│
│ Metric: Giảm thời gian chẩn đoán ban đầu từ 25 min ──> under 5 min.     │
│ Quick Architecture: [x] LLM Feature (RAG + Diagnostic Output)           │
└─────────────────────────────────────────────────────────────────────────┘
```

### 🃏 Quick Problem Card #2

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Hỗ trợ Điều phối viên Xanh SM xử lý sự cố sạc pin thực địa.  │
│ Công ty thành viên: [ ] VinFast   [x] Xanh SM (GSM)   [ ] Vinhomes     │
│                                                                         │
│ Ai đang đau? Tài xế Xanh SM (chờ đợi), Điều phối viên (quá tải).        │
│ Workflow thủ công: Gọi tổng đài -> Tra GPS -> Tra trạm trống -> SMS.   │
│ Bước tốn nhất: Tra cứu trạm sạc trống & soạn SMS chỉ dẫn (⏱ 10-12 phút).│
│ Metric: Giảm thời gian xử lý sự cố từ 15 min ──> under 3 min.          │
│ Quick Architecture: [x] LLM Feature (Smart Dispatch Copilot)            │
└─────────────────────────────────────────────────────────────────────────┘
```

### 🃏 Quick Problem Card #3 (Bài toán được nhóm lựa chọn cho Deep-Dive)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Phân loại & tự động điều hướng phản ánh cư dân trên App      │
│ Vinhomes Resident (Vinhomes Smart Resident Complaint Dispatcher).       │
│ Công ty thành viên: [ ] VinFast   [ ] Xanh SM   [x] Vinhomes           │
│                     [ ] Vinmec    [ ] Vinpearl                          │
│                                                                         │
│ Ai đang đau (Actor)? Ban quản lý tòa nhà Vinhomes (ngợp hàng trăm       │
│                      ticket/ngày), Cư dân Vinhomes (chờ phản hồi lâu). │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Cư dân nộp ticket phản ánh trên App Vinhomes Resident              │
│   ──> 2. Tiếp tân BQL đọc thủ công nội dung & phân loại nhóm sự cố      │
│   ──> 3. Tiếp tân chuyển giao ticket đến đúng bộ phận (Kỹ thuật/An ninh)│
│   ──> 4. Bộ phận chuyên trách xử lý thực địa                            │
│   ──> 5. Tiếp tân soạn phản hồi bằng văn bản gửi lại cư dân             │
│                                                                         │
│ Bước nào tốn thời gian nhất? Bước 2, 3 & 5 (⏱ 12-24 giờ delay SLA)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 5                     │
│ (Phân loại ý định ──> Gán tag bộ phận ──> Soạn phản hồi nháp thân thiện)│
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│   • Giảm thời gian phản hồi ban đầu từ 12 giờ ──> dưới 15 phút.         │
│   • Tỉ lệ phân loại đúng bộ phận chuyên trách đạt ≥ 95%.                │
│                                                                         │
│ Quick Architecture: [x] LLM Feature + Rule-based Router (Copilot)       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn của Nhóm & Lý giải

Nhóm chúng tôi thống nhất lựa chọn **"Card #3 — Phân loại & tự động điều hướng phản ánh cư dân trên App Vinhomes Resident"** để thực hiện báo cáo Phân tích sâu (Deep-Dive).

### Lý do lựa chọn Card #3:
1. **Giá trị tác động cư dân rộng lớn (Scale & Resident CSAT):** Vinhomes quản lý hàng chục đại đô thị (Ocean Park, Smart City, Grand Park...) với hàng trăm nghìn cư dân. Số lượng ticket phản ánh trung bình ~300 ticket/ngày/đô thị. Tự động hóa khâu phân loại và phản hồi ban đầu mang lại sự hài lòng vượt trội cho cư dân.
2. **Khả thi về dữ liệu & công nghệ:** Ý kiến cư dân được gửi dưới dạng văn bản tiếng Việt tự nhiên. Việc ứng dụng LLM Feature phân tích phân loại văn bản (Text Classification & Intent Detection) kết hợp RAG câu hỏi thường gặp (FAQ) có độ chính xác rất cao và triển khai nhanh chóng.
3. **Ranh giới kiểm soát an toàn (Operational Boundary):** Dễ dàng thiết lập cơ chế Human-in-the-loop (tiếp tân BQL bấm 1-click duyệt phản hồi `[DRAFT_RESPONSE]`) và gắn nhãn cảnh báo đỏ khẩn cấp cho các sự cố an ninh/cháy nổ/khí gas.

### Lý do loại bỏ các thẻ khác:
* **Loại Card #1 (VinFast Diagnostics):** Quy trình chẩn đoán kỹ thuật xe điện phụ thuộc nhiều vào thiết bị phần cứng OBD-II vật lý tại xưởng.
* **Loại Card #2 (Xanh SM Charging):** Nhóm muốn ưu tiên mảng Đô thị & Quản lý vận hành bất động sản để giải quyết bài toán giao tiếp quy mô lớn với cư dân.
