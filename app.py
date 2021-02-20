from flask import Flask, render_template
import corona_crawling

app = Flask(__name__)

@app.route('/')
def index():
    data = corona_crawling.corona_summary()
    city_data = corona_crawling.corona_data()
    print("국내 데이터", data)
    print("시도 데이터", city_data)

    return render_template('index.html', corona_data=data, corona_city=city_data)

if __name__ == "__main__":
    app.run(debug=True)