#!/usr/bin/env python3
"""
Main orchestration script for the Digital Product Cash Engine.
Runs the complete pipeline from opportunity to product to launch.
"""

import os
import sys

def run_workflow():
    print("=" * 70)
    print("DIGITAL PRODUCT CASH ENGINE - Orchestration Script")
    print("=" * 70)
    
    print("\n[1/5] Running OpportunityMinerAgent...")
    os.system("python agents/opportunity_miner.py")
    
    print("\n[2/5] Running ValidationAgent...")
    os.system('python agents/validation_agent.py "AI Agent Workflow Bundle for Solopreneurs"')
    
    print("\n[3/5] Running ProductBuilderAgent...")
    os.system("python agents/product_builder_agent.py")
    
    print("\n[4/5] Running DistributionAgent...")
    os.system("python agents/distribution_agent.py")
    
    print("\n[5/5] Running ReportAgent...")
    os.system("python agents/report_agent.py")
    
    print("\n" + "=" * 70)
    print("CASH ENGINE WORKFLOW COMPLETE")
    print("=" * 70)
    print("\nFirst product: AI Agent Workflow Bundle for Solopreneurs")
    print("Status: Built and launch-ready")
    print("Next: Execute distribution (requires checkout account setup)")

if __name__ == "__main__":
    run_workflow()