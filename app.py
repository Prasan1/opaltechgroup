from flask import Flask, render_template_string, url_for
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Opal Tech Lab — Trust Infrastructure for Real-World Decisions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5, user-scalable=yes">
    <meta name="description" content="Opal Tech Lab builds trust-focused software for verification, pricing intelligence, and website trust monitoring.">
    <meta name="theme-color" content="#163b33">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

    <link rel="icon" type="image/png" href="{{ url_for('static', filename='images/opaltechlab-logo.png') }}">
    <!-- Bootstrap 3.4 -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #22302b;
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            background: #ffffff;
        }

        :root {
            --opal-deep: #0d1d35;
            --opal-ink: #111f38;
            --opal-muted: #5a6a82;
            --opal-line: #dde3ed;
            --opal-soft: #f2f5f9;
            --opal-green: #3a6fd8;
            --opal-green-dark: #2a57b8;
            --opal-blue: #2a57b8;
            --opal-gold: #c8963e;
        }

        /* Navigation */
        .navbar-custom {
            background: rgba(255, 255, 255, 0.98);
            border: none;
            border-bottom: 1px solid rgba(16, 36, 31, 0.08);
            margin-bottom: 0;
            min-height: 60px;
            box-shadow: 0 2px 14px rgba(16, 36, 31, 0.06);
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
            border-color: var(--opal-blue);
        }
        .navbar-custom .navbar-toggle .icon-bar {
            background-color: var(--opal-green-dark);
        }
        .navbar-custom .navbar-nav > li > a {
            padding: 15px 20px;
            font-size: 16px;
            font-weight: 600;
            color: #24352f;
            transition: color 0.3s;
        }
        .navbar-custom .navbar-nav > li > a:hover,
        .navbar-custom .navbar-nav > li > a:focus {
            color: var(--opal-green-dark);
            background: transparent;
        }
        .navbar-custom .navbar-collapse {
            border: none;
            box-shadow: none;
        }

        /* Hero */
        .hero {
            position: relative;
            background: url('{{ url_for('static', filename='images/opaltechlabcover.png') }}') center center;
            background-size: cover;
            background-attachment: scroll;
            color: #fff;
            padding: 105px 20px 78px;
            text-align: center;
            min-height: 540px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hero::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(160deg, rgba(10, 20, 40, 0.72) 0%, rgba(6, 13, 28, 0.82) 100%);
        }
        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 920px;
            margin: 0 auto;
            padding: 0 10px;
        }
        .hero-kicker {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: 1px solid rgba(255,255,255,0.18);
            background: rgba(255,255,255,0.08);
            border-radius: 999px;
            padding: 7px 14px;
            color: rgba(255,255,255,0.86);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            margin-bottom: 18px;
        }
        .hero-kicker-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #6a9de8;
            box-shadow: 0 0 0 4px rgba(106,157,232,0.18);
        }
        .hero h1 {
            font-size: 34px;
            font-weight: 800;
            margin-bottom: 16px;
            text-shadow: 0 2px 22px rgba(0, 0, 0, 0.35);
            letter-spacing: -0.045em;
            line-height: 1.06;
        }
        .hero .tagline {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 20px;
            opacity: 0.96;
            color: #8ab2e8;
            letter-spacing: 0.4px;
        }
        .hero p {
            font-size: 15px;
            max-width: 760px;
            margin: 0 auto;
            opacity: 0.91;
            line-height: 1.8;
            color: rgba(255,255,255,0.88);
        }

        /* Sections */
        .section {
            padding: 52px 20px;
        }
        .section-alt {
            background: var(--opal-soft);
            border-top: 1px solid var(--opal-line);
            border-bottom: 1px solid var(--opal-line);
        }
        .section h2 {
            margin-bottom: 30px;
            font-weight: 800;
            font-size: 26px;
            color: var(--opal-ink);
            letter-spacing: -0.03em;
        }
        .section-label {
            color: var(--opal-green-dark);
            display: block;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: .09em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .about-text {
            max-width: 100%;
            margin: 0 auto;
            font-size: 16px;
            line-height: 1.75;
            color: var(--opal-muted);
        }
        .about-text p {
            margin-bottom: 18px;
        }
        .about-text strong {
            color: var(--opal-green-dark);
            font-weight: 700;
        }

        /* Values */
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
            border: 1px solid var(--opal-line);
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(16, 36, 31, 0.04);
            font-size: 15px;
            color: var(--opal-muted);
            transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
        }
        .values li:active {
            transform: scale(0.98);
        }
        .values li strong {
            color: var(--opal-ink);
            font-weight: 800;
            font-size: 17px;
            display: block;
            margin-bottom: 5px;
        }

        /* Product Cards */
        .products-intro {
            max-width: 720px;
            margin: 0 auto 26px;
            color: var(--opal-muted);
            font-size: 15px;
            line-height: 1.75;
        }
        /* Equal-height row: make all col-md-4 siblings stretch to row height */
        .products-row {
            display: flex;
            flex-wrap: wrap;
            margin-left: -15px;
            margin-right: -15px;
        }
        .products-row .product-col {
            padding-left: 15px;
            padding-right: 15px;
            width: 100%;
            display: flex;
            margin-bottom: 24px;
        }
        @media (min-width: 992px) {
            .products-row .product-col {
                width: 33.3333%;
                margin-bottom: 0;
            }
        }
        .product-card {
            border: 1px solid var(--opal-line);
            padding: 32px 24px 28px;
            border-radius: 16px;
            text-align: center;
            background: #fff;
            box-shadow: 0 4px 20px rgba(16, 36, 31, 0.07);
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .product-card-top {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .product-card-top img {
            max-height: 56px;
            max-width: 200px;
            margin-bottom: 14px;
            object-fit: contain;
        }
        .product-card h3 {
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: 800;
            font-size: 22px;
            color: var(--opal-ink);
            letter-spacing: -0.025em;
        }
        .product-tag {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            border-radius: 999px;
            background: #eaf0fb;
            color: var(--opal-green-dark);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: .06em;
            text-transform: uppercase;
            padding: 5px 11px;
            margin-bottom: 12px;
        }
        .product-card p {
            font-size: 14px;
            line-height: 1.75;
            color: var(--opal-muted);
            margin-bottom: 0;
            flex: 1;
        }
        .product-card-btn {
            margin-top: 24px;
        }

        /* Buttons */
        .btn-primary {
            background: var(--opal-green-dark);
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            font-weight: 700;
            border-radius: 10px;
            transition: background 0.3s, transform 0.1s;
            display: inline-block;
            min-height: 48px;
            line-height: 1.1;
            color: #fff;
        }
        .btn-primary:active {
            transform: scale(0.97);
            background: #1e3f8a;
        }
        .btn-primary:hover,
        .btn-primary:focus {
            background: #1a3d96;
            color: #fff;
        }

        /* Thesis strip */
        .thesis-strip {
            background: var(--opal-deep);
            color: #fff;
            padding: 34px 20px;
            border-top: 1px solid rgba(255,255,255,0.06);
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .thesis-strip-inner {
            max-width: 980px;
            margin: 0 auto;
            display: grid;
            gap: 20px;
        }
        .thesis-item strong {
            display: block;
            color: #fff;
            font-size: 14px;
            margin-bottom: 4px;
        }
        .thesis-item span {
            color: rgba(255,255,255,0.62);
            font-size: 13px;
            line-height: 1.55;
        }

        /* Contact */
        .contact-section p {
            font-size: 16px;
            color: var(--opal-muted);
            line-height: 1.7;
        }
        .contact-section a {
            color: var(--opal-green-dark);
            font-weight: 700;
            text-decoration: none;
            word-break: break-word;
        }
        .contact-section a:active {
            opacity: 0.7;
        }

        /* Footer */
        .footer {
            background: #111816;
            padding: 25px 20px;
            text-align: center;
            color: rgba(255,255,255,0.55);
            font-size: 13px;
        }

        /* Tablet/Desktop */
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
                padding: 150px 20px 125px;
                min-height: 670px;
                background-attachment: fixed;
            }
            .hero h1 {
                font-size: 58px;
                margin-bottom: 20px;
            }
            .hero .tagline {
                font-size: 22px;
                margin-bottom: 24px;
            }
            .hero p {
                font-size: 19px;
            }

            .section {
                padding: 84px 40px;
            }
            .section h2 {
                font-size: 38px;
                margin-bottom: 40px;
            }
            .about-text {
                font-size: 17px;
                max-width: 820px;
            }
            .about-text p {
                margin-bottom: 20px;
            }

            .values {
                max-width: 860px;
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 16px;
            }
            .values li {
                padding: 22px;
                margin-bottom: 0;
                font-size: 15px;
            }
            .values li:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 24px rgba(16, 36, 31, 0.08);
                border-color: rgba(42,87,184,0.22);
            }
            .values li strong {
                font-size: 18px;
            }

            .product-card {
                padding: 36px 28px 30px;
                transition: transform 0.25s, box-shadow 0.25s, border-color 0.2s;
            }
            .product-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 16px 36px rgba(16, 36, 31, 0.11);
                border-color: rgba(42,87,184,0.28);
            }
            .product-card h3 {
                font-size: 24px;
            }
            .product-card p {
                font-size: 15px;
            }

            .btn-primary {
                padding: 14px 28px;
                font-size: 16px;
            }

            .thesis-strip-inner {
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 28px;
            }
            .thesis-item strong {
                font-size: 15px;
            }
            .thesis-item span {
                font-size: 13px;
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
                font-size: 64px;
            }
            .section {
                padding: 92px 40px;
            }
        }
    </style>
