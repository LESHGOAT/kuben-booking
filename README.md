KUBEN_BOOKING
IT-utviklingsprosjekt – 2IMI

Navn: Omar Dakhil
Periode: Uke 5–7
Skole: Kuben VGS

Prosjektidé

Jeg ønsker å utvikle et rombookingsystem for Kuben VGS.

I dag har elever lite oversikt over hvilke rom som er booket og når de er ledige. Dette gjør det vanskelig å planlegge aktiviteter som gruppearbeid, møter eller arrangementer. Lærere trenger også en enkel og oversiktlig måte å booke rom på.

Målet med prosjektet er å lage en webapplikasjon der:

Lærere kan booke rom

Elever kan se hvilke rom som er booket

Systemet lagrer all informasjon i en database

Mål for prosjektet

Målet er å:

Lage en fungerende webapplikasjon med frontend og backend

Koble løsningen til en MariaDB-database

Lage et rollebasert system (student og lærer)

Sørge for sikker innlogging

Bruke GitHub og Kanban til å planlegge og strukturere arbeidet

Jeg ønsker at løsningen skal være realistisk og kunne brukes av en skole i praksis.

Målgruppe

Elever ved Kuben VGS

Lærere ved Kuben VGS

Systemet skal være enkelt å bruke og gi tydelig oversikt over rom og bookinger.

Planlagte funksjoner
Brukersystem

Registrering av bruker

Innlogging

Ulike roller (student og lærer)

Roller

Student:

Kan se hvilke rom som er booket

Kan ikke booke selv

Lærer:

Kan booke rom

Kan se egne bookinger

Booking

Velge rom

Velge dato

Velge tidspunkt

Lagre booking i database

Hindre dobbeltbooking

Ekstra (hvis tid)

Slette egne bookinger

Admin-rolle

Sikkerhetsforbedringer

Planlagt datamodell

Jeg planlegger å bruke MariaDB med flere tabeller som henger sammen.

users

id

navn

brukertype (student/lærer)

email

password

rooms

id

navn

bookings

id

user_id (koblet til users)

room_id (koblet til rooms)

start_time

end_time

Databasen skal bruke relasjoner (foreign keys) slik at data henger riktig sammen.

⚙️ Teknologivalg

Jeg planlegger å bruke:

Python

Flask (backend)

HTML/CSS (frontend)

JavaScript

MariaDB (database)

GitHub (versjonskontroll)

GitHub Projects (Kanban)

Valget av Flask og MariaDB gjør det mulig å lage en dynamisk løsning med databasekobling.

🗂 Plan for gjennomføring

Prosjektet skal deles opp i mindre oppgaver ved hjelp av Kanban-board i GitHub.

Eksempel på oppgaver:

Lage database

Lage tabeller

Lage innlogging

Lage registrering

Lage visning av rom

Lage booking-funksjon

Teste systemet

Skrive dokumentasjon

Jeg skal flytte oppgaver fra "To do" → "In progress" → "Done" underveis.

Forventede utfordringer

Jeg forventer at følgende kan bli utfordrende:

Koble frontend til backend

Håndtere dato og tid riktig

Lage rollebasert tilgang

Hindre dobbeltbooking

Strukturere databasen riktig

 Videre utvikling (hvis prosjektet utvides)

Admin-panel

Kalender-visning

E-postbekreftelse ved booking

Bedre design og brukeropplevelse

Mer avansert sikkerhet
