FreeBSD 5.0-CURRENT README

Das FreeBSD Projekt

Copyright © 2000, 2001, 2002, 2003 von The FreeBSD Documentation Project

Copyright © 2002, 2003 von The FreeBSD German Documentation Project

$FreeBSD: src/release/doc/de_DE.ISO8859-1/readme/article.sgml,v 1.10
2003/01/14 07:12:31 ue Exp $

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

  Dieses Dokument enthält eine kurze Einführung zu FreeBSD 5.0-CURRENT.
  Es enthält einige Hinweise, wie Sie FreeBSD beziehen können; wie
  Kontakt zum FreeBSD Project aufnehmen können, sowie Verweise auf
  zusätzliche Informationsquellen.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1. Einführung

Diese Ausgabe von FreeBSD ist eine snapshot-Version von FreeBSD
5.0-CURRENT und repräsentiert den aktuellen Zustand im Entwicklungszweig
5-CURRENT.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.1. Über FreeBSD

FreeBSD ist ein auf 4.4 BSD Lite basierendes Betriebssystem für Intel,
AMD, Cyrix oder NexGen ``x86''-basierte PCs, Compaq (ehemals DEC) Alpha
und UltraSPARC Systeme. Versionen für die Plattformen IA64 und PowerPC
sind ebenfalls in der Entwicklung. FreeBSD unterstützt viele
verschiedene Geräte und Umgebungen und für alle Anwendungen von der
Software-Entwicklung bis zur Anbietung von Diensten im Internet genutzt
werden.

Diese Version von FreeBSD stellt Ihnen alles zur Verfügung, was Sie zum
Betrieb eines derartigen Systems brauchen. Dazu gehört der Quellcode für
den Kernel und alle Programme des Basissystem. Wenn Sie ``source''
Distribution installieren, können Sie das gesamte System mit einem
einzigen Befehl neu kompilieren. Diese Eigenschaft macht es ideal für
Studenten, Forscher, und interessierte Benutzer, die einfach wissen
wollen, wie das System funktioniert.

Die große Sammlung von angepaßter Software anderer Anbieter (die ``Ports
Collection'') macht es Ihnen leicht, ihre Lieblingtools für Unix auch
für FreeBSD zu finden und zu installieren. Jeder ``port'' besteht aus
einer Reihe von Skripten, um eine gegebene Anwendung mit einem einzigen
Kommando herunterladen, konfigurieren, kompilieren, und installieren zu
können. Die über 7,800 Ports (vom Editor über Programmiersprachen bis zu
graphischen Anwendungen) machen FreeBSD zu einer leistungsstarken und
umfassenden Arbeitsumgebung, die viele kommerzielle Unix-Varianten weit
hinter sich läßt. Die meisten Ports sind auch als vorkompilierte
Packages erhältlich, die mit dem Installationsprogramm einfach und
schnell installiert werden können.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.2. Zielgruppe

Dieser snapshot ist primär für Bastler und andere Benutzer gedacht, die
sich an der laufenden Entwicklung von FreeBSD beteiligen wollen. Das
Entwicklerteam von FreeBSD bemüht sich zwar, daß jeder snapshot so
funktioniert wie versprochen, aber 5-CURRENT ist nun einmal der
Entwicklungszweig.

Wenn Sie einen snapshot benutzen wollen, müssen Sie sich mit der Technik
von FreeBSD und den aktuellen Vorgängen bei der Entwicklung von FreeBSD
5-CURRENT (wie sie in der Mailingliste 'FreeBSD-CURRENT'
<freebsd-current@FreeBSD.org> diskutiert werden) auskennen.

[Anmerkung des Übersetzers: Auf der Mailingliste 'FreeBSD-CURRENT'
<freebsd-current@FreeBSD.org> wird Englisch gesprochen und die meisten
Dokumente sind ebenfalls in dieser Sprache verfaßt worden. Ohne gute
Englischkenntnisse kommt man also nicht weit. Allerdings ist die
Beteiligung an der Entwicklung der FreeBSD eine der interessanteren
Varianten, die eigenen Englisch-Kenntnisse zu erweitern.]

Wenn Sie mehr an einem störungsfreien Betrieb von FreeBSD als an den
neuesten Features von FreeBSD interessiert sind, ist eine offizielle
Release (wie z.B. 4.7-RELEASE) die deutliche bessere Wahl. Releases
werden ausführlich getestet und auf Qualität geprüft, um Zuverlässigkeit
und Betriebssicherheit garantieren zu können.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2. Bezugsquellen für FreeBSD

