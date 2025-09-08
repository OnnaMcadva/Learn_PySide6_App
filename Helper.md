

# PySide6.QtCore

* `Signal(int)` — definuje vlastní signál, který vysílá hodnotu typu `int`.
  (v kódu: `clicked = Signal(int)` в `ClickableLabel`)
* `Qt` (konstanta / enumerace) — obsahuje množství konstant (role, zarovnání, módy apod.). Použité konkrétně:

  * `Qt.UserRole` — role pro ukládání vlastních dat v položce (setData/getData).
  * `Qt.AlignmentFlag.AlignCenter` — nastavení zarovnání na střed.
  * `Qt.PlainText` — formát textu (zobrazit jako prostý text).
  * `Qt.MatchExactly` — flaga pro přesné porovnání při hledání položek (`findItems`).
  * `Qt.AspectRatioMode.KeepAspectRatio` — režim škálování, který zachová poměr stran obrázku.
* `QTimer` — časovač; má signál `timeout`. Použito: `QTimer(self)` + `timeout.connect(...)` + `start(ms)`.
  Popis: spouští periodické volání slotu; `start(1000)` spustí interval 1000 ms; `stop()` (zakomentováno) zastaví.
* `QRect` — obdélník definující pozici/rozměry (x, y, w, h) používaný v `setGeometry(...)`.
* `QSize` — objekt velikosti (šířka, výška); používá se v `setSizeHint()` a pro škálování pixmapy.
* `QApplication`

  * `QApplication(sys.argv)` — vytvoří/app inicializuje aplikaci.
  * `QApplication.instance()` — vrátí existující instanci aplikace (pokud již běží).
  * `app.exec()` — spustí hlavní smyčku událostí (event loop).
  * (zakomentováno) `app.setStyle('Fusion')` — nastaví GUI styl aplikace.
* `emit` (metoda signálu) — vyšle signál (v kódu: `self.clicked.emit(self.num)` v `ClickableLabel.mousePressEvent`).

# PySide6.QtGui

* `QPixmap` — reprezentace rastrového obrázku. Použito: `QPixmap(path)` a `pixmap.scaled(...)`.
  Popis: načte obrázek z cesty; `scaled(size, Qt.AspectRatioMode.KeepAspectRatio)` vrátí škálovaný obrázek se zachováním poměru stran.
* `QIcon` — ikona (použita v `setWindowIcon(QIcon(...))`) — reprezentuje ikonku okna/aplikace.
* `QFont` — popis písma; konstruktor `QFont("Segoe UI", 12, QFont.Bold)` — definuje rodinu, velikost a váhu (např. `QFont.Bold` = tučný řez).
* `QColor` — barva (např. `QColor('red')`) — použitá pro nastavení pozadí položek (`setBackground`).

# PySide6.QtWidgets

* `QMainWindow`

  * `resize(width, height)` — nastaví rozměry hlavního okna.
  * `setStyleSheet(...)` — aplikuje CSS-styl (v kódu i jako zakomentovaný příklad).
  * `setWindowTitle(str)` — nastaví titulek okna.
  * `setWindowIcon(QIcon)` — nastaví ikonu okna.
  * `setCentralWidget(widget)` — určí centrální widget okna.
  * `statusBar().showMessage(str)` — získá stavový řádek a zobrazí v něm zprávu.
  * `closeEvent(event)` — událost/metoda volaná při zavírání okna (v kódu přepsaná pro zastavení observeru).
* `QWidget` — základní kontejner widgetu (např. `self.centralwidget = QWidget()`).
* `QPushButton`

  * `setText()` — nastaví text tlačítka.
  * `setGeometry(QRect(...))` — nastaví pozici a velikost tlačítka.
  * `setFont(QFont)` — nastaví font.
  * `setStyleSheet(...)` — aplikuje CSS-styl na tlačítko.
  * `clicked` (signál) + `clicked.connect(slot)` — signál kliknutí; `connect` připojí slot/metodu (v kódu `self.btnFalseNok.clicked.connect(self.btnClickedFalseNeg)`).
