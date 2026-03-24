# Multi-Path Checkout Strategy

## Primary Checkout Path

**Link:** [WAITING ON OPERATOR - PayPal.Me / Ko-fi / Gumroad]

**Flow:**
1. Buyer clicks link
2. Selects product
3. Enters payment
4. Receives download link via email

---

## Backup Checkout Paths

### Path 1: Manual PayPal
- **Setup:** Operator sends PayPal request
- **Use when:** Primary link not working
- **Process:** DM "I'll send you a PayPal request" → Send invoice → Confirm → Send bundle

### Path 2: Manual Stripe
- **Setup:** Operator sends Stripe payment link
- **Use when:** Customer prefers card
- **Process:** DM "Here's your Stripe link" → Customer pays → Confirm → Send bundle

### Path 3: Preorder (No Payment)
- **Setup:** Capture email, promise delivery later
- **Use when:** Checkout not ready, want to capture demand
- **Process:** DM "Reply PREORDER and I'll add you to the list" → Collect emails → Convert when checkout ready

### Path 4: DM-to-Buy Direct
- **Setup:** No link needed, manual everything
- **Use when:** Total checkout failure
- **Process:** Customer says "I want to buy" → Ask PayPal/Stripe → Send payment request → Confirm → Send

### Path 5: Waitlist (Zero Payment)
- **Setup:** Email capture only, no immediate sale
- **Use when:** Checkout down, want to capture interest
- **Process:** Landing page → "Join waitlist" → Email capture → Later convert to sale

---

## Payment Path Selection Matrix

| Situation | Best Path |
|-----------|-----------|
| Checkout link ready | Path 1 (Primary) |
| Link down, customer has PayPal | Path 2 (Manual PayPal) |
| Customer prefers card | Path 3 (Manual Stripe) |
| Customer hesitant, want to preorder | Path 4 (Preorder) |
| Total checkout failure | Path 5 (DM-to-Buy) |
| No checkout at all | Path 6 (Waitlist) |

---

## Quick Switch Protocol

If primary checkout fails:
1. Switch to secondary path in < 5 minutes
2. Update landing page to show alternate
3. Note in control/checkout_status.md which path active

---

## Operator Action Required

**ONE LINK NEEDED** to activate Path 1.

All other paths work without operator but are manual/scalable:
- Preorder: No payment, email only
- Waitlist: No payment, email capture
- DM-to-Buy: Manual close

**Status:** Path 1 blocked. Paths 2-6 operational.