</head>
<body>

<!-- Navigation -->
<nav class="navbar navbar-custom navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse" aria-label="Toggle navigation">
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
        <div class="hero-kicker">
            <span class="hero-kicker-dot" aria-hidden="true"></span>
            Verification · Pricing Intelligence · Trust Monitoring
        </div>
        <h1>Opal Tech Lab</h1>
        <div class="tagline">Software that reduces uncertainty before important decisions.</div>
        <p>
            Opal Tech Lab, under <strong>Opal, LLC</strong>, builds trust-focused software
            that helps people verify information, understand risk, and make clearer decisions —
            from doctor verification to home repair pricing and website trust monitoring.
        </p>
    </div>
</div>

<!-- About -->
<div id="about" class="section container text-center">
    <span class="section-label">About</span>
    <h2>Trust infrastructure for practical decisions</h2>
    <div class="about-text">
        <p>
            Opal Tech Lab is the product and experimentation arm of <strong>Opal, LLC</strong>.
            We build focused software tools for places where people need more clarity before
            they choose, hire, publish, or trust.
        </p>
        <p>
            Our products are intentionally simple: verify what matters, explain what is uncertain,
            and avoid dark patterns that turn users into leads before they understand the decision.
        </p>
    </div>
</div>

<!-- Thesis Strip -->
<div class="thesis-strip">
    <div class="thesis-strip-inner">
        <div class="thesis-item">
            <strong>Verify before trust</strong>
            <span>RankSewa helps people check doctor identity and registration signals before choosing care.</span>
        </div>
        <div class="thesis-item">
            <strong>Understand before paying</strong>
            <span>Lokaaro helps homeowners understand local repair pricing before hiring or approving a quote.</span>
        </div>
        <div class="thesis-item">
            <strong>Monitor before it breaks</strong>
            <span>PolicyGen watches for website trust gaps before customers, clients, or regulators notice.</span>
        </div>
    </div>
