# Password generator

## password_generator.py
 
Der Code ist ein Python-Skript, das zufällige Passwörter mit verschiedenen Optionen für die Länge und die Einbeziehung/Ausschluss von Zeichen generiert. Es definiert eine Funktion `generate_password()`, die mehrere Argumente akzeptiert, um den Prozess der Passwortgenerierung anzupassen, und zeigt dann deren Verwendung, indem es 9 Beispielpasswörter generiert und ausgibt.

Lassen Sie uns den Code Schritt für Schritt durchgehen:

1. `import string`: Dies importiert das Modul `string`, das verschiedene Konstanten für Zeichen enthält, wie z.B. ASCII-Buchstaben, Zahlen und Sonderzeichen.

2. `import random`: Dies importiert das Modul `random`, das Funktionen zum Generieren von Zufallszahlen und zum zufälligen Auswählen bereitstellt.

3. `def generate_password(length=12, include_digits=True, include_special_chars=True, exclude_chars=True):`: Dies definiert die Funktion `generate_password()` mit vier Parametern:
   - `length`: Die Länge des Passworts. Standardmäßig sind es 12 Zeichen.
   - `include_digits`: Ob Zahlen im Passwort enthalten sein sollen. Standardmäßig `True`.
   - `include_special_chars`: Ob Sonderzeichen im Passwort enthalten sein sollen. Standardmäßig `True`.
   - `exclude_chars`: Ob bestimmte Zeichen aus dem Zeichensatz ausgeschlossen werden sollen. Standardmäßig `True`.

4. Die Funktion überprüft, ob die `length` kleiner als 8 ist, und wirft eine `ValueError`-Ausnahme, wenn dies der Fall ist. Dadurch wird sichergestellt, dass Passwörter mindestens 8 Zeichen lang sind.

5. Der Standard-Zeichensatz für die Passwortgenerierung wird auf ASCII-Buchstaben festgelegt.

6. Wenn der Parameter `exclude_chars` `True` ist, werden die Zeichen `'il1Lo0O'` aus dem Zeichensatz ausgeschlossen. Dies geschieht mit einer List Comprehension, die diese Zeichen filtert.

7. Wenn der Parameter `include_digits` `True` ist, wird der Zeichensatz erweitert, um Zahlen (0-9) mit `string.digits` einzuschließen.

8. Wenn der Parameter `include_special_chars` `True` ist, wird der Zeichensatz erweitert, um Sonderzeichen mit `string.punctuation` einzuschließen.

9. Das tatsächliche Passwort wird mithilfe einer List Comprehension und `random.choice()` generiert, um zufällig Zeichen aus dem Zeichensatz auszuwählen. Die Länge des Passworts wird durch den Parameter `length` bestimmt.

10. Das generierte Passwort wird aus der Funktion zurückgegeben.

11. Der Abschnitt "Beispielaufruf" generiert und gibt 9 Passwörter aus, indem die Funktion `generate_password()` mit spezifischen Argumenten aufgerufen wird.

Es ist wichtig zu beachten, dass der Parameter `exclude_chars` nicht wie beabsichtigt funktioniert, da ihm im Funktionsaufruf der Wert `True` zugewiesen wird. Er sollte auf `False` gesetzt werden, um den Ausschluss von Zeichen zu deaktivieren. Zusätzlich demonstriert der Beispielcode derzeit die Generierung von 9 Passwörtern, jeweils mit einer Länge von 16 Zeichen, einschließlich Zahlen, Sonderzeichen und dem Ausschluss bestimmter Zeichen. Wenn Sie verschiedene Passwörter generieren möchten, sollten Sie die Parameter entsprechend anpassen.