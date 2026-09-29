"""Guards for local-only onboarding and profile bootstrap."""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
SETUP_GUIDE = REPO / "SETUP.md"
SETUP_COMMAND = REPO / ".framework" / "commands" / "setup.md"


def section(text: str, heading: str) -> str:
    """Body of a markdown section up to the next heading of the same level."""
    level = heading.split(" ")[0]
    pattern = re.compile(
        rf"^{re.escape(heading)}\n(.*?)(?=^{level} |\Z)", re.MULTILINE | re.DOTALL
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


class TestLocalOnlyProfileAtTheDecisionPoint(unittest.TestCase):
    def test_readme_quick_start_documents_local_only_profile(self):
        body = section(README.read_text(encoding="utf-8"), "### 1. Clone")
        self.assertIn("gh repo clone", body, "sanity: the clone command lives in this section")
        self.assertRegex(body, re.compile(r"public", re.IGNORECASE))
        self.assertIn("personal profile data", body)
        self.assertIn("gitignored local files", body)

    def test_setup_guide_documents_bootstrap_next_to_fork_command(self):
        body = section(SETUP_GUIDE.read_text(encoding="utf-8"), "## 2. Fork and clone")
        self.assertIn("gh repo fork", body, "sanity: the fork command lives in this section")
        self.assertIn("tools/bootstrap_private_profile.py", body)
        self.assertIn("gitignore", body.lower())


class TestSetupChecksIgnoreProtectionBeforeWriting(unittest.TestCase):
    def test_preflight_exists_and_precedes_profile_generation(self):
        text = SETUP_COMMAND.read_text(encoding="utf-8")
        self.assertIn("tools/bootstrap_private_profile.py", text)
        self.assertIn("git check-ignore", text)
        preflight_at = text.index("tools/bootstrap_private_profile.py")
        writes_at = text.index("## Step 3: Generate Profile Files")
        self.assertLess(
            preflight_at,
            writes_at,
            "the privacy bootstrap and ignore check must run before profile generation",
        )


if __name__ == "__main__":
    unittest.main()
