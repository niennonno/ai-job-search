"""Guards for the Codex entrypoint layer.

The detailed workflow specs live under .claude/, but Codex discovers the
short skill routers under .codex/skills/. These tests keep the two layers
from drifting when upstream adds commands or changes file naming rules.
"""

import re
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
CODEX_SKILLS = REPO / ".codex" / "skills"
WORKFLOW_COMMANDS = REPO / ".claude" / "commands"


class CodexEntrypointTests(unittest.TestCase):
    COMMAND_TO_SKILL = {
        "add-portal": "job-search-add-portal",
        "add-template": "job-search-add-template",
        "apply": "job-search-apply",
        "expand": "job-search-expand",
        "gmail-sync": "job-search-gmail-sync",
        "html-report": "job-search-html-report",
        "interview": "job-search-interview",
        "notion-sync": "job-search-notion-sync",
        "outcome": "job-search-outcome",
        "rank": "job-search-rank",
        "reset": "job-search-reset",
        "setup": "job-search-setup",
    }

    def test_each_workflow_command_has_a_codex_entrypoint(self):
        command_names = {path.stem for path in WORKFLOW_COMMANDS.glob("*.md")}
        skill_names = {path.parent.name for path in CODEX_SKILLS.glob("*/SKILL.md")}

        missing = {
            command: skill
            for command, skill in self.COMMAND_TO_SKILL.items()
            if command in command_names and skill not in skill_names
        }
        self.assertEqual(missing, {})

    def test_core_skill_workflows_have_codex_entrypoints(self):
        skill_names = {path.parent.name for path in CODEX_SKILLS.glob("*/SKILL.md")}
        self.assertIn("job-search-scrape", skill_names)
        self.assertIn("job-search-upskill", skill_names)
        self.assertIn("job-application-assistant", skill_names)

    def test_codex_skill_frontmatter_is_well_formed(self):
        for path in CODEX_SKILLS.glob("*/SKILL.md"):
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                match = re.match(r"---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(match)
                frontmatter = match.group(1)
                name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.M)
                description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
                self.assertIsNotNone(name)
                self.assertIsNotNone(description)
                self.assertEqual(name.group(1), path.parent.name)
                self.assertNotIn("PLACEHOLDER", text)
                self.assertNotIn("TODO", text)

    def test_active_codex_docs_use_role_aware_cv_filename(self):
        active_paths = [
            REPO / "CODEX.md",
            REPO / ".codex" / "context" / "job-application-brief.md",
            REPO / ".codex" / "skills" / "job-search-apply" / "SKILL.md",
            REPO / ".codex" / "skills" / "job-application-assistant" / "SKILL.md",
        ]
        for path in active_paths:
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                self.assertIn("cv/main_<company>_<role>.tex", text)
                self.assertNotIn("cv/main_<company>.tex", text)


if __name__ == "__main__":
    unittest.main()
