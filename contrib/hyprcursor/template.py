# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "hyprcursor"
pkgver = "0.1.9"
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
    "hyprlang",
    "libzip-devel",
    "cairo-devel",
    "librsvg-devel",
    "tomlplusplus-static",
]
depends = []
ignore_shlibs = []
pkgdesc = "Hypr config language"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "LGPL-3.0-only"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/hyprcursor/archive/v{pkgver}.tar.gz"
sha256 = "313cd91436af343918e6dec4a666d4bf3666149ac3cac6f36c683b70304eada4"
broken_symlinks = []

# Haven't figured out how to get the tests working
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
