from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Opal Tech Lab</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap 3.4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

    <style>
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color:#333; }
        .hero {
            background: linear-gradient(135deg, #1f3c4a, #0f2027);
            color: #fff;
            padding: 70px 20px 60px;
            text-align: center;
        }
        .hero h1 { font-size: 40px; font-weight: 600; margin-bottom: 10px; }
        .hero p { font-size: 17px; max-width: 720px; margin: 0 auto; opacity: 0.95; }
        .section { padding: 45px 20px; }
        .section h2 { margin-bottom: 25px; font-weight: 600; }
        .about-text { max-width: 780px; margin: 0 auto; font-size: 16px; line-height: 1.7; }
        .product-card {
            border: 1px solid #eaeaea;
            padding: 28px;
            border-radius: 8px;
            text-align: center;
            background: #fff;
            box-shadow: 0 6px 16px rgba(0,0,0,0.04);
        }
        .product-card h3 { margin-top: 0; font-weight: 600; }
        .values li { margin-bottom: 10px; }
        .footer {
            background: #f7f7f7;
            padding: 25px 20px;
            text-align: center;
            color: #777;
            margin-top: 30px;
            font-size: 14px;
        }
    </style>
</head>
<body>

<!-- Hero -->
<div class="hero">
    <h1>Opal Tech Lab</h1>
    <p>
        A technology studio under <strong>Opal, LLC</strong>, focused on building
        clear, compliant, and practical software products that businesses can trust.
    </p>
</div>

<!-- About -->
<div class="section container text-center">
    <h2>Who We Are</h2>
    <div class="about-text">
        <p>
            Opal Tech Lab is the product and experimentation arm of <strong>Opal, LLC</strong>.
            We design and operate focused software tools that solve real operational
            and compliance problems for modern businesses.
        </p>
        <p>
            We believe good software should be <strong>simple</strong>,
            <strong>transparent</strong>, and <strong>maintainable</strong> — not bloated,
            confusing, or built for legal teams instead of users.
        </p>
    </div>
</div>

<!-- Values -->
<div class="section container">
    <div class="row">
        <div class="col-md-10 col-md-offset-1">
            <h2 class="text-center">What We Care About</h2>
            <ul class="values">
                <li><strong>Clarity:</strong> Products should explain themselves.</li>
                <li><strong>Trust:</strong> We don’t sell user data or design dark patterns.</li>
                <li><strong>Simplicity:</strong> Fewer features, done well.</li>
                <li><strong>Longevity:</strong> Built to last, not to churn.</li>
            </ul>
        </div>
    </div>
</div>

<!-- Products -->
<div class="section container">
    <div class="row">
        <div class="col-md-12 text-center">
            <h2>Products</h2>
        </div>
    </div>
    <div class="row" style="margin-top:35px;">
        <div class="col-md-4 col-md-offset-4">
            <div class="product-card">
                <h3>PolicyGen</h3>
                <p>
                    Generate privacy policies, terms, and compliance documents
                    without unnecessary complexity or legal overhead.
                </p>
                <a href="https://policygen.org" class="btn btn-primary">Visit PolicyGen</a>
            </div>
        </div>
    </div>
</div>

<!-- Contact -->
<div class="section container text-center">
    <h2>Contact</h2>
    <p>
        For business inquiries or questions, reach us at
        <a href="mailto:contact@opaltechlab.com">contact@opaltechlab.com</a>
    </p>
</div>

<!-- Footer -->
<div class="footer">
    © {{ year }} Opal, LLC. All rights reserved.
</div>

<!-- jQuery + Bootstrap JS -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

</body>
</html>
"""

@app.route("/")
def home():
    from datetime import datetime
    return render_template_string(HTML, year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)

