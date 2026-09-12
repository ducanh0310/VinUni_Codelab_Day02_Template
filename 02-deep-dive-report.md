
**🏗️ Phase 3 — DEEP-DIVE**
**3.1. Current-State Workflow**
```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận vé │     │ Thẩm định    │     │ Tra cứu sơ đồ│     │ Điều phối &  │
│ qua App      │     │ text & ảnh   │     │ phân quyền   │     │ gán việc BMS │
│              │     │              │     │              │     │              │
│ Ai: Cư dân/HT│ ──→ │ Ai: CSKH     │ ──→ │ Ai: CSKH     │ ──→ │ Ai: CSKH     │
│ ⏱ 3-10 p 🔄  │     │ ⏱ 4-8 p 🔴   │     │ ⏱ 3-5 p 🔴   │     │ ⏱ 1-2 p 🔄   │
│ In: Text, ảnh│     │ In: Raw tkt  │     │ In: Mã căn   │     │ In: BQL, Prio│
│ Out: Raw tkt │     │ Out: Nhóm lỗi│     │ Out: Đích BQL│     │ Out: Tkt gán │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Kỹ thuật nhận│
                                                               │ (hoặc reject)│
                                                               │              │
                                                               │ Ai: Kỹ thuật │
                                                               │ ⏱ 10-20p 🔴🔄│
                                                               │ In: Tkt gán  │
                                                               │ Out: Done/Lặp│
                                                               └──────────────┘
                                                               🔴 = Bottleneck (Điểm nghẽn xử lý thủ công / dễ sai sót)

```
🔴 = Bottleneck (Điểm nghẽn xử lý thủ công / dễ sai sót)

🔄 = Handoff (Điểm chuyển giao thông tin giữa người và hệ thống)

⏱ Tổng thời gian vận hành trung bình: 15–25 phút/lượt (khung giờ cao điểm hoặc bị nảy vé: 40–60 phút/lượt).

