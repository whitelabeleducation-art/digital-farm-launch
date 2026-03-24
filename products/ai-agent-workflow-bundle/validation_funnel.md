# Validation Funnel - Waitlist & Preorder Path

## Purpose
Capture real demand signals and validate interest even without live checkout.

---

## Option 1: Preorder Page (No Checkout Required)

### Preorder Page Copy
```html
<!DOCTYPE html>
<html>
<head>
    <title>AI Agent Workflow Bundle - Preorder</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px; }
        h1 { color: #2c3e50; }
        .price { font-size: 2em; color: #27ae60; font-weight: bold; }
        .cta { background: #3498db; color: white; padding: 15px; text-align: center; border-radius: 5px; display: block; margin: 20px 0; text-decoration: none; }
        .note { background: #fff3cd; padding: 15px; border-radius: 5px; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>AI Agent Workflow Bundle - Preorder</h1>
    <p>Save 15+ hours every week with these copy-paste automation workflows.</p>
    <p class="price">Preorder Price: $37 (20% off)</p>
    <p><strong>Release Date:</strong> [TBD - sign up to be notified]</p>
    <a href="#" class="cta">Join Waitlist - Get Early Access</a>
    <div class="note">
        <strong>Why preorder?</strong> Be among the first customers, get 20% off, and help shape the final product with your feedback.
    </div>
    <p><small>No charge today. You'll be notified when the product launches.</small></p>
</body>
</html>
```

### Preorder Form Fields (Typeform/Cal.com alternative)
- Name
- Email
- Primary pain point (dropdown: "too much admin work", "missed leads", "manual follow-ups", "other")
- Current automation tools used (optional)
- How did you find us? (optional)

---

## Option 2: Lead Magnet Path (Zero Price Barrier)

### Free Lead Magnet: "7 Automation Ideas for Solopreneurs"
- PDF guide with 7 automation concepts
- No email required to download OR
- Email required for download (capture)

### Funnel:
1. Landing page with free guide offer
2. Email capture
3. Deliver free PDF
4. Upsell to paid bundle (email sequence)

---

## Option 3: Interest Capture Form

### Simple Form (Google Forms / Typeform embed)
**Form Title**: Automation Interest Check

**Questions**:
1. What's your biggest time-waster? (text)
2. What tools do you currently use? (checkboxes: Zapier, Make, n8n, None, Other)
3. What's your email? (required)
4. Would you pay for a complete automation bundle? (yes/no/maybe)

### Tracking
- Log all responses in docs/validation_signals.md
- Count yes/maybe as positive signals
- Target: 10+ positive signals = validation

---

## Option 4: "Founding Customer" Offer

### Founding Customer Landing Page
- Limited time: First 50 customers only
- Price: $37 (regular $47)
- Bonus: 1-on-1 Slack support (first 20)
- Urgency: "Founding Customer spots: X remaining"

### This can be run without checkout
- Use Google Form to capture orders
- Manual invoice/PayPal later
- OR use Gumroad waitlist feature

---

## Validation Signal Tracking

### docs/validation_signals.md Format
```markdown
# Validation Signals - AI Agent Workflow Bundle

## Date | Signal Type | Source | Details
2026-03-23 | Preorder interest | Website form | 5 signups
2026-03-23 | Upvote | Reddit r/smallbusiness | 12 upvotes on post
2026-03-23 | DM request | X/Twitter | 3 people asked for link
```

### Signal Definitions
- **Email signup**: Lead captured
- **Preorder**: Intent to buy
- **DM request**: High intent
- **Upvote/Engagement**: Interest signal
- **Payment**: REAL validation (first target)

### Success Criteria
- 10+ email signups = validated lead interest
- 5+ DM requests = validated purchase intent
- 1+ preorders/payments = REAL revenue (target achieved)