FreeBSD kann auf vielen verschiedenen Wegen bezogen werden. Dieses
Kapitel konzentriert sich auf die Varianten, die für den Bezug auf einer
komplett neuen Version von FreeBSD gedacht sind und weniger auf die
Möglichkeit zur Aktualisierung eines bereits bestehenden Systems.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.1. CDROM und DVD

FreeBSD-RELEASE Distributionen können auf CDROM oder DVD von diversen
Firmen bezogen werden. Dies ist normalerweise der bequemste Weg, wenn
Sie FreeBSD zum ersten Mal installieren, da Sie das System einfach neu
installieren können, falls das notwendig ist. Einige Distributionen
enthalten einige der optionalen ``Packages'' aus der FreeBSD Ports
Collection.

Eine Übersicht über die Firmen, die FreeBSD auf CDROM oder DVD
vertreiben, finden Sie im Anhang ``Bezugsquellen für FreeBSD'' des
Handbuches.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.2. FTP

Sie können FreeBSD und/oder die optionalen Packages mit FTP vom primären
FreeBSD-Server ftp://ftp.FreeBSD.org/ und allen seinen ``mirrors''
beziehen.

Eine Liste von alternativen Bezugsquellen für FreeBSD finden Sie im
Kapitel FTP Server des Handbuchs und auf unseren
http://www.freebsdmirrors.org/ Webseiten. Wir raten Ihnen dringend,
einen Mirror in der näheren Umgebung (aus Netzwerksicht) zu verwenden.

Zusätzliche Mirrors sind immer willkommen. Wenden Sie sich bitte an
<freebsd-admin@FreeBSD.org>, wenn Sie an weiteren Informationen zu
diesem Thema interessiert sind. Zusätzliche Informationen zu diesem
Thema finden Sie im Artikel Mirroring FreeBSD.

Sie finden die für den Start der Installation notwendigen Images der
Bootdisketten und die Dateien der eigentlichen Distribution auf allen
Servern. Einige Server stellen auch die ISO-Images bereit, die Sie zur
Erzeugung einer (bootfähige) CDROM der FreeBSD-Release benötigen.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3. Kontaktinformation für das FreeBSD Projekt

3.1. Email und Mailinglisten

Wenn Sie Fragen haben oder Hilfe benötigen, wenden Sie sich bitte an die
Mailingliste 'FreeBSD general questions'
<freebsd-questions@FreeBSD.org>.

Wenn Sie die Entwicklung von 5-CURRENT mitverfolgen, müssen Sie die
Mailingliste 'FreeBSD-CURRENT' <freebsd-current@FreeBSD.org> lesen. Nur
so können Sie die teilweise lebensnotwendigen Informationen über die
aktuellen Entwicklungen und Änderungen erhalten, die Sie für den Betrieb
des Systems benötigen.

Da FreeBSD zum größten Teil von Freiwilligen und Idealisten entwickelt
wird, freuen wir uns über jeden, der mit anpacken möchte -- schon jetzt
gibt es mehr Wünsche als Zeit, um diese umzusetzen. Wenn Sie Kontakt zu
den Entwicklern suchen, um technische Angelegenheiten zu besprechen oder
um Ihre Hilfe anzubieten, wenden Sie sich bitte an Mailingliste 'FreeBSD
technical discussions' <freebsd-hackers@FreeBSD.org>.

Bitte beachten Sie, auf diesen Mailinglisten teilweise extrem viele
Mails erscheinen. Wenn Ihre Mailversorgung nur sehr langsam oder sehr
teuer ist, oder Sie nur an den Schlagzeilen der FreeBSD-Entwicklung
interessiert sind, dürfte es besser sein, wenn Sie sich auf die
Mailingliste 'FreeBSD announcements' <freebsd-announce@FreeBSD.org>
konzentrieren.

Alle Mailinglisten stehen für jeden offen, der sich für das jeweilige
Thema interessiert. Senden Sie einfach eine Mail an
<majordomo@FreeBSD.org>, die als Text nur das Schlüsselwort help in
einer Zeile enthält. Dadurch erhalten Sie weitergehende Informationen,
wie Sie die diversen Mailinglisten abbonieren können, wie Sie auf die
Archive zugreifen können, usw. Es gibt viele Mailinglisten, die nur mit
einem ganz bestimmten Thema befassen und hier nicht aufgeführt sind.
Weitergehende Informationen finden Sie im Bereich Mailinglisten der
FreeBSD Webseite.

  Wichtig: Senden Sie auf gar keinen Fall eine Mail an die
  Mailinglisten, um diese zu abonnieren. Benutzen Sie für diesen Zweck
  die Adresse <majordomo@FreeBSD.org> .

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3.2. Meldungen über Fehler und Probleme

