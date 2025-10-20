# Create ENHANCED CSS with animations, effects, and high-CTR design
enhanced_css = '''/* Enhanced Styles with High CTR/CTA and Interactive Effects */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #2c3e50;
    --secondary-color: #d4a574;
    --accent-color: #8b7355;
    --warm-white: #faf9f7;
    --soft-gray: #f5f3f0;
    --text-dark: #2c3e50;
    --text-light: #6c757d;
    --cozy-orange: #d2691e;
    --winter-blue: #4a6fa5;
    --success-green: #27ae60;
    --urgency-red: #e74c3c;
    --gold: #f39c12;
    
    --font-primary: 'Playfair Display', serif;
    --font-secondary: 'Inter', sans-serif;
    
    --shadow-soft: 0 4px 20px rgba(0, 0, 0, 0.08);
    --shadow-warm: 0 8px 32px rgba(212, 165, 116, 0.15);
    --shadow-strong: 0 12px 40px rgba(0, 0, 0, 0.15);
    --border-radius: 12px;
}

body {
    font-family: var(--font-secondary);
    line-height: 1.7;
    color: var(--text-dark);
    background-color: var(--warm-white);
    overflow-x: hidden;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Snow Effect */
#snow-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 999;
    overflow: hidden;
}

.snowflake {
    position: absolute;
    top: -10px;
    color: rgba(255, 255, 255, 0.8);
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    animation: snowfall linear infinite;
}

@keyframes snowfall {
    0% {
        transform: translateY(-10px) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(100vh) rotate(360deg);
        opacity: 0.5;
    }
}

/* Announcement Bar */
.announcement-bar {
    background: linear-gradient(135deg, var(--urgency-red), #c0392b);
    color: white;
    padding: 0.8rem 0;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1001;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    animation: slideDown 0.5s ease;
}

@keyframes slideDown {
    from {
        transform: translateY(-100%);
    }
    to {
        transform: translateY(0);
    }
}

.announcement-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
    font-size: 0.95rem;
}

#countdown-timer {
    font-weight: 600;
    padding: 0.3rem 0.8rem;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
}

.announcement-cta {
    background: white;
    color: var(--urgency-red);
    padding: 0.4rem 1rem;
    border-radius: 20px;
    text-decoration: none;
    font-weight: 600;
    transition: transform 0.3s ease;
}

.announcement-cta:hover {
    transform: scale(1.05);
}

/* Navigation */
.navbar {
    background: rgba(250, 249, 247, 0.95);
    backdrop-filter: blur(10px);
    position: fixed;
    top: 40px;
    width: 100%;
    z-index: 1000;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(212, 165, 116, 0.1);
    transition: all 0.3s ease;
}

.navbar.scrolled {
    top: 0;
    background: rgba(250, 249, 247, 0.98);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: var(--font-primary);
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--primary-color);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.snowflake-icon {
    animation: rotate 10s linear infinite;
}

@keyframes rotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    text-decoration: none;
    color: var(--text-light);
    font-weight: 400;
    transition: color 0.3s ease;
}

.nav-menu a:hover {
    color: var(--secondary-color);
}

.nav-cta-btn {
    background: linear-gradient(135deg, var(--secondary-color), var(--cozy-orange));
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    box-shadow: var(--shadow-warm);
    transition: all 0.3s ease;
}

.nav-cta-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(212, 165, 116, 0.3);
}

/* Pulse Animation */
.pulse {
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(212, 165, 116, 0.7);
    }
    50% {
        box-shadow: 0 0 0 10px rgba(212, 165, 116, 0);
    }
}

.pulse-continuous {
    animation: pulseContinuous 1.5s ease-in-out infinite;
}

@keyframes pulseContinuous {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
}

/* Hero Section */
.hero {
    padding: 12rem 0 8rem;
    background: linear-gradient(135deg, var(--warm-white) 0%, var(--soft-gray) 50%, var(--warm-white) 100%);
    position: relative;
    overflow: hidden;
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 4rem;
    align-items: center;
}

.urgency-badge {
    background: linear-gradient(135deg, var(--urgency-red), #c0392b);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 30px;
    display: inline-block;
    margin-bottom: 2rem;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
}

.flash {
    animation: flash 2s ease-in-out infinite;
}

@keyframes flash {
    0%, 50%, 100% {
        opacity: 1;
    }
    25%, 75% {
        opacity: 0.7;
    }
}

.hero-content h1 {
    font-size: 4.5rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, var(--primary-color), var(--accent-color), var(--secondary-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}

.hero-content h2 {
    font-size: 2rem;
    color: var(--text-dark);
    margin-bottom: 1rem;
    font-weight: 600;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: var(--text-light);
    margin-bottom: 2rem;
    line-height: 1.6;
}

.hero-stats {
    display: flex;
    gap: 3rem;
    margin-bottom: 2rem;
}

.stat {
    display: flex;
    flex-direction: column;
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: var(--secondary-color);
    font-family: var(--font-primary);
}

.stat-label {
    font-size: 0.9rem;
    color: var(--text-light);
}

/* Buttons */
.btn-primary, .btn-secondary {
    display: inline-block;
    padding: 1.2rem 2.5rem;
    border-radius: var(--border-radius);
    text-decoration: none;
    font-weight: 600;
    font-family: var(--font-secondary);
    transition: all 0.3s ease;
    cursor: pointer;
    border: 2px solid transparent;
    text-align: center;
}

.btn-primary {
    background: linear-gradient(135deg, var(--secondary-color), var(--cozy-orange));
    color: white;
    box-shadow: var(--shadow-warm);
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(212, 165, 116, 0.35);
}

.btn-large {
    padding: 1.5rem 3rem;
    font-size: 1.1rem;
}

.btn-huge {
    padding: 2rem 4rem;
    font-size: 1.3rem;
}

.btn-icon {
    font-size: 1.3rem;
    margin-right: 0.5rem;
}

.btn-subtext {
    display: block;
    font-size: 0.85rem;
    font-weight: 400;
    opacity: 0.9;
    margin-top: 0.3rem;
}

.cta-buttons {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.trust-badges {
    display: flex;
    gap: 2rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.trust-item {
    display: flex;
    align-items: center;
    color: var(--success-green);
    font-weight: 500;
    font-size: 0.95rem;
}

/* Social Proof Ticker */
.social-proof-ticker {
    background: rgba(255, 255, 255, 0.7);
    padding: 1rem;
    border-radius: var(--border-radius);
    overflow: hidden;
    position: relative;
}

.ticker-item {
    color: var(--text-light);
    font-size: 0.9rem;
    animation: ticker 15s linear infinite;
}

@keyframes ticker {
    0% {
        transform: translateX(100%);
    }
    100% {
        transform: translateX(-100%);
    }
}

/* 3D Book Display */
.book-3d-container {
    position: relative;
    perspective: 1000px;
}

.book-cover-3d {
    max-width: 100%;
    height: auto;
    border-radius: var(--border-radius);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    transform: rotateY(-15deg) rotateX(5deg);
    transition: transform 0.5s ease;
}

.book-cover-3d:hover {
    transform: rotateY(0deg) rotateX(0deg) scale(1.05);
}

.gift-badge {
    position: absolute;
    top: -20px;
    right: -20px;
    background: linear-gradient(135deg, var(--urgency-red), var(--gold));
    color: white;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    box-shadow: 0 8px 30px rgba(231, 76, 60, 0.4);
    animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-10px);
    }
}

.gift-icon {
    font-size: 2rem;
}

.gift-text {
    font-size: 0.65rem;
    font-weight: 700;
    line-height: 1.2;
    margin-top: 0.3rem;
}

.bonus-stack {
    margin-top: 2rem;
}

.bonus-item {
    background: white;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    margin-bottom: 0.5rem;
    box-shadow: var(--shadow-soft);
    color: var(--text-dark);
    font-weight: 500;
}

/* Urgency Section */
.urgency-section {
    padding: 4rem 0;
    background: linear-gradient(135deg, var(--urgency-red), #c0392b);
}

.urgency-box {
    background: white;
    border-radius: var(--border-radius);
    padding: 3rem;
    display: flex;
    align-items: center;
    gap: 3rem;
    box-shadow: var(--shadow-strong);
}

.urgency-icon {
    font-size: 5rem;
    animation: ring 1s ease-in-out infinite;
}

@keyframes ring {
    0%, 100% {
        transform: rotate(-10deg);
    }
    50% {
        transform: rotate(10deg);
    }
}

.countdown-display {
    display: flex;
    gap: 2rem;
    margin: 2rem 0;
}

.countdown-item {
    text-align: center;
}

.countdown-number {
    display: block;
    font-size: 4rem;
    font-weight: 700;
    color: var(--urgency-red);
    font-family: var(--font-primary);
    line-height: 1;
}

.countdown-label {
    display: block;
    color: var(--text-light);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

/* Problem-Agitate-Solution */
.pas-section {
    padding: 6rem 0;
    background: var(--warm-white);
}

.pas-section h2 {
    text-align: center;
    font-size: 3rem;
    margin-bottom: 4rem;
}

.pas-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
}

.problem-box, .solution-box {
    background: white;
    padding: 3rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
}

.problem-box {
    border-left: 5px solid var(--urgency-red);
}

.solution-box {
    border-left: 5px solid var(--success-green);
}

.problem-icon, .solution-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
}

.pas-grid h3 {
    margin-bottom: 1.5rem;
}

.pas-grid ul {
    list-style: none;
    padding: 0;
}

.pas-grid li {
    padding: 0.8rem 0;
    padding-left: 2rem;
    position: relative;
}

.problem-box li:before {
    content: "✗";
    position: absolute;
    left: 0;
    color: var(--urgency-red);
    font-weight: 700;
}

.solution-box li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--success-green);
    font-weight: 700;
}

/* Interactive Accordion */
.contents-detailed {
    padding: 6rem 0;
    background: var(--soft-gray);
}

.section-subtitle {
    text-align: center;
    color: var(--text-light);
    font-size: 1.2rem;
    margin-bottom: 3rem;
}

.contents-accordion {
    max-width: 900px;
    margin: 0 auto 3rem;
}

.accordion-part {
    background: white;
    border-radius: var(--border-radius);
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-soft);
    overflow: hidden;
    transition: all 0.3s ease;
}

.accordion-part:hover {
    box-shadow: var(--shadow-warm);
}

.part-header {
    padding: 2rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: white;
    transition: background 0.3s ease;
}

.part-header:hover {
    background: var(--soft-gray);
}

.part-header h3 {
    margin: 0;
    color: var(--primary-color);
}

.season-tag {
    font-size: 0.9rem;
    color: var(--secondary-color);
    font-weight: 400;
}

.accordion-icon {
    font-size: 2rem;
    color: var(--secondary-color);
    transition: transform 0.3s ease;
}

.accordion-part.active .accordion-icon {
    transform: rotate(45deg);
}

.part-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
}

.accordion-part.active .part-content {
    max-height: 2000px;
}

.chapter-item {
    padding: 1.5rem 2rem;
    border-top: 1px solid var(--soft-gray);
}

.chapter-item strong {
    color: var(--accent-color);
    display: block;
    margin-bottom: 0.5rem;
}

.contents-cta {
    text-align: center;
    background: white;
    padding: 3rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-strong);
}

.strike-price {
    text-decoration: line-through;
    color: var(--text-light);
    font-size: 1.2rem;
}

.sale-price {
    color: var(--urgency-red);
    font-size: 2rem;
    font-weight: 700;
}

/* Reviews Section */
.reviews-section {
    padding: 6rem 0;
    background: var(--warm-white);
}

.reviews-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-bottom: 3rem;
}

.review-card {
    background: white;
    padding: 2rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
    transition: all 0.3s ease;
}

.review-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-warm);
}

.review-card.featured {
    grid-column: span 2;
    background: linear-gradient(135deg, var(--winter-blue), var(--primary-color));
    color: white;
}

.review-stars {
    color: var(--gold);
    font-size: 1.3rem;
    margin-bottom: 1rem;
}

.review-card h4 {
    margin-bottom: 1rem;
}

.review-card.featured h4,
.review-card.featured p {
    color: white;
}

.reviewer {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 0.9rem;
    color: var(--text-light);
}

.review-card.featured .reviewer {
    border-top-color: rgba(255, 255, 255, 0.3);
    color: rgba(255, 255, 255, 0.9);
}

.review-stats {
    display: flex;
    gap: 3rem;
    justify-content: center;
    margin-bottom: 3rem;
}

.stat-box {
    text-align: center;
    padding: 2rem;
    background: white;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
}

.stat-big {
    font-size: 3rem;
    font-weight: 700;
    color: var(--secondary-color);
    font-family: var(--font-primary);
}

.stat-label {
    color: var(--text-light);
    margin-top: 0.5rem;
}

.stat-stars {
    color: var(--gold);
    font-size: 1.5rem;
    margin-top: 0.5rem;
}

/* Bonus Section */
.bonus-section {
    padding: 6rem 0;
    background: linear-gradient(135deg, var(--soft-gray), var(--warm-white));
}

.bonus-section h2 {
    text-align: center;
    font-size: 3rem;
}

.bonus-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    margin-top: 3rem;
}

.bonus-card {
    background: white;
    padding: 2rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
    text-align: center;
    transition: all 0.3s ease;
}

.bonus-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: var(--shadow-strong);
}

.bonus-image-placeholder {
    width: 100%;
    height: 150px;
    background: var(--soft-gray);
    border-radius: var(--border-radius);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.gift-box-icon {
    font-size: 4rem;
    animation: bounce 2s ease-in-out infinite;
}

.bonus-value {
    color: var(--success-green);
    font-weight: 600;
    margin: 0.5rem 0;
}

.total-value {
    text-align: center;
    margin: 3rem 0 2rem;
}

.total-value h3 {
    color: var(--text-light);
}

.total-value h2 {
    color: var(--success-green);
    font-size: 3rem;
}

/* Purchase Section */
.purchase-main {
    padding: 6rem 0;
    background: var(--warm-white);
}

.purchase-hero {
    text-align: center;
    margin-bottom: 4rem;
}

.purchase-subtitle {
    font-size: 1.2rem;
    color: var(--text-light);
}

.purchase-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-bottom: 3rem;
}

.purchase-option {
    background: white;
    padding: 2.5rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
    position: relative;
    transition: all 0.3s ease;
}

.purchase-option:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-strong);
}

.purchase-option.recommended {
    border: 3px solid var(--secondary-color);
    transform: scale(1.05);
}

.recommended-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, var(--gold), var(--cozy-orange));
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.9rem;
    box-shadow: 0 4px 15px rgba(243, 156, 18, 0.4);
}

.price-display {
    text-align: center;
    margin: 1.5rem 0;
}

.original-price {
    display: block;
    text-decoration: line-through;
    color: var(--text-light);
    font-size: 1.2rem;
}

.sale-price-big {
    display: block;
    font-size: 4rem;
    font-weight: 700;
    color: var(--secondary-color);
    font-family: var(--font-primary);
    line-height: 1;
}

.savings-badge {
    display: inline-block;
    background: var(--success-green);
    color: white;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-top: 0.5rem;
}

.includes-list {
    list-style: none;
    padding: 0;
    margin: 2rem 0;
}

.includes-list li {
    padding: 0.6rem 0;
    border-bottom: 1px solid var(--soft-gray);
}

.btn-buy {
    width: 100%;
    background: linear-gradient(135deg, var(--secondary-color), var(--cozy-orange));
    color: white;
    padding: 1.2rem;
    border: none;
    border-radius: var(--border-radius);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
    text-decoration: none;
    display: block;
}

.btn-buy:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(212, 165, 116, 0.4);
}

.btn-bundle {
    background: linear-gradient(135deg, var(--success-green), #229954);
}

.store-links {
    text-align: center;
    margin: 3rem 0;
}

.store-label {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.store-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.store-btn {
    background: var(--primary-color);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;
}

.store-btn:hover {
    background: var(--accent-color);
    transform: translateY(-2px);
}

.guarantee-box {
    background: var(--soft-gray);
    padding: 2rem;
    border-radius: var(--border-radius);
    display: flex;
    align-items: center;
    gap: 2rem;
}

.guarantee-icon {
    font-size: 4rem;
}

/* FAQ Section */
.faq-section {
    padding: 6rem 0;
    background: var(--soft-gray);
}

.faq-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
}

.faq-item {
    background: white;
    padding: 2rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-soft);
}

.faq-item h3 {
    color: var(--primary-color);
    margin-bottom: 1rem;
}

/* Final CTA */
.final-cta {
    padding: 6rem 0;
    background: linear-gradient(135deg, var(--winter-blue), var(--primary-color));
    color: white;
}

.final-cta h2 {
    color: white;
    text-align: center;
    font-size: 3.5rem;
    margin-bottom: 2rem;
}

.final-cta p {
    text-align: center;
    font-size: 1.2rem;
    max-width: 800px;
    margin: 0 auto 2rem;
    color: rgba(255, 255, 255, 0.95);
}

.final-offer-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    background: white;
    padding: 3rem;
    border-radius: var(--border-radius);
    color: var(--text-dark);
}

.offer-column ul {
    list-style: none;
    padding: 0;
}

.offer-column li {
    padding: 0.8rem 0;
    font-size: 1.1rem;
}

.final-price-box {
    background: var(--soft-gray);
    padding: 2rem;
    border-radius: var(--border-radius);
    text-align: center;
}

.final-price-label {
    color: var(--text-light);
    font-size: 1rem;
    margin-top: 1rem;
}

.final-price-strike {
    text-decoration: line-through;
    color: var(--text-light);
    font-size: 1.5rem;
}

.final-price-main {
    font-size: 5rem;
    font-weight: 700;
    color: var(--urgency-red);
    font-family: var(--font-primary);
    line-height: 1;
    margin: 1rem 0;
}

.final-savings {
    color: var(--success-green);
    font-weight: 700;
    font-size: 1.2rem;
}

.urgency-text {
    background: var(--urgency-red);
    color: white;
    padding: 1rem;
    border-radius: var(--border-radius);
    margin: 1.5rem 0;
    font-weight: 600;
}

.secure-checkout {
    color: var(--text-light);
    font-size: 0.9rem;
    margin-top: 1rem;
}

/* Exit Popup */
.exit-popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 10000;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.exit-popup.active {
    display: flex;
}

.popup-content {
    background: white;
    padding: 3rem;
    border-radius: var(--border-radius);
    max-width: 600px;
    position: relative;
    animation: slideUp 0.3s ease;
}

@keyframes slideUp {
    from {
        transform: translateY(50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.popup-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: var(--text-light);
}

.popup-offer {
    text-align: center;
    margin-top: 2rem;
}

.popup-timer {
    background: var(--urgency-red);
    color: white;
    padding: 1rem;
    border-radius: var(--border-radius);
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

.popup-price-big {
    font-size: 4rem;
    color: var(--secondary-color);
}

.popup-regular {
    display: block;
    text-decoration: line-through;
    color: var(--text-light);
}

/* Floating CTA */
.floating-cta {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: white;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
    border-radius: 50px;
    padding: 1rem 2rem;
    z-index: 999;
    display: none;
    animation: slideInRight 0.5s ease;
}

@keyframes slideInRight {
    from {
        transform: translateX(100%);
    }
    to {
        transform: translateX(0);
    }
}

.floating-cta.active {
    display: block;
}

.floating-cta-content {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.floating-cta-text {
    font-weight: 600;
    color: var(--text-dark);
}

.floating-cta-btn {
    background: linear-gradient(135deg, var(--secondary-color), var(--cozy-orange));
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

.floating-cta-btn:hover {
    transform: scale(1.05);
}

/* Footer */
.footer {
    background: var(--primary-color);
    color: white;
    padding: 4rem 0 2rem;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 3rem;
    margin-bottom: 2rem;
}

.footer-section h3 {
    color: var(--secondary-color);
    margin-bottom: 1.5rem;
}

.footer-section ul {
    list-style: none;
}

.footer-section li {
    margin-bottom: 0.5rem;
}

.footer-section a {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-section a:hover {
    color: var(--secondary-color);
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 2rem;
    text-align: center;
    color: rgba(255, 255, 255, 0.6);
}

.footer-bottom a {
    color: var(--secondary-color);
    text-decoration: none;
}

/* Responsive Design */
@media (max-width: 1024px) {
    .hero-container,
    .pas-grid,
    .final-offer-box {
        grid-template-columns: 1fr;
    }
    
    .reviews-grid,
    .bonus-grid,
    .purchase-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .container {
        padding: 0 1rem;
    }
    
    h1 {
        font-size: 2.5rem;
    }
    
    h2 {
        font-size: 2rem;
    }
    
    .hero {
        padding: 10rem 0 6rem;
    }
    
    .reviews-grid,
    .bonus-grid,
    .purchase-grid,
    .faq-grid {
        grid-template-columns: 1fr;
    }
    
    .hero-stats,
    .countdown-display,
    .review-stats {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-menu {
        display: none;
    }
    
    .floating-cta {
        bottom: 10px;
        right: 10px;
        padding: 0.8rem 1rem;
    }
    
    .floating-cta-content {
        flex-direction: column;
        gap: 0.5rem;
    }
}'''

with open('styles-enhanced.css', 'w', encoding='utf-8') as f:
    f.write(enhanced_css)

print("✅ ENHANCED CSS created with snow effects, animations, and interactive design!")