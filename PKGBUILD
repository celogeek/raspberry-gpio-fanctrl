pkgname=raspberry-gpio-fanctrl
pkgver=20200111
pkgrel=2
pkgdesc="control fan connect on gpio based on raspberry temperature"
arch=(armv6h armv7h aarch64)
depends=(python python-raspberry-gpio)
source=(
	fanctrl.py
	fanctrl.service
)
sha256sums=(
	3b9a7d223ac6e357e2b081f3c2b579997c42e51a4e3f1cbcdfd869d7bf6069fd
	5b8a1d17046278f3c0e3b531fa9f4c82e1d4e72991b77ed6bcbbc3732e6608f5
)
install=fanctrl.install


package() {
	install -Dm755 fanctrl.py $pkgdir/usr/lib/$pkgname/bin/fanctrl
	install -Dm644 fanctrl.service $pkgdir/usr/lib/systemd/system/fanctrl.service
}


