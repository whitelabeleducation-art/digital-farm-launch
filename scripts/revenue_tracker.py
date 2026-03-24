#!/usr/bin/env python3
"""
REVENUE TRACKING ENGINE
=======================

Log and track all revenue events.

Usage: python scripts/revenue_tracker.py --log --amount 15000 --source warm_network --product "AI Revenue Engine Sprint"
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
import argparse

BASE_DIR = Path(__file__).parent.parent
CONTROL_DIR = BASE_DIR / "control"
DOCS_DIR = BASE_DIR / "docs"

REVENUE_LOG = CONTROL_DIR / "revenue_log.json"
SIGNALS_LOG = CONTROL_DIR / "signals_log.json"

def load_json(path, default):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def log_sale(amount, product, source, method='manual'):
    """Log a sale event."""
    log = load_json(REVENUE_LOG, {'sales': [], 'total_revenue': 0})
    
    sale = {
        'id': len(log['sales']) + 1,
        'timestamp': datetime.now().isoformat(),
        'amount': amount,
        'product': product,
        'source': source,
        'method': method,
        'status': 'completed'
    }
    
    log['sales'].append(sale)
    log['total_revenue'] += amount
    log['last_updated'] = datetime.now().isoformat()
    
    save_json(REVENUE_LOG, log)
    print(f"✓ Logged sale: £{amount} - {product}")
    return sale

def log_signal(signal_type, source, contact=None, score=1):
    """Log a validation signal."""
    log = load_json(SIGNALS_LOG, {'signals': [], 'total_signals': 0})
    
    signal = {
        'id': len(log['signals']) + 1,
        'timestamp': datetime.now().isoformat(),
        'type': signal_type,
        'source': source,
        'contact': contact,
        'score': score
    }
    
    log['signals'].append(signal)
    log['total_signals'] += 1
    log['last_updated'] = datetime.now().isoformat()
    
    save_json(SIGNALS_LOG, log)
    print(f"✓ Logged signal: {signal_type} from {source}")
    return signal

def show_status():
    """Show current revenue status."""
    revenue_log = load_json(REVENUE_LOG, {'sales': [], 'total_revenue': 0})
    signals_log = load_json(SIGNALS_LOG, {'signals': [], 'total_signals': 0})
    
    print("\n--- REVENUE STATUS ---")
    print(f"Total Revenue: £{revenue_log.get('total_revenue', 0)}")
    print(f"Total Sales: {len(revenue_log.get('sales', []))}")
    print(f"Total Signals: {signals_log.get('total_signals', 0)}")
    
    if revenue_log.get('sales'):
        print("\nRecent Sales:")
        for sale in revenue_log['sales'][-5:]:
            print(f"  £{sale['amount']} - {sale['product']} ({sale['source']})")

def main():
    parser = argparse.ArgumentParser(description='Revenue Tracking Engine')
    parser.add_argument('--log-sale', action='store_true', help='Log a sale')
    parser.add_argument('--amount', type=int, help='Sale amount')
    parser.add_argument('--product', type=str, help='Product name')
    parser.add_argument('--source', type=str, help='Source (warm_network, dm, post, etc)')
    parser.add_argument('--log-signal', action='store_true', help='Log a signal')
    parser.add_argument('--signal-type', type=str, help='Signal type')
    parser.add_argument('--contact', type=str, help='Contact name')
    parser.add_argument('--score', type=int, default=1, help='Signal score')
    parser.add_argument('--status', action='store_true', help='Show status')
    
    args = parser.parse_args()
    
    if args.log_sale:
        if not args.amount or not args.product or not args.source:
            print("Error: --amount, --product, and --source required")
            sys.exit(1)
        log_sale(args.amount, args.product, args.source)
    
    elif args.log_signal:
        if not args.signal_type or not args.source:
            print("Error: --signal-type and --source required")
            sys.exit(1)
        log_signal(args.signal_type, args.source, args.contact, args.score)
    
    elif args.status:
        show_status()
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()