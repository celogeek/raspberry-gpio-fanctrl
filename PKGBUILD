pkgname=raspberry-gpio-fanctrl
pkgver=20200115
pkgrel=1
pkgdesc="control fan connect on gpio based on raspberry temperature"
arch=(armv6h armv7h aarch64)
depends=(python python-raspberry-gpio)
source=(
	fanctrl.py
	fanctrl.service
)
sha256sums=('1ce7d1e30042c36cd67a43f40921b8b3b4dc17e699d7394d429a1ec45e1a2e8b'
            '1a66d880f18abe5e452abaf36438dde79ce362f844455af8e36991c2d457c810')
install=fanctrl.install

package() {
	install -Dm755 fanctrl.py $pkgdir/usr/lib/$pkgname/bin/fanctrl.py
	python -m compileall -d /usr/lib/$pkgname/bin $pkgdir/usr/lib/$pkgname/bin/
	python -O -m compileall -d /usr/lib/$pkgname/bin $pkgdir/usr/lib/$pkgname/bin/
	install -Dm644 fanctrl.service $pkgdir/usr/lib/systemd/system/fanctrl.service
}


