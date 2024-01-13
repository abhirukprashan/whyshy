import flet as ft
import json
import random


def main(page: ft.Page):
    page.title = "whyshy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    with open("dares.json", "r") as file:
        dares = json.load(file)

    def get_random_dare():
        return random.choice(dares)

    def handle_button_click(e):
        i = 1000
        for j in range(0,i):
            dare_lol.value = get_random_dare()
            page.update()
    dare_lol = ft.Text(value="Click to get a dare",weight=100 ,size=17,color='#000000')
    image = ft.Image(
                src="assets/icon.png",
                width=40,
                height=40,
                border_radius=ft.border_radius.all(100),
            )
    icon = ft.Icon(ft.icons.ALBUM)
    b = ft.ElevatedButton(text="Dare",
                          on_click=handle_button_click,
                          bgcolor='#FFFFFF',
                          color='#000000',
                          )
    card =  ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                        #leading=image,
                            subtitle=dare_lol,
                            title=ft.Text("WhyUshy?",weight=ft.FontWeight.W_900,color='#000000'),
                        ),
                    ]
                ),
                width=400,
                padding=10,
                #bgcolor='#FFFFFF',
                #border = ft.border.all(1, ft.colors.BLACK),
                #border_radius= ft.border_radius.all(30)
                #on_click=get_random_dare,
            ),
            color=ft.colors.WHITE,
            surface_tint_color=ft.colors.WHITE,
            elevation=2,
            shadow_color=ft.colors.BLACK,
        )
    shake_dector = ft.ShakeDetector(
        minimum_shake_count=2,
        shake_slop_time_ms=300,
        shake_count_reset_time_ms=1000,
        on_shake=handle_button_click,
         )
    page.overlay.append(shake_dector)
    page.bgcolor='#000000'
    page.add(
        ft.ResponsiveRow(
            [card,shake_dector],
            alignment=ft.CrossAxisAlignment.CENTER,  
        ),
        ft.Row(
            [b],
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
ft.app(target=main)