**3.2. Problem Statement (6-field)**
| Field | Nội dung chi tiết |
| :--- | :--- |
| **1. Actor / Operator**<br>*(Ai đang thực hiện tác vụ hằng ngày?)* | • **Điều phối viên CSKH Trung tâm (Central Operation Center):** Tiếp nhận, đọc nội dung và phân loại hàng đợi ticket tập trung của toàn bộ đại đô thị.<br>• **Trực ban Ban Quản lý (BQL) Tòa nhà / Cụm phân khu:** Tiếp nhận ticket tại hiện trường và giao việc cho kỹ thuật viên hoặc đội lao công trực ca.<br>• **Kỹ thuật viên / Đội hiện trường:** Mở việc kiểm tra xử lý; nếu phát hiện gán nhầm bộ phận thì bấm *Reject* để trả ngược vé. |
| **2. Current Workflow**<br>*(Mô tả tóm tắt quy trình thủ công hiện tại và công cụ sử dụng)* | • **Công cụ sử dụng:** App Vinhomes Resident (cư dân), Cổng quản trị vận hành PMS/BMS (vận hành đô thị).<br>• **Quy trình 6 bước:**<br>1. *Bước 1:* Cư dân tạo phản ánh trên App (hệ thống tự gán mã căn, cư dân nhập text mô tả, đính kèm 1–3 ảnh/video).<br>2. *Bước 2:* Ticket đổ về hàng đợi tập trung (*Unassigned Queue*) trên PMS/BMS.<br>3. *Bước 3:* Điều phối viên mở từng vé, đọc text và soi ảnh/video để chẩn đoán nhóm lỗi (Cơ điện, Vệ sinh, An ninh, Thang máy).<br>4. *Bước 4:* Tra cứu sơ đồ phân quyền/vị trí (trong căn hộ, khu dùng chung tòa nhà, hay hạ tầng cảnh quan ngoài trời) để xác định BQL phụ trách.<br>5. *Bước 5:* Chọn Category, Priority, chọn đích đến BQL tòa phụ trách rồi bấm *Dispatch*.<br>6. *Bước 6:* Kỹ thuật viên tòa mở việc; nếu bị gán sai thì bấm *Reject* trả ngược vé về hàng đợi trung tâm để phân loại lại. |
| **3. Bottleneck**<br>*(Bước nào chậm, lỗi, hoặc cần xử lý ngôn ngữ tự động nhiều nhất?)* | • **Bước thẩm định text & ảnh (Bước 3 - Cần NLP & Multimodal nhất):** Cư dân viết tắt, dùng tiếng lóng, ngôn từ bức xúc cảm tính, hoặc chỉ gửi ảnh chụp rò rỉ/video mà không có mô tả -> Điều phối viên mất 4–8 phút/vé để zoom ảnh và đọc dịch thủ công.<br>• **Bước tra cứu sơ đồ phân quyền (Bước 4 - Dễ sai sót nhất):** Nhầm lẫn ranh giới xử lý giữa Kỹ thuật Tòa nhà và Hạ tầng Đô thị ngoài trời, hoặc giữa CSKH và Đội An ninh tiếng ồn -> Mất 3–5 phút/vé.<br>• **Bước nảy vé qua lại (Bước 5 & 6 - Gây trễ nhất):** Hiện tượng *Ping-pong ticket* do gán sai khiến kỹ thuật viên reject vé, đẩy ngược về đầu quy trình làm phát sinh thêm 10–20 phút trễ nải. |
| **4. Business Impact**<br>*(Tổn thất thực tế đo bằng thời gian, chi phí, hoặc SLA của Vingroup)* | • **Độ trễ điều phối kéo dài:** Mất 15–25 phút/vé vào giờ thường và lên tới 40–60 phút/vé vào giờ cao điểm (18h–21h tối hoặc cuối tuần).<br>• **Vi phạm cam kết SLA:** Khoảng 15% ticket vi phạm thời gian phản hồi ban đầu (*First Response Time*).<br>• **Lãng phí chi phí nhân sự:** Phải duy trì 3–5 nhân sự/ca trực chỉ để làm thao tác đọc, click và chuyển tiếp thủ công.<br>• **Sụt giảm chỉ số CSAT:** Cư dân bức xúc đánh giá 1 sao trên App khi các sự cố khẩn cấp (mất nước, kẹt thang máy, hỏng barie hầm xe) bị ngâm tắc ở khâu điều phối. |
| **5. Success Metric**<br>*(AI giải quyết được thì đạt ngưỡng số mấy?)* | • **Độ chính xác phân luồng (Routing Accuracy):** $\ge 92\%$ ticket được gán đúng danh mục kỹ thuật và đúng đích BQL tòa ngay lần đầu.<br>• **Thời gian xử lý điều phối (Triage Latency):** $\le 5$ giây/ticket (từ lúc cư dân bấm gửi trên App đến khi hiện lên bảng việc của kỹ thuật tòa).<br>• **Tỷ lệ nảy vé (Bounce / Misroute Rate):** Giảm từ mức 15% xuống dưới 3%.<br>• **Tỷ lệ tự động hóa hoàn toàn (Zero-touch Rate):** $\ge 75\%$ ticket thường quy được chuyển tự động hoàn toàn mà không cần con người can thiệp. |
| **6. Operational Boundary**<br>*(AI được phép làm gì, TUYỆT ĐỐI không được làm gì, điểm nào cần duyệt?)* | • **AI ĐƯỢC PHÉP LÀM:**<br>1. Tự động bóc tách thực thể: Mã căn, số tầng, vị trí sự cố, nhóm nghiệp vụ (Cơ điện, Vệ sinh, An ninh, Tiện ích).<br>2. Nhận diện hỏng hóc từ hình ảnh/video khi cư dân không nhập mô tả text.<br>3. Tự động chuyển thẳng vé (*Auto-dispatch*) nếu điểm tin cậy (*Confidence Score*) $\ge 0.85$.<br>4. Gửi tin nhắn xác nhận chuẩn hóa kèm SLA tiếp nhận dự kiến về App cư dân.<br><br>• **TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM:**<br>1. Không được tự ý đóng (*Close/Resolve*) hoặc hủy bỏ (*Reject*) ticket của cư dân.<br>2. Không tự ý hứa bồi thường vật chất, giảm phí quản lý hoặc phát ngôn pháp lý thay BQL.<br>3. Không gửi lệnh điều khiển trực tiếp vào phần cứng BMS (không tự ngắt van nước tổng hay nhảy aptomat khu vực).<br><br>• **ĐIỂM CẦN CON NGƯỜI DUYỆT (Human-in-the-loop):**<br>1. **Sự cố khẩn cấp P1 (Cháy nổ, rò gas, chập điện, kẹt thang máy):** Agent kích hoạt cảnh báo đỏ trên BMS và gọi tự động cho Trưởng ca BQL trong 30 giây.<br>2. **Độ tin cậy thấp (Confidence < 0.85):** Đẩy vào *Review Queue* để điều phối viên chọn đích bằng 1 click.<br>3. **Khiếu nại nhạy cảm / Bức xúc cao:** Phản ánh thái độ nhân viên, tranh chấp quyền lợi -> Chuyển thẳng hòm thư Trưởng ban Quản lý duyệt phương án. |

