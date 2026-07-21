import unittest
import os
import shutil
import tempfile
import json
from pathlib import Path

# Target module under test
import sys
sys.path.append(os.path.abspath("sccd"))
import seo_refactor

class TestSEOAnalyzerSkill(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.inbox_file = os.path.join(self.test_dir, "test_drop.md")
        self.outbox_dir = os.path.join(self.test_dir, "outbox_master")
        
        with open(self.inbox_file, "w", encoding="utf-8") as f:
            f.write("""---
title: "Test SEO Refactor"
---

# Test SEO Refactor

This is a test paragraph for SEO refactoring verification.

## Section 1: Breakdown

Content in section 1 detailing technical topics.

## Section 2: Deep Dive

Content in section 2 with deep dive insights.
""")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_seo_analysis_and_prompt_generation(self):
        """Test that refactor_content outputs valid markdown and metadata JSON with GitHub prompt templates."""
        out_md, out_json = seo_refactor.refactor_content(self.inbox_file, output_dir=self.outbox_dir)
        
        self.assertTrue(os.path.exists(out_md))
        self.assertTrue(os.path.exists(out_json))
        
        with open(out_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertIn("seo_stats", data)
        self.assertIn("overall_seo_score", data["seo_stats"])
        self.assertEqual(len(data["images"]), 2)
        # Check for GitHub notebooklm-prompt-styles tokens in prompts
        self.assertIn("Design Theme:", data["images"][0]["prompt"])
        self.assertIn("Style:", data["images"][0]["prompt"])

    def test_skill_manifest_exists(self):
        """Test that the project-specific seo-analyzer SKILL.md exists and is valid."""
        skill_path = Path(".agents/skills/seo-analyzer/SKILL.md")
        self.assertTrue(skill_path.exists(), "seo-analyzer SKILL.md must exist")
        content = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: \"seo-analyzer\"", content)

if __name__ == "__main__":
    unittest.main()
