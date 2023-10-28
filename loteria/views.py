from django.shortcuts import render
import random
from django.http import JsonResponse
from django.db.models import Count, Q, Sum, Subquery, F, ExpressionWrapper, IntegerField, FloatField
from django.db import transaction

from django.views import View
from loteria.models import *

class Juego(View):
    def genera_tabla(self):
        # Generar 20 números enteros aleatorios únicos entre 1 y 54
        random_numbers_unique = random.sample(range(1, 55), 20)

        # Generar 30 listas diferentes con números aleatorios únicos y ordenarlas en orden ascendente
        listas = [sorted(random.sample(range(1, 55), 20)) for _ in range(200)]

        for index, lst in enumerate(listas, start=1):
            print(f"Lista {index}: {lst}")
        
        return listas

    def get(self, request):
        listas_generadas = self.genera_tabla()
        context = {}
        context['loterias'] = listas_generadas
        return render(request, 'loteria/loterias.html', context)
    
class Bingo(View):
    def generar_tarjeta(self):
        # Generar una tarjeta de bingo única (5x5) con números aleatorios
        tarjeta = []
        for i in range(5):
            column = random.sample(range(i*15+1, i*15+16), 5)
            tarjeta.append(column)
        tarjeta[2][2] = "FREE"  # Agregar el espacio central como espacio gratuito
        return tarjeta

    def transponer_tarjeta(self, tarjeta):
        # Transponer la tarjeta
        tarjeta_transpuesta = list(map(list, zip(*tarjeta)))
        return tarjeta_transpuesta

    def get(self, request):
        cliente_tablas = Cliente_comanda.objects.all().values('cliente').aggregate(total_tablas=Sum('cantidad'))
        total_tablas = cliente_tablas['total_tablas']

        tarjetas_de_bingo = [self.generar_tarjeta() for _ in range(total_tablas)]

        tarjetas_transpuestas = [self.transponer_tarjeta(tarjeta) for tarjeta in tarjetas_de_bingo]

        cliente_comandas = Cliente_comanda.objects.values('cliente__id').annotate(total_tablas=Sum('cantidad'))

        Tabla_bingo.objects.all().delete()

        with transaction.atomic():
            for i, tarjeta in enumerate(tarjetas_transpuestas, start=1):
                print(f"Tarjeta {i}:")
                tabla = Tabla_bingo()
                y = 0
                for row in tarjeta:
                    y += 1
                    if y == 1:
                        tabla.tabla_numero = i
                        tabla.num1=row[0]
                        tabla.num2=row[1]
                        tabla.num3=row[2]
                        tabla.num4=row[3]
                        tabla.num5=row[4]
                    elif y == 2:
                        tabla.num6=row[0]
                        tabla.num7=row[1]
                        tabla.num8=row[2]
                        tabla.num9=row[3]
                        tabla.num10=row[4]
                    elif y == 3:
                        tabla.num11=row[0]
                        tabla.num12=row[1]
                        tabla.num13=row[3]
                        tabla.num14=row[4]
                    elif y == 4:
                        tabla.num15=row[0]
                        tabla.num16=row[1]
                        tabla.num17=row[2]
                        tabla.num18=row[3]
                        tabla.num19=row[4]
                    else:
                        tabla.num20=row[0]
                        tabla.num21=row[1]
                        tabla.num22=row[2]
                        tabla.num23=row[3]
                        tabla.num24=row[4]
                    print(row)
                tabla.save()
                print("\n")

        context = {}
        context['bingos'] = tarjetas_transpuestas
        return render(request, 'loteria/bingo.html', context)

def obtener_numeros_bingo(request):
    sorteos = Sorteo.objects.all()
    numeros = [sorteo.numero for sorteo in sorteos]
    return JsonResponse({'numeros': numeros})        

