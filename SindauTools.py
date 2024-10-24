import customtkinter as ctk
import tkinter as tk
import json
import re


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
appWidth, appHeight = 1366, 768

def menu_principal():
    menu_window = ctk.CTk()
    menu_window.title("SindauTools")
    menu_window.geometry("240x425")
    

    label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="gray30")
    label.pack(pady=10)
    
    def voltar():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="gray30")
        label.pack(pady=10)
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas", command=menu_ferramentas, width=200)
        btn_1.pack(pady=10)
        btn_5 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
        btn_5.pack(pady=10)

    def menu_ferramentas():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="gray30")
        label.pack(pady=10)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador Notificação", command=abrir_formatador_notificacao, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Formatador CPF", command=abrir_formatar_cpf, width=200)
        btn_2.pack(pady=10)
        #btn_5 = ctk.CTkButton(menu_window, text="Formatador Vincular/Desvincular Aula", command=abrir_formatar_cpf, width=200)
        #btn_5.pack(pady=10)
        #btn_4 = ctk.CTkButton(menu_window, text="Formatador Matricula", command=abrir_formatar_cpf, width=200)
        #btn_4.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
        btn_3.pack(pady=80)
    
    
    btn_1 = ctk.CTkButton(menu_window, text="Ferramentas", command=menu_ferramentas, width=200)
    btn_1.pack(pady=10)
    
    
    
    
    #btn_2 = ctk.CTkButton(menu_window, text="Atualizações", command=atualizar, width=200)
    #btn_2.pack(pady=10)

    #btn_3 = ctk.CTkButton(menu_window, text="Formatador de Vinculação", width=200)
    #btn_3.pack(pady=10)

    #btn_4 = ctk.CTkButton(menu_window, text="Corretor ortográfico", width=200)
    #btn_4.pack(pady=10)
    def sobre():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=24, weight="bold"))
        label.pack(pady=20)
        
        label = ctk.CTkLabel(menu_window, text= "A SindauTools foi criada\n para se adaptar continuamente\nàs demandas de suporte do\n Sindauto,visando proporcionar\n mais facilidade e eficiência\nao trabalho da nossa equipe.", font=ctk.CTkFont(size=14, weight="bold"))
        label.pack(pady=20)

        label = ctk.CTkLabel(menu_window, text="Desenvolvido por:\nJefferson e Rafael", font=ctk.CTkFont(size=14, weight="bold"))
        label.pack(pady=20)
        btn_3 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
        btn_3.pack(pady=20)
    

    btn_5 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
    btn_5.pack(pady=10)
    
    
        

    menu_window.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
def abrir_formatador_notificacao():
    formatador_window = ctk.CTk()  
    formatador_window.title("SindauTools")
    formatador_window.geometry(f"{appWidth}x{appHeight}")


    label = ctk.CTkLabel(formatador_window, text="Formatador Notificação", font=ctk.CTkFont(size=24, weight="bold"))
    label.grid(row=0, column=0, columnspan=2, pady=(20, 10))


    inserir = ctk.CTkTextbox(formatador_window, width=600, height=580, border_width=1, border_color="gray40", fg_color="gray15")
    inserir.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="n")

    btn_frame = ctk.CTkFrame(formatador_window)
    btn_frame.grid(row=1, column=0, padx=20, pady=(0, 10))

    def formatar():
        try:
            texto = inserir.get("1.0", tk.END).strip()
            linhas = texto.split("\n")
            resultados.clear()

            for widget in resultados_frame.winfo_children():
                widget.destroy()

            for idx, linha in enumerate(linhas):
                elementos = linha.split("\t")
                
                if len(elementos) == 13 and elementos[12] == "paid":
                    
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
                    resultado_box = ctk.CTkTextbox(resultados_frame, width=450, height=150, border_width=1, border_color="gray40", fg_color="gray20")
                    resultado_box.insert(tk.END, resultado_json)
                    resultado_box.grid(row=idx, column=0, padx=5, pady=5, sticky="nw")

                    btn_copiar = ctk.CTkButton(resultados_frame, text="Copiar", width=50, height=30, 
                                                command=lambda r=resultado_json: copiar_texto(r),
                                                font=ctk.CTkFont(size=10), fg_color="gray25", hover_color="teal")
                    btn_copiar.grid(row=idx, column=1, padx=5, pady=5, sticky="nw")

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
        inserir.delete("1.0", tk.END)
        for widget in resultados_frame.winfo_children():
            widget.destroy()
        resultados.clear()
        status_label.configure(text="Resultados limpos.", text_color="yellow")

    btn_formatar = ctk.CTkButton(btn_frame, text="Formatar", width=50, height=30, command=formatar, font=ctk.CTkFont(size=10), fg_color="gray25", hover_color="darkblue")
    btn_formatar.grid(row=0, column=1, padx=5)

    btn_limpar = ctk.CTkButton(btn_frame, text="Limpar", width=50, height=30, command=limpar_resultados, font=ctk.CTkFont(size=10), fg_color="red", hover_color="darkred")
    btn_limpar.grid(row=0, column=2, padx=5)

    resultados_frame = ctk.CTkScrollableFrame(formatador_window, width=600, border_width=1, border_color="gray40", fg_color="gray15")
    resultados_frame.grid(row=1, column=1, rowspan=2, padx=20, pady=(20, 20), sticky="nsew")

    resultados = []

    status_label = ctk.CTkLabel(formatador_window, text="", font=ctk.CTkFont(size=14), text_color="yellow")
    status_label.grid(row=3, column=0, columnspan=2, pady=(10, 20), sticky="ew")

    formatador_window.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
