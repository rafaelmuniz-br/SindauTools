import customtkinter as ctk
import requests
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk

from formatador_notificacao import abrir_formatador_notificacao
from formatador_vinculador import abrir_formatador_vinculador
from formatador_CPF import abrir_formatar_cpf

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
#-------------------------------------------------------------------

def menu_claro():
    menu_window = ctk.CTk("gray75")
    menu_window.title("SindauTools")
    menu_window.geometry("240x425")
    menu_window.resizable(False, False)

    def voltar():
        for widget in menu_window.winfo_children():
            widget.destroy()
        menu()

    def ferramentas_api():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - API", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador Notificação", command=abrir_formatador_notificacao, width=200)
        btn_1.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Formatador Vinculação", command=abrir_formatador_vinculador,  width=200)
        btn_3.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Formatador CPF", command=abrir_formatar_cpf, width=200)
        btn_2.pack(pady=10)
        btn_4 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
        btn_4.pack(pady=80)
     
    def ferramentas_geral():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - Geral", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador CPF", command=abrir_formatar_cpf, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
        btn_2.pack(pady=20)
        
    def sobre():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label_1 = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=24, weight="bold"), text_color="darkred")
        label_1.pack(pady=20)
        label_2 = ctk.CTkLabel(menu_window, text= "A SindauTools foi criada\n para se adaptar continuamente\nàs demandas de suporte do\n Sindauto,visando proporcionar\n mais facilidade e eficiência\nao trabalho da nossa equipe.", font=ctk.CTkFont(size=14, weight="bold"), text_color="black")
        label_2.pack(pady=20)
        label_3 = ctk.CTkLabel(menu_window, text="Desenvolvido por:\nJefferson e Rafael", font=ctk.CTkFont(size=14, weight="bold"), text_color="teal")
        label_3.pack(pady=(20,5))
        btn_1 = ctk.CTkButton(menu_window, text="Conhecer mais...", command=mais, width=20, fg_color="gray75", hover_color="gray60",text_color="teal")
        btn_1.pack(pady=0)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
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
        label_1 = ctk.CTkLabel(menu_window, text="Novidades - 1.0.1", font=ctk.CTkFont(size=24, weight="bold"), text_color="teal")
        label_1.pack(pady=10)
        label_2 = ctk.CTkLabel(menu_window, text= "Melhorias e Ajustes:\n1. Novo visual do menu principal.\n2. Adicionado Des/Vincular Aulas\n3. Melhorado sistema notificação\n4. Aprimorado formatador de CPF", font=ctk.CTkFont(size=14), text_color="gray15")
        label_2.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Verificar atualizações", command=veri, width=20, fg_color="gray75", hover_color="gray60",text_color="teal", font=ctk.CTkFont(size=15))
        btn_1.pack(pady=(30,0))
        status_label = ctk.CTkLabel(menu_window, text="", font=ctk.CTkFont(size=14), text_color="yellow")
        status_label.pack(pady=10)

    def mais():
        def opc(value):
            if value == "JEFFERSON":
                webbrowser.open("https://github.com/D-Jefferson")
            elif value == "RAFAEL M.":
                webbrowser.open("https://github.com/rafaelmuniz-br/")
        seg_button_1 = ctk.CTkSegmentedButton(menu_window, fg_color="teal",unselected_color="gray75",text_color="teal", height=70)
        seg_button_1.pack(pady=10)
        seg_button_1.configure(values=["JEFFERSON","RAFAEL M."], command=opc)
    
    def modo():
        menu_window.destroy()
        from modo_escuro import menu_escuro
        menu_escuro()
    
    def menu():
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas - API", command=ferramentas_api, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Ferramentas - Geral", command=ferramentas_geral, width=200)
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
        btn_3.pack(pady=10)
        btn_frame = ctk.CTkFrame(menu_window, fg_color="gray75")
        btn_frame.pack(pady=(180,0))
        btn_6 = ctk.CTkButton(btn_frame, text="\nBeta 1.0.1", width=50,command=atualizacao, text_color="#103454",fg_color="gray75",hover_color="gray75", font=ctk.CTkFont(size=12, weight="bold"))
        btn_6.grid(row=0, column=1, padx=(50,0))
        btn_7 = ctk.CTkButton(btn_frame, text="💡", width=50,command=modo, hover_color="gray75", fg_color="gray75", text_color="gray15")
        btn_7.grid(row=0, column=0, padx=(0,50))    
    menu()

    menu_window.mainloop()
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    menu_claro()