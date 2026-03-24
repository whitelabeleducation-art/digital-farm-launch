#!/usr/bin/env python3
"""
PAYMENT LINK ACTIVATION ENGINE
===============================

Purpose: Automatically inject payment link into all assets and activate revenue engine.

Usage: python scripts/payment_link_activator.py

Behavior:
- Reads payment link from control/payment_link.txt
- Validates the link format
- Propagates link to all target assets
- Updates status in master_state.json
- Creates activation report
"""

import os
import re
import json
import sys
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent.parent
CONTROL_DIR = BASE_DIR / "control"
SCRIPTS_DIR = BASE_DIR / "scripts"
DIST_DIR = BASE_DIR / "distribution"
DOCS_DIR = BASE_DIR / "docs"
PRODUCTS_DIR = BASE_DIR / "products"

PAYMENT_LINK_FILE = CONTROL_DIR / "payment_link.txt"
MASTER_STATE_FILE = CONTROL_DIR / "master_state.json"
ACTIVATION_REPORT_FILE = CONTROL_DIR / "activation_report.md"

# Targets that need payment link injection
PROPAGATION_TARGETS = {
    # Distribution packets
    "warm_network_100k_packet.md": DIST_DIR / "warm_network_100k_packet.md",
    "founder_outreach_100k_packet.md": DIST_DIR / "founder_outreach_100k_packet.md",
    "enterprise_outreach_packet.md": DIST_DIR / "enterprise_outreach_packet.md",
    "same_day_100k_packet.md": DIST_DIR / "same_day_100k_packet.md",
    "high_ticket_dm_packet.md": DIST_DIR / "high_ticket_dm_packet.md",
    "day0_dm_closers.md": DIST_DIR / "day0_dm_closers.md",
    "day0_execution_stack.md": DIST_DIR / "day0_execution_stack.md",
    
    # Control files
    "manual_cash_capture.md": CONTROL_DIR / "manual_cash_capture.md",
    "operator_dashboard.md": CONTROL_DIR / "operator_dashboard.md",
    "100k_today_command_center.md": CONTROL_DIR / "100k_today_command_center.md",
    
    # Product assets
    "launch_page.html": PRODUCTS_DIR / "ai-agent-workflow-bundle" / "assets" / "public_launch_page.html",
    "landing_page.html": PRODUCTS_DIR / "ai-agent-workflow-bundle" / "assets" / "landing_page.html",
    
    # Docs
    "checkout_strategy.md": DOCS_DIR / "checkout_strategy.md",
}

def read_payment_link():
    """Read payment link from single source file."""
    if not PAYMENT_LINK_FILE.exists():
        return None
    
    content = PAYMENT_LINK_FILE.read_text(encoding='utf-8')
    
    # Extract link - handle various formats
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            # Format: PAYPAL_ME_LINK=https://...
            if 'PAYPAL_ME_LINK=' in line:
                link = line.split('=', 1)[1].strip()
                if link:
                    return link
            # Format: PAYMENT_LINK=...
            elif 'PAYMENT_LINK=' in line:
                link = line.split('=', 1)[1].strip()
                if link:
                    return link
            # Format: paypal.me/... (direct URL)
            elif 'paypal.me' in line.lower() or 'ko-fi' in line.lower() or 'gumroad' in line.lower() or 'stripe' in line.lower():
                return line
    
    return None

def validate_payment_link(link):
    """Validate payment link format."""
    if not link:
        return False, "No link provided"
    
    # Check for valid URL patterns
    valid_patterns = [
        r'paypal\.me/',
        r'ko-fi\.com',
        r'gumroad\.com',
        r'buy\.stripe\.com',
        r'stripe\.com',
        r'gum\.co',
    ]
    
    for pattern in valid_patterns:
        if re.search(pattern, link, re.IGNORECASE):
            return True, "Valid"
    
    return False, "Invalid format - must be PayPal/Ko-fi/Gumroad/Stripe"

def inject_link_into_file(file_path, link):
    """Inject payment link into a file, replacing PLACEHOLDER or creating CTA."""
    if not file_path.exists():
        return False, "File not found"
    
    content = file_path.read_text(encoding='utf-8')
    
    # Replace common placeholders
    replacements = [
        (r'\[PAYLINK\]', link),
        (r'\[PAYMENT_LINK\]', link),
        (r'\[CHECKOUT_LINK\]', link),
        (r'\[BUY_LINK\]', link),
        (r'\[PURCHASE_LINK\]', link),
        (r'PLACEHOLDER_LINK', link),
        (r'YOUR_PAYMENT_LINK', link),
        (r'your-payment-link', link),
        (r'PAYTMENT_LINK_PLACEHOLDER', link),
        (r'paypal\.me/YourName', link.replace('https://', '')),
    ]
    
    modified = False
    for pattern, replacement in replacements:
        new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        if new_content != content:
            content = new_content
            modified = True
    
    # If no placeholders found, try to append a note or update existing CTA
    if not modified:
        # Add CTA section if not present
        if '[INSERT PAYMENT LINK]' in content or '[LINK]' in content:
            content = content.replace('[INSERT PAYMENT LINK]', link)
            content = content.replace('[LINK]', link)
            modified = True
    
    if modified:
        file_path.write_text(content, encoding='utf-8')
        return True, "Updated"
    
    return False, "No placeholder found"

