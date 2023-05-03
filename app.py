from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

# Pengambilan POST 
@app.route("/hitung", methods=["POST"])
def hitung_post():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hitung = bil1 + bil2
    return jsonify({'hasil' : hitung})

# POST dan GET menyatu
@app.route("/pembagian", methods=['POST', 'GET'])
def pembagian():
    if(request.method == "POST"):
        bil1 = int(request.form['bil1'])
        bil2 = int(request.form['bil2'])
        hitung = bil1 / bil2
        return jsonify({'hasil' : hitung}) 
    return render_template('pembagian.html')

# POST dan GET menyatu
@app.route("/perkalian", methods=['POST', 'GET'])
def perkalian():
    if(request.method == "POST"):
        bil1 = int(request.form['bil1'])
        bil2 = int(request.form['bil2'])
        hitung = bil1 * bil2
        return jsonify({'hasil' : hitung}) 
    return render_template('perkalian.html')


# POST dan GET terpisah
@app.route("/pengurangan", methods=["POST"])
def pengurangan_post():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hitung = bil1 - bil2
    return jsonify({'hasil' : hitung})

@app.route("/pengurangan", methods=["GET"])
def pengurangan_get():
    return render_template('pengurangan.html')




if __name__ == '__main__':
 app.run('0.0.0.0', port=5000, debug=True)