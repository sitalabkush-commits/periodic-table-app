import flet as ft

# কালার প্যালেট (সবুজ, গ্রে, সাদা এবং কালো)
BG_COLOR = "#0A0A0A"       # ডিপ ব্ল্যাক ব্যাকগ্রাউন্ড
CARD_BG = "#161616"        # ডার্ক গ্রে কার্ড
ACCENT_GREEN = "#00FF66"   # ব্রাইট নিয়ন গ্রিন
BORDER_GRAY = "#2A2A2A"    # বর্ডার কালার
TEXT_WHITE = "#FFFFFF"     # হেডার টেক্সট
TEXT_MUTED = "#888888"     # সেকেন্ডারি টেক্সট

# পেরিওডিক টেবিলের সম্পূর্ণ ১১৮টি মৌল
ELEMENTS = [
    {"num": 1, "sym": "H", "name": "Hydrogen", "mass": "1.008", "cat": "Nonmetal"},
    {"num": 2, "sym": "He", "name": "Helium", "mass": "4.0026", "cat": "Noble Gas"},
    {"num": 3, "sym": "Li", "name": "Lithium", "mass": "6.94", "cat": "Alkali Metal"},
    {"num": 4, "sym": "Be", "name": "Beryllium", "mass": "9.0122", "cat": "Alkaline Earth"},
    {"num": 5, "sym": "B", "name": "Boron", "mass": "10.81", "cat": "Metalloid"},
    {"num": 6, "sym": "C", "name": "Carbon", "mass": "12.011", "cat": "Nonmetal"},
    {"num": 7, "sym": "N", "name": "Nitrogen", "mass": "14.007", "cat": "Nonmetal"},
    {"num": 8, "sym": "O", "name": "Oxygen", "mass": "15.999", "cat": "Nonmetal"},
    {"num": 9, "sym": "F", "name": "Fluorine", "mass": "18.998", "cat": "Halogen"},
    {"num": 10, "sym": "Ne", "name": "Neon", "mass": "20.180", "cat": "Noble Gas"},
    {"num": 11, "sym": "Na", "name": "Sodium", "mass": "22.990", "cat": "Alkali Metal"},
    {"num": 12, "sym": "Mg", "name": "Magnesium", "mass": "24.305", "cat": "Alkaline Earth"},
    {"num": 13, "sym": "Al", "name": "Aluminium", "mass": "26.982", "cat": "Post-Transition"},
    {"num": 14, "sym": "Si", "name": "Silicon", "mass": "28.085", "cat": "Metalloid"},
    {"num": 15, "sym": "P", "name": "Phosphorus", "mass": "30.974", "cat": "Nonmetal"},
    {"num": 16, "sym": "S", "name": "Sulfur", "mass": "32.06", "cat": "Nonmetal"},
    {"num": 17, "sym": "Cl", "name": "Chlorine", "mass": "35.45", "cat": "Halogen"},
    {"num": 18, "sym": "Ar", "name": "Argon", "mass": "39.948", "cat": "Noble Gas"},
    {"num": 19, "sym": "K", "name": "Potassium", "mass": "39.098", "cat": "Alkali Metal"},
    {"num": 20, "sym": "Ca", "name": "Calcium", "mass": "40.078", "cat": "Alkaline Earth"},
    {"num": 21, "sym": "Sc", "name": "Scandium", "mass": "44.956", "cat": "Transition Metal"},
    {"num": 22, "sym": "Ti", "name": "Titanium", "mass": "47.867", "cat": "Transition Metal"},
    {"num": 23, "sym": "V", "name": "Vanadium", "mass": "50.942", "cat": "Transition Metal"},
    {"num": 24, "sym": "Cr", "name": "Chromium", "mass": "51.996", "cat": "Transition Metal"},
    {"num": 25, "sym": "Mn", "name": "Manganese", "mass": "54.938", "cat": "Transition Metal"},
    {"num": 26, "sym": "Fe", "name": "Iron", "mass": "55.845", "cat": "Transition Metal"},
    {"num": 27, "sym": "Co", "name": "Cobalt", "mass": "58.933", "cat": "Transition Metal"},
    {"num": 28, "sym": "Ni", "name": "Nickel", "mass": "58.693", "cat": "Transition Metal"},
    {"num": 29, "sym": "Cu", "name": "Copper", "mass": "63.546", "cat": "Transition Metal"},
    {"num": 30, "sym": "Zn", "name": "Zinc", "mass": "65.38", "cat": "Transition Metal"},
    {"num": 31, "sym": "Ga", "name": "Gallium", "mass": "69.723", "cat": "Post-Transition"},
    {"num": 32, "sym": "Ge", "name": "Germanium", "mass": "72.630", "cat": "Metalloid"},
    {"num": 33, "sym": "As", "name": "Arsenic", "mass": "74.922", "cat": "Metalloid"},
    {"num": 34, "sym": "Se", "name": "Selenium", "mass": "78.971", "cat": "Nonmetal"},
    {"num": 35, "sym": "Br", "name": "Bromine", "mass": "79.904", "cat": "Halogen"},
    {"num": 36, "sym": "Kr", "name": "Krypton", "mass": "83.798", "cat": "Noble Gas"},
    {"num": 37, "sym": "Rb", "name": "Rubidium", "mass": "85.468", "cat": "Alkali Metal"},
    {"num": 38, "sym": "Sr", "name": "Strontium", "mass": "87.62", "cat": "Alkaline Earth"},
    {"num": 39, "sym": "Y", "name": "Yttrium", "mass": "88.906", "cat": "Transition Metal"},
    {"num": 40, "sym": "Zr", "name": "Zirconium", "mass": "91.224", "cat": "Transition Metal"},
    {"num": 41, "sym": "Nb", "name": "Niobium", "mass": "92.906", "cat": "Transition Metal"},
    {"num": 42, "sym": "Mo", "name": "Molybdenum", "mass": "95.95", "cat": "Transition Metal"},
    {"num": 43, "sym": "Tc", "name": "Technetium", "mass": "98", "cat": "Transition Metal"},
    {"num": 44, "sym": "Ru", "name": "Ruthenium", "mass": "101.07", "cat": "Transition Metal"},
    {"num": 45, "sym": "Rh", "name": "Rhodium", "mass": "102.91", "cat": "Transition Metal"},
    {"num": 46, "sym": "Pd", "name": "Palladium", "mass": "106.42", "cat": "Transition Metal"},
    {"num": 47, "sym": "Ag", "name": "Silver", "mass": "107.87", "cat": "Transition Metal"},
    {"num": 48, "sym": "Cd", "name": "Cadmium", "mass": "112.41", "cat": "Transition Metal"},
    {"num": 49, "sym": "In", "name": "Indium", "mass": "114.82", "cat": "Post-Transition"},
    {"num": 50, "sym": "Sn", "name": "Tin", "mass": "118.71", "cat": "Post-Transition"},
    {"num": 51, "sym": "Sb", "name": "Antimony", "mass": "121.76", "cat": "Metalloid"},
    {"num": 52, "sym": "Te", "name": "Tellurium", "mass": "127.60", "cat": "Metalloid"},
    {"num": 53, "sym": "I", "name": "Iodine", "mass": "126.90", "cat": "Halogen"},
    {"num": 54, "sym": "Xe", "name": "Xenon", "mass": "131.29", "cat": "Noble Gas"},
    {"num": 55, "sym": "Cs", "name": "Caesium", "mass": "132.91", "cat": "Alkali Metal"},
    {"num": 56, "sym": "Ba", "name": "Barium", "mass": "137.33", "cat": "Alkaline Earth"},
    {"num": 57, "sym": "La", "name": "Lanthanum", "mass": "138.91", "cat": "Lanthanide"},
    {"num": 58, "sym": "Ce", "name": "Cerium", "mass": "140.12", "cat": "Lanthanide"},
    {"num": 59, "sym": "Pr", "name": "Praseodymium", "mass": "140.91", "cat": "Lanthanide"},
    {"num": 60, "sym": "Nd", "name": "Neodymium", "mass": "144.24", "cat": "Lanthanide"},
    {"num": 61, "sym": "Pm", "name": "Promethium", "mass": "145", "cat": "Lanthanide"},
    {"num": 62, "sym": "Sm", "name": "Samarium", "mass": "150.36", "cat": "Lanthanide"},
    {"num": 63, "sym": "Eu", "name": "Europium", "mass": "151.96", "cat": "Lanthanide"},
    {"num": 64, "sym": "Gd", "name": "Gadolinium", "mass": "157.25", "cat": "Lanthanide"},
    {"num": 65, "sym": "Tb", "name": "Terbium", "mass": "158.93", "cat": "Lanthanide"},
    {"num": 66, "sym": "Dy", "name": "Dysprosium", "mass": "162.50", "cat": "Lanthanide"},
    {"num": 67, "sym": "Ho", "name": "Holmium", "mass": "164.93", "cat": "Lanthanide"},
    {"num": 68, "sym": "Er", "name": "Erbium", "mass": "167.26", "cat": "Lanthanide"},
    {"num": 69, "sym": "Tm", "name": "Thulium", "mass": "168.93", "cat": "Lanthanide"},
    {"num": 70, "sym": "Yb", "name": "Ytterbium", "mass": "173.05", "cat": "Lanthanide"},
    {"num": 71, "sym": "Lu", "name": "Lutetium", "mass": "174.97", "cat": "Lanthanide"},
    {"num": 72, "sym": "Hf", "name": "Hafnium", "mass": "178.49", "cat": "Transition Metal"},
    {"num": 73, "sym": "Ta", "name": "Tantalum", "mass": "180.95", "cat": "Transition Metal"},
    {"num": 74, "sym": "W", "name": "Tungsten", "mass": "183.84", "cat": "Transition Metal"},
    {"num": 75, "sym": "Re", "name": "Rhenium", "mass": "186.21", "cat": "Transition Metal"},
    {"num": 76, "sym": "Os", "name": "Osmium", "mass": "190.23", "cat": "Transition Metal"},
    {"num": 77, "sym": "Ir", "name": "Iridium", "mass": "192.22", "cat": "Transition Metal"},
    {"num": 78, "sym": "Pt", "name": "Platinum", "mass": "195.08", "cat": "Transition Metal"},
    {"num": 79, "sym": "Au", "name": "Gold", "mass": "196.97", "cat": "Transition Metal"},
    {"num": 80, "sym": "Hg", "name": "Mercury", "mass": "200.59", "cat": "Transition Metal"},
    {"num": 81, "sym": "Tl", "name": "Thallium", "mass": "204.38", "cat": "Post-Transition"},
    {"num": 82, "sym": "Pb", "name": "Lead", "mass": "207.2", "cat": "Post-Transition"},
    {"num": 83, "sym": "Bi", "name": "Bismuth", "mass": "208.98", "cat": "Post-Transition"},
    {"num": 84, "sym": "Po", "name": "Polonium", "mass": "209", "cat": "Post-Transition"},
    {"num": 85, "sym": "At", "name": "Astatine", "mass": "210", "cat": "Halogen"},
    {"num": 86, "sym": "Rn", "name": "Radon", "mass": "222", "cat": "Noble Gas"},
    {"num": 87, "sym": "Fr", "name": "Francium", "mass": "223", "cat": "Alkali Metal"},
    {"num": 88, "sym": "Ra", "name": "Radium", "mass": "226", "cat": "Alkaline Earth"},
    {"num": 89, "sym": "Ac", "name": "Actinium", "mass": "227", "cat": "Actinide"},
    {"num": 90, "sym": "Th", "name": "Thorium", "mass": "232.04", "cat": "Actinide"},
    {"num": 91, "sym": "Pa", "name": "Protactinium", "mass": "231.04", "cat": "Actinide"},
    {"num": 92, "sym": "U", "name": "Uranium", "mass": "238.03", "cat": "Actinide"},
    {"num": 93, "sym": "Np", "name": "Neptunium", "mass": "237", "cat": "Actinide"},
    {"num": 94, "sym": "Pu", "name": "Plutonium", "mass": "244", "cat": "Actinide"},
    {"num": 95, "sym": "Am", "name": "Americium", "mass": "243", "cat": "Actinide"},
    {"num": 96, "sym": "Cm", "name": "Curium", "mass": "247", "cat": "Actinide"},
    {"num": 97, "sym": "Bk", "name": "Berkelium", "mass": "247", "cat": "Actinide"},
    {"num": 98, "sym": "Cf", "name": "Californium", "mass": "251", "cat": "Actinide"},
    {"num": 99, "sym": "Es", "name": "Einsteinium", "mass": "252", "cat": "Actinide"},
    {"num": 100, "sym": "Fm", "name": "Fermium", "mass": "257", "cat": "Actinide"},
    {"num": 101, "sym": "Md", "name": "Mendelevium", "mass": "258", "cat": "Actinide"},
    {"num": 102, "sym": "No", "name": "Nobelium", "mass": "259", "cat": "Actinide"},
    {"num": 103, "sym": "Lr", "name": "Lawrencium", "mass": "266", "cat": "Actinide"},
    {"num": 104, "sym": "Rf", "name": "Rutherfordium", "mass": "267", "cat": "Transition Metal"},
    {"num": 105, "sym": "Db", "name": "Dubnium", "mass": "268", "cat": "Transition Metal"},
    {"num": 106, "sym": "Sg", "name": "Seaborgium", "mass": "269", "cat": "Transition Metal"},
    {"num": 107, "sym": "Bh", "name": "Bohrium", "mass": "270", "cat": "Transition Metal"},
    {"num": 108, "sym": "Hs", "name": "Hassium", "mass": "277", "cat": "Transition Metal"},
    {"num": 109, "sym": "Mt", "name": "Meitnerium", "mass": "278", "cat": "Transition Metal"},
    {"num": 110, "sym": "Ds", "name": "Darmstadtium", "mass": "281", "cat": "Transition Metal"},
    {"num": 111, "sym": "Rg", "name": "Roentgenium", "mass": "282", "cat": "Transition Metal"},
    {"num": 112, "sym": "Cn", "name": "Copernicium", "mass": "285", "cat": "Transition Metal"},
    {"num": 113, "sym": "Nh", "name": "Nihonium", "mass": "286", "cat": "Post-Transition"},
    {"num": 114, "sym": "Fl", "name": "Flerovium", "mass": "289", "cat": "Post-Transition"},
    {"num": 115, "sym": "Mc", "name": "Moscovium", "mass": "290", "cat": "Post-Transition"},
    {"num": 116, "sym": "Lv", "name": "Livermorium", "mass": "293", "cat": "Post-Transition"},
    {"num": 117, "sym": "Ts", "name": "Tennessine", "mass": "294", "cat": "Halogen"},
    {"num": 118, "sym": "Og", "name": "Oganesson", "mass": "294", "cat": "Noble Gas"}
]

