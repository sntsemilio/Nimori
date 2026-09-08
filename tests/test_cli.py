"""Integration checks for the installable starter's public behavior."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


def run_cli(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-m", "nimori", *args], capture_output=True, text=True, cwd=cwd, timeout=15)


class PublicBehaviorTests(unittest.TestCase):
    def test_catalog_is_available_outside_repository_and_claims_no_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = run_cli("--json", "models", "list", cwd=Path(temporary))
            self.assertEqual(result.returncode, 0, result.stderr)
            entries = json.loads(result.stdout)["items"]
            self.assertTrue(entries)
            self.assertTrue(all(item["status"] == "candidate" and not item["validated_capabilities"] for item in entries))
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_init_preserves_existing_user_work(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "my-lab"
            first = run_cli("lab", "init", "serving/prefill-decode", "--path", str(target), "--json")
            self.assertEqual(first.returncode, 0, first.stderr)
            notes = target / "NOTES.md"
            notes.write_text("Mi predicción original", encoding="utf-8")
            second = run_cli("lab", "init", "serving/prefill-decode", "--path", str(target), "--json")
            self.assertEqual(second.returncode, 1)
            self.assertEqual(notes.read_text(encoding="utf-8"), "Mi predicción original")
            self.assertIn("error", json.loads(second.stderr))

    def test_incompatible_model_leaves_no_workspace(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "bad-lab"
            result = run_cli("lab", "init", "serving/prefill-decode", "--model", "mamba-130m", "--path", str(target))
            self.assertEqual(result.returncode, 1)
            self.assertFalse(target.exists())

    def test_scripted_harness_plan_does_not_require_a_model(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "harness"
            result = run_cli("lab", "init", "harness/tool-retry", "--path", str(target), "--json")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("model: null", (target / "lab.yaml").read_text(encoding="utf-8"))
            self.assertEqual(json.loads(result.stdout)["execution_status"], "planned")

    def test_unimplemented_run_command_cannot_succeed(self):
        result = run_cli("lab", "run")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)


if __name__ == "__main__":
    unittest.main()
