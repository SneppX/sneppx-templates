from pathlib import Path

def test_three_templates_exist():
    root = Path(__file__).parent.parent / "templates"
    for name in ("train", "serve", "edge"):
        assert (root / name / "README.md").exists()
