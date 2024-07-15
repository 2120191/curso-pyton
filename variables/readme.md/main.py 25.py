
horarios_disponibles = ["10:00", "12:00", "14:00", "16:00", "18:00"]
print("Horarios disponibles:")
for horario in horarios_disponibles:
    print("-", horario)
horario_reserva = input("Ingrese el horario deseado para la reserva: ")
if horario_reserva in horarios_disponibles:

    costo_alquiler = 50
    confirmacion = input("¿Desea reservar el horario " + horario_reserva + " por $" + str(costo_alquiler) + "? (Sí/No): ")

    if confirmacion.lower() == "sí":
    
        fecha_reserva = "25 de junio de 2023"
    # mostarar detalles de la reserva
    
        print("\nDetalles de la reserva:")
        print("Fecha de la reserva:", fecha_reserva)
        print("Hora de la reserva:", horario_reserva)
        print("Costo de la reserva: $" + str(costo_alquiler))

        
        confirmacion_pago = input("¿Desea realizar el pago ahora? (Sí/No): ")
        if confirmacion_pago.lower() == "sí":
            print("Pago realizado con éxito. ¡Reserva completada!")
        else:
            print("La reserva ha sido cancelada. Gracias por su interés.")
    else:
        print("Reserva cancelada. Gracias por su interés.")
else:
    print("El horario seleccionado no está disponible. Por favor, elija otro horario.")


## trabajo hoy:

horarios_disponibles = ["9:00 AM", "11:00 AM", "2:00 PM"]
print("Horarios Disponibles:")
for horario in horarios_disponibles:
    print(horario)
horario_elegido = input("Ingrese el horario deseado para la reserva: ")
print("Ha reservado el horario:", horario_elegido)
fecha_reserva = "2024-05-23"
hora_reserva = "9:00 AM"
costo_reserva = 50

print("Detalles de la reserva:")
print("Fecha:", fecha_reserva)
print("Hora:", hora_reserva)
print("Costo:", costo_reserva)

confirmacion_pago = input("¿Desea confirmar el pago? (Sí/No): ")
if confirmacion_pago.lower() == "sí":
    print("El pago se ha realizado con éxito.")
else:
    print("La reserva no ha sido pagada.")
