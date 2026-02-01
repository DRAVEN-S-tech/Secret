from flask import Flask, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Get Well Soon Gouri</title>
<style>
body {
    margin: 0;
    min-height: 100vh;
    background: #f4efe8;
    font-family: Georgia, serif;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #5a3e2b;
    overflow: hidden;
}
.box {
    background: #fffaf3;
    padding: 32px 28px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(90,62,43,0.15);
    text-align: center;
    max-width: 420px;
    width: 90%;
    position: relative;
    z-index: 2;
    animation: up 1.6s ease;
}
h1 {
    font-size: 30px;
    margin-bottom: 12px;
    animation: pulse 3s infinite;
}
p {
    font-size: 17px;
    line-height: 1.6;
    margin-bottom: 18px;
}
.line {
    font-size: 18px;
    font-weight: bold;
    color: #7a5236;
}
.seed {
    position: absolute;
    width: 6px;
    height: 6px;
    background: #c8b6a6;
    border-radius: 50%;
    opacity: 0.7;
    animation: float 12s linear infinite;
}
.seed::after {
    content: "";
    position: absolute;
    width: 14px;
    height: 1px;
    background: #c8b6a6;
    top: 50%;
    left: 6px;
}
@keyframes float {
    from {
        transform: translateY(110vh) translateX(0);
        opacity: 0;
    }
    20% { opacity: 0.7; }
    to {
        transform: translateY(-20vh) translateX(40px);
        opacity: 0;
    }
}
@keyframes up {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.04); }
    100% { transform: scale(1); }
}
</style>
</head>
<body>
<div class="seed" style="left:10%; animation-delay:0s"></div>
<div class="seed" style="left:25%; animation-delay:3s"></div>
<div class="seed" style="left:40%; animation-delay:6s"></div>
<div class="seed" style="left:60%; animation-delay:2s"></div>
<div class="seed" style="left:75%; animation-delay:5s"></div>
<div class="seed" style="left:90%; animation-delay:1s"></div>

<div class="box">
    <h1>Get Well Soon, Gouri 🤍</h1>
    <p>
        Take all the time you need to rest and heal.
        May each day feel lighter and calmer.
    </p>
    <div class="line">
        jaldi theek hoja waffles 🧇
    </div>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)

if __name__ == "__main__":
    app.run(debug=True)
