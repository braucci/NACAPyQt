![](/home/biagio/Insync/raucci@gmail.com/Google Drive/LinuxSwap/python/QtGragico/NACA4412.png)

I **profili alari NACA** sono particolari forme di profilo alare studiati dalla *National Advisory Committee for Aeronautics* (NACA) statunitense. La forma di un profilo alare NACA è descritta  mediante la parola “NACA” seguita da un numero. I valori presenti in  tale codice numerico possono essere inseriti nelle equazioni per  calcolare le proprietà della sezione alare.

Le sezioni alari NACA a quattro cifre definiscono il profilo in questo modo:

1. la prima cifra indica la curvatura massima come percentuale della corda;
2. la seconda cifra fornisce la distanza del punto di massima curvatura dal  bordo d’attacco espressa come percentuale della corda e in multipli di  10;
3. le ultime due cifre descrivono il massimo spessore del profilo alare espresso come percentuale della corda.

La distribuzione degli spessori, lungo la linea media è:

![img](https://i2.wp.com/www.raucci.net/wp-content/uploads/2021/10/Schermata-2021-10-29-alle-17.27.03.jpg?resize=585%2C49)

dove:

- *c* è la lunghezza della corda;
- *x* è la posizione lungo la corda da 0 a *c*;
- *yt* è metà dello spessore ad un dato valore di *x*;
- *t* è lo spessore massimo espresso come frazione della corda, in modo che 100 *t* sia uguale alle ultime due cifre del codice NACA.

Si noti che in questa equazione, a (*x*/*c*) = 1 (il  bordo d’uscita del profilo), lo spessore non è esattamente uguale a  zero. Se per motivi computazionali è necessario uno spessore nullo al  bordo d’uscita, si deve modificare uno dei coefficienti in modo che la  loro somma dia zero. Modificando l’ultimo coefficiente a −0,1036, ad  esempio, produrrà un piccolo cambiamento nella forma generale del  profilo. Il bordo d’attacco è approssimabile ad un cilindro con raggio  uguale a:

![{\displaystyle r=1{,}1019\,t^{2}.\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dc6cfe619a5c328ec695fe2b0b7a94be458cd978)

L’equazione della curvatura del profilo è:

![img](https://i2.wp.com/www.raucci.net/wp-content/uploads/2021/10/Schermata-2021-10-29-alle-17.31.55.jpg?resize=508%2C162)

dove:

- *m* è la massima curvatura espressa come percentuale della corda ed è la prima delle quattro cifre del codice;
- *p* è la posizione della massima curvatura, espressa in multipli di 10 e come percentuale della corda, ed è la seconda cifra del codice.

Qui si propone un codice per generare i profili NACA della serie a  quattro cifre sfruttando le potenzialità di Python e delle librerie  PyQt5 e Matplotlib.