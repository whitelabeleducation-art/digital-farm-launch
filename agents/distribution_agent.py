#!/usr/bin/env python3
"""
DistributionAgent - Handles product distribution and launch.
"""

import os

class DistributionAgent:
    def __init__(self):
        self.docs_dir = "docs"
        
    def run(self, product_slug):
        """Run distribution for a product."""
        print("=" * 60)
        print(f"DISTRIBUTION AGENT - Distributing: {product_slug}")
        print("=" * 60)
        
        channels = self.identify_channels()
        self.create_channel_assets(channels, product_slug)
        return channels
    
    def identify_channels(self):
        """Identify distribution channels."""
        print("\n[1] Identifying distribution channels...")
        
        channels = [
            {
                "name": "Reddit",
                "platforms": ["r/smallbusiness", "r/entrepreneur", "r/ChatGPT"],
                "type": "community",
                "priority": "HIGH"
            },
            {
                "name": "X/Twitter",
                "platforms": ["threads", "comments"],
                "type": "social",
                "priority": "HIGH"
            },
            {
                "name": "LinkedIn",
                "platforms": ["posts", "articles"],
                "type": "social",
                "priority": "MEDIUM"
            },
            {
                "name": "Product Hunt",
                "platforms": ["launch"],
                "type": "marketplace",
                "priority": "MEDIUM"
            }
        ]
        
        for ch in channels:
            print(f"   - {ch['name']}: {ch['priority']}")
        
        return channels
    
    def create_channel_assets(self, channels, product_slug):
        """Create assets for each channel."""
        print("\n[2] Creating channel-specific assets...")
        
        assets_dir = os.path.join("products", product_slug, "assets", "distribution")
        os.makedirs(assets_dir, exist_ok=True)
        
        for channel in channels:
            if channel["name"] == "Reddit":
                reddit_file = os.path.join(assets_dir, "reddit_posts.md")
                with open(reddit_file, "w") as f:
                    f.write("# Reddit Distribution Posts\n\n")
                    f.write("## r/smallbusiness\n\n")
                    f.write("**Title**: I automated 80% of my client follow-up process - here's how\n\n")
                    f.write("**Body**:\n")
                    f.write("As a solopreneur, I was drowning in admin work. Built this automation bundle to fix it.\n\n")
                    f.write("What's included:\n")
                    f.write("- 5 ready-to-use automation templates\n")
                    f.write("- Step-by-step setup guide\n")
                    f.write("- Video walkthroughs\n\n")
                    f.write("Link in comments if you want it.\n\n")
                    f.write("---\n\n")
                    f.write("## r/entrepreneur\n\n")
                    f.write("**Title**: Free resource: My complete automation workflow templates\n\n")
                    f.write("**Body**:\n")
                    f.write("After 2 years of building automations, I packaged everything into a copy-paste system.\n\n")
                    f.write("Includes:\n")
                    f.write("- Lead capture to follow-up sequence\n")
                    f.write("- Client onboarding automation\n")
                    f.write("- Appointment scheduling\n\n")
                    f.write("Drop a comment and I'll DM you the link.\n")
                
                print(f"   Created: {reddit_file}")
            
            elif channel["name"] == "X/Twitter":
                twitter_file = os.path.join(assets_dir, "twitter_posts.md")
                with open(twitter_file, "w") as f:
                    f.write("# X/Twitter Distribution Posts\n\n")
                    f.write("## Post 1: Problem Hook\n\n")
                    f.write("I used to spend 3 hours every day on manual follow-ups.\n")
                    f.write("Then I built an automation that does it for me.\n")
                    f.write("Now I reclaim 15+ hours/week.\n")
                    f.write("Copy the exact workflow here.\n\n")
                    f.write("#solopreneur #automation #productivity\n\n")
                    f.write("---\n\n")
                    f.write("## Post 2: Value + CTA\n\n")
                    f.write("Just realized I've saved 60+ hours this month using automation workflows.\n\n")
                    f.write("The key wasn't fancy tools - it was having the right templates to start with.\n\n")
                    f.write("Turns out, you don't need to be a developer to automate your business.\n\n")
                    f.write("You just need the right starting point.\n\n")
                    f.write("DM 'AUTOMATE' for details.\n\n")
                    f.write("#Solopreneur #Automation #BusinessGrowth\n")
                
                print(f"   Created: {twitter_file}")
            
            elif channel["name"] == "LinkedIn":
                linkedin_file = os.path.join(assets_dir, "linkedin_posts.md")
                with open(linkedin_file, "w") as f:
                    f.write("# LinkedIn Distribution Posts\n\n")
                    f.write("## Post 1: Story Format\n\n")
                    f.write("I used to work 80 hours weeks as a solopreneur.\n\n")
                    f.write("Then I built automation workflows.\n\n")
                    f.write("Now I work 30 hours and make more money.\n\n")
                    f.write("Here's the exact system that changed everything:\n\n")
                    f.write("1. Lead capture automation (never miss a lead again)\n")
                    f.write("2. Client onboarding workflow (save 5+ hours per client)\n")
                    f.write("3. Follow-up sequences (convert 30% more leads)\n\n")
                    f.write("I've packaged all these templates into a ready-to-use bundle.\n\n")
                    f.write("Comment 'AUTOMATE' and I'll send you the details.\n\n")
                    f.write("#Solopreneur #Automation #BusinessSystems #Entrepreneur\n")
                
                print(f"   Created: {linkedin_file}")
        
        print("\n   Distribution assets ready")
        print("   Ready for launch execution")

if __name__ == "__main__":
    import sys
    product = sys.argv[1] if len(sys.argv) > 1 else "ai-agent-workflow-bundle"
    agent = DistributionAgent()
    agent.run(product)