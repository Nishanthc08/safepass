import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from ..core.vault import Vault

class LoginWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="SafePass Login")
        self.vault = Vault()
        self.set_default_size(300, 150)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.password_entry = Gtk.Entry(visibility=False)
        unlock_btn = Gtk.Button(label="Unlock")
        unlock_btn.connect("clicked", self.on_unlock)

        box.pack_start(self.password_entry, True, True, 0)
        box.pack_start(unlock_btn, True, True, 0)
        self.add(box)

    def on_unlock(self, button):
        password = self.password_entry.get_text()
        self.vault.unlock_vault(password)
        if not self.vault.is_locked:
            self.hide()
            MainWindow(self.vault).show_all()


class MainWindow(Gtk, Window):
    def __init__(self, vault):
        super().__init__(title="SafePass")
        self.vault = vault
        # Add password list, buttons, etc.

if __name__ == "__main__":
    win = LoginWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

