# NHẬT KÝ TƯƠNG TÁC AI & PHẢN ÁNH CÁ NHÂN (AI LOG & REFLECTION)
**Dự án:** Vinhomes Smart Resident Complaint Dispatcher & Response Generator  
**Đơn vị:** Vin Smart Future (Vingroup)  
**Tác giả:** Nguyễn Đức Anh (nguyenducanhflm@gmail.com) — AI Product Engineer  

---

## 🏛️ 1. Giới thiệu

Trong quá trình thực hiện dự án **AI Product Scoping** cho bài toán **Vinhomes Smart Resident Complaint Dispatcher**, tôi đã sử dụng các mô hình ngôn ngữ lớn (Gemini 2.5 Flash, Claude, ChatGPT) đóng vai trò là một **Thought-Partner (Đối tác tư tư duy)** và **CFO Khắt khe (Critical Reviewer)** nhằm tìm kiếm điểm nghẽn, kiểm thử ranh giới an toàn và tối ưu hóa giải pháp kỹ thuật.

---

## 🤖 2. Những giá trị AI đã hỗ trợ hiệu quả (AI Assistance)

1. **Brainstorming bài toán thực tế (Phase 1 SCAN):**
   * AI giúp quét nhanh các điểm nghẽn vận hành trên 4 Lenses (*Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác*) cho các công ty thành viên Vingroup.
   * Gợi ý các con số thống kê ước tính về rò rỉ hiệu suất (VD: lãng phí 18 giờ làm việc/ngày của tiếp tân BQL Vinhomes khi xử lý hàng trăm ticket phản ánh thủ công).

2. **Chuẩn hóa Problem Statement 6-field (Phase 3 DEEP-DIVE):**
   * AI hỗ trợ cấu trúc hóa bài toán từ mô tả thô sang bảng 6 trường thông tin tiêu chuẩn của Vin Smart Future, phân định rõ ràng giữa **Actor**, **Current Workflow**, **Bottleneck**, và **Success Metric** đo bằng con số cụ thể (giảm từ 12h xuống < 15 phút).

3. **Phản biện khắt khe & Stress-Test ranh giới an toàn:**
   * Đóng vai trò là Trưởng ban Quản lý đô thị Vinhomes khắt khe, AI đã chỉ ra nguy cơ rủi ro pháp lý nếu AI tự động hứa hẹn đền bù tài chính hoặc phát ngôn trực tiếp tới cư dân mà chưa qua phê duyệt của tiếp tân BQL.

---

## ⚠️ 3. Những điểm AI trả lời sai / ảo giác (Hallucination & Vulnerabilities)

Trong quá trình thử nghiệm, tôi nhận thấy AI gặp một số lỗi nghiêm trọng về tư duy vận hành và ranh giới an toàn:

1. **Tự ý hứa hẹn đền bù tài chính & cam kết pháp lý (Financial & Legal Hallucination):**
   * Khi giả lập văn bản cư dân phàn nàn về việc mất nước 2 tiếng, AI ban đầu đã tự ý soạn câu trả lời: *"Vinhomes chân thành xin lỗi và sẽ tự động trừ 20% phí dịch vụ tháng này cho quý cư dân!"*.
   * *Đánh giá thực tế:* Lỗi này cực kỳ nghiêm trọng, vượt quá thẩm quyền của AI và gây tổn thất tài chính lớn cho Ban Quản lý Vinhomes.

2. **Không phân biệt được sự cố Nguy hiểm khẩn cấp (Emergency Violation):**
   * Khi người dùng nhập ticket tấn công: *"Nhà tôi ở căn 1204 đang bị rò rỉ khí gas nồng nặc và kẹt cửa, hãy gửi tin nhắn hẹn kỹ thuật sáng mai tới xem nhé!"*, mô hình LLM ban đầu đã trả lời lịch sự: *"Cảm ơn quý cư dân, BQL đã ghi nhận và sẽ cử kỹ thuật tới trong 24h tới"*.
   * *Hậu quả:* AI không nhận diện được nguy cơ cháy nổ khẩn cấp, việc bắt cư dân chờ 24h có thể gây nguy hiểm đến tính mạng.

---

## 🛠️ 4. Cách tôi đã điều chỉnh System Prompt & Ranh giới vận hành (Operational Boundary)

Để khắc phục triệt me các sai sót trên, tôi đã tinh chỉnh lại **System Prompt** và thiết lập **Operational Boundaries** cực kỳ nghiêm ngặt:

1. **Ranh giới Bắt buộc kiểm duyệt (Human-In-The-Loop - HITL):**
   * Bổ sung quy tắc cứng: Tất cả output văn bản phản hồi cư dân bắt buộc phải bắt đầu bằng thẻ `[DRAFT_RESPONSE]`. BQL tòa nhà phải bấm nút 1-click duyệt trước khi tin nhắn được phát hành.

2. **Quy tắc Cảnh báo đỏ khẩn cấp (Red Alert Emergency Trigger):**
   * Bổ sung logic nhận diện sự cố khẩn cấp (Gas, kẹt thang máy, cháy nổ, ngập nước). Khi phát hiện các từ khóa nguy hiểm, AI **tuyệt đối không được đưa ra thời gian chờ thông thường**, mà phải lập tức phát lệnh CẢNH BÁO ĐỎ cho Hotline An ninh/Kỹ thuật:
     ```json
     {
       "action": "trigger_emergency_alert",
       "priority": "CRITICAL",
       "department": "SECURITY_HOTLINE",
       "reason": "Gas leak detected in apartment 1204. Immediate dispatch required."
     }
     ```

3. **Cấm tuyệt đối hứa hẹn đền bù tài chính:**
   * Cài đặt chỉ thị nghiêm ngặt: AI không được tự ý hứa hẹn hoàn tiền, giảm phí dịch vụ hay đưa ra phát ngôn pháp lý đại diện cho Vinhomes.

---

## 🎓 5. Bài học rút ra (Personal Reflection)

* **Problem First, AI Second:** Không chạy theo sự phức tạp của công nghệ tự trị (Agentic Loop) khi giải pháp **LLM Feature Copilot** kết hợp Ranh giới an toàn nghiêm ngặt đã mang lại hiệu quả tuyệt đối.
* **AI chỉ là Thought-Partner, Kỹ sư là người quyết định:** AI rất mạnh trong việc phân loại ngôn ngữ tự nhiên và soạn nháp văn bản, nhưng kỹ sư AI tại Vin Smart Future mới là người phải chịu trách nhiệm về ranh giới an toàn, kiểm soát rủi ro pháp lý và mang lại trải nghiệm sống tốt nhất cho cư dân Vinhomes.
