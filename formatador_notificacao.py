import customtkinter as ctk
import json
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
#-------------------------------------------------------------------
def abrir_formatador_notificacao():
    formatador_window = ctk.CTk()  
    formatador_window.title("SindauTools")
    formatador_window.geometry(f"800x600")
    formatador_window.grid_rowconfigure(0, weight=0)
    formatador_window.grid_rowconfigure(1, weight=0)
    formatador_window.grid_rowconfigure(2, weight=1) 
    formatador_window.grid_rowconfigure(3, weight=1)
    formatador_window.grid_columnconfigure(0, weight=1) 
    formatador_window.grid_columnconfigure(1, weight=1) 
    
    label = ctk.CTkLabel(formatador_window, text="Formatador Notificação", font=ctk.CTkFont(size=24, weight="bold"), width=2000, fg_color="gray35", height=30, text_color="gray85")
    label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

    # Criando a caixa de texto
    inserir = ctk.CTkTextbox(formatador_window, width=600, height=580, border_width=1, border_color="gray40", fg_color="gray15")
    inserir.grid(row=2, column=0, padx=2, pady=(0, 10), sticky="n")

    # Inserindo a mensagem inicial na caixa de texto
    inserir.insert(tk.END, "Copie e cole aqui os dados para a notificação financeira\n")

    btn_frame = ctk.CTkFrame(formatador_window, fg_color="gray14")
    btn_frame.grid(row=1, column=0, padx=2, pady=(0,4))

    def formatar():
        try:
            texto = inserir.get("1.0", tk.END).strip()
            linhas = texto.split("\n")
            resultados.clear()
            resultados_frame.destroy()
            frame()
            for idx, linha in enumerate(linhas):
                elementos = linha.split("\t")
                if len(elementos) == 13 and elementos[12] == "paid" or elementos[12] == "New": 
                    try:
                        valor = float(elementos[8])
                    except ValueError:
                        continue
                    
                    json_obj = {
                        "_id": elementos[0],
                        "operacao": elementos[1],
                        "data_hora": elementos[2],
                        "uuid_matricula": elementos[3],
                        "cnpj": elementos[4],
                        "financeiro": {
                            "situacao": elementos[5],
                            "numero_cobranca": elementos[6],
                            "operadora": elementos[7],
                            "valor": valor,
                            "data_criacao": elementos[9],
                            "data_atualizacao": elementos[10],
                            "data_vencimento": elementos[11],
                            "status_atual": elementos[12],
                        }
                    }
                             
                    resultado_json = json.dumps(json_obj, indent=4, ensure_ascii=False)
                    resultados.append(resultado_json)
                    resultado_box = ctk.CTkTextbox(resultados_frame, width=350, height=150, border_width=1, border_color="gray40", fg_color="gray20")
                    resultado_box.insert(tk.END, resultado_json)
                    resultado_box.grid(row=idx, column=0, padx=5, pady=5, sticky="nw")
                    resultado_label = ctk.CTkLabel(resultados_frame, text=f"{idx + 1}.", font=ctk.CTkFont(size=10), fg_color="teal", corner_radius=2)
                    resultado_label.grid(row=idx, column=0, padx=5, pady=5, sticky="nw")
                    btn_copiar = ctk.CTkButton(resultados_frame, text="Copiar", width=70, height=40, command=lambda r=resultado_json: copiar_texto(r), font=ctk.CTkFont(size=10), fg_color="gray23", hover_color="teal", border_width=2, bg_color="gray20")
                    btn_copiar.grid(row=idx, column=0, padx=(282,0), pady=(112,0), sticky="nw")
        except Exception as e:
                print("erro")

        def copiar_texto(linha):
            try:
                formatador_window.clipboard_clear()
                formatador_window.clipboard_append(linha)
            except tk.TclError:
                print("erro")

    def limpar_resultados():
        inserir.delete("1.0", tk.END)
        resultados_frame.destroy()
        frame()
        resultados.clear()
        
    btn_formatar = ctk.CTkButton(btn_frame, text="Formatar", width=50, height=30, command=formatar, font=ctk.CTkFont(size=12), hover_color="#103454", border_width=1, border_color="gray20")
    btn_formatar.grid(row=0, column=1, padx=2)
    btn_limpar = ctk.CTkButton(btn_frame, text="Limpar", width=50, height=30, command=limpar_resultados, font=ctk.CTkFont(size=12), fg_color="gray23", hover_color="darkred", border_width=1, border_color="gray20")
    btn_limpar.grid(row=0, column=2, padx=2)

    def frame():
        global resultados_frame
        resultados_frame = ctk.CTkScrollableFrame(formatador_window, width=600, border_width=0, border_color="gray40", fg_color="gray14", scrollbar_button_color="gray14", scrollbar_button_hover_color="gray16")
        resultados_frame.grid(row=1, column=1, rowspan=2, padx=2, pady=(20, 20), sticky="nsew")
    
    frame()
    resultados = []

    formatador_window.mainloop()