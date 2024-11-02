import flet as ft
import datetime
import os
import excell_generation

#TODO de revizuit codul
#TODO de facut prima build pe windows
#TODO de facut primul release pe web
#TODO salvare pe desktop
#TODO add icon
#TODO de securizat codul cu pyarmor



def main(page: ft.Page):

    #Page setting
    page.window.width = 1300
    page.window.height = 1000

    # Set the title of the app
    page.title = "Borderou MTC"
    # Set the theme mode to light
    page.theme_mode = ft.ThemeMode.LIGHT
    # Enable scrolling on the page
    page.scroll = "auto"

    #Objects declaration
    date_text_field = ft.TextField(label="Data", expand=True,read_only=True,bgcolor="lightgrey")
    date_picker = ft.DatePicker(expand=True)
    bancnote = ['1 leu', '5 lei', '10 lei', '20 lei', '50 lei', '100 lei', '200 lei', '500 lei', '1000 lei']
    bani = ['1 leu', '2 lei', '5 lei', '10 lei', '1 ban', '5 bani', '10 bani', '25 bani', '50 bani']
    bancnote_dict={'1 leu':1, '5 lei':5, '10 lei':10, '20 lei':20, '50 lei':50, '100 lei':100, '200 lei':200, '500 lei':500, '1000 lei':1000}
    bani_dict= {'1 leu':1, '2 lei':2, '5 lei':5, '10 lei':10, '1 ban':1, '5 bani':5, '10 bani':10, '25 bani':25, '50 bani':50}
    input_values = {}  # Dictionary to store input values

    # Function to calculate value multiplied by 4
    def calculate_value(event, text_field, result_field, multiplier):
        try:
            input_value = float(text_field.value) if text_field.value.strip() != "" else 0  # Treat empty input as 0
            result_field.value = str(round(input_value * multiplier, 2))  # Round to 2 decimal places
        except ValueError:
            result_field.value = "0"  # Treat invalid input as 0
        result_field.update()

    def calculate_sum(result_fields, sum_field):
        total_sum = 0
        for result_field in result_fields:
            try:
                total_sum += float(
                    result_field.value) if result_field.value.strip() != "" else 0  # Treat empty result as 0
            except ValueError:
                total_sum += 0  # Treat invalid result as 0
        sum_field.value = str(round(total_sum, 2))  # Round to 2 decimal places
        sum_field.update()

    def update_date_text(event):
        selected_date = event.control.value
        if selected_date:
            date_text_field.value = selected_date.strftime("%d.%m.%Y")  # Format date as YYYY-MM-DD
        else:
            date_text_field.value = ""  # Clear the TextField if no date is selected
        date_text_field.update()


    def store_input_values(e):
        input_values.clear()  # Clear any previous values
        for i, field in enumerate(
                container1_inputs + container1_results + container2_inputs + container3_inputs + container3_results + container4_fields + [
                    container1_sum_field, container3_sum_field]):
            input_values[f"input_{i}"] = field.value
       # input_values["date"] = date_text_field.value
        #print(input_values)  # Print values to verify, can be
        #generam excell file
        excell_generation.fill_excel_template(input_values)

        dialog = ft.AlertDialog(
            title=ft.Text("Success!"),
            content=ft.Text("Borderoul a fost generat pe desktop!"),
            on_dismiss=lambda e: page.update()
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

        # Function to clear all input fields except read-only fields

    def clear_all_inputs(event):
        for field in [date_text_field, *container1_inputs, *container2_inputs, *container3_inputs, *container4_fields,*container1_results,*container3_results,container3_sum_field,container1_sum_field]:
            if field.read_only and field in container4_fields:
                pass
            else:# Only clear fields that are not read-only
                field.value = ""
                field.update()

    def confirm_clear_all(event):
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmare Actiune"),
            content=ft.Text("Sunteti sigur ca doriti sa resetati borderoul?"),
            actions=[
                ft.TextButton("Da", on_click=lambda e: (clear_all_inputs(e), page.close(confirmation_dialog))),
                ft.TextButton("Renunta", on_click=lambda e: page.close(confirmation_dialog))

            ],
            on_dismiss=lambda e: page.update()
        )
        page.overlay.append(confirmation_dialog)
        confirmation_dialog.open = True
        page.update()


     #main code
    date_picker.on_change = update_date_text


    # Container 1: 9 input boxes with calculation
    container1_inputs = []
    container1_results = []
    container1_sum_field = ft.TextField(label="Total Bancnote MDL", read_only=True, expand=True, bgcolor="lightgray")
    for i in bancnote:  # Adjusted to 9 inputs
        input_field = ft.TextField(label=f"{i}", expand=True)
        result_field = ft.TextField(label="Total", read_only=True, expand=True,bgcolor="lightgray")
        multiplier = bancnote_dict[i]
        input_field.on_change = lambda e, inp=input_field, res=result_field, mult=multiplier: (calculate_value(e, inp,
                                                                                                              res, mult), calculate_sum(container1_results, container1_sum_field))

        container1_inputs.append(input_field)
        container1_results.append(result_field)

    container1 = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="BANCNOTE:", size=14, weight="bold"),  # Single label for the container
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=container1_inputs,
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True
                        ),
                        ft.Column(
                            controls=container1_results,
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True
                        ),

                    ],
                    spacing=10,
                    expand=True
                ),
                container1_sum_field
            ],
            spacing=5,
            auto_scroll=False  # Disable auto scrolling
        ),
        padding=10,
        height=600,  # Set fixed height for alignment
        border=ft.border.all(2, "black"),  # Border for the container
        border_radius=ft.border_radius.all(10),  # Rounded corners
        bgcolor="white",  # Background color for container
        expand=True  # Enable expansion for the container
    )

    # Container 2: 3 input boxes (without calculation)
    container2_inputs = [
        date_text_field,
        ft.TextField(label="Geanta nr.", expand=True),
        ft.TextField(label="Casier", expand=True)
    ]

    container2 = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="GEANTA:", size=14, weight="bold"),
                container2_inputs[0],
                ft.ElevatedButton(
                    "Pick date",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: page.open(
                        ft.DatePicker(
                            # first_date=datetime.datetime(year=2023, month=10, day=1),
                            # last_date=datetime.datetime(year=2024, month=10, day=1),
                            on_change=update_date_text,
                            # on_dismiss=handle_dismissal,
                        )
                    ),
                ),
                container2_inputs[1],
                container2_inputs[2],
            ],
            spacing=5,
            auto_scroll=False  # Disable auto scrolling
        ),
        padding=10,
        height=600,  # Set fixed height for alignment
        border=ft.border.all(2, "black"),  # Border for the container
        border_radius=ft.border_radius.all(10),  # Rounded corners
        bgcolor="white",  # Background color for container
        expand=True  # Enable expansion for the container
    )

    # Container 3: 9 input boxes with calculation
    container3_inputs = []
    container3_results = []
    container3_sum_field = ft.TextField(label="Total Monede MDL", read_only=True, expand=True, bgcolor="lightgray")
    for i in bani:  # Adjusted to 9 inputs
        input_field = ft.TextField(label=f"{i}", expand=True)
        result_field = ft.TextField(label="Total", read_only=True, expand=True,bgcolor="lightgray")

        # Event listener for input field changes
        if i.split(' ')[1] in ('bani','ban'):
             multiplier = round(bani_dict[i]/100,2)
        else:
             multiplier = bani_dict[i]
        input_field.on_change = lambda e, inp=input_field, res=result_field, mult=multiplier: (calculate_value(e, inp,
                                                                                                              res, mult), calculate_sum(container3_results, container3_sum_field))

        container3_inputs.append(input_field)
        container3_results.append(result_field)

    container3 = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="MONEDE", size=14, weight="bold"),  # Single label for the container
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=container3_inputs,
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True
                        ),
                        ft.Column(
                            controls=container3_results,
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                            expand=True
                        )
                    ],
                    spacing=10,
                    expand=True
                ),
                container3_sum_field
            ],
            spacing=5,
            auto_scroll=False  # Disable auto scrolling
        ),
        padding=10,
        height=600,  # Set fixed height for alignment
        border=ft.border.all(2, "black"),  # Border for the container
        border_radius=ft.border_radius.all(10),  # Rounded corners
        bgcolor="white",  # Background color for container
        expand=True  # Enable expansion for the container
    )
    container4_fields = [
        ft.TextField(label="Compania", expand=True, read_only=True, bgcolor="lightgray", value="Moldtelecom SA"),
        ft.TextField(label="Cod fiscal", expand=True, read_only=True, bgcolor="lightgray", value="1002600048836"),
        ft.TextField(label="Cont nr.", expand=True),
        ft.TextField(label="Locul", expand=True),
        ft.TextField(label="Subdiviziunea", expand=True),
        ft.TextField(label="tel.", expand=True)
    ]
    # Container 4: 9 input boxes divided into 2 columns (static layout)
    container4 = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="INFORMATIA GENERALA:", size=14, weight="bold"),  # Single label for the container
                ft.Row(
                    controls=[
                        ft.Column(controls=container4_fields[:3], expand=True),
                        ft.Column(controls=container4_fields[3:], expand=True)
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    expand=True
                )
            ],
            spacing=5,
            auto_scroll=False  # Disable auto scrolling
        ),
        padding=10,
        border=ft.border.all(2, "black"),  # Border for the container
        border_radius=ft.border_radius.all(10),  # Rounded corners
        bgcolor="white",  # Background color for container
        expand=True  # Enable expansion for the container
    )

    # Create a button for the footer
    generate_button = ft.ElevatedButton(
        text="Generare Borderou",
        on_click=store_input_values,  # Placeholder for on-click event
        width=300,  # Set button width
        height=60,   # Set button height
        elevation=7,
        bgcolor="#B7B7B7",
    )
    clear_button = ft.ElevatedButton(
        text="Curata Borderou",
        on_click=confirm_clear_all,
        width=150,
        height=60,
        elevation=7,
        bgcolor="#B7B7B7",
       # color="black"
    )


    footer_container = ft.Container(
        content=ft.Row(
            controls=[
                clear_button,    # Left-aligned button
                generate_button  # Right-aligned button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Space out buttons to opposite ends
            expand=True,
        ),
        padding=10,
    )

    # Layout with scrolling
    page.add(
        ft.Column(
            controls=[
                container4,  #info generala
                ft.Row(
                    controls=[
                        container2, #geanta
                        container1, #bancnote
                        container3 #monede
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    expand=True  # Make the row expand
                ),
                footer_container    # Add footer button
            ],
            spacing=20,
            scroll="auto"  # Enable scrolling on this column as well
        )
    )


# Run the app
ft.app(target=main)

