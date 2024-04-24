pkgname = "xfce4-settings"
pkgver = "4.18.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-pluggable-dialogs",
    "--enable-sound-settings",
    "--enable-upower-glib",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "colord-devel",
    "exo-devel",
    "fontconfig-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxi-devel",
    "libxklavier-devel",
    "libxrandr-devel",
    "upower-devel",
    "xfconf-devel",
    "xorgproto",
    "xserver-xorg-input-libinput-devel",
]
pkgdesc = "Xfce settings app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/xfce4-settings/start"
source = f"$(XFCE_SITE)/xfce/xfce4-settings/{pkgver[:-2]}/xfce4-settings-{pkgver}.tar.bz2"
sha256 = "f10c55d0360308d9944f415645d9596d4352f952a20fc7c4a66f30fe511ca1dc"


@subpackage("xfce4-settings-default-themes")
def _default_themes(self):
    self.pkgdesc = f"{pkgdesc} (default themes)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    # See patches/defaults.patch
    self.depends = ["adw-gtk3", "adwaita-icon-theme", "papirus-icon-theme"]
    self.options = ["empty"]

    return []
