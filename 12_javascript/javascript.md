# JavaScript
## Czym jest JavaScript?
JavaScript (JS) jest obiektowym językiem skryptowym wykorzystywanym w sieci. Często wykorzystuje się go w celu zapewnienia różnych funkcjonalności stron internetowych. Atutem przy zastosowaniu JS jest zwiększenie poziomu interaktywności stron poprzez wprowadzenie dynamicznych elementów, których "zachowanie" zmienia się w zależności od akcji podejmowanych przez użytkownika.

## Podstawowa składania
Skrypty w JS umieszczamy w zasięgu znacznika `<script>`.
Musimy zdefiniować wykorzystywany przez nas język przy pomocy atrybutu type — javascript jest jednym z wielu możliwych języków skryptowych używanych w stronach internetowych.

```
<script>
    document.write("Mój pierwszy skrypt");
</script>
```
Skrypty umieszczamy w dokumencie HTML w części body i/lub head, przy czym definicje funkcji zaleca się umieszczać w head.

```
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>

      <script>
          document.write("Mój pierwszy skrypt");
      </script>

    </body>
</html>
```
```
<html>
    <head>
      <meta charset="utf-8">

    <script>
        document.write("<title>A tytuł jego "+(11*4)+"</title>");
    </script>

    </head>
    <body>
        Jakaś niezwykle zajmująca treść.
    </body>
</html>
```
Nasz skrypt jest interpretowany, uruchamiany oraz wykonywany przez przeglądarkę. Oznacza to, że możemy "testować" naszą stronę bez potrzeby wrzucania jej na serwer. :)

## Zmienne
Zmienne deklarujemy przy pomocy wyrażenia var, np.:

```
var x;
var i = 0;
```

###   Zadanie <img src="../images/pencil.png" width="20" align="left">

Stwórz zmienną typu string z nazwą obecnej pory roku.

Korzystając z metody `getElementById()` zmień poniższy przykład HTML, tak aby posiadał informacje o obecnej porze roku:

```
document.getElementById("id znacznika").innerHTML = "string";
```

Przykład:
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>

    <p> Obecna pora roku to <span id='pora'> xxx </span>. </p>

  </body>
</html>
```


## Funkcje

Funkcje definiujemy w sposób następujący:

```
<script>
    function moja_funkcja() {
        kod;
    }
</script>
```


Funkcje można tez dodawać załączając plik o rozszerzeniu `*.js`, przykład: "External JavaScript" dostępny tutaj: https://www.w3schools.com/js/js_whereto.asp.

## Obiekty
JavaScript jest językiem obiektowym, co oznacza, że w trakcie korzystania z niego posługujemy się obiektami, a także mamy możliwość tworzenia nowych obiektów. Na zajęciach nie będziemy zajmowali się tworzeniem obiektów, natomiast zapoznamy się z kilkoma gotowymi obiektami.

Mówiąc ogólnie, obiekty charakteryzują się tym, że mają swoje właściwości (properties) i metody (methods).

Przykład wykorzystania właściwości (w tym przypadku length obiektu typu Array):

```
<script>
    var moi_przyjaciele = new Array();
    moi_przyjaciele[0] = "Jan";
    moi_przyjaciele[1] = "Eustachy";
    moi_przyjaciele[2] = "Teofania";

    document.write("Tylu mam przyjaciół: " + moi_przyjaciele.length);
</script>
```

Przykład wykorzystania metody (random() obiektu typu Math):

```
document.write(Math.random());
```

## Korzystanie z języka

W JS standardowo wykorzystujemy wyrażenia, które znamy już z zajęć z programowania, np: if if-else, pętle: for, while, operatory: +, -, etc.

Korzystamy również z predefiniowanych obiektów, tj. String, Array, Math, Boolean i wielu innych.

Aby zwiększyć interaktywność naszych stron, posługujemy się możliwością wykrywania działań (actions) użytkownika przy pomocy obiektów typu Event. Ogólnie rzecz biorąc:

```
<html>
    <head>
    <script>
         function pokaz() {
             alert("Już pokazuje")
         }
    </script>
    </head>

    <body>
        <button onclick="pokaz()">Pokaż</button>
    </body>
</html>
```

Działanie dotyczy tu kliknięcia na przycisk — onclick.

## Komentarze

```
// krótki, jednolinijkowy

/* To jest nieco dłuższy, wielolinijkowy
     komentarz. Niech ten dzień będzie
     dobrym dniem. */

/* Komentarze /* nie mogą być zagnieżdżone, wtedy otrzymamy: */ Syntax error */

```
## Przykładowe skrypty

- Zliczanie kliknięć na określonym elemencie graficznym. Przydatne: onclick="…", document.getElementById("id").
```
<html>
    <head>
        <script>
            var x=0;

            function clicker() {
                x++;

                document.getElementById("pole").value=x;
            }
        </script>
    </head>

    <body onclick="clicker()">
        <input type="text" id="pole" />
    </body>
</html>
```

- Różne powitania na wybrane pory dnia (można zastosować if…else… lub switch (poniżej podane ze swich). Przydatne: get.Hours - metoda obiektu Date.
```
<html>
    <head>
    </head>
    <body>
        <script>
            var d = new Date(); // tworzenie obiektu zawierającego informacje o dzisiejszej dacie
            var h = d.getHours(); // pobiera pełne godziny - bez minut

            switch (h){
            case 8:
                  document.write("Tak wcześnie, a my już działamy!");
             break;
            case 10:
                  document.write("Zbliża się lunch!");
                  break;
            case 11:
             document.write("Czy już po zajęciach?");
             break;
            default:
              document.write("Działamy, działamy!");
        }
        </script>
    </body>
</html>
```

- Liczenie czasu pomiędzy kliknięciami na dwa przyciski. Przydatne: setTimeout, clearTimeout (metody Window, zastosowane poniżej), lub timeStamp (metoda Event).
```
<html>
    <head>
        <script>
            var i = 0;
            var t;

            function start(){
                t = setTimeout("start()",1);
                i++;
                document.getElementById("tekst").value = i + " ms";
                }

            function stop(){
                clearTimeout(t);
            }

            function reset(){
                i = 0;
                document.getElementById("tekst").value = i + " ms";
            }
    </script>
    </head>
    <body>
        <input type="button" onclick="start()" value="kliknij"/>
        <input type="button" onclick="stop()" value="stop"/>
        <input type="text" id="tekst" value="Ile czasu"/>
        <input type="button" onclick="reset()" value="reset"/>
    </body>
</html>
```

## Przydatne linki:
Kurs JavaScript: http://www.w3schools.com/js w tym:

Obiekty i ich metody: http://www.w3schools.com/jsref