## 3.3. Future-State Flow & AI Fit

### 1. Xác định mức AI Fit (AI-Fit Matrix)

- [ ] **Rule / State-Machine:** *Không khả thi* do đầu vào ngôn ngữ tự nhiên của cư dân phi cấu trúc (tiếng lóng, viết tắt, cảm xúc bức xúc) và có tới 30% ticket chỉ gửi ảnh/video mà không có mô tả chữ.
- [ ] **LLM Feature:** *Chưa đủ* vì bài toán không chỉ dừng lại ở việc trích xuất văn bản (Single-shot extraction), mà đòi hỏi phải kết hợp đa phương tiện (Multimodal), tra cứu dữ liệu phân quyền theo ngữ cảnh (Lookup/RAG), đánh giá độ tin cậy và tự động rẽ nhánh hành động.
- [x] **Agentic Loop (Lựa chọn tối ưu):**
  * **Lý do lựa chọn:**
    1. **Tác vụ chuỗi đa phương tiện (Multimodal Reasoning Loop):** Agent tiếp nhận đồng thời cả text và ảnh/video -> phân tích thị giác để phát hiện loại sự cố -> trích xuất thực thể.
    2. **Sử dụng công cụ tra cứu động (Tool Calling):** Agent chủ động gọi API tra cứu sơ đồ phân cấp mặt bằng (Mã căn `S2.08-12A06` -> Phân khu -> BQL phụ trách) để xác định đúng ranh giới trách nhiệm (Kỹ thuật tòa nhà vs Hạ tầng đô thị ngoài trời).
    3. **Đánh giá tự tin & Tự động ra quyết định (Self-Reflection & Conditional Routing):** Tự tính toán điểm tin cậy (*Confidence Score*). Nếu $\ge 0.85 \to$ tự động Dispatch; nếu $< 0.85 \to$ kích hoạt Fallback đẩy về hàng đợi duyệt; nếu phát hiện P1 $\to$ kích hoạt quy trình ứng phó khẩn cấp.

---

### 2. Sơ đồ Future-State Flow (Mermaid Diagram)

