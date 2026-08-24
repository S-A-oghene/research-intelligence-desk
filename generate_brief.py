#!/usr/bin/env python3
"""
Research Intelligence Desk – Generate Executive Brief
"""
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'research_data.json')
BRIEF_FILE = os.path.join(BASE_DIR, 'examples', 'decision_brief.md')

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {DATA_FILE} not found.")
        return None
    except json.JSONDecodeError:
        print(f"❌ Error: {DATA_FILE} contains invalid JSON.")
        return None

def generate_brief(data):
    if not data:
        return "Error: No data available."

    lines = []
    lines.append("# EXECUTIVE RESEARCH BRIEF")
    lines.append(f"**Generated:** {datetime.now().strftime('%B %d, %Y')}\n")
    lines.append(f"## 🎯 Decision Question\n{data['question']}\n")

    # Score options: pros - cons
    scores = {}
    for opt in data['options']:
        scores[opt['name']] = len(opt['pros']) - len(opt['cons'])
    
    # Handle edge case: if no options, we can't recommend
    if not scores:
        lines.append("## ⚠️ No options provided to evaluate.")
        return '\n'.join(lines)
    
    best_option = max(scores, key=lambda k: scores[k])   # Fixed: explicit lambda

    lines.append("## 📊 Executive Bottom Line")
    lines.append(f"Based on the evidence, the recommended approach is **{best_option}**.\n")

    lines.append("## 🔍 Key Findings")
    for finding in data['discovery']['key_findings']:
        lines.append(f"- {finding}")
    lines.append("")

    lines.append("## 📚 Sources")
    for src in data['discovery']['sources']:
        lines.append(f"- **{src['title']}** ({src['type']}, {src['date']})")
        lines.append(f"  - {src.get('note', '')}")
    lines.append("")

    lines.append("## 📋 Options Analysis")
    for opt in data['options']:
        lines.append(f"### {opt['name']}")
        lines.append(f"**Pros:** {', '.join(opt['pros'])}")
        lines.append(f"**Cons:** {', '.join(opt['cons'])}\n")

    lines.append("## ⚖️ Trade‑offs Summary")
    for opt in data['options']:
        score = len(opt['pros']) - len(opt['cons'])
        lines.append(f"- **{opt['name']}**: {len(opt['pros'])} pros vs {len(opt['cons'])} cons (Score: {score})")
    lines.append("")

    lines.append(f"## 🏆 Recommendation\nWe recommend **{best_option}** because it offers the best balance of features and adoption potential.\n")

    lines.append("## ⚠️ Risks")
    lines.append("- Adoption may be slower than expected if the tool is unfamiliar.")
    lines.append("- Integration complexity may require IT resources.")
    lines.append("- Cost may increase with premium features.\n")

    lines.append("## ❓ Unknowns")
    for u in data['unknowns']:
        lines.append(f"- {u}")
    lines.append("")

    lines.append("## 🔄 What Would Change the Recommendation?")
    lines.append("- If the executive team has specific needs not covered.")
    lines.append("- If a competitor offers a superior solution.")
    lines.append("- If budget constraints limit tool selection.\n")

    lines.append("## 📋 Next Actions")
    lines.append("1. Conduct a 2‑week pilot with the recommended tool.")
    lines.append("2. Gather feedback from 3‑5 executive users.")
    lines.append("3. Evaluate integration requirements with IT.")
    lines.append("4. Present recommendation to leadership for approval.")

    return '\n'.join(lines)

def main():
    print("\n" + "="*50)
    print("   📊 RESEARCH INTELLIGENCE DESK")
    print("="*50)
    data = load_data()
    if data is None:
        return
    brief = generate_brief(data)
    os.makedirs(os.path.dirname(BRIEF_FILE), exist_ok=True)
    with open(BRIEF_FILE, 'w', encoding='utf-8') as f:
        f.write(brief)
    print(f"✅ Executive brief saved to {BRIEF_FILE}")

if __name__ == "__main__":
    main()