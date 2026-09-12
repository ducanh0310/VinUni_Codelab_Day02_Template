# AI Log & Reflection

Trong buổi Lab 02, tôi đã sử dụng AI như một “thought partner” để hỗ trợ quá trình scoping bài toán AI cho Vin Smart Future, đặc biệt là trong mảng Vinhomes. Tôi dùng AI để brainstorm, rà soát cấu trúc bài toán, và xây dựng các prompt/prototype. Vai trò của AI không phải là người quyết định cuối cùng, mà là người hỗ trợ suy nghĩ, định hình vấn đề và kiểm tra các ranh giới vận hành.

AI đã giúp tôi rất nhiều ở các bước đầu tiên của quá trình:

1. Brainstorm các bài toán thực tế trong Vinhomes.  
   Tôi dán prompt mô tả vai trò “AI Engineer tại Vin Smart Future” và yêu cầu AI gợi ý 5 bài toán vận hành. AI giúp tôi nhanh chóng nghĩ ra các pain point như phản ánh sự cố kỹ thuật, phản hồi cư dân, hồ sơ quản lý cư dân, và xử lý yêu cầu dịch vụ nội bộ. Đây là bước rất hữu ích vì AI giúp tôi chuyển từ một ý tưởng mơ hồ sang một danh sách cụ thể.

2. Tạo và định hình Quick Problem Cards.  
   Tôi dùng AI để tạo cấu trúc thẻ vấn đề: mô tả bài toán, actor, workflow thủ công, bottleneck, metric và kiến trúc AI phù hợp. AI giúp tôi tiết kiệm thời gian trong việc viết theo template chuẩn của worksheet.

3. Hoàn thiện Problem Deep-Dive.  
   Trong Phase 3, AI hỗ trợ tôi diễn giải workflow hiện tại, xác định bottleneck, viết Problem Statement 6-field, và định nghĩa ranh giới vận hành. Nó giúp tôi tổ chức nội dung rõ ràng hơn, đồng thời gợi ý cách xác định AI fit theo LLM Feature và Rule/State-Machine.

4. Dựng prompt prototype.  
   AI cũng giúp tôi sắp xếp logic của prompt: xác định role, output schema, hệ thống ranh giới an toàn và các trường dữ liệu cần trích xuất. Điều này giúp tôi hình dung được một bản mẫu thử nghiệm kỹ thuật.

Tuy nhiên, quá trình sử dụng AI cũng cho thấy rõ các điểm mà AI trả lời sai, thiếu căn cứ, hoặc “hallucination”.

Một lỗi đầu tiên là AI đã gợi ý các bài toán khá rộng và chưa đủ bám sát Vinhomes. Ví dụ, nó đề xuất các bài toán liên quan đến “phản hồi 1-star” hoặc “nội dung phản ánh cư dân” mà thiếu ngữ cảnh kỹ thuật cụ thể. Tôi đã nhận ra rằng câu trả lời này quá trừu tượng và không thể trực tiếp đưa vào problem statement. Tôi đã sửa prompt bằng cách yêu cầu AI “chỉ gợi ý bài toán có thể được mô hình hóa bằng LLM Feature, có người chịu trách nhiệm và có workflow rõ, không dùng dữ liệu giả.” Sau đó, AI mới bắt đầu đưa ra các bài toán bám sát hơn.

Một lỗi thứ hai là AI cố gắng sinh metric và workflow quá đẹp nhưng thiếu căn cứ về thời gian và đơn vị vận hành. Ví dụ, AI đề xuất “giảm thời gian xử lý từ 15 phút xuống dưới 1 phút” mà không giải thích rõ nguồn dữ liệu. Tôi đã sửa lại bằng cách yêu cầu: “không được đặt metric không có căn cứ; hãy ưu tiên lập luận dựa trên workflow thủ công và handoff hiện tại”, và yêu cầu “metric cần có số, có phạm vi, có ranh giới cho hệ thống AI”.

Một lỗi thứ ba quan trọng là AI dễ vượt ranh giới vận hành nếu tôi không ràng buộc. Ví dụ, khi tôi thử hỏi AI gợi ý cách tự động gửi phản hồi hay tự động chốt xử lý sự cố, AI có xu hướng trả lời như một người xử lý công việc hoàn toàn thay con người. Tôi đã sửa prompt bằng cách định nghĩa rõ “AI được phép đề xuất, không được quyết định cuối cùng; AI không tự động chốt sửa chữa, không tự động đóng ticket, không hứa thời gian xử lý mà không có xác nhận.” Tôi còn thêm yêu cầu “nếu thiếu thông tin như căn hộ, khu vực, loại sự cố thì cần chuyển sang Human-in-the-loop”.

Tôi cũng nhận thấy AI dễ “học theo phong cách” của worksheet và tạo ra câu trả lời quá “lạnh”, không phản ánh được bối cảnh thực tế doanh nghiệp Vin Smart Future. Do đó, tôi đã chỉnh prompt theo một cấu trúc rõ: vai trò, nhiệm vụ, ranh giới, output schema, và yêu cầu đề cao tính thực tế. Tôi nhấn mạnh rằng bài toán phải thuộc Vinhomes; phải có workflow thủ công hiện tại; phải có bottleneck và metric; không được tạo thông tin giả hoặc quá mức.

Về ý nghĩa cá nhân, việc dùng AI trong buổi học đã giúp tôi hiểu rõ hơn rằng AI là một công cụ hỗ trợ tư duy, không phải thay thế người ra quyết định. AI làm tăng tốc độ brainstorm và tổ chức thông tin, nhưng điều quan trọng là con người phải kiểm tra logic, dữ liệu, metric, và ranh giới vận hành. Nếu không làm rõ ranh giới và không kiểm thử, AI có thể đưa ra lời giải đáp mơ hồ, thậm chí nguy hiểm cho quy trình vận hành.

Tóm lại, tôi học được rằng với một bài toán scoping AI ở Vin Smart Future, AI phải được sử dụng như một “trợ lý đồng hành” có ràng buộc chặt chẽ, không được dùng tùy tiện để sinh thông tin. Tôi đã sửa prompt theo hướng bám dữ kiện, bám workflow, bám Human-in-the-loop, và cấm AI tự động quyết định hay tự động gửi phản hồi. Cách làm này giúp cho output có tính khả thi kỹ thuật và rủi ro nằm trong tầm kiểm soát, đồng thời tạo nền tảng tốt cho phase prototype.