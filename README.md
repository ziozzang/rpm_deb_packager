rpm & deb packager
==================

- by Jioh L. Jung (ziozzang@gmail.com)

The Skeleton Template of debian/RHEL package generation.

You can make debian package and rpm package for your linux dist.

How To
======

* for Ubuntu/Debian

1st, you must edit deb/*. it has package information.

2nd, edit make-deb-package.sh for package copy procedure.

3rd, run make-deb-package.sh


* for rpm

1st, you must edit rpm/*.

2nd, edit make-deb-package.sh for package copy procedure.

3rd, run make-rpm-package.sh

Notice
======

You can copy this source and edit freely.
