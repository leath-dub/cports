# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "hyprland"
pkgver = "0.42.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE:STRING=Release",
    "-DCMAKE_INSTALL_PREFIX:PATH=/usr",
    "-DNO_SYSTEMD:STRING=true",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "git",
]
makedepends = [
    "mesa-devel",
    "hyprutils",
    "hyprlang",
    "hyprwayland-scanner",
    "hyprcursor",
    "aquamarine",
    "libinput-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
    "cairo-devel",
    "pango-devel",
    "pixman-devel",
    "libxcursor-devel",
    "hwdata-devel",
    "libseat-devel",
    "libdisplay-info-devel",
    "libliftoff-devel",
    "xwayland-devel",
    "libxcb-devel",
    "xcb-util-devel",
    "xcb-util-errors-devel",
    "xcb-util-wm-devel",
]
depends = []
ignore_shlibs = []
pkgdesc = "Hyprland tiling Wayland compositor"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/Hyprland/releases/download/v0.42.0/source-v{pkgver}.tar.gz"
sha256 = "278c137ad28f5e4ef9d65032b18cb230799c982d008654a90b5060dd32eaa54a"
broken_symlinks = []

def post_install(self):
    self.install_license("LICENSE")
