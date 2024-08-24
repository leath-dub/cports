# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "tomlplusplus-static"
pkgver = "3.4.0"
pkgrel = 0
build_style = "meson"
configure_args = []
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = []
depends = []
ignore_shlibs = []
pkgdesc = "Header-only TOML config file parser and serializer for C++17"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "MIT"
url = "https://marzer.github.io/tomlplusplus"
source = f"https://github.com/marzer/tomlplusplus/archive/v{pkgver}.tar.gz"
sha256 = "8517f65938a4faae9ccf8ebb36631a38c1cadfb5efa85d9a72e15b9e97d25155"
broken_symlinks = []

def post_install(self):
    self.install_license("LICENSE")
