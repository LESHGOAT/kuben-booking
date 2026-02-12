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

Teknologivalg

Jeg planlegger å bruke:

Python

Flask (backend)

HTML/CSS (frontend)

JavaScript

MariaDB (database)

GitHub (versjonskontroll)

GitHub Projects (Kanban)

Valget av Flask og MariaDB gjør det mulig å lage en dynamisk løsning med databasekobling.

Plan for gjennomføring

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
____________________________________________________________________________________________________________________________________________________________________________________________________________________
Prosjektlogg – KUBEN_BOOKING
Uke 5 – Planlegging og idéutvikling

I uke 5 startet jeg med å planlegge prosjektet ordentlig før jeg begynte å kode. Jeg definerte problemet jeg ønsket å løse, nemlig at elever ikke har oversikt over hvilke rom som er booket på skolen. Dette gjør det vanskelig å planlegge aktiviteter eller arrangementer. Jeg bestemte meg derfor for å lage et bookingsystem der lærere kan booke rom, og elever kan se hva som er booket.

Jeg opprettet repository på GitHub og laget et Kanban-board for å strukturere arbeidet mitt. Der delte jeg prosjektet opp i mindre oppgaver som database, innlogging, booking-funksjon og sikkerhet. Dette gjorde at prosjektet føltes mer oversiktlig og mindre stressende.

Jeg planla også datamodellen og bestemte hvilke tabeller jeg trengte. Jeg valgte å lage tre hovedtabeller. users, rooms og bookings. Jeg måtte sette meg inn i hvordan foreign keys fungerer for å forstå hvordan tabellene skulle kobles sammen.

Uke 6 – Backend, database og innlogging

I uke 6 begynte jeg å jobbe med backend og databasen. Jeg opprettet MariaDB-database og laget tabellene jeg hadde planlagt. Deretter koblet jeg Flask-applikasjonen til databasen.

Det tok litt tid før alt fungerte. Jeg fikk blant annet feilmeldinger som “Column 'navn' cannot be null”. Dette gjorde at jeg måtte undersøke hvordan data ble sendt fra HTML-skjemaet til backend. Jeg oppdaget at navnene på input-feltene i HTML ikke stemte helt overens med det backend forventet. Etter å ha rettet dette fungerte registrering av bruker.

Jeg implementerte også innlogging med hashing av passord. Det var viktig for meg at passord ikke lagres i klartekst i databasen. Etter flere forsøk fikk jeg både registrering og innlogging til å fungere.

Jeg la også til en logg ut-knapp slik at brukeren kan avslutte økten sin på en sikker måte.

Denne delen av prosjektet lærte meg mye om hvordan frontend og backend må samsvare helt nøyaktig for at systemet skal fungere.

Uke 7 – Booking og rollebasert tilgang

I uke 7 begynte jeg å utvikle selve booking-funksjonen. Jeg laget først en oversikt over rom og bookinger slik at brukere kan se hva som er reservert.

Deretter implementerte jeg selve booking-funksjonen for lærere. Jeg sørget for at bookinger lagres i databasen og kobles til riktig bruker og riktig rom.

En viktig del av prosjektet var rollebasert tilgang. Jeg laget en løsning der studenter ikke kan booke rom, men kun se hva som er booket. Lærere derimot kan både se og opprette bookinger. Dette krevde at jeg sjekket brukertype i backend før booking ble gjennomført.

Jeg opplevde noen problemer underveis, spesielt med validering av skjema og tilgangskontroll. Noen ganger fungerte ikke begrensningen slik den skulle, og jeg måtte teste flere ganger før det ble riktig.

Refleksjon over arbeidsprosessen

Dette prosjektet var mer komplekst enn jeg først trodde. Det vanskeligste var samspillet mellom database, backend og frontend. Små feil, som feil navn på input-felter eller manglende verdier, kunne føre til store problemer.

Jeg lærte spesielt mye om:

Hvordan databaser kobles til en webapplikasjon

Hvordan rollebasert tilgang fungerer

Hvor viktig det er med strukturert planlegging

Hvordan feilsøking fungerer i praksis

Bruken av Kanban-board hjalp meg med å holde oversikt og jobbe systematisk. Når jeg støtte på problemer, måtte jeg lese feilmeldinger nøye og teste meg frem til løsninger.

Hvis jeg skulle gjort prosjektet på nytt, ville jeg brukt enda mer tid på å planlegge databasen helt i starten. Samtidig er jeg veldig fornøyd med at systemet fungerer fra registrering til innlogging og booking, med rollebegrensning og sikkerhet.
