import customtkinter as ctk
import json
import keyboard
import pytz
import re
import requests
import tkinter as tk
import webbrowser

from datetime import datetime
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
appWidth, appHeight = 800, 600
#-------------------------------------------------------------------

def abrir_formatador_vinculador():
    formatador_window = ctk.CTk()  
    formatador_window.title("SindauTools - Formatador Vinculação")
    formatador_window.geometry(f"{appWidth}x{appHeight}")
    formatador_window.grid_rowconfigure(0, weight=0)
    formatador_window.grid_rowconfigure(1, weight=0)
    formatador_window.grid_rowconfigure(2, weight=1) 
    formatador_window.grid_rowconfigure(3, weight=1)
    formatador_window.grid_columnconfigure(0, weight=1) 
    formatador_window.grid_columnconfigure(1, weight=1) 

    def obter_data_hora_atual():
        timezone = pytz.timezone("America/Sao_Paulo")
        data_hora_atual = datetime.now(timezone)
        return data_hora_atual.strftime("%Y-%m-%dT%H:%M:%S%z")

    label = ctk.CTkLabel(formatador_window, text="Formatador Vinculação", font=ctk.CTkFont(size=24, weight="bold"), width=2000, fg_color="gray35", height=30, text_color="#faad55")
    label.grid(row=0, column=0, columnspan=2, pady=(20, 50))

    # Primeira caixa: UUIDs
    uuid_entry = ctk.CTkTextbox(formatador_window, width=400, height=300, border_width=1, border_color="gray40", fg_color="gray15")
    uuid_entry.grid(row=1, column=0, padx=30, pady=(0, 20), sticky="n")
    uuid_entry.insert(tk.END, "Copie e cole aqui os dados para vinculação/desvinculação\n")  # Mensagem inicial

    # Segunda caixa: CPF
    cpf_entry = ctk.CTkEntry(formatador_window, width=200, height=20)
    cpf_entry.grid(row=2, column=0, padx=30, pady=(0, 0), sticky="n")
    cpf_entry.insert(tk.END, "Copie e cole aqui o CPF\n")  # Mensagem inicial

    # Remover o rótulo "CPF:"
    # ctk.CTkLabel(formatador_window, text="CPF:").grid(row=2, column=0, padx=40, pady=(0, 30), sticky="w")  # Esta linha foi removida

    operacao_var = tk.StringVar(value="VINCULADO")
    operacao_menu = ctk.CTkOptionMenu(formatador_window, variable=operacao_var, values=["VINCULADO", "DESVINCULADO"], corner_radius=5)
    operacao_menu.grid(row=4, column=0, padx=30, pady=(0, 20))
    
    btn_frame = ctk.CTkFrame(formatador_window, fg_color="gray14")
    btn_frame.grid(row=5, column=0, padx=20, pady=(0, 0))
    
    status_label = ctk.CTkLabel(formatador_window, text="", font=ctk.CTkFont(size=14), text_color="yellow")
    status_label.grid(row=6, column=0, columnspan=2, pady=(10, 20), sticky="ew")
    
    def frame():
        global resultados_frame
        resultados_frame = ctk.CTkScrollableFrame(formatador_window, width=400, height=1000, border_width=0, fg_color="gray14", scrollbar_button_color="gray14", scrollbar_button_hover_color="gray17")
        resultados_frame.grid(row=1, column=1, rowspan=2, padx=0, pady=(0, 0), sticky="nsew")
    
    def formatar():
        try:
            uuids = uuid_entry.get("1.0", tk.END).strip().split("\n")
            uuids = [uuid.strip() for uuid in uuids if uuid.strip()]
            cpf = cpf_entry.get().strip()
            vinculacao = operacao_var.get()

            resultados_frame.destroy()
            frame()

            for idx, uuid in enumerate(uuids):
                json_obj = {
                    "_id": uuid,
                    "operacao": vinculacao,
                    "data_hora": obter_data_hora_atual(),
                    "agendamento": {
                        "uuid": uuid
                    },
                    "candidato": {
                        "cpf": cpf
                    }
                }
                
                resultado_json = json.dumps(json_obj, indent=4, ensure_ascii=False)
                resultado_box = ctk.CTkTextbox(resultados_frame, width=300, height=150, border_width=1, border_color="gray40", fg_color="gray20")
                resultado_box.insert(tk.END, resultado_json)
                resultado_box.grid(row=idx, column=0, padx=5, pady=5, sticky="nsew")
                resultado_label = ctk.CTkLabel(resultados_frame, text=f"{idx + 1}.", font=ctk.CTkFont(size=10), fg_color="teal", corner_radius=2)
                resultado_label.grid(row=idx, column=0, padx=5, pady=5, sticky="nw")
                btn_copiar = ctk.CTkButton(resultados_frame, text="Copiar", width=60, height=30, command=lambda r=resultado_json: copiar_texto(r), font=ctk.CTkFont(size=10), fg_color="gray23", hover_color="teal", border_width=2, bg_color="gray20")
                btn_copiar.grid(row=idx, column=0, padx=(240,0), pady=(122,0), sticky="nw")
        except Exception as e:
            status_label.configure(text=f"Erro ao formatar para JSON: {e}", text_color="red")

    def copiar_texto(linha):
        try:
            formatador_window.clipboard_clear()
            formatador_window.clipboard_append(linha)
            status_label.configure(text="Texto copiado com sucesso!", text_color="green")
        except tk.TclError:
            status_label.configure(text="Erro ao copiar texto", text_color="red")

    def limpar_resultados():
        uuid_entry.delete("1.0", tk.END)
        cpf_entry.delete(0, tk.END)
        resultados_frame.destroy()
        frame()
        status_label.configure(text="Resultados limpos.", text_color="yellow")

    btn_formatar = ctk.CTkButton(btn_frame, text="Formatar", command=formatar, font=ctk.CTkFont(size=12), fg_color="gray23", hover_color="#103454", border_width=1, border_color="gray20")
    btn_formatar.grid(row=0, column=0, padx=5)
    btn_limpar = ctk.CTkButton(btn_frame, text="Limpar", command=limpar_resultados, font=ctk.CTkFont(size=12), fg_color="gray23", hover_color="darkred", border_width=1, border_color="gray20")
    btn_limpar.grid(row=0, column=1, padx=5)
    
    frame()

    formatador_window.mainloop()