Vorschläge, Fehlermeldungen und zusätzlicher Sourcecode sind immer
willkommen -- bitte informieren Sie uns über jedes Problem, das sie
finden. Fehlermeldungen, die sofort auch die entsprechende Korrektur
enthalten, sind natürlich noch willkommener.

Wenn Ihr System an das Internet angeschlossen ist, sollten Sie
send-pr(1) oder das Formular auf der Webseite
http://www.FreeBSD.org/send-pr.html benutzen. Wenn Sie Ihren ``Problem
Reports'' (PRs) auf dieser Art und Weise absetzen, wird er automatisch
archiviert und weiterverfolgt. Die Entwickler von FreeBSD bemühen sich,
so schnell wie möglich auf alle gemeldeten Fehler zu reagieren. Eine
Übersicht über alle offenen PRs ist auf dem Webserver von FreeBSD
verfügbar. Diese Liste ist sehr nützlich, wenn Sie wissen wollen, welche
möglichen Probleme schon von anderen Benutzern gefunden wurden.

Bitte beachten Sie, daß send-pr(1) nur ein Shell-Skript ist, daß man
relativ einfach auch auf anderen Systemen als FreeBSD verwenden kann.
Wir empfehlen Ihnen dringend, diese Variante zu verwenden. Wenn Sie
allerdings aus irgendeinem Grund send-pr(1) nicht benutzen können,
können Sie versuchen, Ihren Problem Report an die Mailingliste 'FreeBSD
problem reports' <freebsd-bugs@FreeBSD.org> zu senden.

Weitere Informationen finden Sie im Dokument ``Writing FreeBSD Problem
Reports'' auf der Webseite von FreeBSD. Es enthält viele nützliche Tips
zum Verfassen und Versenden effektiver Fehlermeldungen.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4. Weiterführende Dokumente

Es gibt viele verschiedene Quellen für Informationen über FreeBSD,
einige sind Bestandteil dieser Distribution, während andere über das
Internet oder in gedruckter Form verfügbar sind.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.1. Dokumentation zur Release

Sie finden weitergehende über diese snapshot Distribution in anderen
Dokumenten. Diese Dokumente stehen in verschiedenen Formaten zur
Verfügung. Die Varianten Text (.TXT) und HTML (.HTM) stehen fast immer
zur Verfügung. Einige Distributionen stellen weitere Formate wie
PostScript (.PS) oder das Portable Document Format (.PDF) zur Verfügung.

-   README.TXT: Sie lesen es gerade. Hier finden Sie allgemeine
    Informationen über FreeBSD und ein paar allgemeine Hinweise zum
    Bezug einer Distribution.

-   EARLY.TXT: Spezielle Hinweise für die ersten Anwender von FreeBSD
    5.0-RELEASE. Wenn dies Ihre erste Begegnung mit FreeBSD 5-CURRENT
    ist und/oder Sie noch eine 5.X Version benutzt haben, sollten Sie
    diesen Artikel auf jeden Fall lesen.

-   RELNOTES.TXT: Die begleitenden Informationen zu dieser Release
    enthalten die Neuerungen in dieser Version von FreeBSD (5.0-CURRENT)
    und die Änderungen seit der letzten Version (FreeBSD 4.0-RELEASE).

-   HARDWARE.TXT: Die Liste der unterstützten Hardware enthält eine
    Übersicht über die Geräte, auf den FreeBSD erfolgreich getestet
    wurde.

-   INSTALL.TXT: Die Anleitung zur Installation von FreeBSD von dem
    Distributions-Medium.

-   ERRATA.TXT: Die Errata. Brandaktuelle Informationen, die erst nach
    dem Erscheinen dieser Version bekannt wurden, finden Sie hier. Diese
    Datei ist speziell für die Anwender einer Release (und nicht der
    Snapshots) von Interesse. Sie sollten diesen Text auf jeden Fall
    lesen, bevor Sie FreeBSD installieren, da er die aktuellsten
    Informationen über die seit der Veröffentlichung gefundenen und
    behobenen Probleme enthält.

  Anmerkung: Einige dieser Dokumente (speziell RELNOTES.TXT,
  HARDWARE.TXT, und INSTALL.TXT) enthalten Informationen, die nur für
  eine bestimmte Architektur gellten. Zum Beispiel enthalten die Release
  Notes für die Alpha keine Informationen über i386-Systeme, und
  umgekehrt. Die Information, zu welcher Architektur ein Dokument
  gehört, steht immer am Anfang des Textes.

