# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "hyprutils"
pkgver = "0.2.1"
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
    "pixman-devel",
]
depends = []
ignore_shlibs = []
pkgdesc = "Hyprland utilities library used across the ecosystem"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/hyprutils/archive/v{pkgver}.tar.gz"
sha256 = "061449c828d0cdaf7b147d9e232282fd0dde997c6ec7c43d51fe96d878b66c12"
broken_symlinks = []

def post_install(self):
    self.install_license("LICENSE")
