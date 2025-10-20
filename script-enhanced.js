// Enhanced JavaScript for High-Converting Sales Page

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive features
    initSnowEffect();
    initCountdownTimer();
    initScrollEffects();
    initAccordion();
    initExitIntent();
    initFloatingCTA();
    initSocialProofTicker();
    initPurchaseTracking();
});

// ===== SNOW EFFECT =====
function initSnowEffect() {
    const snowContainer = document.getElementById('snow-container');
    if (!snowContainer) return;

    const snowflakes = ['❄', '❅', '❆'];
    const numberOfSnowflakes = 50;

    for (let i = 0; i < numberOfSnowflakes; i++) {
        createSnowflake(snowContainer, snowflakes);
    }
}

function createSnowflake(container, snowflakes) {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    snowflake.innerHTML = snowflakes[Math.floor(Math.random() * snowflakes.length)];

    // Random properties
    const size = Math.random() * 15 + 10;
    const left = Math.random() * 100;
    const duration = Math.random() * 15 + 10;
    const delay = Math.random() * 10;

    snowflake.style.fontSize = `${size}px`;
    snowflake.style.left = `${left}%`;
    snowflake.style.animationDuration = `${duration}s`;
    snowflake.style.animationDelay = `${delay}s`;

    container.appendChild(snowflake);

    // Remove and recreate after animation completes
    setTimeout(() => {
        if (snowflake.parentNode) {
            snowflake.parentNode.removeChild(snowflake);
            createSnowflake(container, snowflakes);
        }
    }, (duration + delay) * 1000);
}

// ===== COUNTDOWN TIMER =====
function initCountdownTimer() {
    // Set end time (24 hours from now)
    const endTime = new Date().getTime() + (24 * 60 * 60 * 1000);

    function updateTimer() {
        const now = new Date().getTime();
        const distance = endTime - now;

        if (distance < 0) {
            // Reset timer if expired
            const newEndTime = new Date().getTime() + (24 * 60 * 60 * 1000);
            updateTimerDisplay(newEndTime - now);
            return;
        }

        updateTimerDisplay(distance);
    }

    function updateTimerDisplay(distance) {
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Update all timer elements
        const timerElements = ['timer', 'final-timer'];
        timerElements.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
            }
        });

        // Update individual countdown elements
        const hoursEl = document.getElementById('hours');
        const minutesEl = document.getElementById('minutes');
        const secondsEl = document.getElementById('seconds');

        if (hoursEl) hoursEl.textContent = pad(hours);
        if (minutesEl) minutesEl.textContent = pad(minutes);
        if (secondsEl) secondsEl.textContent = pad(seconds);
    }

    function pad(num) {
        return num < 10 ? '0' + num : num;
    }

    // Update every second
    updateTimer();
    setInterval(updateTimer, 1000);
}

// ===== SCROLL EFFECTS =====
function initScrollEffects() {
    const navbar = document.getElementById('mainNav');
    const floatingCta = document.getElementById('floatingCta');

    window.addEventListener('scroll', debounce(() => {
        const scrolled = window.pageYOffset;

        // Navbar effect
        if (navbar) {
            if (scrolled > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        // Show floating CTA after scrolling 30%
        if (floatingCta) {
            const windowHeight = document.documentElement.scrollHeight;
            const thirtyPercent = windowHeight * 0.3;

            if (scrolled > thirtyPercent) {
                floatingCta.classList.add('active');
            } else {
                floatingCta.classList.remove('active');
            }
        }

        // Fade in elements on scroll
        fadeInOnScroll();
    }, 10));
}

function fadeInOnScroll() {
    const elements = document.querySelectorAll('.review-card, .bonus-card, .faq-item');

    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (elementTop < windowHeight - 100) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
}

// ===== ACCORDION =====
function togglePart(element) {
    const part = element.parentElement;
    const isActive = part.classList.contains('active');

    // Close all parts
    document.querySelectorAll('.accordion-part').forEach(p => {
        p.classList.remove('active');
    });

    // Open clicked part if it wasn\'t active
    if (!isActive) {
        part.classList.add('active');
    }
}

// Make togglePart global
window.togglePart = togglePart;

// ===== EXIT INTENT POPUP =====
function initExitIntent() {
    const exitPopup = document.getElementById('exit-popup');
    if (!exitPopup) return;

    let popupShown = false;

    // Track mouse leaving viewport
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY < 0 && !popupShown) {
            showExitPopup();
            popupShown = true;
        }
    });

    // Mobile: show after 30 seconds if not purchased
    if (window.innerWidth <= 768) {
        setTimeout(() => {
            if (!popupShown && !localStorage.getItem('purchased')) {
                showExitPopup();
                popupShown = true;
            }
        }, 30000);
    }

    function showExitPopup() {
        exitPopup.classList.add('active');
        startPopupTimer();
    }

    function startPopupTimer() {
        let timeLeft = 300; // 5 minutes
        const popupTimerEl = document.getElementById('popup-timer');

        if (!popupTimerEl) return;

        const interval = setInterval(() => {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            popupTimerEl.textContent = `${pad(minutes)}:${pad(seconds)}`;

            if (timeLeft <= 0) {
                clearInterval(interval);
            }
        }, 1000);
    }

    function pad(num) {
        return num < 10 ? '0' + num : num;
    }
}

