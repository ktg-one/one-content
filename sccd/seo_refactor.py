#!/usr/bin/env python3
"""
SEO Refactoring Plugin for Content Pipeline
Analyzes raw drops, refactors markdown for SEO best practices, identifies 2 optimal image placement points,
and outputs refactored drafts to outbox/master/.
Python stdlib only.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

def parse_frontmatter(content):
    """Extract YAML frontmatter and body."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        yaml_text, body = match.groups()
        meta = {}
        for line in yaml_text.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"\'')
        return meta, body
    return {}, content

def build_frontmatter(meta):
    """Format dictionary back into YAML frontmatter."""
    lines = ["---"]
    for k, v in meta.items():
        lines.append(f"{k}: {json.dumps(v) if isinstance(v, (list, dict)) else v}")
    lines.append("---")
    return "\n".join(lines)

def analyze_seo(title, body):
    """Perform SEO checks and compute readability score."""
    word_count = len(body.split())
    headings = re.findall(r'^(#{1,6})\s+(.+)$', body, re.MULTILINE)
    h1_count = sum(1 for h in headings if h[0] == '#')
    h2_count = sum(1 for h in headings if h[0] == '##')
    
    title_score = 100 if 40 <= len(title) <= 65 else 70
    heading_score = 100 if h1_count == 1 and h2_count >= 2 else 70
    length_score = 100 if word_count >= 600 else (70 if word_count >= 300 else 50)
    
    overall_score = int((title_score + heading_score + length_score) / 3)
    
    return {
        "word_count": word_count,
        "h1_count": h1_count,
        "h2_count": h2_count,
        "overall_seo_score": overall_score,
        "readability": "Good" if word_count > 400 else "Needs Expansion"
    }

def find_image_placement_points(body):
    """Locate 2 optimal insertion points for generated images."""
    paragraphs = [p for p in body.split('\n\n') if p.strip()]
    
    # Insertion Point 1: After the first major section / H2 or after paragraph 2
    idx1 = 2 if len(paragraphs) > 2 else 1
    # Insertion Point 2: Around the middle section of the article
    idx2 = max(idx1 + 2, len(paragraphs) // 2)
    if idx2 >= len(paragraphs):
        idx2 = len(paragraphs) - 1

    return min(idx1, len(paragraphs)-1), min(idx2, len(paragraphs)-1)

def refactor_content(file_path, output_dir="outbox/master"):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    raw_text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw_text)

    # Extract title
    title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    title = meta.get("title") or (title_match.group(1) if title_match else path.stem.replace("-", " ").title())
    
    # Clean H1 from body if title exists
    if title_match and meta.get("title"):
        body = re.sub(r'^#\s+.+\n+', '', body, count=1, flags=re.MULTILINE)

    seo_stats = analyze_seo(title, body)
    
    # Meta description generation if missing
    if "description" not in meta:
        clean_p = re.sub(r'#+\s*', '', body).strip()
        first_p = clean_p.split('\n\n')[0] if '\n\n' in clean_p else clean_p[:150]
        meta["description"] = first_p[:155].strip() + "..."
    
    meta["title"] = title
    meta["status"] = "seo-refactored"
    meta["seo_score"] = seo_stats["overall_seo_score"]

    idx1, idx2 = find_image_placement_points(body)
    
    # Image prompts & placeholders using Awesome NotebookLM Prompt Templates
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import image_prompt_templates
        prompt_1 = image_prompt_templates.build_awesome_prompt(title, style_key="silicon_refined", focus_description=f"Conceptual illustration for {title}")
        prompt_2 = image_prompt_templates.build_awesome_prompt(title, style_key="strategic_blue", focus_description=f"Technical architectural breakdown of {title}")
    except Exception as e:
        prompt_1 = f"Professional cinematic conceptual illustration representing {title}, high quality modern aesthetic"
        prompt_2 = f"Detailed schematic diagram and modern aesthetic overview of {title}"

    slug = path.stem.lower().replace(" ", "_")
    img1_rel = f"outbox/assets/image_1_{slug}.png"
    img2_rel = f"outbox/assets/image_2_{slug}.png"
    
    img1_tag = f"\n\n![Image 1: Visual representation of {title}]({img1_rel})\n*Caption: Key insight visual for {title}*\n"
    img2_tag = f"\n\n![Image 2: Deep dive illustration for {title}]({img2_rel})\n*Caption: Conceptual overview of core themes*\n"

    paragraphs = [p for p in body.split('\n\n') if p.strip()]
    if paragraphs:
        paragraphs.insert(idx1, img1_tag.strip())
        if idx2 < len(paragraphs):
            paragraphs.insert(idx2 + 1, img2_tag.strip())
        else:
            paragraphs.append(img2_tag.strip())
    
    refactored_body = "\n\n".join(paragraphs)
    final_output = build_frontmatter(meta) + "\n\n# " + title + "\n\n" + refactored_body

    os.makedirs(output_dir, exist_ok=True)
    out_path = Path(output_dir) / f"{path.stem}_refactored.md"
    out_path.write_text(final_output, encoding="utf-8")

    meta_json_path = Path(output_dir) / f"{path.stem}_meta.json"
    metadata_payload = {
        "title": title,
        "description": meta.get("description"),
        "seo_stats": seo_stats,
        "images": [
            {
                "id": "image_1",
                "path": img1_rel,
                "alt": f"Visual representation of {title}",
                "caption": f"Key insight visual for {title}",
                "prompt": prompt_1
            },
            {
                "id": "image_2",
                "path": img2_rel,
                "alt": f"Deep dive illustration for {title}",
                "caption": "Conceptual overview of core themes",
                "prompt": prompt_2
            }
        ]
    }
    meta_json_path.write_text(json.dumps(metadata_payload, indent=2), encoding="utf-8")

    print(f"[SUCCESS] SEO Refactored: {out_path}")
    print(f"[SUCCESS] Metadata Saved: {meta_json_path}")
    print(f"SEO Score: {seo_stats['overall_seo_score']}/100 | Word Count: {seo_stats['word_count']}")
    return str(out_path), str(meta_json_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO Refactoring Engine for Content Drops")
    parser.add_argument("file", help="Path to input markdown/text drop in inbox/")
    parser.add_argument("--output", default="outbox/master", help="Output directory")
    args = parser.parse_args()
    
    refactor_content(args.file, args.output)