def main(page: ft.Page):
    page.title = "Periodic Table"
    page.bgcolor = BG_COLOR
    page.padding = 15
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("PERIODIC TABLE", size=24, weight=ft.FontWeight.BOLD, color=ACCENT_GREEN)

    # ডিটেইলস প্যানেল
    det_sym = ft.Text("H", size=36, weight=ft.FontWeight.BOLD, color=ACCENT_GREEN)
    det_name = ft.Text("Hydrogen", size=20, weight=ft.FontWeight.BOLD, color=TEXT_WHITE)
    det_num = ft.Text("Atomic Number: 1", size=13, color=TEXT_MUTED)
    det_mass = ft.Text("Atomic Mass: 1.008", size=13, color=TEXT_MUTED)
    det_cat = ft.Text("Category: Nonmetal", size=13, color=TEXT_MUTED)

    details_card = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=det_sym,
                    alignment=ft.alignment.center,
                    width=70,
                    height=70,
                    border=ft.border.all(2, ACCENT_GREEN),
                    border_radius=10,
                    bgcolor=CARD_BG
                ),
                ft.Column([det_name, det_num, det_mass, det_cat], spacing=2)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
        padding=15,
        bgcolor=CARD_BG,
        border=ft.border.all(1, BORDER_GRAY),
        border_radius=12,
        width=360
    )

    def select_element(e, el):
        det_sym.value = el["sym"]
        det_name.value = el["name"]
        det_num.value = f"Atomic Number: {el['num']}"
        det_mass.value = f"Atomic Mass: {el['mass']}"
        det_cat.value = f"Category: {el['cat']}"
        page.update()

    # গ্রিড তৈরি
    grid = ft.GridView(
        runs_count=5,
        max_extent=70,
        child_aspect_ratio=1.0,
        spacing=8,
        run_spacing=8,
        expand=False
    )

    for el in ELEMENTS:
        card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(str(el["num"]), size=9, color=ACCENT_GREEN, weight=ft.FontWeight.BOLD),
                    ft.Text(el["sym"], size=18, color=TEXT_WHITE, weight=ft.FontWeight.BOLD),
                    ft.Text(el["name"], size=7, color=TEXT_MUTED, no_wrap=True),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=CARD_BG,
            padding=4,
            border_radius=6,
            border=ft.border.all(1, BORDER_GRAY),
            ink=True,
            on_click=lambda e, item=el: select_element(e, item)
        )
        grid.controls.append(card)

    page.add(
        title,
        ft.Container(height=5),
        details_card,
        ft.Container(height=15),
        grid
    )

ft.app(target=main)
