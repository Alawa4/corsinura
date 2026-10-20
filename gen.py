#!/usr/bin/env python3
"""Erzeugt index.html und datenschutz.html (4 Sprachen) – Quelle der Texte ist diese Datei."""
import html
DATE = {'de': '17. Oktober 2026', 'en': '17 October 2026', 'fr': '17 octobre 2026', 'es': '17 de octubre de 2026'}
MAIL = 'corsinura.app@gmail.com'
FORM = ''  # Formspree-Formular-ID (z. B. 'xyzabcd'); leer: nur E-Mail
NAME = 'Abdul Karim Alawa'
COL = lambda l: '\u202f: ' if l == 'fr' else ': '
NAMES = {'de': 'Deutsch', 'en': 'English', 'fr': 'Français', 'es': 'Español'}
P = {
'de': {'title': 'Datenschutzerklärung', 'intro': 'Corsinura ist eine Lern-App für Kardiologie (EKG, Herztöne, Echokardiographie). Sie funktioniert ohne Konto und ohne Anmeldung. Wir haben die App so gebaut, dass möglichst keine personenbezogenen Daten anfallen.',
 'sec': [
  ('Verantwortlich', f'Verantwortlich für die Datenverarbeitung ist der Anbieter der App (siehe <a href="impressum.html">Impressum</a>). Kontakt: <a href="mailto:{MAIL}">{MAIL}</a>.'),
  ('Keine Erhebung von Daten durch die App', 'Die App erhebt keine personenbezogenen Daten und überträgt keine Daten an uns. Es gibt keine Werbung, keine Analyse- oder Tracking-Werkzeuge und keine Absturzberichte an Dritte.'),
  ('Daten auf deinem Gerät', 'Lernfortschritt, Einstellungen und Dateien, die du selbst hinzufügst (z. B. eigene EKG-Bilder oder Herzton-Aufnahmen), werden ausschließlich lokal auf deinem Gerät gespeichert. Wir haben darauf keinen Zugriff. Wenn du in den Android-Einstellungen die Sicherung über Google aktiviert hast, kann Android deinen Lernfortschritt in deiner Google-Sicherung speichern; das steuert Google bzw. dein Gerät, nicht wir. Eigene Dateien sind von der Sicherung ausgenommen. Mit „Fortschritt sichern“ in den Einstellungen kannst du eine Datei selbst exportieren.'),
  ('Käufe über Google Play', 'Abonnements und der einmalige Kauf werden über Google Play abgewickelt. Zahlungsdaten erhält ausschließlich Google. Die App erfährt nur, ob ein Kauf besteht, um die Vollversion freizuschalten. Es gilt die <a href="https://policies.google.com/privacy">Datenschutzerklärung von Google</a>.'),
  ('Internetverbindung', 'Alle Inhalte liegen in der App und funktionieren offline. Eine Verbindung wird nur für Käufe und deren Wiederherstellung über Google Play genutzt sowie, wenn du selbst einen Link (z. B. zu einer Leitlinie oder Quelle) öffnest. Dieser öffnet sich in deinem Browser.'),
  ('Themenwünsche und Aufnahmen per E-Mail', 'Wenn du über „Thema wünschen“ oder „Aufnahme beisteuern“ eine E-Mail schreibst, öffnet sich dein E-Mail-Programm; die App selbst sendet nichts. Deine E-Mail-Adresse und deine Nachricht verwenden wir nur, um dein Anliegen zu bearbeiten und dir zu antworten; zugesandte Aufnahmen nutzen wir nur nach deiner Zustimmung in der App (Art. 6 Abs. 1 lit. f DSGVO), und löschen sie, wenn sie dafür nicht mehr benötigt werden.'),
  ('Berechtigungen', 'Die App nutzt nur den Internetzugriff (für Käufe) und die Google-Play-Abrechnung. Sie greift nicht auf Kamera, Mikrofon, Standort oder Kontakte zu. Eigene Dateien wählst du selbst über die Dateiauswahl von Android aus.'),
  ('Deine Rechte', 'Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren, z. B. beim Landesbeauftragten für den Datenschutz und die Informationsfreiheit Baden-Württemberg.'),
  ('Zielgruppe', 'Die App richtet sich an Erwachsene, insbesondere Medizinstudierende, Ärztinnen und Ärzte und Pflegekräfte. Sie ersetzt keine ärztliche Beratung.'),
  ('Änderungen', 'Wir passen diese Erklärung an, wenn sich die App oder die Rechtslage ändert. Es gilt die jeweils hier veröffentlichte Fassung.')],
 'stand': 'Stand'},
'en': {'title': 'Privacy policy', 'intro': 'Corsinura is a cardiology learning app (ECG, heart sounds, echocardiography). It works without an account or sign-in. We built the app so that as little personal data as possible is involved.',
 'sec': [
  ('Controller', f'The controller is the provider of the app (see <a href="impressum.html">legal notice</a>). Contact: <a href="mailto:{MAIL}">{MAIL}</a>.'),
  ('No data collection by the app', 'The app does not collect personal data and does not send any data to us. There are no ads, no analytics or tracking tools and no crash reports to third parties.'),
  ('Data on your device', 'Learning progress, settings and files you add yourself (e.g. your own ECG images or heart sound recordings) are stored only locally on your device. We have no access to them. If you have enabled Google backup in your Android settings, Android may store your learning progress in your Google backup; this is controlled by Google and your device, not by us. Your own files are excluded from backup. You can export a file yourself with “Back up progress” in the settings.'),
  ('Purchases via Google Play', 'Subscriptions and the one-time purchase are handled by Google Play. Only Google receives payment data. The app only learns whether a purchase exists in order to unlock the full version. <a href="https://policies.google.com/privacy">Google’s privacy policy</a> applies.'),
  ('Internet connection', 'All content is included in the app and works offline. A connection is only used for purchases and restoring them via Google Play, and when you open a link yourself (e.g. to a guideline or source), which opens in your browser.'),
  ('Topic requests and recordings by e-mail', 'If you write an e-mail via “Request a topic” or “Contribute a recording”, your e-mail app opens; the app itself sends nothing. We use your e-mail address and message only to handle your request and reply; recordings you send are only used in the app with your consent (Art. 6(1)(f) GDPR) and delete them when they are no longer needed for that purpose.'),
  ('Permissions', 'The app only uses internet access (for purchases) and Google Play billing. It does not access the camera, microphone, location or contacts. You select your own files yourself via the Android file picker.'),
  ('Your rights', 'You have the right of access, rectification, erasure, restriction of processing, data portability and objection, and the right to lodge a complaint with a data protection supervisory authority.'),
  ('Audience', 'The app is intended for adults, in particular medical students, physicians and nurses. It does not replace medical advice.'),
  ('Changes', 'We update this policy when the app or the law changes. The version published here applies.')],
 'stand': 'Last updated'},
'fr': {'title': 'Politique de confidentialité', 'intro': 'Corsinura est une application d’apprentissage de la cardiologie (ECG, bruits du cœur, échocardiographie). Elle fonctionne sans compte ni connexion. Nous l’avons conçue pour traiter le moins possible de données personnelles.',
 'sec': [
  ('Responsable du traitement', f'Le responsable est le fournisseur de l’application (voir <a href="impressum.html">mentions légales</a>). Contact : <a href="mailto:{MAIL}">{MAIL}</a>.'),
  ('Aucune collecte de données par l’application', 'L’application ne collecte aucune donnée personnelle et ne nous transmet aucune donnée. Il n’y a ni publicité, ni outils d’analyse ou de suivi, ni rapports de plantage envoyés à des tiers.'),
  ('Données sur votre appareil', 'La progression, les réglages et les fichiers que vous ajoutez vous-même (par ex. vos propres images d’ECG ou enregistrements de bruits du cœur) sont enregistrés uniquement sur votre appareil. Nous n’y avons pas accès. Si vous avez activé la sauvegarde Google dans les réglages Android, Android peut enregistrer votre progression dans votre sauvegarde Google ; cela relève de Google et de votre appareil, pas de nous. Vos propres fichiers sont exclus de la sauvegarde. Vous pouvez exporter un fichier vous-même via « Sauvegarder la progression » dans les réglages.'),
  ('Achats via Google Play', 'Les abonnements et l’achat unique sont gérés par Google Play. Seul Google reçoit les données de paiement. L’application apprend seulement si un achat existe afin de débloquer la version complète. La <a href="https://policies.google.com/privacy">politique de confidentialité de Google</a> s’applique.'),
  ('Connexion Internet', 'Tous les contenus sont inclus dans l’application et fonctionnent hors ligne. Une connexion n’est utilisée que pour les achats et leur restauration via Google Play, et lorsque vous ouvrez vous-même un lien (par ex. vers une recommandation ou une source), qui s’ouvre dans votre navigateur.'),
  ('Propositions de thèmes et enregistrements par e-mail', 'Si vous écrivez un e-mail via « Proposer un thème » ou « Proposer un enregistrement », votre messagerie s’ouvre ; l’application elle-même n’envoie rien. Nous utilisons votre adresse e-mail et votre message uniquement pour traiter votre demande et vous répondre ; les enregistrements envoyés ne sont utilisés dans l’application qu’avec votre accord (art. 6, par. 1, point f du RGPD) et les supprimons lorsqu’ils ne sont plus nécessaires.'),
  ('Autorisations', 'L’application utilise uniquement l’accès à Internet (pour les achats) et la facturation Google Play. Elle n’accède ni à l’appareil photo, ni au micro, ni à la localisation, ni aux contacts. Vous choisissez vous-même vos fichiers via le sélecteur de fichiers d’Android.'),
  ('Vos droits', 'Vous disposez d’un droit d’accès, de rectification, d’effacement, de limitation du traitement, de portabilité et d’opposition, ainsi que du droit d’introduire une réclamation auprès d’une autorité de contrôle.'),
  ('Public visé', 'L’application s’adresse aux adultes, en particulier aux étudiants en médecine, médecins et soignants. Elle ne remplace pas un avis médical.'),
  ('Modifications', 'Nous adaptons cette politique lorsque l’application ou la législation évoluent. La version publiée ici fait foi.')],
 'stand': 'Mise à jour'},
'es': {'title': 'Política de privacidad', 'intro': 'Corsinura es una aplicación para aprender cardiología (ECG, ruidos cardiacos, ecocardiografía). Funciona sin cuenta ni registro. La hemos diseñado para que se traten los menos datos personales posibles.',
 'sec': [
  ('Responsable', f'El responsable del tratamiento es el proveedor de la aplicación (ver <a href="impressum.html">aviso legal</a>). Contacto: <a href="mailto:{MAIL}">{MAIL}</a>.'),
  ('La aplicación no recoge datos', 'La aplicación no recoge datos personales ni nos envía ningún dato. No hay publicidad, herramientas de análisis o seguimiento ni informes de errores a terceros.'),
  ('Datos en tu dispositivo', 'El progreso, los ajustes y los archivos que añades tú mismo (p. ej., tus propias imágenes de ECG o grabaciones de ruidos cardiacos) se guardan solo en tu dispositivo. No tenemos acceso a ellos. Si has activado la copia de seguridad de Google en los ajustes de Android, Android puede guardar tu progreso en tu copia de seguridad de Google; esto lo controlan Google y tu dispositivo, no nosotros. Tus propios archivos quedan excluidos de la copia. Puedes exportar un archivo tú mismo con «Guardar progreso» en los ajustes.'),
  ('Compras a través de Google Play', 'Las suscripciones y la compra única se gestionan a través de Google Play. Solo Google recibe los datos de pago. La aplicación solo sabe si existe una compra para desbloquear la versión completa. Se aplica la <a href="https://policies.google.com/privacy">política de privacidad de Google</a>.'),
  ('Conexión a Internet', 'Todo el contenido está en la aplicación y funciona sin conexión. Solo se usa la conexión para las compras y su restauración en Google Play, y cuando abres tú mismo un enlace (p. ej., a una guía o fuente), que se abre en tu navegador.'),
  ('Peticiones de temas y grabaciones por correo', 'Si escribes un correo con «Pedir un tema» o «Aportar una grabación», se abre tu aplicación de correo; la aplicación en sí no envía nada. Usamos tu dirección de correo y tu mensaje solo para tramitar tu petición y responderte; las grabaciones que envíes solo se usan en la aplicación con tu consentimiento (art. 6.1.f del RGPD) y los borramos cuando ya no son necesarios.'),
  ('Permisos', 'La aplicación solo usa el acceso a Internet (para las compras) y la facturación de Google Play. No accede a la cámara, el micrófono, la ubicación ni los contactos. Tú eliges tus propios archivos con el selector de archivos de Android.'),
  ('Tus derechos', 'Tienes derecho de acceso, rectificación, supresión, limitación del tratamiento, portabilidad y oposición, así como a presentar una reclamación ante una autoridad de control.'),
  ('Destinatarios', 'La aplicación está dirigida a adultos, en particular a estudiantes de medicina, médicos y personal de enfermería. No sustituye el consejo médico.'),
  ('Cambios', 'Actualizamos esta política cuando cambian la aplicación o la ley. Se aplica la versión publicada aquí.')],
 'stand': 'Actualización'},
}
HOME = {
 'de': ('Kardiologie verstehen. Mit echten EKGs, Herztönen und Echos.', 'Lern-App für Android: über 1.300 echte 12-Kanal-EKGs, Herztöne mit Phonokardiogramm, Echo-Videos, interaktive Labore, Rechner und Scores, Fallbeispiele und Prüfungsmodus. Offline nutzbar, ohne Konto.', 'Datenschutzerklärung', 'Impressum', 'Kontakt'),
 'en': ('Understand cardiology. With real ECGs, heart sounds and echoes.', 'Learning app for Android: over 1,300 real 12-lead ECGs, heart sounds with phonocardiogram, echo videos, interactive labs, calculators and scores, clinical cases and exam mode. Works offline, no account.', 'Privacy policy', 'Legal notice', 'Contact'),
 'fr': ('Comprendre la cardiologie. Avec de vrais ECG, bruits du cœur et échos.', 'Application d’apprentissage pour Android : plus de 1 300 vrais ECG 12 dérivations, bruits du cœur avec phonocardiogramme, vidéos d’échographie, labos interactifs, calculateurs et scores, cas cliniques et mode examen. Hors ligne, sans compte.', 'Politique de confidentialité', 'Mentions légales', 'Contact'),
 'es': ('Entender la cardiología. Con ECG, ruidos cardiacos y ecos reales.', 'Aplicación de aprendizaje para Android: más de 1.300 ECG reales de 12 derivaciones, ruidos cardiacos con fonocardiograma, vídeos de eco, laboratorios interactivos, cálculos y escalas, casos clínicos y modo examen. Sin conexión y sin cuenta.', 'Política de privacidad', 'Aviso legal', 'Contacto'),
}
def page(title, body, lang='de'):
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"><link rel="icon" href="img/logo.png"></head>
<body><div class="wrap"><header><img src="img/logo.png" alt=""><a href="./">Corsinura</a></header>
{body}
</div></body></html>
'''
nav = '<nav class="lang">' + ''.join(f'<a href="#{l}">{NAMES[l]}</a>' for l in P) + '</nav>'
body = nav + ''.join(
    f'<section id="{l}" lang="{l}"><h1>{p["title"]}</h1><p>{p["intro"]}</p>' + ''.join(f'<h2>{h}</h2><p>{t}</p>' for h, t in p['sec']) + f'<p class="muted">{p["stand"]}{COL(l)}{DATE[l]}</p></section>'
    for l, p in P.items())
open('datenschutz.html', 'w').write(page('Corsinura: Datenschutz / Privacy', body))
body = nav + ''.join(
    f'<section id="{l}" lang="{l}"><h1>{h[0]}</h1><p>{h[1]}</p><footer><a href="datenschutz.html#{l}">{h[2]}</a><a href="impressum.html">{h[3]}</a><a href="mailto:{MAIL}">{h[4]}</a></footer></section>'
    for l, h in HOME.items())
open('index.html', 'w').write(page('Corsinura', body))
# Impressum / Kontakt (Adresse folgt am Ende der Alpha-Phase)
IMP = {
'de': ('Impressum', 'Anbieter', 'Kontakt', 'Schreib uns über das Formular oder per E-Mail.', 'Deine E-Mail-Adresse', 'Nachricht', 'Senden', 'Die Angaben aus dem Formular werden über den Dienst Formspree (Formspree Inc., USA) an uns weitergeleitet und nur zur Bearbeitung deiner Anfrage verwendet.'),
'en': ('Legal notice', 'Provider', 'Contact', 'Write to us using the form or by e-mail.', 'Your e-mail address', 'Message', 'Send', 'Form data is forwarded to us via the service Formspree (Formspree Inc., USA) and used only to handle your request.'),
'fr': ('Mentions légales', 'Éditeur', 'Contact', 'Écris-nous via le formulaire ou par e-mail.', 'Ton adresse e-mail', 'Message', 'Envoyer', 'Les données du formulaire nous sont transmises par le service Formspree (Formspree Inc., États-Unis) et utilisées uniquement pour traiter ta demande.'),
'es': ('Aviso legal', 'Responsable', 'Contacto', 'Escríbenos con el formulario o por correo.', 'Tu correo electrónico', 'Mensaje', 'Enviar', 'Los datos del formulario nos llegan a través del servicio Formspree (Formspree Inc., EE. UU.) y solo se usan para tramitar tu solicitud.')}
def form(l, i):
    if not FORM: return ''
    return (f'<form class="contact" action="https://formspree.io/f/{FORM}" method="POST"><label>{i[4]}<input type="email" name="email" required></label>'
            f'<label>{i[5]}<textarea name="message" rows="5" required></textarea></label><input type="hidden" name="_language" value="{l}"><button type="submit">{i[6]}</button></form><p class="muted">{i[7]}</p>')
body = nav + ''.join(
    f'<section id="{l}" lang="{l}"><h1>{i[0]}</h1><h2>{i[1]}</h2><p>{NAME}</p><h2>{i[2]}</h2><p>{i[3]}</p>{form(l, i)}<p>E-Mail{COL(l)}<a href="mailto:{MAIL}">{MAIL}</a></p></section>'
    for l, i in IMP.items())
open('impressum.html', 'w').write(page('Corsinura: Impressum / Legal notice', body))
print('ok')