Auf den Plattformen, auf denen sysinstall(8) zur Verfügung steht (zur
Zeit i386 und alpha) finden Sie diese Dokumente während der Installation
normalerweise unter dem Menüpunkt Dokumentation. Um nach der
Installation des Systems dieses Menü zugreifen zu können, müssen Sie das
Programm sysinstall(8) erneut aufrufen.

  Anmerkung: Sie sollten auf jeden Fall die Errata zur jeweiligen
  Version lesen, bevor Sie die Installation beginnen. Dies ist der
  einzige Weg, die aktuellsten Informationen zu erhalten und sich über
  eventuell nach der Installation auftretende Probleme zu informieren.
  Die zusammen mit der Veröffentlichung erschienene Version ist per
  Definition veraltet. Allerdings sind im Internet aktualisierte
  Versionen verfügbar, die die ``aktuellen Errata'' für diese Version
  sind. Diese Versionen sind bei http://www.FreeBSD.org/releases/ und
  allen aktuellen Mirrors dieser Webseite verfügbar.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.2. Onlinehilfe (Manual Pages)

Wie bei fast jedem anderen UNIX-ähnlichen System steht Ihnen auch bei
FreeBSD eine Onlinehilfe zur Verfügung, die Sie über das Kommando man(1)
oder über das hypertext manual pages gateway auf dem Webserver von
FreeBSD ansprechen können. Die Onlinehilfe stellt den Benutzern von
FreeBSD Informationen zu einzelnen Befehlen und Interfaces zur
Programmierung zur Verfügung.

In einige Fällen behandelt die Online-Hilfe spezielle Themen.
Interessante Beispiele dafür sind tuning(7) (Hinweise, wie sie die
Performance Ihres Systems verbessern können), security(7) (eine
Einführung in das Thema Sicherheit unter FreeBSD), und style(9) (die
Spielregeln für die Kernel-Programmierung).

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.3. Bücher und Artikel

Zwei extrem nützliche Sammlungen von Informationen über FreeBSD, die vom
FreeBSD Project verwaltet werden, sind das FreeBSD Handbuch und der
FreeBSD FAQ. Die aktuellen Versionen des Handbuches und der FAQ sind
immer auf der Webseite FreeBSD Dokumentation und allen Ihren
Mirror-Sites verfügbar. Wenn Sie die Distribution doc installiert haben,
können Sie den FAQ und Handbuch mit einem Web-Browser direkt auf Ihrem
System lesen.

Es gibt eine ganze Reihe von Online verfügbaren Büchern und Artikeln,
die vom FreeBSD Project herausgegeben werden und auf einzelne
FreeBSD-bezogene Themen genauer eingehen. Dabei wird ein sehr breites
Spektrum abgedeckt, es gibt Informationen zur effektiven Nutzung der
Mailinglisten, den parallelen Betrieb von FreeBSD und anderen
Betriebssystem, und Hinweise für neue Entwickler. Wie das Handbuch und
die FAQ sind auch diese Dokumente auf Webseite FreeBSD Dokumentation und
in der Distribution doc verfügbar.

Eine Liste zusätzlicher Bücher und Dokumentationen zu FreeBSD finden Sie
im Kapitel Bibliographie des Handbuchs. Da FreeBSD ganz klar aus der
UNIX-Welt stammt, enthalten auch andere Artikel und Bücher über
UNIX-Systeme nützliche Informationen. Eine Auswahl dieser Dokumente
finden Sie ebenfalls in der Bibliographie.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

5. Danksagung

FreeBSD ist das Ergebnis der Arbeit vieler hundert, wenn nicht Tausender
Personen aus der ganzen Welt, die ungezählte Stunden investiert haben,
um diese Version möglich zu machen. Die vollständige Liste aller
Entwickler und Helfer finden Sie auf der FreeBSD-Webseite ``Beteiligte''
und allen aktuellen Mirrors dieser Webseite.

Wir möchten uns speziell bei den vielen tausend Anwendern und Testern
aus der ganzen Welt bedanken, ohne die diese snapshot niemals möglich
gewesen wäre.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

Diese Datei und andere Dokumente zu dieser Version sind bei
http://snapshots.jp.FreeBSD.org/verfuegbar.

Wenn Sie Fragen zu FreeBSD haben, lesen Sie erst die Dokumentation,
bevor Sie sich an <de-bsd-questions@de.FreeBSD.org> wenden.

Alle Anwender von FreeBSD 5-CURRENT sollten sich in die Mailingliste
<current@FreeBSD.org> eintragen.

Wenn Sie Fragen zu dieser Dokumentation haben, wenden Sie sich an
<de-bsd-translators@de.FreeBSD.org>.