* `QLabel`

  * `setText()` — nastaví text.
  * `setGeometry(QRect(...))` — pozice/velikost.
  * `setFrameShape(QFrame.Box)` — tvar rámečku (zde Box).
  * `setTextFormat(Qt.PlainText)` — určí formát textu (plain).
  * `setAlignment(Qt.AlignmentFlag.AlignCenter)` — nastaví zarovnání obsahu.
  * `setFont(QFont)` — nastaví písmo.
  * `setStyleSheet(...)` — nastaví styl.
  * `setPixmap(QPixmap)` — vloží obrázek do labelu.
  * `clear()` — vymaže obsah labelu (text/pixmapu).
    (v kódu: `self.lblNew`, `self.img_big`, `ClickableLabel` dědí z `QLabel`).
* `QFrame` (enum)

  * `QFrame.Box` — konstanta tvaru rámečku (obdélníkový rámeček), použitá v `setFrameShape(...)`.
* `QListWidgetItem`

  * konstruktor `QListWidgetItem(text)` — vytvoří položku seznamu. (v kódu i zakomentovaně).
  * `setData(role, value)` — uloží vlastní data v položce (použito `Qt.UserRole`).
  * `setTextAlignment(...)` — nastaví zarovnání textu v položce.
  * `setSizeHint(QSize(...))` — doporučená velikost položky.
  * `setBackground(QColor(...))` — nastaví pozadí položky.
  * `setText(...)` — (obvyklá metoda pro změnu zobrazovaného textu).
* `QListWidget`

  * `setGeometry(QRect(...))` — pozice/velikost widgetu seznamu.
  * `setStyleSheet(...)` — vytvoření CSS stylu pro položky.
  * `itemSelectionChanged` (signál) + `.connect(self.lstSetsItemSelectionChanged)` — signál změny výběru položek.
  * `insertItem(index, item)` — vloží položku do seznamu na pozici.
  * `insertItems(index, [list])` — (zakomentováno) vloží více položek najednou.
  * `findItems(text, Qt.MatchExactly)` — najde položky přesnou shodou textu.
  * `setCurrentRow(index)` — (zakomentováno/používáno v logice) nastaví vybraný řádek.
  * `setFocus()` — nastaví fokus na widget.
  * `count()` — počet položek.
  * `selectedItems()` — vrátí seznam aktuálně vybraných položek.
  * `hasFocus()` — vrátí, zda má widget fokus.
  * `takeItem(row)` — (zakomentováno) odebere položku a vrátí ji.
  * `itemWidget(item)` — (zakomentováno) vrátí widget přiřazený k položce (pokud byl použit).
  * `removeItemWidget(item)` — (zmíněno v komentáři) odstraní widget z položky.
* `QListWidget.insertItems(...)` — (zakomentováno v kódu: `# self.lstSets.insertItems(0,['Set0',...])`) — vloží více položek.
* `QListWidget.findItems(...)` — hledání položek podle textu a režimu porovnání (`Qt.MatchExactly`).
* `QStyleFactory.keys()` — (zakomentováno: `# print(QStyleFactory.keys())`) — vrátí seznam dostupných GUI stylů.
* `QMessageBox`

  * `QMessageBox()` — vytvoří dialog.
  * `dlg.critical(None, 'Error', '...', QMessageBox.Ok)` — zobrazí kritický chybový dialog (v kódu při neexistujícím adresáři).
  * `QMessageBox.Ok` — konstanta pro tlačítko OK.
* Signal/slot usage v widgetech:

  * `clicked.connect(...)` (u `QPushButton` i u `ClickableLabel.clicked`) — připojí signál kliknutí k metodě.
  * `itemSelectionChanged.connect(...)` — připojí změnu výběru v `QListWidget`.
  * `QTimer.timeout.connect(...)` — připojí timeout timeru k metodě `read_dataset`.
* Události (event handlers) přepsané v kódu:

  * `mousePressEvent(self, event)` (v `ClickableLabel`) — přepsaná událost stisku myši; v kódu volá `self.clicked.emit(self.num)`.
  * `closeEvent(self, event)` (v `MainWindow`) — přepsaná metoda volaná při zavření okna (v kódu zastaví watchdog observer).

---

