$:.push('gen-rb')

require 'thrift'
require 'calculadora_remota_servicio'
require 'calculadora_remota_types'

class CalculadoraRemotaHandler

    def RealizarAdicion(enteroA, enteroB)
            resultado = Resultado.new
            resultado.resultadoOperacion = enteroA + enteroB
            puts "[Servidor] Adición realizada"
        return resultado
    end

    def RealizarSubstraccion(enteroA, enteroB)
            resultado = Resultado.new
            resultado.resultadoOperacion = enteroA - enteroB
            puts "[Servidor] Substracción realizada"
        return resultado
    end  
    
    def RealizarMultiplicacion(enteroA, enteroB)
        resultado = Resultado.new
        resultado.resultadoOperacion = enteroA * enteroB
        puts "[Servidor] Multiplicación realizada"
        return resultado
    end


    def RealizarDivision(enteroA, enteroB)
        resultado = Resultado.new
        if enteroB == 0
            resultado.resultadoOperacion = 0
            resultado.mensaje = "Aquí se permite dividir entre 0, crack"
            puts "[Servidor] Error de división"
        else
            resultado.resultadoOperacion = enteroA / enteroB
            puts "[Servidor] División realizada"
        end
        return resultado
    end

end

handler = CalculadoraRemotaHandler.new()
processor = CalculadoraRemotaServicio::Processor.new(handler)
transporte = Thrift::ServerSocket.new(8080)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transporte, transportFactory)

puts "[Servidor] Iniciado, compadre"
server.serve()
