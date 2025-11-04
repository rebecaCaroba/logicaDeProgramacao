function calcIdadeEmDias(dias) {
    var resto = 0

    const qtdAnos = Math.trunc(dias / 365)
    resto = dias % 365

    const qtdMes = Math.trunc(resto / 30)
    resto = resto % 30

    const qtdDias = resto

    console.log(`
            ${qtdAnos} ano(s)  \n
            ${qtdMes} mes(es) \n
            ${qtdDias} dia(s) \n
        `)
}

calcIdadeEmDias(30)

