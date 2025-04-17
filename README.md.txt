Demo Thuật Toán PageRank

Dự án này là một demo thuật toán PageRank được triển khai bằng Python và Flask, cho phép tính toán và hiển thị kết quả PageRank cho các đồ thị trực tuyến. Thuật toán PageRank được sử dụng để đánh giá mức độ quan trọng của các nút trong đồ thị dựa trên các liên kết giữa các nút.

Giới Thiệu

Thuật toán PageRank của Google xếp hạng các trang web dựa trên sự liên kết giữa các trang đó. PageRank không chỉ đánh giá số lượng liên kết mà còn xem xét chất lượng của các liên kết. Mỗi liên kết giữa các trang web đại diện cho một "phiếu bầu" cho trang được liên kết.

Trong dự án này, bạn sẽ nhập các cạnh của đồ thị và thuật toán PageRank sẽ tính toán giá trị PageRank cho mỗi nút trong đồ thị.

 Yêu Cầu

Trước khi bắt đầu, bạn cần cài đặt một số công cụ và thư viện sau:

- Python: Đảm bảo rằng bạn đã cài đặt Python (phiên bản 3.x).
- Pip: Hệ thống quản lý thư viện Python, được cài sẵn với Python.

Cài Đặt

 1. Tạo môi trường ảo

Để đảm bảo rằng tất cả các thư viện cần thiết được cài đặt trong môi trường riêng biệt, bạn nên sử dụng môi trường ảo.

```bash
python -m venv venv

Cấu trúc dự án
Dự án có cấu trúc thư mục như sau:
PageRankDemo
│
├── app.py                  # File Python chính sử dụng Flask
├── templates/              # Thư mục chứa các file HTML
│   └── index.html          # File HTML chính cho giao diện người dùng
Giới thiệu về thuật toán PageRank
PageRank là một thuật toán được sử dụng để xếp hạng các trang web trong các công cụ tìm kiếm như Google. Thuật toán này dựa trên ý tưởng rằng một trang web có nhiều liên kết từ các trang khác sẽ có độ tin cậy cao hơn.

PageRank tính toán một giá trị cho mỗi nút trong đồ thị, biểu thị mức độ quan trọng của nó trong hệ thống. Các nút có giá trị PageRank cao hơn thường có ảnh hưởng lớn hơn trong mạng.

