self.description = "Fileconflict with symlinks (2)"

p1 = pmpkg("pkg1")
p1.files = ["dir/realdir/file",
            "dir/symdir -> realdir"]
self.addpkg(p1)

p2 = pmpkg("pkg2")
p2.files = ["dir/symdir/file"]
self.addpkg(p2)

self.args = "-A %s" % " ".join([p.filename() for p in p1, p2])

self.addrule("PACMAN_RETCODE=1")
self.addrule("!PKG_EXIST=pkg1")
self.addrule("!PKG_EXIST=pkg2")
