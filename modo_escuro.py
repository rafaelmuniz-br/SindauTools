import customtkinter as ctk
import requests
import webbrowser
from tkinter import ttk

from formatador_notificacao import abrir_formatador_notificacao
from formatador_vinculador import abrir_formatador_vinculador
from formatador_CPF import abrir_formatar_cpf

#-------------------------------------------------------------------
def menu_escuro():
    menu_window = ctk.CTk()
    menu_window.title("SindauTools")
    menu_window.geometry("242x425")
    menu_window.resizable(False, False)

    def voltar():
        for widget in menu_window.winfo_children():
            widget.destroy()
        menu()
        
    def ferramentas_api():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - API", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15)
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador Notificação", command=abrir_formatador_notificacao, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Formatador Vinculação", command=abrir_formatador_vinculador,  width=200)
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20)
        btn_3.pack(pady=80)
        

    def ferramentas_geral():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - Geral", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15)
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador CPF", command=abrir_formatar_cpf, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20)
        btn_2.pack(pady=20)

    def sobre():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label_2 = ctk.CTkLabel(menu_window, text= "O SindauTools é um conjunto de ferramentas criado para apoiar a equipe de suporte técnico, adaptando-se constantemente às suas demandas, com o objetivo de aumentar a produtividade, ao acelerar processos encontrados nos trabalhos realizados.",  wraplength=220)
        label_2.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Desenvolvedores", command=abrir_linkedin_desenvolvedores, width=20, hover_color="gray60")
        btn_1.pack(pady=0)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20)
        btn_2.pack(pady=20)
        
    def verificar_atualizacoes(url = "https://d-jefferson.github.io/Update/"):
        try:
            resposta = requests.head(url)
            if resposta.status_code < 400:
                print(f"O link {url} é válido.")
                webbrowser.open("https://d-jefferson.github.io/Update/")
                status_label = ctk.CTkLabel(menu_window, text="[ Há atualizações disponiveis ]", font=ctk.CTkFont(size=14), text_color="green")
                status_label.pack(pady=10)
            else:
                print(f"O link {url} é inválido. Código de status: {resposta.status_code}")
                status_label = ctk.CTkLabel(menu_window, text="[ Não há atualizações disponiveis ]", font=ctk.CTkFont(size=14), text_color="teal")
                status_label.pack(pady=10)
        except requests.exceptions.RequestException:
            print(f"O link {url} é inválido.")
            
    def veri():
        style = ttk.Style()
        style.theme_use("default")
        progressbar = ttk.Progressbar(menu_window, orient="horizontal", length=200, mode="indeterminate")
        progressbar.pack(pady=10)
        progressbar.start()
        def parar():
            progressbar.pack_forget()
        menu_window.after(5500, verificar_atualizacoes)
        menu_window.after(5500, parar)
        
    def atualizacao():
        for widget in menu_window.winfo_children():
            widget.destroy()
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20,height=3, fg_color="teal", hover_color="darkred",font=ctk.CTkFont(size=9))
        btn_2.pack(pady=0)
        label_1 = ctk.CTkLabel(menu_window, text="Novidades - 1.0.3", font=ctk.CTkFont(size=24, weight="bold"), text_color="teal")
        label_1.pack(pady=10)
        label_2 = ctk.CTkLabel(menu_window, text= "Melhorias e Ajustes:\n1. Novo visual do menu principal.\n2. Adicionado Des/Vincular Aulas\n3. Melhorado sistema notificação\n4. Aprimorado formatador de CPF", font=ctk.CTkFont(size=14), text_color="gray15")
        label_2.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Verificar atualizações", command=veri, width=20, fg_color="gray75", hover_color="gray60",text_color="teal", font=ctk.CTkFont(size=15))
        btn_1.pack(pady=(30,0))
        status_label = ctk.CTkLabel(menu_window, text="", font=ctk.CTkFont(size=14), text_color="yellow")
        status_label.pack(pady=10)

    def abrir_linkedin_desenvolvedores():
        webbrowser.open("https://www.linkedin.com/in/jefferson-levy-57551317b/")
        webbrowser.open("https://www.linkedin.com/in/rafael-muniz-88b417245/")
        
    def modo():
        menu_window.destroy()
        from modo_claro import menu_claro
        menu_claro()
        
    def menu():
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15)
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas - API", command=ferramentas_api, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Ferramentas - Geral", command=ferramentas_geral, width=200)
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
        btn_3.pack(pady=10)
        btn_frame = ctk.CTkFrame(menu_window, fg_color="gray14")
        btn_frame.pack(pady=(180,0))
        btn_6 = ctk.CTkButton(btn_frame, text="Beta 1.0.1", width=50,command=atualizacao, text_color="teal",fg_color="gray14",hover_color="gray14", font=ctk.CTkFont(size=12, weight="bold"))
        btn_6.grid(row=0, column=1, padx=(50,0))
        btn_7 = ctk.CTkButton(btn_frame, text="Light", width=50,height=15,command=modo, text_color="gray15",hover_color="gray100", font=ctk.CTkFont(size=12, weight="bold"), corner_radius=70,fg_color="gray75",text_color_disabled="yellow")
        btn_7.grid(row=0, column=0, padx=(0,50))
    menu()

    menu_window.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------    
if __name__ == "__main__":
    menu_escuro()
