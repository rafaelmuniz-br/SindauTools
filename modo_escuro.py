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
    
    def config():
        menu_window.destroy()
        from config import janela
        janela.mainloop()
        
    def modo():
        menu_window.destroy()
        from modo_claro import menu_claro
        menu_claro()
        
    def sobre():
        def abrir_github_desenvolvedores():
            webbrowser.open("https://github.com/D-Jefferson"), webbrowser.open("https://github.com/rafaelmuniz-br")
        for widget in menu_window.winfo_children():
            widget.destroy()
        label_2 = ctk.CTkLabel(menu_window, text= "O SindauTools é um conjunto de ferramentas criado para apoiar a equipe de suporte técnico, adaptando-se constantemente às suas demandas, com o objetivo de aumentar a produtividade, ao acelerar processos encontrados nos trabalhos realizados.",  wraplength=220)
        label_2.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Desenvolvedores", command=abrir_github_desenvolvedores, width=20, hover_color="gray60")
        btn_1.pack(pady=0)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20)
        btn_2.pack(pady=20)
        
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
        
    def menu():
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15)
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas - API", command=ferramentas_api, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Ferramentas - Geral", command=ferramentas_geral, width=200)
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Preferêcias", width=200,command=config)
        btn_3.pack(pady=10)
        btn_4 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
        btn_4.pack(pady=10)
        btn_frame = ctk.CTkFrame(menu_window, fg_color="gray14")
        btn_frame.pack(pady=(135,0))
        btn_6 = ctk.CTkButton(btn_frame, text="\nBeta 1.0.1", width=50,command="atualizacao", text_color="#103454",fg_color="gray14",hover_color="gray14", font=ctk.CTkFont(size=12, weight="bold"))
        btn_6.grid(row=0, column=1, padx=(50,0))
        btn_7 = ctk.CTkButton(btn_frame, text="💡 ", width=50,command=modo, hover_color="gray14", fg_color="gray14")
        btn_7.grid(row=0, column=0, padx=(0,50))
    menu()

    menu_window.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------    
if __name__ == "__main__":
    menu_escuro()