def abrir_formatar_cpf():
    cpf_window = ctk.CTk()
    cpf_window.title("SindauTools")
    cpf_window.geometry("1000x800")
    
    def extrair_cpfs(texto):
        padrao_cpf_formatado = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
        padrao_cpf_numerico = r'\b\d{11}\b'
        padrao_cpf_outros = r'\d{3}\.\d{3}\.\d{3}\.\d{2}'
        sem_padrao_1 = r'\d{3}\.\d{6}\.\d{2}'
        sem_padrao_2 = r'\d{3}\.\d{8}'
        sem_padrao_3 = r'\d{3}\.\d{3}\.\d{5}'
        sem_padrao_4 = r'\d{6}\.\d{3}\.\d{2}'
        sem_padrao_5 = r'\d{9}\.\d{2}'
        sem_padrao_6 = r'\d{3}-\d{6}-\d{2}'
        sem_padrao_7 = r'\d{3}-\d{8}'
        sem_padrao_8 = r'\d{3}-\d{3}-\d{5}'
        sem_padrao_9 = r'\d{9}-\d{2}'
        sem_padrao_10 = r'\d{3}-\d{3}-\d{3}-\d{2}'

        cpfs_formatados = re.findall(padrao_cpf_formatado, texto)
        cpfs_numericos = re.findall(padrao_cpf_numerico, texto)
        cpfs_outros = re.findall(padrao_cpf_outros, texto)
        padra_1 = re.findall(sem_padrao_1, texto)
        padra_2 = re.findall(sem_padrao_2, texto)
        padra_3 = re.findall(sem_padrao_3, texto)
        padra_4 = re.findall(sem_padrao_4, texto)
        padra_5 = re.findall(sem_padrao_5, texto)
        padra_6 = re.findall(sem_padrao_6, texto)
        padra_7 = re.findall(sem_padrao_7, texto)
        padra_8 = re.findall(sem_padrao_8, texto)
        padra_9 = re.findall(sem_padrao_9, texto)
        padra_10 = re.findall(sem_padrao_10, texto)

        cpfs_formatados_limpos = [re.sub(r'\D', '', cpf) for cpf in cpfs_formatados]
        cpfs_formatados_outros = [re.sub(r'\D', '', cpf) for cpf in cpfs_outros]
        a_1 = [re.sub(r'\D', '', cpf) for cpf in padra_1]
        a_2 = [re.sub(r'\D', '', cpf) for cpf in padra_2]
        a_3 = [re.sub(r'\D', '', cpf) for cpf in padra_3]
        a_4 = [re.sub(r'\D', '', cpf) for cpf in padra_4]
        a_5 = [re.sub(r'\D', '', cpf) for cpf in padra_5]
        a_6 = [re.sub(r'\D', '', cpf) for cpf in padra_6]
        a_7 = [re.sub(r'\D', '', cpf) for cpf in padra_7]
        a_8 = [re.sub(r'\D', '', cpf) for cpf in padra_8]
        a_9 = [re.sub(r'\D', '', cpf) for cpf in padra_9]
        a_10 = [re.sub(r'\D', '', cpf) for cpf in padra_10]
        cpfs_todos = cpfs_formatados_limpos + cpfs_numericos + cpfs_formatados_outros + a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + a_8 + a_9 + a_10

        return cpfs_todos

    def processar_cpfs():
        try:
            texto = inserir.get("1.0", tk.END)
            cpfs = extrair_cpfs(texto)

            terco = len(cpfs) // 3
            cpfs_coluna_1 = cpfs[:terco]
            cpfs_coluna_2 = cpfs[terco:terco * 2]
            cpfs_coluna_3 = cpfs[terco * 2:]
        
            displayBox1.delete("1.0", tk.END)
            displayBox1.insert(tk.END, '\n'.join(cpfs_coluna_1))

            displayBox2.delete("1.0", tk.END)
            displayBox2.insert(tk.END, '\n'.join(cpfs_coluna_2))
            
            displayBox3.delete("1.0", tk.END)
            displayBox3.insert(tk.END, '\n'.join(cpfs_coluna_3))
            status_label.configure(text="CPFs convertidos!", text_color="teal")
        except:
            status_label.configure(text="Não há CPFs para conversão", text_color="red")
        
    def processar_virgula():
        try:
            texto = inserir.get("1.0", tk.END)
            cpfs = extrair_cpfs(texto)

            terco = len(cpfs) // 3
            cpfs_coluna_1 = cpfs[:terco]
            cpfs_coluna_2 = cpfs[terco:terco * 2]
            cpfs_coluna_3 = cpfs[terco * 2:]

            displayBox1.delete("1.0", tk.END)
            displayBox1.insert(tk.END, ',\n'.join(cpfs_coluna_1))

            displayBox2.delete("1.0", tk.END)
            displayBox2.insert(tk.END, ',\n'.join(cpfs_coluna_2))
            
            displayBox3.delete("1.0", tk.END)
            displayBox3.insert(tk.END, ',\n'.join(cpfs_coluna_3))
            status_label.configure(text="CPFs convertidos e adicionado virgulas!", text_color="teal")
        except:
        
            status_label.configure(text="Não há CPFs para conversão", text_color="red")
        
        
            

    label_1 = ctk.CTkLabel(cpf_window, text="Formatador CPF", font=ctk.CTkFont(size=20, weight="bold"))
    label_1.pack(pady=10)
    
    inserir = ctk.CTkTextbox(cpf_window, width=600, height=200, border_width=1, border_color="gray40")
    inserir.pack(pady=10)
    def copiar_texto():
        try:
            cpf_window.clipboard_clear()
            conteudo_coluna_1 = displayBox1.get("1.0", tk.END).strip()
            conteudo_coluna_2 = displayBox2.get("1.0", tk.END).strip()
            conteudo_coluna_3 = displayBox2.get("1.0", tk.END).strip()
            texto_copiado = conteudo_coluna_1 + "\n" + conteudo_coluna_2 + "\n" + conteudo_coluna_3
            cpf_window.clipboard_append(texto_copiado)
            status_label.configure(text="Texto das caixas de texto copiado com sucesso!", text_color="green")
        except tk.TclError:
            status_label.configure(text="Erro ao copiar texto", text_color="red")

    def limpar_resultados():
        inserir.delete("1.0", tk.END)
        displayBox1.delete("1.0", tk.END)
        displayBox2.delete("1.0", tk.END)
        displayBox3.delete("1.0", tk.END)
        status_label.configure(text="Resultados limpos.", text_color="yellow")
        
        
    def segment_button_function(value):
        if value == "Listar CPFs":
            processar_cpfs()
        elif value == "CPFs + ,":
            processar_virgula()
        elif value == "Copiar":
            copiar_texto()
        elif value == "Apagar":
            limpar_resultados()
            
    seg_button_1 = ctk.CTkSegmentedButton(cpf_window)
    seg_button_1.pack(pady=5)
    seg_button_1.configure(values=["Listar CPFs", "CPFs + ,", "Copiar","Apagar"], command=segment_button_function)
    
    colunas_frame = ctk.CTkFrame(cpf_window)
    colunas_frame.pack(padx=5, pady=10)
    displayBox1 = ctk.CTkTextbox(colunas_frame, width=190, height=400, border_width=1, border_color="gray40")
    displayBox1.grid(row=0, column=0, padx=5)
    displayBox2 = ctk.CTkTextbox(colunas_frame, width=190, height=400, border_width=1, border_color="gray40")
    displayBox2.grid(row=0, column=1, padx=5)
    displayBox3 = ctk.CTkTextbox(colunas_frame, width=190, height=400, border_width=1, border_color="gray40")
    displayBox3.grid(row=0, column=2, padx=5)

    status_label = ctk.CTkLabel(cpf_window, text="", font=ctk.CTkFont(size=14), text_color="yellow")
    status_label.pack(pady=10)
    
    cpf_window.mainloop()
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    menu_principal()
