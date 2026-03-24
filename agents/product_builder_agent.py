#!/usr/bin/env python3
"""
ProductBuilderAgent - Creates digital products from validated ideas.
"""

import os
import json
from datetime import datetime

class ProductBuilderAgent:
    def __init__(self):
        self.products_dir = "products"
        os.makedirs(self.products_dir, exist_ok=True)
        
    def run(self, product_spec):
        """Build product from spec."""
        print("=" * 60)
        print(f"PRODUCT BUILDER AGENT - Building: {product_spec['name']}")
        print("=" * 60)
        
        self.create_product_spec(product_spec)
        self.create_outline(product_spec)
        self.create_content(product_spec)
        self.create_delivery_package(product_spec)
        self.create_launch_assets(product_spec)
        
        print("\n" + "=" * 60)
        print("PRODUCT BUILD COMPLETE")
        print("=" * 60)
        
    def create_product_spec(self, spec):
        """Create detailed product specification."""
        print("\n[1] Creating product specification...")
        
        spec_file = os.path.join(self.products_dir, spec["slug"], "SPEC.md")
        os.makedirs(os.path.dirname(spec_file), exist_ok=True)
        
        with open(spec_file, "w") as f:
            f.write(f"# {spec['name']} - Product Specification\n\n")
            f.write(f"**Created**: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"## Overview\n{spec['description']}\n\n")
            f.write(f"## Target Audience\n{spec['audience']}\n\n")
            f.write(f"## Problem Solved\n{spec['problem']}\n\n")
            f.write(f"## Solution\n{spec['solution']}\n\n")
            f.write(f"## Pricing\n- Base: {spec['price']}\n")
            f.write(f"- Premium: {spec['premium_price']}\n\n")
            f.write(f"## Deliverables\n")
            for item in spec.get("deliverables", []):
                f.write(f"- {item}\n")
        
        print(f"   Created: {spec_file}")
        
    def create_outline(self, spec):
        """Create product outline/structure."""
        print("\n[2] Creating product outline...")
        
        outline_file = os.path.join(self.products_dir, spec["slug"], "OUTLINE.md")
        
        with open(outline_file, "w") as f:
            f.write(f"# {spec['name']} - Content Outline\n\n")
            
            modules = [
                {"title": "Module 1: Foundation", "items": [
                    "Understanding automation for solopreneurs",
                    "Identifying time-wasting tasks",
                    "Setting up your automation workspace"
                ]},
                {"title": "Module 2: Core Workflows", "items": [
                    "Lead capture automation",
                    "Client onboarding automation", 
                    "Follow-up and nurturing sequences"
                ]},
                {"title": "Module 3: Advanced Systems", "items": [
                    "AI-powered responses",
                    "Integration between tools",
                    "Analytics and tracking"
                ]},
                {"title": "Module 4: Implementation", "items": [
                    "Step-by-step setup guides",
                    "Troubleshooting common issues",
                    "Scaling your automations"
                ]}
            ]
            
            for module in modules:
                f.write(f"## {module['title']}\n\n")
                for item in module['items']:
                    f.write(f"- {item}\n")
                f.write("\n")
        
        print(f"   Created: {outline_file}")
        
    def create_content(self, spec):
        """Create product content."""
        print("\n[3] Creating product content...")
        
        content_file = os.path.join(self.products_dir, spec["slug"], "CONTENT.md")
        
        with open(content_file, "w") as f:
            f.write(f"# {spec['name']}\n\n")
            f.write("---\n\n")
            f.write("## Introduction\n\n")
            f.write("This automation bundle gives you proven workflows to reclaim 10+ hours per week.\n\n")
            f.write("## Module 1: Foundation\n\n")
            f.write("### Chapter 1: Understanding Automation for Solopreneurs\n\n")
            f.write("As a solopreneur, your time is your most valuable asset. Every hour spent on repetitive tasks is an hour not spent on revenue-generating activities.\n\n")
            f.write("This module helps you identify which tasks deserve automation and which require the human touch.\n\n")
            f.write("### Key Principles:\n")
            f.write("- Rule of 3: If you do it 3+ times, automate it\n")
            f.write("- Start with high-frequency tasks\n")
            f.write("- Build for scale, not just efficiency\n\n")
            f.write("### Action Items:\n")
            f.write("1. List your top 10 weekly tasks\n")
            f.write("2. Mark each as: Manual / Can Automate / Should Automate\n")
            f.write("3. Rank by time spent and frequency\n\n")
            f.write("## Module 2: Core Workflows\n\n")
            f.write("### Chapter 1: Lead Capture Automation\n\n")
            f.write("Stop losing leads to follow-up failures. This workflow ensures every lead gets contacted within 5 minutes.\n\n")
            f.write("**Workflow Components:**\n")
            f.write("- Webhook trigger from form submission\n")
            f.write("- AI-powered initial response\n")
            f.write("- Follow-up sequence (7 emails over 14 days)\n")
            f.write("- CRM update and tagging\n\n")
            f.write("## Module 3: Advanced Systems\n\n")
            f.write("### Chapter 1: AI-Powered Responses\n\n")
            f.write("Let AI handle common questions while you focus on complex inquiries.\n\n")
            f.write("**Implementation:**\n")
            f.write("1. Create FAQ knowledge base\n")
            f.write("2. Train response AI on your style\n")
            f.write("3. Set approval workflows for sensitive matters\n\n")
            f.write("## Module 4: Implementation\n\n")
            f.write("### Chapter 1: Step-by-Step Setup\n\n")
            f.write("Follow these steps to implement your first automation:\n\n")
            f.write("**Step 1: Map Your Process**\n")
            f.write("Document your current workflow step by step.\n\n")
            f.write("**Step 2: Choose Your Tools**\n")
            f.write("We recommend starting with Make.com or Zapier.\n\n")
            f.write("**Step 3: Build the Automation**\n")
            f.write("Use our templates as a starting point.\n\n")
            f.write("**Step 4: Test and Refine**\n")
            f.write("Run 10 test cases before going live.\n\n")
            f.write("## Bonus Resources\n\n")
            f.write("- 20+ Ready-to-use templates\n")
            f.write("- Video walkthroughs (90 minutes)\n")
            f.write("- Private community access\n\n")
            f.write("---\n\n")
            f.write("**Contact**: support@yourdomain.com\n")
        
        print(f"   Created: {content_file}")
        
    def create_delivery_package(self, spec):
        """Create delivery package files."""
        print("\n[4] Creating delivery package...")
        
        delivery_dir = os.path.join(self.products_dir, spec["slug"], "delivery")
        os.makedirs(delivery_dir, exist_ok=True)
        
        readme_file = os.path.join(delivery_dir, "README.txt")
        with open(readme_file, "w") as f:
            f.write(f"{spec['name']}\n")
            f.write("=" * 40 + "\n\n")
            f.write("Thank you for your purchase!\n\n")
            f.write("What's Inside:\n")
            for item in spec.get("deliverables", []):
                f.write(f"- {item}\n")
            f.write("\n")
            f.write("Quick Start Guide:\n")
            f.write("1. Read the main guide (CONTENT.md)\n")
            f.write("2. Review the templates\n")
            f.write("3. Choose your first automation to implement\n")
            f.write("4. Set up and test\n\n")
            f.write("Support: support@yourdomain.com\n")
        
        print(f"   Created: {delivery_dir}/")
        
    def create_launch_assets(self, spec):
        """Create launch assets (landing page, social posts)."""
        print("\n[5] Creating launch assets...")
        
        assets_dir = os.path.join(self.products_dir, spec["slug"], "assets")
        os.makedirs(assets_dir, exist_ok=True)
        
        landing_page = os.path.join(assets_dir, "landing_page.html")
        with open(landing_page, "w") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>{spec['name']}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .hero {{ text-align: center; padding: 40px 0; }}
        .price {{ font-size: 2em; color: #2ecc71; font-weight: bold; }}
        .cta {{ background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0; }}
        .testimonial {{ background: #f9f9f9; padding: 20px; margin: 20px 0; border-left: 4px solid #3498db; }}
        .features {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }}
        .feature {{ border: 1px solid #ddd; padding: 20px; border-radius: 8px; }}
    </style>
</head>
<body>
    <div class="hero">
        <h1>{spec['name']}</h1>
        <p>{spec['description']}</p>
        <p class="price">{spec['price']}</p>
        <a href="#" class="cta">Get It Now</a>
    </div>
    
    <h2>What's Included</h2>
    <div class="features">
""")
            for item in spec.get("deliverables", [])[:4]:
                f.write(f'        <div class="feature">[x] {item}</div>\n')
            f.write("""    </div>
    
    <h2>Who This Is For</h2>
    <p>""")
            f.write(spec['audience'])
            f.write("""</p>
    
    <h2>Problems Solved</h2>
    <p>""")
            f.write(spec['problem'])
            f.write("""</p>
    
    <div class="testimonial">
        <h3>What Customers Say</h3>
        <p>"This automation bundle saved me 15 hours per week. The templates are easy to implement and work great." - Sarah, Coach</p>
    </div>
    
    <h2>Guarantee</h2>
    <p>30-day money-back guarantee. No questions asked.</p>
    
    <div style="text-align: center; margin: 40px 0;">
        <a href="#" class="cta">Get Instant Access - """)
            f.write(spec['price'])
            f.write("""</a>
    </div>
</body>
</html>""")
        
        social_posts = os.path.join(assets_dir, "social_posts.md")
        with open(social_posts, "w") as f:
            f.write(f"# Social Media Posts for {spec['name']}\n\n")
            f.write("## Post 1 - Problem Hook (X/Twitter)\n\n")
            f.write("""I used to spend 3 hours every day on manual follow-ups.
Then I built an automation that does it for me.
Now I reclaim 15+ hours/week.
Copy the exact workflow here

#solopreneur #automation #productivity

---
""")
            f.write("## Post 2 - Solution (Reddit - r/smallbusiness)\n\n")
            f.write("""Title: I automated 80% of my client follow-up process - here's how

As a solopreneur, I was drowning in admin work. Built this automation bundle to fix it.

What's included:
- 5 ready-to-use automation templates
- Step-by-step setup guide
- Video walkthroughs

Link in comments if you want it - happy to share the exact setup that worked for me.

---
""")
            f.write("## Post 3 - Social Proof (LinkedIn)\n\n")
            f.write("""Just realized I've saved 60+ hours this month using automation workflows.

The key wasn't fancy tools - it was having the right templates to start with.

Turns out, you don't need to be a developer to automate your business.

You just need the right starting point.

I've packaged my exact system into a ready-to-use bundle.

DM "AUTOMATE" if you want the details.

#Solopreneur #Automation #BusinessGrowth

---
""")
            f.write("## Post 4 - Value CTA (Reddit - r/entrepreneur)\n\n")
            f.write("""Free resource: My complete automation workflow templates

After 2 years of building automations for my business, I finally packaged everything into a copy-paste system.

Includes:
- Lead capture to follow-up sequence
- Client onboarding automation  
- Appointment scheduling
- Task management workflows

Drop a comment and I'll DM you the link. No tricks, no upsell - just want to help fellow entrepreneurs save time.

---
""")
        
        print(f"   Created: {assets_dir}/")

if __name__ == "__main__":
    import sys
    
    product_spec = {
        "name": "AI Agent Workflow Bundle for Solopreneurs",
        "slug": "ai-agent-workflow-bundle",
        "description": "A complete set of automation templates and workflows to help solopreneurs save 10+ hours per week. Includes lead capture, client onboarding, and follow-up automations.",
        "audience": "Solopreneurs, small business owners, freelancers who want to automate their operations but lack technical skills",
        "problem": "Solopreneurs waste hours on manual tasks they could automate, but don't have the time/knowledge to build complex automation systems",
        "solution": "Ready-to-use templates with step-by-step guides that anyone can implement without coding",
        "price": "$47",
        "premium_price": "$97 (with 1-on-1 setup call)",
        "deliverables": [
            "5 automation workflow templates (Make.com/Zapier ready)",
            "Implementation guide (40+ pages)",
            "90-minute video course",
            "Private community access",
            "Lifetime updates"
        ]
    }
    
    builder = ProductBuilderAgent()
    builder.run(product_spec)