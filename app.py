from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Tugas Docker Compose</h1>

    <h2>Data Mahasiswa</h2>

    <p>Nama : Ahmad Tamrani Noprian</p>
    <p>NPM : 2410010022</p>
    <p>Mata Kuliah : Cloud Computing</p>

    <hr>

    <h3>Docker Compose Berhasil Berjalan</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)