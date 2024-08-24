# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "aquamarine"
pkgver = "0.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE:STRING=Release",
    "-DCMAKE_INSTALL_PREFIX:PATH=/usr",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "mesa-devel",
    "glew-devel",
    "hyprutils",
    "hyprwayland-scanner",
    "libseat-devel",
    "libinput-devel",
    "wayland-devel",
    "wayland-protocols",
    "pixman-devel",
    "libdisplay-info-devel",
    "hwdata-devel",
]
depends = []
ignore_shlibs = []
pkgdesc = "Aquamarine is a very light linux rendering backend library"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/aquamarine/archive/v{pkgver}.tar.gz"
sha256 = "8785d2d0d23ece3dda39c6a51d36b321611578a8339fcfe9f110e17b309d8047"
broken_symlinks = []
# Cant get this to work!
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