</div>

<!-- Values -->
<div id="values" class="section section-alt">
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <span class="section-label text-center">Values</span>
                <h2 class="text-center">What We Care About</h2>
                <ul class="values">
                    <li><strong>Clarity:</strong> Products should explain what they know, what they do not know, and what users can do next.</li>
                    <li><strong>Trust:</strong> We do not build dark patterns, lead traps, or tools that quietly sell user intent.</li>
                    <li><strong>Focus:</strong> We prefer narrow tools that solve real problems over bloated platforms that promise everything.</li>
                    <li><strong>Longevity:</strong> We build systems that can improve over time through better evidence, feedback, and monitoring.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Products -->
<div id="products" class="section container">
    <div class="row">
        <div class="col-md-12 text-center">
            <span class="section-label">Products</span>
            <h2>Focused tools, one trust-first direction</h2>
            <p class="products-intro">
                Each product tackles a different kind of uncertainty: professional identity,
                local pricing, and website trust.
            </p>
        </div>
    </div>
    <div class="products-row" style="margin-top:28px;">
        <div class="product-col">
            <div class="product-card">
                <div class="product-card-top">
                    <img src="{{ url_for('static', filename='images/ranksewa-logo.svg') }}" alt="RankSewa" style="height:40px;width:40px;">
                    <div class="product-tag">Doctor Verification</div>
                    <h3>RankSewa</h3>
                    <p>
                        A verification-first doctor directory for Nepal. Search doctors by name,
                        specialty, or city and look for clear registration and verification signals.
                    </p>
                </div>
                <div class="product-card-btn">
                    <a href="https://ranksewa.com" class="btn btn-primary" target="_blank" rel="noopener">Visit RankSewa</a>
                </div>
            </div>
        </div>
        <div class="product-col">
            <div class="product-card">
                <div class="product-card-top">
                    <img src="{{ url_for('static', filename='images/lokaaro-logo.svg') }}" alt="Lokaaro" style="height:40px;width:40px;">
                    <div class="product-tag">Pricing Intelligence</div>
                    <h3>Lokaaro</h3>
                    <p>
                        Local home repair pricing guidance for homeowners. Check typical ranges,
                        compare quotes, and understand what to ask before hiring anyone.
                    </p>
                </div>
                <div class="product-card-btn">
                    <a href="https://lokaaro.com" class="btn btn-primary" target="_blank" rel="noopener">Visit Lokaaro</a>
                </div>
            </div>
        </div>
        <div class="product-col">
            <div class="product-card">
                <div class="product-card-top">
                    <img src="{{ url_for('static', filename='images/policygen-logo.svg') }}" alt="PolicyGen" style="height:40px;width:40px;">
                    <div class="product-tag">Website Trust Monitoring</div>
                    <h3>PolicyGen</h3>
                    <p>
                        Website trust monitoring for SMBs and agencies. Scan for missing policy links,
                        broken legal pages, tracking disclosure gaps, and trust-breaking changes.
                    </p>
                </div>
                <div class="product-card-btn">
                    <a href="https://policygen.org" class="btn btn-primary" target="_blank" rel="noopener">Visit PolicyGen</a>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Contact -->
<div id="contact" class="section section-alt">
    <div class="container text-center contact-section">
        <span class="section-label">Contact</span>
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
    $(document).ready(function(){
        $('a[href^="#"]').on('click', function(e) {
            e.preventDefault();
            var target = $(this.getAttribute('href'));
            if(target.length) {
                var offset = window.innerWidth >= 768 ? 70 : 60;
                $('html, body').stop().animate({
                    scrollTop: target.offset().top - offset
                }, 400);

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
    return render_template_string(HTML, year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
