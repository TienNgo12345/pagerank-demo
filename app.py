from flask import Flask, render_template
import pagerank  # Gọi file pagerank.py đã tạo

app = Flask(__name__)

@app.route('/')
def index():
    pr = pagerank.calculate_pagerank()
    return render_template('index.html', pagerank=pr)

if __name__ == '__main__':
    app.run(debug=True)
