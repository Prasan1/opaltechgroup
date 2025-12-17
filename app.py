from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Opal Tech Lab - Forms · Templates · Solutions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5, user-scalable=yes">
    <meta name="description" content="Opal Tech Lab - A technology studio building clear, compliant, and practical software products for businesses.">
    <meta name="theme-color" content="#2c5f7f">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

    <!-- Bootstrap 3.4 -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        /* Mobile-First Design */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* Navigation - Mobile First */
        .navbar-custom {
            background: rgba(255, 255, 255, 0.98);
            border: none;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            margin-bottom: 0;
            min-height: 60px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }
        .navbar-custom .navbar-brand {
            padding: 5px 15px;
            height: 60px;
        }
        .navbar-custom .navbar-brand img {
            height: 45px;
            width: auto;
        }
        .navbar-custom .navbar-toggle {
            margin-top: 13px;
            margin-bottom: 13px;
            border-color: #2c5f7f;
        }
        .navbar-custom .navbar-toggle .icon-bar {
            background-color: #2c5f7f;
        }
        .navbar-custom .navbar-nav > li > a {
            padding: 15px 20px;
            font-size: 16px;
            font-weight: 500;
            color: #333;
            transition: color 0.3s;
        }
        .navbar-custom .navbar-nav > li > a:hover,
        .navbar-custom .navbar-nav > li > a:focus {
            color: #2c5f7f;
            background: transparent;
        }
        .navbar-custom .navbar-collapse {
            border: none;
            box-shadow: none;
        }

        /* Hero Section - Mobile Optimized */
        .hero {
            position: relative;
            background: url('{{ url_for('static', filename='images/opaltechlabcover.png') }}') center center;
            background-size: cover;
            background-attachment: scroll;
            color: #fff;
            padding: 100px 20px 80px;
            text-align: center;
            min-height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(31, 60, 74, 0.88), rgba(15, 32, 39, 0.92));
        }
        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 100%;
            margin: 0 auto;
            padding: 0 10px;
        }
        .hero h1 {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 0 2px 20px rgba(0, 0, 0, 0.4);
            letter-spacing: -0.5px;
        }
        .hero .tagline {
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 20px;
            opacity: 0.95;
            color: #87CEEB;
            letter-spacing: 1px;
        }
        .hero p {
            font-size: 15px;
            max-width: 100%;
            margin: 0 auto;
            opacity: 0.92;
            line-height: 1.7;
        }

        /* Sections - Mobile First */
        .section {
            padding: 50px 20px;
        }
        .section-alt {
            background: #f8f9fa;
        }
        .section h2 {
            margin-bottom: 30px;
            font-weight: 700;
            font-size: 26px;
            color: #1a1a1a;
        }
        .about-text {
            max-width: 100%;
            margin: 0 auto;
            font-size: 16px;
            line-height: 1.75;
            color: #555;
        }
        .about-text p {
            margin-bottom: 18px;
        }
        .about-text strong {
            color: #2c5f7f;
            font-weight: 600;
        }

        /* Values - Mobile Optimized */
        .values {
            list-style: none;
            max-width: 100%;
            margin: 0 auto;
            padding: 0;
        }
        .values li {
            margin-bottom: 15px;
            padding: 18px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            font-size: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .values li:active {
            transform: scale(0.98);
        }
        .values li strong {
            color: #2c5f7f;
            font-weight: 600;
            font-size: 17px;
            display: block;
            margin-bottom: 5px;
        }

        /* Product Card - Mobile Optimized */
        .product-card {
            border: 1px solid #e0e0e0;
            padding: 30px 20px;
            border-radius: 12px;
            text-align: center;
            background: #fff;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            max-width: 100%;
            margin: 0 auto;
        }
        .product-card h3 {
            margin-top: 0;
            margin-bottom: 15px;
            font-weight: 700;
            font-size: 24px;
            color: #1a1a1a;
        }
        .product-card p {
            font-size: 15px;
            line-height: 1.7;
            color: #666;
            margin-bottom: 25px;
        }

        /* Buttons - Touch Optimized */
        .btn-primary {
            background: #2c5f7f;
            border: none;
            padding: 16px 40px;
            font-size: 17px;
            font-weight: 600;
            border-radius: 8px;
            transition: background 0.3s, transform 0.1s;
            display: inline-block;
            min-height: 48px;
            line-height: 1;
        }
        .btn-primary:active {
            transform: scale(0.97);
            background: #1e4a5f;
        }
        .btn-primary:hover,
        .btn-primary:focus {
            background: #1e4a5f;
            color: #fff;
        }

        /* Contact - Mobile Optimized */
        .contact-section p {
            font-size: 16px;
            color: #555;
            line-height: 1.7;
        }
        .contact-section a {
            color: #2c5f7f;
            font-weight: 600;
            text-decoration: none;
            word-break: break-word;
        }
        .contact-section a:active {
            opacity: 0.7;
        }

        /* Footer */
        .footer {
            background: #1a1a1a;
            padding: 25px 20px;
            text-align: center;
            color: #aaa;
            font-size: 13px;
        }

        /* Tablet and Desktop Enhancements */
        @media (min-width: 768px) {
            .navbar-custom {
                min-height: 70px;
            }
            .navbar-custom .navbar-brand {
                padding: 10px 15px;
                height: 70px;
            }
            .navbar-custom .navbar-brand img {
                height: 50px;
            }
            .navbar-custom .navbar-nav {
                margin-top: 12px;
            }

            .hero {
                padding: 140px 20px 120px;
                min-height: 650px;
                background-attachment: fixed;
            }
            .hero h1 {
                font-size: 56px;
                margin-bottom: 20px;
            }
            .hero .tagline {
                font-size: 22px;
                margin-bottom: 25px;
            }
            .hero p {
                font-size: 19px;
                max-width: 750px;
            }

            .section {
                padding: 80px 40px;
            }
            .section h2 {
                font-size: 38px;
                margin-bottom: 40px;
            }
            .about-text {
                font-size: 17px;
                max-width: 800px;
            }
            .about-text p {
                margin-bottom: 20px;
            }

            .values {
                max-width: 800px;
            }
            .values li {
                padding: 22px;
                margin-bottom: 18px;
                font-size: 16px;
            }
            .values li:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
            }
            .values li strong {
                font-size: 18px;
            }

            .product-card {
                padding: 45px;
                max-width: 550px;
                transition: transform 0.3s, box-shadow 0.3s;
            }
            .product-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
            }
            .product-card h3 {
                font-size: 30px;
            }
            .product-card p {
                font-size: 16px;
            }

            .btn-primary {
                padding: 14px 36px;
                font-size: 17px;
            }

            .contact-section p {
                font-size: 18px;
            }

            .footer {
                font-size: 14px;
                padding: 30px 20px;
            }
        }

        @media (min-width: 992px) {
            .hero h1 {
                font-size: 60px;
            }
            .section {
                padding: 90px 40px;
            }
        }
    </style>
