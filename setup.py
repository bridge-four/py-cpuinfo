import os
from setuptools import setup
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

# 1. Define the Bash command you want to run
def run_custom_setup_script():
    print("running custom setup script...")
    try:
        # 'shell=True' allows you to write the command exactly as you would in bash
        subprocess.check_call("echo 'Hello from the fork!' && mkdir -p /tmp/my_custom_dir", shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Custom setup script failed: {e}")
        # Optionally exit if this step is critical
        sys.exit(1)

# 2. Override the standard 'install' command
class CustomInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        run_custom_setup_script()
        install.run(self)

# 3. Override the 'develop' command (for 'pip install -e' or 'python setup.py develop')
class CustomDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        run_custom_setup_script()
        develop.run(self)

with open(os.path.join(os.getcwd(), 'README.rst')) as f:
    readme_content = f.read()

setup(
    name = "py-cpuinfo",
    version = "9.0.1",
    author = "test",
    author_email = "test,
    description = "Get CPU info with pure Python",
    long_description=readme_content,
    python_requires='>=3',
    license = "MIT",
    url = "https://github.com/bridge-four/py-cpuinfo",
    packages=['cpuinfo'],
    test_suite="test_suite",
    entry_points = {
        'console_scripts': ['cpuinfo = cpuinfo:main'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
    },
)
