struct Resultado {
    1: i32 resultadoOperacion
    2: string mensaje
}

service CalculadoraRemotaServicio {
    Resultado RealizarAdicion(1: i32 enteroA, 2: i32 enteroB)
    Resultado RealizarSubstraccion(1: i32 enteroA, 2: i32 enteroB)
    Resultado RealizarMultiplicacion(1: i32 enteroA, 2: i32 enteroB)
    Resultado RealizarDivision(1: i32 enteroA, 2: i32 enteroB)
}