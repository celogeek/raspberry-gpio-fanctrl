pkgname=raspberry-gpio-fanctrl
pkgver=20200110
pkgrel=4
pkgdesc="control fan connect on gpio based on raspberry temperature"
arch=(armv6h armv7h aarch64)
depends=(python python-raspberry-gpio)
source=(
	fanctrl.py
	fanctrl.service
)
sha256sums=(
	b25d22ec279ba6615a28fe52c5dd212de389676fb72fc6f25830b03be58e50a2
	5b8a1d17046278f3c0e3b531fa9f4c82e1d4e72991b77ed6bcbbc3732e6608f5
)
install=fanctrl.install


package() {
	install -Dm755 fanctrl.py $pkgdir/usr/lib/$pkgname/bin/fanctrl
	install -Dm644 fanctrl.service $pkgdir/usr/lib/systemd/system/fanctrl.service

}


