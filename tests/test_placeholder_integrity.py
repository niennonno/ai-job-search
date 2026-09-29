"""Guards for the personalised Aditya/Codex edition.

This repository is no longer published as a pristine, person-neutral template.
These checks keep its public identity and the CI branding guard aligned.
"""

import os
import unittest
from pathlib import Path


PROJECT_REPOSITORY = "niennonno/ai-job-search"
REPO = Path(__file__).resolve().parent.parent
CI = REPO / ".github" / "workflows" / "ci.yml"
README = REPO / "README.md"
PROFILE = REPO / ".framework" / "skills" / "job-application-assistant" / "01-candidate-profile.md"


@unittest.skipIf(
    os.environ.get("GITHUB_REPOSITORY", PROJECT_REPOSITORY) != PROJECT_REPOSITORY,
    "brand-integrity applies to the maintained project repository",
)
class TestPersonalisedEditionIntegrity(unittest.TestCase):
    def test_ci_checks_the_maintainer_identity(self):
        ci = CI.read_text(encoding="utf-8")
        self.assertIn("Created and maintained by", ci)
        self.assertIn("Aditya Vikram Godawat", ci)

    def test_readme_presents_aditya_as_creator_and_maintainer(self):
        readme = README.read_text(encoding="utf-8")
        self.assertIn("Created and maintained by **Aditya Vikram Godawat**", readme)

    def test_private_profile_exists_after_bootstrap(self):
        self.assertTrue(PROFILE.is_file())

if __name__ == "__main__":
    unittest.main()
