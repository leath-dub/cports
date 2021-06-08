from cbuild.core import template

import os

def invoke(pkg):
    template.call_pkg_hooks(pkg, "init_fetch")
    template.run_pkg_func(pkg, "init_fetch")

    fetch_done = pkg.statedir / f"{pkg.pkgname}__fetch_done"
    if fetch_done.is_file():
        return

    template.call_pkg_hooks(pkg, "pre_fetch")
    template.run_pkg_func(pkg, "pre_fetch")

    if hasattr(pkg, "do_fetch"):
        if len(pkg.build_wrksrc) > 0:
            os.makedirs(pkg.abs_build_wrksrc, exist_ok = True)
        template.run_pkg_func(pkg, "do_fetch")
    else:
        template.call_pkg_hooks(pkg, "do_fetch")

    template.run_pkg_func(pkg, "post_fetch")
    template.call_pkg_hooks(pkg, "post_fetch")

    fetch_done.touch()
