pkgname = "python-trio"
pkgver = "0.26.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--pyargs",
    "trio",
    "--skip-optional-imports",
    "-k",
    "not test_signals and not test_for_leaking_fds",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-attrs",
    "python-idna",
    "python-outcome",
    "python-sniffio",
    "python-sortedcontainers",
]
checkdepends = ["python-pytest", "python-astor", *depends]
pkgdesc = "Python library for async concurrency"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/python-trio/trio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "463cc8cc437cdfd01bdff576519d753d2c35cd5cfb4b657b614ba4eabbab3bb2"


def post_install(self):
    self.install_license("LICENSE.MIT")
