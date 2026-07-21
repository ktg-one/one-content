import unittest
import os
import shutil
import tempfile
from pathlib import Path

class TestContentRefactoringEngineSkill(unittest.TestCase):
    def test_personas_exist_and_enforce_verbatim_voice(self):
        """Test that all 4 channel persona files exist and explicitly mandate verbatim author voice preservation."""
        personas = ["reddit_persona.md", "linkedin_persona.md", "x_persona.md", "meta_persona.md"]
        for p in personas:
            p_path = Path(".agents/personas") / p
            self.assertTrue(p_path.exists(), f"Persona {p} must exist in .agents/personas/")
            content = p_path.read_text(encoding="utf-8")
            self.assertIn("PRESERVE AUTHOR VOICE VERBATIM", content, f"Persona {p} must preserve author voice verbatim")

    def test_skill_manifest_exists(self):
        """Test that content-refactoring-engine SKILL.md exists and is valid."""
        skill_path = Path(".agents/skills/content-refactoring-engine/SKILL.md")
        self.assertTrue(skill_path.exists(), "content-refactoring-engine SKILL.md must exist")
        content = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: \"content-refactoring-engine\"", content)

    def test_mcp_config_validity(self):
        """Test that project-specific mcp_config.json exists and registers composio and n8n-api with bunx."""
        mcp_path = Path(".agents/mcp_config.json")
        self.assertTrue(mcp_path.exists(), "Project .agents/mcp_config.json must exist")
        content = mcp_path.read_text(encoding="utf-8")
        self.assertIn("composio", content)
        self.assertIn("n8n-api", content)
        self.assertIn("bunx", content)

if __name__ == "__main__":
    unittest.main()
