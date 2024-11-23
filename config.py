import customtkinter as ctk
import json
import os
from tkinter import ttk
import requests
import webbrowser

def aplicar_tema_claro():
    from modo_claro import menu_claro
    menu_claro()

def aplicar_tema_escuro():
    from modo_escuro import menu_escuro
    menu_escuro()
        
def cancelar():
    janela.withdraw()
    carregar_preferencias()
    
def salvar_preferencias():
    preferencias = {
        "tema": tema_var.get(),
        "check": check_var.get(),
    }
    with open("preferencias.json", "w") as arquivo:
        json.dump(preferencias, arquivo, indent=4)
    status_label.configure(text="Preferências salvas", text_color="green")

def carregar_preferencias():
    if not os.path.exists("preferencias.json"):
        preferencias_padrao = {
    "tema": "Claro", 
    "check": 0,
    "Texto 1": {
        "titulo": "Resposta 1",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 2": {
        "titulo": "Resposta 2",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 3": {
        "titulo": "Resposta 3",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 4": {
        "titulo": "Resposta 4",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 5": {
        "titulo": "Resposta 5",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 6": {
        "titulo": "Resposta 6",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 7": {
        "titulo": "Resposta 7",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 8": {
        "titulo": "Resposta 8",
        "conteudo": "Salve seu texto aqui! Utilize o bot\u00e3o salvar."
    },
    "Texto 9": {
        "titulo": "Reposi\u00e7\u00e3o",
        "conteudo": "Prezado CFC, a  reposi\u00e7\u00e3o \u00e9 feita pelo pr\u00f3prio CFC atrav\u00e9s da matricula do candidato. O suporte interv\u00e9m apenas em caso de erro ou reposi\u00e7\u00f5es referente a aluno de reciclagem.\n\nLink para orienta\u00e7\u00f5es: https://www.loom.com/share/d76f3b6db0c548ce8a78c28161609f8b\n\nAparece algum erro ao tentar repor?"
    },
    "Texto 10": {
        "titulo": "Inserir em Turma",
        "conteudo": "Prezado CFC, o agendamento na turma \u00e9 feita pelo pr\u00f3prio CFC. O suporte interv\u00e9m apenas em caso de erro. Aparece algum erro ao tentar agendar?\n\nLink para orienta\u00e7\u00f5es de como agendar: https://www.loom.com/share/f728f746277f48688bcc65f22fdfa04b"
    },
    "Texto 11": {
        "titulo": "Instabilidade Sindauto",
        "conteudo": "Pedimos desculpas pelos transtorno causados, estamos passando por uma instabilidade na plataforma. Estamos cientes de como esta situa\u00e7\u00e3o pode impactar a sua experi\u00eancia e queremos assegurar que nossa equipe t\u00e9cnica est\u00e1 trabalhando intensivamente para resolver o problema o mais r\u00e1pido poss\u00edvel.\n\nA nossa prioridade \u00e9 garantir a continuidade e a qualidade dos servi\u00e7os prestados. Agradecemos a vossa compreens\u00e3o neste momento. Caso tenham alguma d\u00favida ou precisem de suporte adicional basta nos informar."
    },
    "Texto 12": {
        "titulo": "Instabilidade Renova",
        "conteudo": "Pedimos desculpas pelos transtorno causados, estamos passando por uma instabilidade na plataforma. Estamos No momento estamos enfrentando instabilidade na plataforma de aulas Renova. Pedimos desculpa pelo acontecido e informamos que os desenvolvedores j\u00e1 est\u00e3o trabalhando para corre\u00e7\u00e3o.Caso tenham alguma d\u00favida ou precisem de suporte adicional, por favor, entre em contato com o suporte Renova:  wa.me/71999868062"
    }
}
        with open("preferencias.json", "w") as arquivo:
            json.dump(preferencias_padrao, arquivo, indent=4)
        status_label.configure(text="Preferências padrão criadas.", text_color="red")
        aplicar_preferencias(preferencias_padrao)
    else:
        try:
            with open("preferencias.json", "r") as arquivo:
                preferencias = json.load(arquivo)
                aplicar_preferencias(preferencias)
        except (json.JSONDecodeError, ValueError):
            preferencias_padrao = {"tema": "Claro", "check": 0}
            with open("preferencias.json", "w") as arquivo:
                json.dump(preferencias_padrao, arquivo, indent=4)
            status_label.configure(text="Arquivo corrompido, preferências padrão aplicadas.", text_color="red")
            aplicar_preferencias(preferencias_padrao)

