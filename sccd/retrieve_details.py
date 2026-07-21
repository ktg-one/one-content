#!/usr/bin/env python3
"""
Full Automated Retrieval & Indexing Script for _content
Scans drafts/, inbox/, and outbox/, updates wiki/index.md, and refreshes wiki/hot.md context cache.
Python stdlib only.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(__file__).parent.parent
DRAFTS_DIR = VAULT_ROOT / "drafts"
INBOX_DIR = VAULT_ROOT / "inbox"
OUTBOX_DIR = VAULT_ROOT / "outbox"
WIKI_DIR = VAULT_ROOT / "wiki"

def scan_markdown_files():
    catalog = []
    
    for folder, label in [(DRAFTS_DIR, "draft"), (INBOX_DIR, "inbox_drop"), (OUTBOX_DIR / "master", "master_outbox")]:
        if not folder.exists():
            continue
        for f in folder.glob("*.md"):
            content = f.read_text(encoding="utf-8", errors="ignore")
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else f.stem.replace("-", " ").title()
            word_count = len(content.split())
            
            catalog.append({
                "filename": f.name,
                "path": str(f.relative_to(VAULT_ROOT)),
                "title": title,
                "status": label,
                "words": word_count,
                "modified": datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            })
            
    return catalog

def update_wiki_index(catalog):
    WIKI_DIR.mkdir(exist_ok=True)
    index_path = WIKI_DIR / "index.md"
    
    lines = [
        "# Master Content Index",
        f"*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "| File | Title | Category | Words | Last Modified |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for item in catalog:
        lines.append(f"| `{item['filename']}` | **{item['title']}** | `{item['status']}` | {item['words']} | {item['modified']} |")
        
    index_path.write_text("\n".join(lines), encoding="utf-8")
    
    hot_path = WIKI_DIR / "hot.md"
    recent = catalog[:10]
    hot_lines = [
        "# Hot Context Cache",
        f"*Cached: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "## Active Drafts & Recent Pipeline Files",
    ]
    for r in recent:
        hot_lines.append(f"- **{r['title']}** (`{r['filename']}`) — {r['words']} words [{r['status']}]")
        
    hot_path.write_text("\n".join(hot_lines), encoding="utf-8")
    print(f"[SUCCESS] Updated {index_path} and {hot_path} with {len(catalog)} cataloged items.")

if __name__ == "__main__":
    items = scan_markdown_files()
    update_wiki_index(items)