function closePopup() {
    const exitPopup = document.getElementById('exit-popup');
    if (exitPopup) {
        exitPopup.classList.remove('active');
    }
}

// Make closePopup global
window.closePopup = closePopup;

// ===== FLOATING CTA =====
function initFloatingCTA() {
    const floatingCta = document.getElementById('floatingCta');
    if (!floatingCta) return;

    // Pulse effect every 5 seconds
    setInterval(() => {
        floatingCta.style.animation = 'none';
        setTimeout(() => {
            floatingCta.style.animation = 'pulse 0.5s ease';
        }, 10);
    }, 5000);
}

// ===== SOCIAL PROOF TICKER =====
function initSocialProofTicker() {
    const names = [
        { name: 'Sarah', location: 'London, UK' },
        { name: 'Michael', location: 'Toronto, Canada' },
        { name: 'Emma', location: 'Boston, US' },
        { name: 'James', location: 'Edinburgh, UK' },
        { name: 'Lisa', location: 'Vancouver, Canada' },
        { name: 'Rachel', location: 'Portland, US' },
        { name: 'David', location: 'Manchester, UK' },
        { name: 'Sophie', location: 'Montreal, Canada' },
        { name: 'John', location: 'Seattle, US' }
    ];

    // Update ticker every 5 seconds
    setInterval(() => {
        const randomPerson = names[Math.floor(Math.random() * names.length)];
        const tickerItems = document.querySelectorAll('.ticker-item');

        tickerItems.forEach(item => {
            item.textContent = `${randomPerson.name} from ${randomPerson.location} just purchased ✨`;
            item.style.animation = 'none';
            setTimeout(() => {
                item.style.animation = 'ticker 15s linear infinite';
            }, 10);
        });
    }, 8000);
}

// ===== PURCHASE TRACKING =====
function initPurchaseTracking() {
    const buyButtons = document.querySelectorAll('.btn-buy, .btn-bundle');

    buyButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Track purchase intent
            const format = this.textContent.includes('Bundle') ? 'bundle' : 
                         this.textContent.includes('eBook') ? 'ebook' : 'paperback';

            trackEvent('purchase_intent', {
                format: format,
                price: this.closest('.purchase-option')?.querySelector('.sale-price-big')?.textContent || 'unknown'
            });

            // Show loading state
            const originalText = this.innerHTML;
            this.innerHTML = '⏳ Processing...';
            this.style.pointerEvents = 'none';

            // Simulate processing (replace with actual purchase flow)
            setTimeout(() => {
                this.innerHTML = originalText;
                this.style.pointerEvents = 'auto';
            }, 2000);
        });
    });

    // Track store button clicks
    document.querySelectorAll('.store-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            const storeName = this.textContent.trim();
            trackEvent('store_click', { store: storeName });
        });
    });
}

// ===== ANALYTICS TRACKING =====
function trackEvent(eventName, eventData = {}) {
    // Google Analytics 4 tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, eventData);
    }

    // Facebook Pixel tracking
    if (typeof fbq !== 'undefined') {
        fbq('track', eventName, eventData);
    }

    // Console log for development
    console.log(`Event tracked: ${eventName}`, eventData);
}

// ===== SMOOTH SCROLLING =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 120;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// ===== FORM HANDLING =====
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]')?.value;

        if (email && validateEmail(email)) {
            // Track lead capture
            trackEvent('lead_capture', { email: email });

            // Show success message
            showSuccessMessage(this);

            // Reset form
            this.reset();
        } else {
            showErrorMessage('Please enter a valid email address', this);
        }
    });
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showSuccessMessage(form) {
    const successMsg = document.createElement('div');
    successMsg.className = 'success-message';
    successMsg.innerHTML = '✨ Success! Check your email for your free gift.';
    successMsg.style.cssText = `
        background: linear-gradient(135deg, #27ae60, #229954);
        color: white;
        padding: 1rem;
        border-radius: 12px;
        margin-top: 1rem;
        text-align: center;
        animation: fadeInUp 0.5s ease;
    `;

    form.parentNode.insertBefore(successMsg, form.nextSibling);

    setTimeout(() => {
        successMsg.remove();
    }, 5000);
}

