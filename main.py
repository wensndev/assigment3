# modüllerin import edilmesi
import os
import inquirer
from rich.console import Console
from rich.panel import Panel
from modul import power, factorial, gcd, lcm, is_prime, isNaN

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# sayı girişini tür kontrolü yaparak almak ve hatalı girişte tekrar sormak için fonksiyon
def get_number_input(prompt, number_type="float"):
    while True:
        value = console.input(f"[bold yellow]{prompt}: [/bold yellow]")
        # float veya int türünde bir sayı mı kontrolü
        if not isNaN(value, "int" if number_type == "int" else None):
            return int(value) if number_type == "int" else float(value)
        console.print("[red]Geçersiz giriş![/red]")

# işlem fonksiyonlarını çalıştırırken hata yakalama ve kullanıcıya bildirme
def execute_operation(operation_func):
    try:
        operation_func()
    # modülden dönen value error'ları yakalama
    except ValueError as e:
        console.print(f"[red]{e}[/red]\n")
    # beklenmeyen hatalar için genel hata yakalama
    except Exception as e:
        console.print(f"[red]Beklenmeyen bir hata oluştu: {e}[/red]\n")

# işlem fonksiyonları
def calculate_power():
    base = get_number_input("Taban değerini girin", "float")
    exponent = get_number_input("Üs değerini girin", "float")
    result = power(base, exponent)
    console.print(f"[bold green]Sonuç: {result}[/bold green]\n")

def calculate_factorial():
    while True:
        number = get_number_input("Faktöriyel için pozitif bir tam sayı girin", "int")
        if number >= 0:
            result = factorial(number)
            console.print(f"[bold green]Sonuç: {result}[/bold green]\n")
            break
        console.print("[red]Negatif sayı için faktöriyel hesaplanamaz![/red]")

def calculate_gcd():
    num1 = get_number_input("İlk sayıyı girin", "int")
    num2 = get_number_input("İkinci sayıyı girin", "int")
    result = gcd(num1, num2)
    console.print(f"[bold green]Sonuç: {result}[/bold green]\n")

def calculate_lcm():
    num1 = get_number_input("İlk sayıyı girin", "int")
    num2 = get_number_input("İkinci sayıyı girin", "int")
    result = lcm(num1, num2)
    console.print(f"[bold green]Sonuç: {result}[/bold green]\n")

def check_prime():
    number = get_number_input("Bir sayı girin", "int")
    is_prime_result = is_prime(number)
    message = f"Bu bir asal sayı{'dır' if is_prime_result else ' değildir'}!"
    color = "green" if is_prime_result else "red"
    console.print(f"[bold {color}]{message}[/bold {color}]\n")

# ana fonksiyon
def main():
    operations = {
        "Üs Hesaplama": calculate_power,
        "Faktöriyel Hesaplama": calculate_factorial,
        "En Büyük Ortak Bölen (GCD)": calculate_gcd,
        "En Küçük Ortak Kat (LCM)": calculate_lcm,
        "Asal Sayı Kontrolü": check_prime,
        "Çıkış": None
    }

    questions = [
        inquirer.List(
            "operation",
            message="Hangi matematiksel işlemi yapmak istersiniz?",
            choices=list(operations.keys())
        )
    ]

    # işlem seçim döngüsü
    while True:
        clear_screen()
        console.print(Panel("[bold blue]Matematiksel İşlem Sihirbazına Hoş Geldiniz![/bold blue]", expand=False))
        operation = inquirer.prompt(questions)["operation"]
        if operation == "Çıkış":
            console.print(Panel("[bold cyan]Çıkış yapılıyor...[/bold cyan]", expand=False))
            break
        execute_operation(operations[operation])
        console.input("\n[bold magenta]Devam etmek için Enter'a basın...[/bold magenta]")

if __name__ == "__main__":
    main()