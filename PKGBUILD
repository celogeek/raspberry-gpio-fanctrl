pkgname=raspberry-gpio-fanctrl
pkgver=20200114
pkgrel=1
pkgdesc="control fan connect on gpio based on raspberry temperature"
arch=(armv6h armv7h aarch64)
depends=(python python-raspberry-gpio)
source=(
	fanctrl.py
	fanctrl.service
)
sha256sums=('0585fdd7e2a6bb56046dfc010daaa743c0f89e1de6d5dd305e1552211a57c3fb'
            '1a66d880f18abe5e452abaf36438dde79ce362f844455af8e36991c2d457c810')
install=fanctrl.install

package() {
	install -Dm755 fanctrl.py $pkgdir/usr/lib/$pkgname/bin/fanctrl.py
	python -m compileall -d /usr/lib/$pkgname/bin $pkgdir/usr/lib/$pkgname/bin/
	python -O -m compileall -d /usr/lib/$pkgname/bin $pkgdir/usr/lib/$pkgname/bin/
	install -Dm644 fanctrl.service $pkgdir/usr/lib/systemd/system/fanctrl.service
}


