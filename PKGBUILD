# PKGBUILD for 'araste'
# Maintainer: Mobin Aydinfar <mobin@mobintestserver.ir>

pkgname('araste')
pkgver=1.0
pkgrel=1
pkgdesc="Araste: a tool for converting Persion/Arabic to ASCII art"
arch(any)
url="https://github.com/ekm507/araste
depends=('python3')

# Unfortunately 'makedeb' does not currently support 'priority' & 'section' control field
# Issue #190: https://github.com/makedeb/issues/190
#priority='optional'
#section='text'
# Workaround #190
# https://github.com/makedeb/makedeb/issues/190#issuecomment-1179339372
control_fields=('Priority: optional' 'Section: text')

source(araste::git+https://github.com/ekm507/araste#branch=main)

pkgver() {
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
    cd "$srcdir"
    cp araste.py "$pkgdir/usr/bin/araste"
}
