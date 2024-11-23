import customtkinter as ctk
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

from formatador_notificacao import abrir_formatador_notificacao
from formatador_vinculador import abrir_formatador_vinculador
from formatador_CPF import abrir_formatar_cpf
from macro import abrir_macro

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
#-------------------------------------------------------------------

def menu_claro():
    menu_window = ctk.CTk("gray75")
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
    
    def sobre():
        for widget in menu_window.winfo_children():
            widget.destroy()
        def desenvolvedores():
            webbrowser.open("https://github.com/D-Jefferson"), webbrowser.open("https://github.com/rafaelmuniz-br")
        label_1 = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=24, weight="bold"), text_color="darkred")
        label_1.pack(pady=20)
        label_2 = ctk.CTkLabel(menu_window,text_color="gray14", text= "O SindauTools é um conjunto de ferramentas criado para apoiar a equipe de suporte técnico, adaptando-se constantemente às suas demandas, com o objetivo de aumentar a produtividade, ao acelerar processos encontrados nos trabalhos realizados.",  wraplength=220)
        label_2.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Desenvolvedores", command=desenvolvedores, width=20, fg_color="gray75", hover_color="gray60",text_color="#005fb1")
        btn_1.pack(pady=0)
        btn_2 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="#005fb1", hover_color="darkred")
        btn_2.pack(pady=20)
        
    def ferramentas():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador Notificação", command=abrir_formatador_notificacao, width=200, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=1,border_color="#005fb1")
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Formatador Vinculação", command=abrir_formatador_vinculador,  width=200, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=1,border_color="#005fb1")
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Formatador CPF", command=abrir_formatar_cpf, width=200, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=1,border_color="#005fb1")
        btn_3.pack(pady=10)
        btn_4 = ctk.CTkButton(menu_window, text="Respostas Rápidas", command=abrir_macro, width=200, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=1,border_color="#005fb1")
        btn_4.pack(pady=10)
        btn_5 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="#005fb1", hover_color="darkred")
        btn_5.pack(pady=50)
    
    def menu():
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=(30,20))
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas", command=ferramentas, width=200, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=2,border_color="#4682B4")
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Configurações", width=200,command=config, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=2,border_color="#4682B4")
        btn_2.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre, hover_color="gray85",corner_radius=15,fg_color="gray75",text_color="gray14",font=ctk.CTkFont(size=16), border_width=2,border_color="#4682B4")
        btn_3.pack(pady=10)


        btn_frame = ctk.CTkFrame(menu_window, fg_color="gray75")
        btn_frame.pack(pady=(173,0))
        btn_6 = ctk.CTkButton(btn_frame, text="Beta 1.0.1", width=50,command="atualizacao", text_color="darkred",fg_color="gray75",hover_color="gray75", font=ctk.CTkFont(size=12, weight="bold"))
        btn_6.grid(row=0, column=1, padx=(167,0))
    menu()

    menu_window.mainloop()
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    menu_claro()
