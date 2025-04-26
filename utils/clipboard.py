import time
import subprocess
from ..core.vault import Vault

def copy_to_clipboard(text, timeout=30):
    # Use /dev/shm for temporary storage (RAM)
    tmp_file = "/dev/shm/safepass_clipboard.txt"
    with open(tmp_file, "w") as f:
        f.write(text)
    subprocess.run(["xclip", "-selection", "clipboard", tmp_file])
    time.sleep(timeout)
    subprocess.run(["xclip", "-selection", "clipboard", "-rm"])
