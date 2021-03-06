import os, pathlib, warnings, setuptools, subprocess

os.environ["CHOOSENIM_NO_ANALYTICS"] = "1"
if subprocess.run(f"sh { pathlib.Path(__file__).parent / 'init.sh' } -y", shell=True, check=True, timeout=999).returncode == 0:
  if Path(pathlib.Path.home() / ".nimble/bin").exists() and subprocess.run(str(pathlib.Path.home() / '.nimble/bin/nimble -y --noColor refresh'), shell=True, check=True, timeout=999).returncode == 0:
    new_path = f"export PATH={ pathlib.Path.home() / '.nimble/bin' }:$PATH"
    try:
      found = False
      with open(pathlib.Path.home() / ".bashrc", "a") as f:
        for line in f:
          if new_path == line:
            found = True
        if not found:
          f.write(new_path)
    except:
      warnings.warn("Failed to write file ~/.bashrc")
    try:
      found = False
      with open(pathlib.Path.home() / ".profile", "a") as f:
        for line in f:
          if new_path == line:
            found = True
        if not found:
          f.write(new_path)
    except:
      warnings.warn("Failed to write file ~/.profile")
    try:
      found = False
      with open(pathlib.Path.home() / ".bash_profile", "a") as f:
        for line in f:
          if new_path == line:
            found = True
        if not found:
          f.write(new_path)
    except:
      warnings.warn("Failed to write file ~/.bash_profile")
    try:
      found = False
      with open(pathlib.Path.home() / ".zshrc", "a") as f:
        for line in f:
          if new_path == line:
            found = True
        if not found:
          f.write(new_path)
    except:
      warnings.warn("Failed to write file ~/.zshrc")

setuptools.setup()
