# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | Time-consuming | Phê duyệt hồ sơ đăng ký thi công/sửa chữa nội thất bằng tay, rà soát bản vẽ PDF/DWG và danh sách nhân công/vật tư thủ công. |
| 2 | Vinhomes | Repetitive | Phân loại và điều vận sự cố kỹ thuật (điện, nước, thẻ từ) từ phản ánh của cư dân trên App Vinhomes Resident về cho Ban Quản Lý tòa nhà. |
| 3 | Vinhomes | Stakeholder Pain | Soạn và phản hồi các khiếu nại/đánh giá 1 sao của cư dân về CSKH, vệ sinh, bảo trì, và điều kiện sống, đồng thời đề xuất xử lý theo quy định. |
| 4 | Vinhomes | AI-upgrade | Tóm tắt, chuẩn hóa và phân loại yêu cầu cư dân từ chat, cuộc gọi, email, và App Resident thành ticket hỗ trợ cho bộ phận vận hành. |
| 5 | Vinhomes | Time-consuming | Kiểm tra và cập nhật hồ sơ cư dân/đơn đề nghị dịch vụ nội bộ (đăng ký xe, thẻ cư dân, thay đổi thông tin, hồ sơ quản lý nhà) bằng cách đối chiếu nhiều hệ thống thủ công. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và soạn phản hồi khiếu │
│ nại của cư dân về vệ sinh, bảo trì, CSKH trong Vinhomes.   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH và Ban Quản Lý tòa nhà │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân gửi phản hồi qua app/email/call ──> 2. CSKH đọc │
│      và tóm tắt nội dung ──> 3. Gán loại vấn đề và đề xuất  │
│      phản hồi ──> 4. Chuyển cho bộ phận xử lý                │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Soạn phản hồi thủ công và │
│ phân loại yêu cầu (⏱ 8–12 phút/lượt)                         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tóm tắt nội dung, phân │
│ loại vấn đề, viết draft phản hồi chuẩn theo ngữ cảnh        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian phản │
│ hồi từ 10 phút xuống dưới 2 phút; đạt >80% độ chính xác     │
│ phân loại vấn đề                                             │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và điều phối sự cố kỹ  │
│ thuật từ phản ánh cư dân đến bộ phận xử lý đúng người.      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Ban Quản Lý tòa nhà và đội kỹ thuật     │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân báo sự cố điện/nước/điều hòa/thẻ từ ──> 2. Văn  │
│      phòng nhận tin ──> 3. Phân loại theo loại sự cố ──> 4. │
│      Chuyển cho đội xử lý và cập nhật trạng thái              │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Phân loại và điều phối đội │
│ xử lý (⏱ 15–25 phút/lượt)                                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Đọc nội dung phản ánh, │
│ gắn tag loại sự cố và gợi ý đội/nhân sự phù hợp              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian gắn tag │
│ xuống dưới 1 phút; cải thiện tỷ lệ route đúng >90%; giảm số │
│ lần chuyển sai bộ phận xuống <5%                             │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tóm tắt, chuẩn hóa và chuẩn bị ticket yêu │
│ cầu dịch vụ cư dân từ nhiều kênh khác nhau.                  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên tiếp nhận và bộ phận vận hành │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân gửi yêu cầu qua App/Call/Email ──> 2. Nhân viên │
│      đọc và trích xuất thông tin ──> 3. Viết ticket chi tiết │
│      ──> 4. Chuyển cho bộ phận xử lý                         │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Tóm tắt và nhập dữ liệu    │
│ bằng tay vào hệ thống (⏱ 10–15 phút/lượt)                    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Sinh sơ đồ ticket,     │
│ tóm tắt yêu cầu, trích xuất thông tin bắt buộc và ưu tiên     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian nhập   │
│ dữ liệu từ 12 phút xuống dưới 3 phút; đạt >85% ticket có    │
│ thông tin đầy đủ khi tạo tự động                             │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---

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

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

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

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
