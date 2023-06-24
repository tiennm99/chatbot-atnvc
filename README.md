# chatbot-atnvc
Chat bot with knowledge of "Anh trai nhân vật chính", a novel from https://ln.hako.vn/sang-tac/8476-kiep-nay-la-anh-trai-cua-nhan-vat-chinh

# How to run
1. Install requirements
    ```
    pip install -r requirements.txt
    ```
2. Run prepare.py to prepare data
    ```
    python prepare.py
    ```
    __Note__: You may get `HTTP Error 429: Too Many Requests`. Then you can try again later, and skip downloaded chapters, example skip 50 first chapters like:
    ```
    for chapter in chapters[50:]:
    ```
3. Run app.py to start chatbot
    ```
    python app.py
    ```