function showErrorMessage(message, form) {
    const errorMsg = document.createElement('div');
    errorMsg.className = 'error-message';
    errorMsg.textContent = message;
    errorMsg.style.cssText = `
        background: #e74c3c;
        color: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin-top: 0.5rem;
        text-align: center;
    `;

    form.appendChild(errorMsg);

    setTimeout(() => {
        errorMsg.remove();
    }, 3000);
}

// ===== LAZY LOADING =====
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

initLazyLoading();

// ===== 3D BOOK EFFECT =====
document.querySelectorAll('.book-cover-3d').forEach(book => {
    book.addEventListener('mousemove', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 10;
        const rotateY = -(x - centerX) / 10;

        this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
    });

    book.addEventListener('mouseleave', function() {
        this.style.transform = 'perspective(1000px) rotateY(-15deg) rotateX(5deg)';
    });
});

// ===== URGENCY COUNTER =====
function updateUrgencyBadge() {
    const urgencyBadge = document.querySelector('.urgency-badge');
    if (!urgencyBadge) return;

    // Simulate decreasing stock
    setInterval(() => {
        const currentNumber = parseInt(urgencyBadge.innerHTML.match(/\d+/)[0]);
        const newNumber = currentNumber - Math.floor(Math.random() * 3) - 1;

        if (newNumber > 450) {
            urgencyBadge.innerHTML = urgencyBadge.innerHTML.replace(/\d+/, newNumber);
        }
    }, 30000); // Update every 30 seconds
}

updateUrgencyBadge();

// ===== GIFT BOX ANIMATION =====
document.querySelectorAll('.gift-badge').forEach(badge => {
    badge.addEventListener('mouseenter', function() {
        this.style.animation = 'none';
        setTimeout(() => {
            this.style.animation = 'bounce 0.5s ease';
        }, 10);
    });
});

// ===== DEBOUNCE UTILITY =====
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ===== KEYBOARD ACCESSIBILITY =====
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closePopup();
    }
});

// ===== PRINT PREVENTION FOR PIRACY =====
window.addEventListener('beforeprint', function(e) {
    if (confirm('This content is protected. Would you like to purchase a legal copy instead?')) {
        window.location.href = '#get-book';
        e.preventDefault();
    }
});

// ===== LOCAL STORAGE TRACKING =====
function trackUserSession() {
    // Track visits
    let visits = parseInt(localStorage.getItem('visits') || '0');
    visits++;
    localStorage.setItem('visits', visits);

    // First visit timestamp
    if (!localStorage.getItem('firstVisit')) {
        localStorage.setItem('firstVisit', new Date().toISOString());
    }

    // Show special offer for returning visitors
    if (visits > 2 && !localStorage.getItem('purchased')) {
        setTimeout(() => {
            showReturnVisitorOffer();
        }, 10000);
    }
}

function showReturnVisitorOffer() {
    const announcement = document.querySelector('.announcement-bar');
    if (announcement) {
        announcement.style.background = 'linear-gradient(135deg, #27ae60, #229954)';
        announcement.querySelector('.announcement-content').innerHTML = 
            '🎉 <strong>WELCOME BACK!</strong> Here\'s an extra 10% OFF just for you! Use code: <strong>COMEBACK10</strong> at checkout';
    }
}

trackUserSession();

// ===== A/B TESTING PLACEHOLDER =====
function initABTesting() {
    // Randomly assign variant
    const variant = Math.random() > 0.5 ? 'A' : 'B';
    localStorage.setItem('variant', variant);

    // Track variant
    trackEvent('ab_test_assigned', { variant: variant });

    // Apply variant changes
    if (variant === 'B') {
        // Example: Change CTA text
        document.querySelectorAll('.btn-primary').forEach(btn => {
            if (btn.textContent.includes('Get Your Copy')) {
                btn.textContent = btn.textContent.replace('Get Your Copy', 'Start Reading Now');
            }
        });
    }
}

// Uncomment to enable A/B testing
// initABTesting();

// ===== PERFORMANCE MONITORING =====
window.addEventListener('load', function() {
    const loadTime = performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart;
    trackEvent('page_load_time', { load_time: loadTime });

    console.log(`Page loaded in ${loadTime}ms`);
});

// ===== CONSOLE ART =====
console.log(`
╔═══════════════════════════════════════╗
║                                       ║
║     ❄ THE WINTERING WELL ❄           ║
║                                       ║
║   A Cozy Guide to Finding Joy         ║
║   in the Quiet Season                 ║
║                                       ║
║   Built with love & mindfulness       ║
║   © 2025 All Rights Reserved          ║
║                                       ║
╚═══════════════════════════════════════╝
`);