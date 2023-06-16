# ML-AI_miniproject
Mesterséges intelligencia építése, egyszerű példa

Ez a program egy döntési fát épít ki az Iris adathalmazzal. A program először betölti az adatokat a `pandas` könyvtár segítségével,
majd a `train_test_split` függvény segítségével felosztja az adathalmazt tanítási és teszthalmazokra. Ezután létrehoz egy döntési fát, 
és a `fit` függvénnyel tanítja az adathalmazt. Végül teszteli a modellt és kiszámítja a tesztpontosságot.

Az utolsó sorokban a program létrehozza a döntési fát és megjeleníti az eredményt. A `export_graphviz` függvény létrehoz egy DOT formátumú leírást a döntési fáról, 
amelyet a `pydotplus` és az `Image` csomagok segítségével lehet megjeleníteni. Ezzel az eredménnyel egyértelműen megérthetőek a döntési pontok és a fa felépítése.

Ez csak egy példa azonban, amelyet a döntési fák használatával lehet használni a mesterséges intelligencia területén. 
A döntési fák általában egyszerűek és könnyen érthetőek, és számos különböző problémában használhatók.