```text
[Cư dân gửi Ticket qua App (Text + Ảnh/Video + Mã căn)]
                        │
                        ▼
       ┌─────────────────────────────────────────────────┐
       │ 🔵 AI Step 1: Multimodal Ingestion & Parsing    │
       │ (Bóc tách text lóng, nhận diện ảnh rò rỉ/nứt vỡ) │
       └────────────────────────┬────────────────────────┘
                                │
                                ▼
       ┌─────────────────────────────────────────────────┐
       │ 🔵 AI Step 2: Policy Lookup & Triage            │
       │ (Tra cứu sơ đồ ranh giới BQL, gán Category/Prio) │
       └────────────────────────┬────────────────────────┘
                                │
                                ▼
       ┌─────────────────────────────────────────────────┐
       │ 🔵 AI Step 3: Confidence & Risk Gate            │
       └────┬───────────────────┼───────────────────┬────┘
            │                   │                   │
    [Nguy cơ P1]         [Confidence < 0.85]  [Confidence >= 0.85]
(Cháy nổ/kẹt thang)        (Ảnh mờ/dữ liệu yếu)     (Thường quy/rõ ràng)
            │                   │                   │
            ▼                   ▼                   ▼
 ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐
 │ 🔵 Bật cảnh báo đỏ  │ │ ↩️ Fallback 1:     │ │ 🔵 AI Step 4:       │
 │ BMS & Auto-Call     │ │ Review Queue        │ │ Auto-Dispatch       │
 └──────────┬──────────┘ └──────────┬──────────┘ └──────────┬──────────┘
            │                   │ Gợi ý Top-3 nhãn          │
            ▼                   ▼                           │
 ┌─────────────────────┐ ┌─────────────────────┐            │
 │ 🟢 HITL Step:       │ │ 🟢 HITL Step:       │            │
 │ Trưởng ca BQL nhận  │ │ Điều phối viên chọn │            │
 │ cuộc gọi trong 30s  │ │ đích bằng 1-Click   │────────────┘
 └─────────────────────┘ └─────────────────────┘
                                                    │
                                                    ▼
                                         ┌─────────────────────┐
                                         │ 🔵 AI Step 5:       │
                                         │ Gửi xác nhận & SLA  │
                                         │ về App cho Cư dân   │
                                         └──────────┬──────────┘
                                                    │
                                                    ▼
                                         ┌─────────────────────┐
                                         │ Kỹ thuật viên Tòa   │
                                         │ nhận việc xử lý     │
                                         └─────────────────────┘

* ↩️ Fallback 2 (Sự cố kỹ thuật): Nếu LLM timeout quá 5s hoặc lỗi JSON, ticket tự động chuyển về Hàng đợi trung tâm để xử lý thủ công.
```

---

### 3. Chi tiết các bước trong Quy trình Vận hành Tương lai

| Ký hiệu | Loại bước | Tên bước | Tác nhân | Mô tả chi tiết hành động |
| :---: | :--- | :--- | :--- | :--- |
| 🔵 | **AI Step** | **Multimodal Parsing & Ingestion** | AI Agent (LLM + Vision) | Đọc văn bản tiếng lóng, viết tắt; soi ảnh/video nhận diện hiện tượng (nước rỉ, nứt tường, rác tồn đọng); bóc tách thực thể (vị trí, thiết bị). |
| 🔵 | **AI Step** | **Policy & Boundary Lookup** | AI Agent | Gọi Tool API tra cứu sơ đồ phân quyền dựa trên mã căn hộ để xác định đúng ranh giới xử lý (Kỹ thuật Tòa vs Hạ tầng Đô thị). |
| 🔵 | **AI Step** | **Triage & Confidence Scoring** | AI Agent | Gán nhãn Category, Sub-category, mức độ Priority (P1-P4) và tính toán điểm tin cậy $C \in [0, 1]$. |
| 🔵 | **AI Step** | **Auto-Dispatch & Notification** | AI Agent | Nếu $C \ge 0.85$, tự động gọi API đẩy ticket vào bảng việc của BQL Tòa; gửi tin nhắn xác nhận kèm SLA chuẩn về App cư dân. |
| 🟢 | **Human Step (HITL)** | **Duyệt khẩn cấp P1 (Critical Emergency)** | Trưởng ca BQL Tòa | Khi AI phát hiện từ khóa/hình ảnh nguy hiểm (cháy nổ, kẹt thang máy), hệ thống hú còi đỏ BMS và gọi điện thoại tự động cho Trưởng ca duyệt xử lý trong 30 giây. |
| 🟢 | **Human Step (HITL)** | **Review Queue (Bán tự động)** | Điều phối viên CSKH | Khi $C < 0.85$, ticket hiện lên giao diện kèm 3 nhãn gợi ý có xác suất cao nhất; điều phối viên chỉ cần nhấn **1-click** để xác nhận thay vì đọc từ đầu. |
| 🟢 | **Human Step (HITL)** | **Duyệt khiếu nại bức xúc/nhạy cảm** | Trưởng BQL Tòa | Với các phản ánh bức xúc về thái độ phục vụ hoặc quyền lợi cư dân, AI gom tóm tắt và đẩy riêng vào hòm thư Trưởng ban để duyệt phương án xử lý. |
| ↩️ | **Fallback** | **Fallback 1: Độ tin cậy thấp / Dữ liệu yếu** | Hệ thống | Khi ảnh quá mờ hoặc văn bản vô nghĩa không xác định được đích đến, tự động hạ cờ chuyển sang **Review Queue** cho con người quyết định. |
| ↩️ | **Fallback** | **Fallback 2: Lỗi kỹ thuật (Timeout / API Error)** | Hệ thống | Nếu LLM quá 5 giây không phản hồi hoặc trả về JSON sai format, ngắt kết nối an toàn (*Fail-safe*) và trả ticket nguyên bản về **Hàng đợi tập trung thủ công** để đảm bảo không thất lạc vé. |


