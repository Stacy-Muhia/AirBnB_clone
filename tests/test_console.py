import unittest
import subprocess
import os
import console


class TestConsole(unittest.TestCase):

    def test_console_func(self):
        self.console_process = subprocess.Popen(
            ["./console.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def tearDown_func(self):
        self.console_process.stdin.write("EOF\n")
        self.console_process.stdin.flush()
        self.console_process.terminate()
        self.console_process.wait()

    def run_command_func(self, command):
        self.console_process.stdin.write(command + "\n")
        self.console_process.stdin.flush()
        output = self.console_process.stdout.readline().strip()
        return output

    def test_create_and_show_func(self):
        """Tests create and show."""
        create_output = self.run_command("create BaseModel")
        self.assertTrue(create_output)
        show_output = self.run_command("show BaseModel " + create_output)
        self.assertIn(create_output, show_output)

    def test_create_and_destroy_func(self):
        """Tests create and destroy."""
        create_output = self.run_command("create BaseModel")
        destroy_output = self.run_command("destroy BaseModel " + create_output)
        self.assertEqual(destroy_output, "")

    def test_create_and_all_func(self):
        """Tests create and all."""
        create_output = self.run_command("create BaseModel")
        all_output = self.run_command("all")
        self.assertIn(create_output, all_output)

    def test_create_and_update_func(self):
        """Tests create and update."""
        create_output = self.run_command("create BaseModel")
        update_output = self.run_command(f"update \
                BaseModel {create_output} name 'NewName'")
        self.assertEqual(update_output, "")
        show_output = self.run_command(f"show BaseModel {create_output}")
        self.assertIn("'name': 'NewName'", show_output)


if __name__ == "__main__":
    unittest.main()