</head>
<body>

<!-- Navigation -->
<nav class="navbar navbar-custom navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">
                <img src="{{ url_for('static', filename='images/opaltechlab-logo.png') }}" alt="Opal Tech Lab">
            </a>
        </div>
        <div class="collapse navbar-collapse" id="navbar-collapse">
            <ul class="nav navbar-nav navbar-right" style="margin-top: 12px;">
                <li><a href="#about">About</a></li>
                <li><a href="#values">Values</a></li>
                <li><a href="#products">Products</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </div>
</nav>

<!-- Hero -->
<div class="hero">
    <div class="hero-content">
        <h1>Opal Tech Lab</h1>
        <div class="tagline">Forms · Templates · Solutions</div>
        <p>
            A technology studio under <strong>Opal, LLC</strong>, focused on building
            clear, compliant, and practical software products that businesses can trust.
        </p>
    </div>
</div>

<!-- About -->
<div id="about" class="section container text-center">
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
<div id="values" class="section section-alt">
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <h2 class="text-center">What We Care About</h2>
                <ul class="values">
                    <li><strong>Clarity:</strong> Products should explain themselves.</li>
                    <li><strong>Trust:</strong> We don't sell user data or design dark patterns.</li>
                    <li><strong>Simplicity:</strong> Fewer features, done well.</li>
                    <li><strong>Longevity:</strong> Built to last, not to churn.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Products -->
<div id="products" class="section container">
    <div class="row">
        <div class="col-md-12 text-center">
            <h2>Products</h2>
        </div>
    </div>
    <div class="row" style="margin-top:35px;">
        <div class="col-md-8 col-md-offset-2">
            <div class="product-card">
                <h3>PolicyGen</h3>
                <p>
                    Generate privacy policies, terms, and compliance documents
                    without unnecessary complexity or legal overhead.
                </p>
                <a href="https://policygen.org" class="btn btn-primary" target="_blank">Visit PolicyGen</a>
            </div>
        </div>
    </div>
</div>

<!-- Contact -->
<div id="contact" class="section section-alt">
    <div class="container text-center contact-section">
        <h2>Contact</h2>
        <p>
            For business inquiries or questions, reach us at
            <a href="mailto:contact@opaltechlab.com">contact@opaltechlab.com</a>
        </p>
    </div>
</div>

<!-- Footer -->
<div class="footer">
    © {{ year }} Opal, LLC. All rights reserved.
</div>

<!-- jQuery + Bootstrap JS -->
<script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>

<script>
    // Smooth scroll with offset for fixed navbar (responsive)
    $(document).ready(function(){
        $('a[href^="#"]').on('click', function(e) {
            e.preventDefault();
            var target = $(this.getAttribute('href'));
            if(target.length) {
                // Different navbar heights for mobile vs desktop
                var offset = window.innerWidth >= 768 ? 70 : 60;
                // Faster scroll animation (400ms instead of 800ms)
                $('html, body').stop().animate({
                    scrollTop: target.offset().top - offset
                }, 400);

                // Close mobile menu after clicking
                if(window.innerWidth < 768) {
                    $('.navbar-collapse').collapse('hide');
                }
            }
        });
    });
</script>

</body>
</html>
"""

@app.route("/")
def home():
    from datetime import datetime
    return render_template_string(HTML, year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)

