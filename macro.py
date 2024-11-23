import customtkinter as ctk
from datetime import datetime
import json
import os
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ARQUIVO_JSON = "preferencias.json"

def carregar_preferencias():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r") as file:
            return json.load(file)
    return {f"Texto {i+1}": {"titulo": f"Texto {i+1}", "conteudo": ""} for i in range(4)}

def salvar_preferencias(preferencias):
    with open(ARQUIVO_JSON, "w") as file:
        json.dump(preferencias, file, indent=4)

def abrir_macro():
    preferencias = carregar_preferencias()

    macro = ctk.CTk()
    macro.title("SindauTools")
    macro.geometry("484x425")
    macro.grid_rowconfigure(0, weight=0)
    macro.grid_rowconfigure(1, weight=1)
    macro.grid_columnconfigure(0, weight=1)
    macro.resizable(False, False)
    
    def copiar_texto():
        try:
            macro.clipboard_clear()
            conteudo = texto_box.get("1.0", tk.END).strip()
            macro.clipboard_append(conteudo)
        except tk.TclError:
            print("erro")
    def limpar_resultados():
        texto_box.delete("1.0", tk.END)
        titulo_box.delete("1.0", tk.END)
    
    texto_frame = ctk.CTkFrame(macro)
    texto_frame.grid(row=0, column=0, padx=(10,10), pady=(10, 0))

    titulo_box = ctk.CTkTextbox(texto_frame, width=190, height=30, wrap="none",font=ctk.CTkFont(size=16, weight="bold"))
    titulo_box.grid(row=0, column=0, padx=5, pady=(5, 5))

    texto_box = ctk.CTkTextbox(texto_frame, width=390, height=200, wrap="word",font=ctk.CTkFont(size=14))
    texto_box.grid(row=1, column=0, padx=5, pady=5)
    
    frameg = ctk.CTkFrame(macro)
    frameg.grid(row=1, column=0, padx=0, pady=(5, 0),columnspan=2)
    
    btns_frame = ctk.CTkFrame(frameg)
    btns_frame.grid(row=1, column=0, padx=0, pady=(5, 5))
    
    btns2_frame = ctk.CTkFrame(frameg)
    btns2_frame.grid(row=1, column=1, padx=0, pady=(5, 5))
    
    btns3_frame = ctk.CTkFrame(frameg)
    btns3_frame.grid(row=1, column=2, padx=0, pady=(5, 5))
    
    btn_2 = ctk.CTkButton(texto_frame, text="Copiar", width=30,height=10, command=copiar_texto, text_color="white", fg_color="gray23",hover_color="#103454", border_width=1, border_color="gray20", font=ctk.CTkFont(size=12, weight="bold"))
    btn_2.grid(row=1, column=0, padx=(340, 0), pady=(180, 0))
    btn_3 = ctk.CTkButton(macro, text="Limpar", width=30,height=10, command=limpar_resultados, text_color="white", fg_color="gray23", hover_color="darkred", border_width=1, border_color="gray20", font=ctk.CTkFont(size=12, weight="bold"))
    btn_3.grid(row=0, column=1, padx=(0,0), pady=(230, 0))
    
    def atualizar_relogio():
        hora_atual = datetime.now().strftime("%H:%M")
        label_relogio.configure(text=hora_atual)
        macro.after(10000, atualizar_relogio)
    label_relogio = ctk.CTkButton(macro, text="",font=ctk.CTkFont(size=20, weight="bold"),fg_color="gray20",corner_radius=5,height=10,width=10)
    label_relogio.grid(row=0, column=1, padx=0, pady=0)

    def carregar_texto(titulo, conteudo):
        titulo_box.delete("1.0", "end")
        titulo_box.insert("1.0", titulo)
        texto_box.delete("1.0", "end")
        texto_box.insert("1.0", conteudo)

    def salvar_texto_personalizado(indice):
        titulo = titulo_box.get("1.0", "end").strip()
        conteudo = texto_box.get("1.0", "end").strip()
        if titulo and conteudo:
            preferencias[f"Texto {indice}"] = {"titulo": titulo, "conteudo": conteudo}
            salvar_preferencias(preferencias)
            atualizar_botoes()

    botoes_carregar = []

    def atualizar_botoes():
        for i, botao in enumerate(botoes_carregar):
            botao.configure(text=preferencias[f"Texto {i+1}"]["titulo"])

    for i in range(4):
        botao = ctk.CTkButton(btns_frame,width=152,text={preferencias[f"Texto {i+1}"]["titulo"]},command=lambda i=i: carregar_texto(preferencias[f"Texto {i+1}"]["titulo"],preferencias[f"Texto {i+1}"]["conteudo"]),fg_color="gray14",border_color="gray20",border_width=1)
        botao.pack(pady=3, fill="x",padx=3)
        botoes_carregar.append(botao)
         
    for i in range(4,8):
            botao = ctk.CTkButton(btns2_frame,width=152,text=preferencias[f"Texto {i+1}"]["titulo"],command=lambda i=i: carregar_texto(preferencias[f"Texto {i+1}"]["titulo"],preferencias[f"Texto {i+1}"]["conteudo"]),fg_color="gray14",border_color="gray20",border_width=1)
            botao.pack(pady=3, fill="x",padx=3)
            botoes_carregar.append(botao)
        
    for i in range(8,12):
            botao = ctk.CTkButton(btns3_frame,width=152,text=preferencias[f"Texto {i+1}"]["titulo"],command=lambda i=i: carregar_texto(preferencias[f"Texto {i+1}"]["titulo"],preferencias[f"Texto {i+1}"]["conteudo"]),fg_color="gray14",border_color="gray20",border_width=1)
            botao.pack(pady=3, fill="x",padx=3)
            botoes_carregar.append(botao)
    
    def botoes_salvar():
        def voltar():
            salvar_frame.grid_remove()
            btn_1.grid_remove()
        btn_1 = ctk.CTkButton(macro, text="voltar", width=60,height=10, command=voltar, fg_color="gray14",border_color="#4682B4",border_width=1, font=ctk.CTkFont(size=12, weight="bold"))
        btn_1.grid(row=0, column=1, padx=(0, 0), pady=(0, 260))
        salvar_frame.grid()
        btn_1.grid()
    btn_2 = ctk.CTkButton(macro, text="salvar", width=60,height=10, command=botoes_salvar, fg_color="gray14",border_color="#4682B4",border_width=1, font=ctk.CTkFont(size=12, weight="bold"))
    btn_2.grid(row=0, column=1, padx=(0, 0), pady=(0, 260))
    
    salvar_frame = ctk.CTkFrame(macro,width=0,height=0)
    salvar_frame.grid(row=0, column=1, padx=0, pady=0)
    
    for i in range(8):
        ctk.CTkButton(
            salvar_frame,
            text=f"Salvar {i+1}",
            command=lambda i=i: salvar_texto_personalizado(i+1),width=30,height=10
        ).pack(pady=5, fill="x",padx=0)
    salvar_frame.grid_remove()
    
    atualizar_relogio()
    atualizar_botoes()
    carregar_preferencias()
    macro.mainloop()

