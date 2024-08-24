pkgname = "hyprwayland-scanner"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_PREFIX=/usr",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "pugixml-devel"
]
depends = []
ignore_shlibs = []
pkgdesc = "Hyprland implementation of wayland-scanner, in and for C++"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/hyprwayland-scanner/archive/v{pkgver}.tar.gz"
sha256 = "4091122777ade12b8edc8de6f2df4917ced73b81cd40d946a995de73880ec71f"
broken_symlinks = []

def post_install(self):
    self.install_license("LICENSE")
