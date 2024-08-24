# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "hyprlang"
pkgver = "0.5.2"
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
makedepends = []
depends = []
ignore_shlibs = []
pkgdesc = "Hypr config language"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "LGPL-3.0-only"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/hyprlang/archive/v{pkgver}.tar.gz"
sha256 = "66a1f87634c8ecdeb67d7ccc499a3fc1c19b064a098b103be042751e7430b5cc"
broken_symlinks = []

def post_install(self):
    self.install_license("LICENSE")
