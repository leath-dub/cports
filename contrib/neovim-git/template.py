# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "neovim-git"
pkgver = "0.11.0"
_commit = "7588ff2d8986e343d440dc8e025b1b5d4d8974b5"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "gperf",
    "lua5.1-bitop",
    "lua5.1-libluv",
    "lua5.1-lpeg",
    "lua5.1-mpack",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libuv-devel",
    "libvterm-devel",
    "lua5.1-libluv-devel",
    "msgpack-c-devel",
    "tree-sitter-devel",
    "unibilium-devel",
    "utf8proc-devel",
]
depends = [
    "lua5.1-lpeg",
    "tree-sitter-bash",
    "tree-sitter-c",
    "tree-sitter-lua",
    "tree-sitter-markdown",
    "tree-sitter-python",
    "tree-sitter-query",
    "tree-sitter-vimdoc",
]
ignore_shlibs = ["/usr/lib/lua/5.1/lpeg.so"]
pkgdesc = "Fork of Vim aiming to improve user experience, plugins and GUIs"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0 AND custom:Vim"
url = "https://neovim.io"
source = f"https://github.com/neovim/neovim/archive/{_commit}.tar.gz"
sha256 = "807d6d8846b5f7fcd22c4232ae4898f6bff139bc8496b7bc41927ae2d904d5d5"
broken_symlinks = ["usr/share/nvim/runtime/parser"]
# hardening: visibility is needed for "nvim --api-info"
# testing unchecked yet (via "make test", see test/README.md)
options = ["!check"]


match self.profile().arch:
    case "aarch64" | "ppc64le" | "x86_64":
        # ppc64 could work but it misgenerates?
        configure_args += ["-DPREFER_LUA=OFF"]
        hostmakedepends += ["luajit"]
        makedepends += ["luajit-devel"]
    case _:
        configure_args += ["-DPREFER_LUA=ON"]
        hostmakedepends += ["lua5.1"]
        makedepends += ["lua5.1-devel"]


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link(
        "usr/share/nvim/runtime/parser", "../../../lib/tree-sitter"
    )
