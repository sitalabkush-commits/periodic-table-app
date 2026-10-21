import flet as ft

# কালার প্যালেট (সবুজ, গ্রে, সাদা এবং কালো)
BG_COLOR = "#000000"       # কালো (ব্যাকগ্রাউন্ড)
CARD_BG = "#1E1E1E"        # ডার্ক গ্রে (মৌলের কার্ড)
ACCENT_GREEN = "#00FF66"   # উজ্জ্বল সবুজ (হাইলাইট ও বর্ডার)
TEXT_WHITE = "#FFFFFF"     # সাদা (প্রধান টেক্সট)
TEXT_MUTED = "#B0B0B0"     # হালকা গ্রে (সাব-টেক্সট)

# পেরিওডিক টেবিলের প্রাথমিক মৌলসমূহের ডাটা
ELEMENTS = [
    {"symbol": "H", "name": "Hydrogen", "number": 1, "mass": "1.008", "category": "Nonmetal"},
    {"symbol": "He", "name": "Helium", "number": 2, "mass": "4.003", "category": "Noble Gas"},
    {"symbol": "Li", "name": "Lithium", "number": 3, "mass": "6.94", "category": "Alkali Metal"},
    {"symbol": "Be", "name": "Beryllium", "number": 4, "mass": "9.012", "category": "Alkaline Earth"},
    {"symbol": "B", "name": "Boron", "number": 5, "mass": "10.81", "category": "Metalloid"},
    {"symbol": "C", "name": "Carbon", "number": 6, "mass": "12.011", "category": "Nonmetal"},
    {"symbol": "N", "name": "Nitrogen", "number": 7, "mass": "14.007", "category": "Nonmetal"},
    {"symbol": "O", "name": "Oxygen", "number": 8, "mass": "15.999", "category": "Nonmetal"},
    {"symbol": "F", "name": "Fluorine", "number": 9, "mass": "18.998", "category": "Halogen"},
    {"symbol": "Ne", "name": "Neon", "number": 10, "mass": "20.180", "category": "Noble Gas"},
    {"symbol": "Na", "name": "Sodium", "number": 11, "mass": "22.990", "category": "Alkali Metal"},
    {"symbol": "Mg", "name": "Magnesium", "number": 12, "mass": "24.305", "category": "Alkaline Earth"},
    {"symbol": "Al", "name": "Aluminium", "number": 13, "mass": "26.982", "category": "Post-transition"},
    {"symbol": "Si", "name": "Silicon", "number": 14, "mass": "28.085", "category": "Metalloid"},
    {"symbol": "P", "name": "Phosphorus", "number": 15, "mass": "30.974", "category": "Nonmetal"},
    {"symbol": "S", "name": "Sulfur", "number": 16, "mass": "32.06", "category": "Nonmetal"},
    {"symbol": "Cl", "name": "Chlorine", "number": 17, "mass": "35.45", "category": "Halogen"},
    {"symbol": "Ar", "name": "Argon", "number": 18, "mass": "39.948", "category": "Noble Gas"},
]

def main(page: ft.Page):
    page.title = "Periodic Table App"
    page.bgcolor = BG_COLOR
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # টাইটেল
    header = ft.Text(
        "PERIODIC TABLE", 
        size=28, 
        weight=ft.FontWeight.BOLD, 
        color=ACCENT_GREEN
    )

    # মৌলের বিস্তারিত তথ্য দেখানোর জন্য ডিসপ্লে বক্স
    details_name = ft.Text("একটি মৌল নির্বাচন করুন", size=18, weight=ft.FontWeight.BOLD, color=TEXT_WHITE)
    details_info = ft.Text("উপরে বা তালিকার যেকোনো মৌলে ক্লিক করলে বিস্তারিত দেখাবে।", size=14, color=TEXT_MUTED)

    details_card = ft.Container(
        content=ft.Column(
            [details_name, details_info],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=CARD_BG,
        padding=15,
        border_radius=10,
        border=ft.border.all(1, ACCENT_GREEN),
        width=350,
        alignment=ft.alignment.center
    )

    # কার্ডে ক্লিক করলে তথ্য আপডেট করার ফাংশন
    def show_details(e, element):
        details_name.value = f"{element['name']} ({element['symbol']})"
        details_info.value = f"Atomic Number: {element['number']} | Mass: {element['mass']}\nCategory: {element['category']}"
        page.update()

    # গ্রিড লেআউট তৈরি
    grid = ft.GridView(
        runs_count=4,
        max_extent=90,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
        expand=False
    )

    # পেরিওডিক টেবিলের কার্ড তৈরি
    for el in ELEMENTS:
        card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(str(el["number"]), size=10, color=ACCENT_GREEN, weight=ft.FontWeight.BOLD),
                    ft.Text(el["symbol"], size=22, color=TEXT_WHITE, weight=ft.FontWeight.BOLD),
                    ft.Text(el["name"], size=9, color=TEXT_MUTED, no_wrap=True),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=CARD_BG,
            padding=6,
            border_radius=8,
            border=ft.border.all(1, "#333333"),
            ink=True,
            on_click=lambda e, item=el: show_details(e, item)
        )
        grid.controls.append(card)

    # পেজে সব এলিমেন্ট যোগ করা
    page.add(
        header,
        ft.Divider(color="#333333", height=20),
        details_card,
        ft.Container(height=15),
        grid
    )

ft.app(target=main)
