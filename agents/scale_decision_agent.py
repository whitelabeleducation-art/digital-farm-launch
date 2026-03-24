#!/usr/bin/env python3
"""
ScaleDecisionAgent - Makes decisions about scaling or killing products.
"""

import os
import json

class ScaleDecisionAgent:
    def __init__(self):
        self.control_dir = "control"
        self.docs_dir = "docs"
        
    def run(self, product_metrics):
        """Run scale decision analysis."""
        print("=" * 60)
        print("SCALE DECISION AGENT")
        print("=" * 60)
        
        decision = self.make_decision(product_metrics)
        self.record_decision(decision)
        return decision
    
    def make_decision(self, metrics):
        """Make scale/kill decision based on metrics."""
        print("\n[1] Analyzing product metrics...")
        
        revenue = metrics.get("revenue", 0)
        conversions = metrics.get("conversions", 0)
        conversion_rate = metrics.get("conversion_rate", 0)
        
        print(f"   Revenue: ${revenue}")
        print(f"   Conversions: {conversions}")
        print(f"   Conversion Rate: {conversion_rate}%")
        
        print("\n[2] Applying decision rules...")
        
        if revenue > 0 and conversions > 0:
            decision = "SCALE"
            reasoning = "Positive revenue and conversions - scale up distribution"
        elif conversions > 0 and revenue == 0:
            decision = "ITERATE_PRICING"
            reasoning = "Interest but no purchases - adjust pricing or offer"
        elif conversion_rate > 5 and conversions < 10:
            decision = "INCREASE_TRAFFIC"
            reasoning = "Good conversion rate but low volume - increase distribution"
        else:
            decision = "COLLECT_MORE_DATA"
            reasoning = "Insufficient data - continue collecting signals"
        
        print(f"   Decision: {decision}")
        print(f"   Reasoning: {reasoning}")
        
        return {
            "decision": decision,
            "reasoning": reasoning,
            "metrics": metrics
        }
    
    def record_decision(self, decision):
        """Record decision to log."""
        print("\n[3] Recording decision...")
        
        log_file = os.path.join(self.docs_dir, "scale_decisions.md")
        
        with open(log_file, "a") as f:
            f.write(f"\n## Decision: {decision['decision']}\n")
            f.write(f"**Reasoning**: {decision['reasoning']}\n")
            f.write(f"**Metrics**: {decision['metrics']}\n")
        
        print("   Decision recorded")

if __name__ == "__main__":
    import sys
    
    default_metrics = {
        "revenue": 0,
        "conversions": 0,
        "conversion_rate": 0.0,
        "views": 0
    }
    
    metrics = default_metrics
    if len(sys.argv) > 1:
        try:
            metrics = json.loads(sys.argv[1])
        except:
            pass
    
    agent = ScaleDecisionAgent()
    agent.run(metrics)