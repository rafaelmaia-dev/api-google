import unittest
import subprocess
import os
import sys


class TestScriptExecution(unittest.TestCase):

    def test_script_creates_html_file(self):
        script_path = os.path.join("projeto", "src", "main.py")

        subprocess.run([sys.executable, script_path], check=True)

        self.assertTrue(
            os.path.exists("files/page.html"),
            "O arquivo files/page.html não foi criado",
        )


if __name__ == "__main__":
    unittest.main()