def update_master_state(link, status):
    """Update master_state.json with activation status."""
    if not MASTER_STATE_FILE.exists():
        return False
    
    with open(MASTER_STATE_FILE, 'r', encoding='utf-8') as f:
        state = json.load(f)
    
    # Update activation fields
    state['payment_link_present'] = (link is not None)
    state['payment_link'] = link
    state['automated_checkout_mode'] = (link is not None and status == 'valid')
    state['manual_close_mode'] = (link is None)
    state['payment_link_propagated'] = status == 'valid'
    state['product_1_activated'] = status == 'valid'
    state['product_2_activation_ready'] = status == 'valid'
    state['launch_surface_live_cta_injected'] = status == 'valid'
    state['distribution_live_cta_injected'] = status == 'valid'
    state['dm_close_live_cta_injected'] = status == 'valid'
    state['warm_network_live_cta_injected'] = status == 'valid'
    state['activation_engine_built'] = True
    state['activation_date'] = datetime.now().isoformat()
    state['engine_version'] = '2.1'  # Activated version
    
    with open(MASTER_STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)
    
    return True

def create_activation_report(link, status, targets_updated):
    """Create activation report."""
    report = f"""# ACTIVATION REPORT

## Status: {"ACTIVATED" if status == "valid" else "PENDING"}

**Generated:** {datetime.now().isoformat()}

---

## Payment Link

**Link:** {link if link else "NOT PROVIDED"}

**Validation:** {status}

---

## Propagation Results

| Target | Status |
|--------|--------|
"""
    
    for target, path in targets_updated.items():
        report += f"| {target} | {path.get('status', 'N/A')} |\n"
    
    report += f"""
---

## System Mode

- **Automated Checkout Mode:** {link is not None and status == 'valid'}
- **Manual Close Mode:** {link is None}

---

## Next Steps

{"Execute: python scripts/run_revenue_engine.py" if link else "Add payment link to control/payment_link.txt and re-run"}

---
"""
    
    ACTIVATION_REPORT_FILE.write_text(report, encoding='utf-8')
    return True

def main():
    """Main activation process."""
    print("=" * 60)
    print("PAYMENT LINK ACTIVATION ENGINE v2.1")
    print("=" * 60)
    
    # Step 1: Read payment link
    print("\n[1/4] Reading payment link...")
    link = read_payment_link()
    if not link:
        print("  [!] No payment link found in control/payment_link.txt")
        print("  -> System remains in MANUAL_CLOSE_MODE")
        
        update_master_state(None, 'no_link')
        create_activation_report(None, 'no_link', {})
        
        print("\n" + "=" * 60)
        print("ACTIVATION ENGINE READY - AWAITING PAYMENT LINK")
        print("=" * 60)
        return
    
    # Step 2: Validate payment link
    print("\n[2/4] Validating payment link...")
    is_valid, message = validate_payment_link(link)
    print(f"  [+] Link: {link}")
    print(f"  -> Validation: {message}")
    
    if not is_valid:
        print(f"  [!] Invalid link format")
        update_master_state(link, 'invalid')
        create_activation_report(link, 'invalid', {})
        return
    
    # Step 3: Propagate to all targets
    print("\n[3/4] Propagating payment link to assets...")
    targets_updated = {}
    
    for target_name, target_path in PROPAGATION_TARGETS.items():
        if target_path.exists():
            success, result = inject_link_into_file(target_path, link)
            targets_updated[target_name] = {'status': result, 'path': str(target_path)}
            print(f"  {'[+]' if success else '[-]'} {target_name}: {result}")
        else:
            targets_updated[target_name] = {'status': 'file_not_found', 'path': str(target_path)}
            print(f"  [!] {target_name}: file not found")
    
    # Step 4: Update state and create report
    print("\n[4/4] Updating system state...")
    update_master_state(link, 'valid')
    create_activation_report(link, 'valid', targets_updated)
    print("  [+] master_state.json updated")
    print("  [+] activation_report.md created")
    
    print("\n" + "=" * 60)
    print("ACTIVATION COMPLETE - REVENUE ENGINE ARMED")
    print("=" * 60)
    print(f"\nMode: AUTOMATED_CHECKOUT_MODE")
    print(f"Payment Link: {link}")
    print(f"\nNext: Execute distribution and capture revenue")

if __name__ == "__main__":
    main()