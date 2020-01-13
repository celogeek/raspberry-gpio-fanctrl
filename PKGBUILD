pkgname=raspberry-gpio-fanctrl
pkgver=20200113
pkgrel=1
pkgdesc="control fan connect on gpio based on raspberry temperature"
arch=(armv6h armv7h aarch64)
depends=(python python-raspberry-gpio)
source=(
	fanctrl.py
	fanctrl.service
)
sha256sums=('31e3cd794abb9d2cae828797207d84aaca641b2281ccee56ac5c05719959d99c'
            '5b8a1d17046278f3c0e3b531fa9f4c82e1d4e72991b77ed6bcbbc3732e6608f5')
install=fanctrl.install


package() {
	install -Dm755 fanctrl.py $pkgdir/usr/lib/$pkgname/bin/fanctrl
	install -Dm644 fanctrl.service $pkgdir/usr/lib/systemd/system/fanctrl.service
}


