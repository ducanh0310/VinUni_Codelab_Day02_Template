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