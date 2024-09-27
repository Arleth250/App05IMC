import flet as ft
from flet_core.elevated_button import ElevatedButton


def main(page: ft.Page):
    page.title="Calculadora de IMC"
    page.bgcolor="purple"
    
    txtPeso=ft.TextField(label="Ingresa tu peso")
    txtAltura=ft.TextField(label="Ingresa tu altura")
    lblIMC=ft.Text(" Tu IMC es :")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png"
                width=200
                height=200
                
                )
    
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft,ElevatedButton(text="limpiar")
    
    page.add(
        ft.column(
                controls=[txtPeso,
                          txtAltura,
                      lblIMC
                    ],alignment="CENTER"),
        ft.Row()
    
    

ft.app(main)