# 🏁 Phase 5 — EVALUATE (Đánh giá & Ra quyết định)

### 📋 AI Readiness Checklist:

1. **[x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?**
   * **Đánh giá:** **SẴN SÀNG (High Readiness)**.
   * **Minh chứng:** Hệ thống quản lý vận hành Vinhomes Resident / BMS hiện lưu trữ hàng triệu bản ghi ticket lịch sử từ các đại đô thị (Ocean Park, Smart City, Grand Park...). Dữ liệu bao gồm văn bản mô tả thực tế (chứa tiếng lóng, viết tắt), ảnh chụp hiện trường, lịch sử điều phối thủ công và kết quả nghiệm thu từ kỹ thuật viên tòa. Đây là tập ground-truth chất lượng cao để đánh giá độ chính xác (*Routing Accuracy*) và tinh chỉnh prompt/few-shot examples.

2. **[x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?**
   * **Đánh giá:** **HOÀN TOÀN KIỂM SOÁT ĐƯỢC (Fail-safe Guaranteed)**.
   * **Minh chứng:**
     * **Chốt chặn khẩn cấp (P1 Critical):** Sự cố đe dọa sinh mạng/cháy nổ/kẹt thang máy được định tuyến thẳng tới chuông báo động đỏ BMS và kích hoạt cuộc gọi tự động (Auto-call) đến Trưởng ca BQL trong 30 giây.
     * **Chốt chặn độ tin cậy (HITL):** Các ca dữ liệu mờ mịt hoặc điểm tự tin $< 0.85$ tự động chuyển vào *Review Queue* để điều phối viên chọn đích bằng 1-Click.
     * **Ranh giới bất khả xâm phạm:** Tuyệt đối cấm AI tự ý đóng/hủy ticket hoặc cam kết bồi thường tài chính.
     * **Kế hoạch dự phòng (Fallback):** Nếu AI timeout quá 5 giây hoặc gặp sự cố API, ticket nguyên bản tự động chuyển về *Central Unassigned Queue* để xử lý thủ công, không bao giờ bị thất lạc vé.

3. **[x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?**
   * **Đánh giá:** **ĐỒNG THUẬN CAO (Strong Buy-in)**.
   * **Minh chứng:**
     * *Điều phối viên CSKH Trung tâm:* Được giải phóng khỏi 75% tác vụ lặp lại nhàm chán (đọc, zoom ảnh, chọn menu thủ công), tập trung xử lý các ca khiếu nại phức tạp.
     * *Kỹ thuật viên BQL Tòa:* Hài lòng vì chấm dứt tình trạng "nảy vé" (ping-pong ticket), nhận đúng việc đúng chuyên môn ngay lần đầu.
     * *Cư dân:* Tăng mạnh mức độ hài lòng (CSAT) khi thời gian xác nhận phản ánh giảm từ 25–40 phút xuống dưới 5 giây.

---