def aplicar_preferencias(preferencias):
    tema_var.set(preferencias.get("tema", "Claro"))
    check_var.set(preferencias.get("check", 0))
    if preferencias.get("tema") == "Claro":
        aplicar_tema_claro()
    else:
        aplicar_tema_escuro()
        
def verificar_atualizacoes(url = "https://d-jefferson.github.io/Update/"):
    try:
        resposta = requests.head(url)
        if resposta.status_code < 400:
            print(f"O link {url} é válido.")
            def abrir():
                webbrowser.open("https://d-jefferson.github.io/Update/")
            janela.after(2000, abrir)
            status_label = ctk.CTkLabel(janela, text="[ Há atualizações disponiveis ]", font=ctk.CTkFont(size=14), text_color="green")
            status_label.pack(pady=10)
        else:
            print(f"O link {url} é inválido. Código de status: {resposta.status_code}")
            status_label = ctk.CTkLabel(janela, text="[ Não há atualizações disponiveis ]", font=ctk.CTkFont(size=14), text_color="Teal", corner_radius=15)
            status_label.pack(pady=(180,0))
            btn_2 = ctk.CTkButton(janela, text="Voltar", width=50,height=15,command=cancelar, text_color="white",hover_color="darkred", font=ctk.CTkFont(size=12, weight="bold"), corner_radius=70,fg_color="gray15")
            btn_2.pack(pady=20)
    except requests.exceptions.RequestException:
        print(f"O link {url} é inválido.")
def veri():        
    for widget in janela.winfo_children():
        widget.destroy()
    style = ttk.Style()
    style.theme_use("default")
    progressbar = ttk.Progressbar(janela, orient="horizontal", length=200, mode="indeterminate")
    progressbar.pack(pady=(180,10))
    progressbar.start()
    def parar():
        progressbar.pack_forget()
    janela.after(5500, verificar_atualizacoes)
    janela.after(5500, parar)
        
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
janela = ctk.CTk("gray40")
janela.title("Configurações")
janela.geometry("242x425")
janela.resizable(False, False)

tema_var = ctk.StringVar(value="Claro")
check_var = ctk.IntVar(value=0)
volume_var = ctk.IntVar(value=50)
titulo_label = ctk.CTkLabel(janela, text="Configurações", font=("Arial", 20, "bold"))
titulo_label.pack(pady=10)
label1 = ctk.CTkLabel(janela, text="Tema:")
label1.pack(anchor="w", padx=20, pady=(10, 0))
tema_menu = ctk.CTkOptionMenu(janela, values=["Claro", "Escuro"], variable=tema_var, command="")
tema_menu.pack(padx=20, pady=10)
#check = ctk.CTkCheckBox(janela, text="", variable=check_var)
#check.pack(anchor="w", padx=20, pady=5)
label2 = ctk.CTkLabel(janela, text="Atualizações:")
label2.pack(anchor="w", padx=20, pady=(10, 0))
btn_1 = ctk.CTkButton(janela, text="Verificar...",command=veri, font=ctk.CTkFont(size=12, weight="bold"))
btn_1.pack(pady=10)
status_label = ctk.CTkLabel(janela, text="", font=("Arial", 16))
status_label.pack()
btn_frame = ctk.CTkFrame(janela, fg_color="gray40", width=242)
btn_frame.pack(pady=(145,0))
btn_2 = ctk.CTkButton(btn_frame, text="Voltar", width=50,height=15,command=cancelar, text_color="white",hover_color="darkred", font=ctk.CTkFont(size=12, weight="bold"), corner_radius=70,fg_color="gray15")
btn_2.grid(row=0, column=0, padx=(0,128))
salvar_button = ctk.CTkButton(btn_frame, text="Salvar", width=50,height=15, command=salvar_preferencias)
salvar_button.grid(row=0, column=1, padx=(0,100))

carregar_preferencias()
janela.mainloop()
