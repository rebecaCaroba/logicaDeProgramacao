function quantidadeDeCedulas(n) {
    if (!(n < 1000000 && n > 0)) {
        console.log('Apenas números de 0 até 1.000.000')
        return
    }

    var resto = 0
    const notas100 = Math.trunc(n / 100)
    resto = n % 100

    const notas50 = Math.trunc(resto / 50) // 1
    resto = resto % 50

    const notas20 = Math.trunc(resto / 20)
    resto = resto % 20
    const notas10 = Math.trunc(resto / 10)
    resto = resto % 10
    const notas5 = Math.trunc(resto / 5)
    resto = resto % 5
    const notas2 = Math.trunc(resto / 2)
    resto = resto % 2
    const notas1 = Math.trunc(resto / 1)


    console.log(`
            ${notas100} nota(s) de R$ 100,00 \n
            ${notas50} nota(s) de R$ 50,00 \n
            ${notas20} nota(s) de R$ 20,00 \n
            ${notas10} nota(s) de R$ 10,00 \n
            ${notas5} nota(s) de R$ 5,00 \n
            ${notas2} nota(s) de R$ 2,00 \n
            ${notas1} nota(s) de R$ 1,00 \n
        `)

}

quantidadeDeCedulas(576)
