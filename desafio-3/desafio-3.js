let INDICE = 12;
let SOMA = 0;
let K = 1;

while (K < INDICE) {
    console.log("interacao " + K + "\n" + SOMA);
    K = K + 1;
    SOMA = SOMA + K;
}

console.log("valor apos a interacao final: " + SOMA);
