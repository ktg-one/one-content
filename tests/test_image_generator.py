import unittest
import os
import shutil
import tempfile
from pathlib import Path

# Target module under test
import sys
sys.path.append(os.path.abspath("sccd"))
import image_prompt_templates

class TestImageGeneratorSkill(unittest.TestCase):
    def test_build_awesome_prompt_templates(self):
        """Test that build_awesome_prompt produces structured GitHub notebooklm-prompt-styles prompts."""
        prompt_tech = image_prompt_templates.build_awesome_prompt("AI Systems", style_key="silicon_refined")
        self.assertIn("Design Theme: Silicon Refined Ultra-Minimalist", prompt_tech)
        self.assertIn("Matte Charcoal", prompt_tech)
        
        prompt_gold = image_prompt_templates.build_awesome_prompt("Luxury Content", style_key="prestige_gold")
        self.assertIn("Design Theme: Prestige Gold Dark Luxury", prompt_gold)
        self.assertIn("Old Gold", prompt_gold)

    def test_skill_manifest_exists(self):
        """Test that the project-specific image-generator SKILL.md exists and is valid."""
        skill_path = Path(".agents/skills/image-generator/SKILL.md")
        self.assertTrue(skill_path.exists(), "image-generator SKILL.md must exist")
        content = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: \"image-generator\"", content)

if __name__ == "__main__":
    unittest.main()
