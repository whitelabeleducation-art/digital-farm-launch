#!/usr/bin/env python3
"""
REVENUE STATUS CHECK
====================

Check current status of the revenue engine.

Usage: python scripts/revenue_status.py
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
CONTROL_DIR = BASE_DIR / "control"

def main():
    print("=" * 60)
    print("REVENUE ENGINE STATUS")
    print("=" * 60)
    
    # Check payment link
    payment_file = CONTROL_DIR / "payment_link.txt"
    if payment_file.exists():
        content = payment_file.read_text()
        if "PAYTMENT_LINK_PLACEHOLDER" in content:
            print("\n[!] PAYMENT LINK: Not provided")
            print("   -> Mode: MANUAL_CLOSE_MODE")
        else:
            print("\n[+] PAYMENT LINK: Provided")
            print("   -> Mode: AUTOMATED_CHECKOUT_MODE")
    else:
        print("\n[!] PAYMENT LINK FILE: Missing")
    
    # Check master state
    state_file = CONTROL_DIR / "master_state.json"
    if state_file.exists():
        with open(state_file) as f:
            state = json.load(f)
        
        print("\n--- SYSTEM STATUS ---")
        print(f"Engine Version: {state.get('engine_version', 'unknown')}")
        print(f"Payment Link Present: {state.get('payment_link_present', False)}")
        print(f"Automated Checkout Mode: {state.get('automated_checkout_mode', False)}")
        print(f"Manual Close Mode: {state.get('manual_close_mode', True)}")
        print(f"Activation Engine Built: {state.get('activation_engine_built', False)}")
        
        print("\n--- PRODUCT STATUS ---")
        p1 = state.get('first_product', {})
        print(f"Product #1: {p1.get('status', 'unknown')}")
        p2 = state.get('second_product', {})
        print(f"Product #2: {p2.get('status', 'unknown')}")
        
        print("\n--- ACTIVATION STATUS ---")
        print(f"Product #1 Activated: {state.get('product_1_activated', False)}")
        print(f"Product #2 Activation Ready: {state.get('product_2_activation_ready', False)}")
        print(f"Launch CTA Injected: {state.get('launch_surface_live_cta_injected', False)}")
        print(f"Distribution CTA Injected: {state.get('distribution_live_cta_injected', False)}")
        
        print("\n--- REVENUE TARGETS ---")
        targets = state.get('30_day_targets', {})
        print(f"30-day Revenue Target: £{targets.get('revenue', 0)}")
        print(f"High-Ticket Target: {targets.get('high_ticket_target', 'N/A')}")
        
    else:
        print("\n⚠ master_state.json: Not found")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()