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

from formatador_notificacao import abrir_formatador_notificacao
from formatador_vinculador import abrir_formatador_vinculador

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
appWidth, appHeight = 800, 600
#-------------------------------------------------------------------

def menu_principal():
    menu_window = ctk.CTk("gray75")
    menu_window.title("SindauTools")
    menu_window.geometry("240x425")
    menu_window.resizable(False, False)

    def voltar():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Ferramentas - API", command=ferramentas_api, width=200)
        btn_1.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Ferramentas - Geral", command=ferramentas_geral, width=200)
        btn_2.pack(pady=10)
        btn_5 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
        btn_5.pack(pady=10)
        btn_6 = ctk.CTkButton(menu_window, text="                                       Beta 1.0.3", width=280,command=atualizacao, text_color="teal",fg_color="gray75",hover_color="gray75", font=ctk.CTkFont(size=12, weight="bold"))
        btn_6.pack(pady=(180,0))
        keyboard.remove_hotkey('ctrl+m')

    def ferramentas_api():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - API", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador Notificação", command=abrir_formatador_notificacao, width=200)
        btn_1.pack(pady=10)
        btn_3 = ctk.CTkButton(menu_window, text="Formatador (Des)Vincular", command=abrir_formatador_vinculador,  width=200)
        btn_3.pack(pady=10)
        btn_2 = ctk.CTkButton(menu_window, text="Formatador CPFs", command=abrir_formatar_cpf, width=200)
        btn_2.pack(pady=10)
        btn_4 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred")
        btn_4.pack(pady=80)
     
    def ferramentas_geral():
        for widget in menu_window.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(menu_window, text="Ferramentas - Geral", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
        label.pack(pady=20)
        btn_1 = ctk.CTkButton(menu_window, text="Formatador CPFs", command=abrir_formatar_cpf, width=200)
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
        label_1 = ctk.CTkLabel(menu_window, text="Novidades - 1.0.3", font=ctk.CTkFont(size=24, weight="bold"), text_color="teal")
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
        
    label = ctk.CTkLabel(menu_window, text="SindauTools", font=ctk.CTkFont(size=20, weight="bold"),corner_radius=15,fg_color="darkred")
    label.pack(pady=20)
    btn_1 = ctk.CTkButton(menu_window, text="Ferramentas - API", command=ferramentas_api, width=200)
    btn_1.pack(pady=10)
    btn_2 = ctk.CTkButton(menu_window, text="Ferramentas - Geral", command=ferramentas_geral, width=200)
    btn_2.pack(pady=10)
    btn_5 = ctk.CTkButton(menu_window, text="Sobre", width=200,command=sobre)
    btn_5.pack(pady=10)
    btn_6 = ctk.CTkButton(menu_window, text="                                       Beta 1.0.3", width=280,command=atualizacao, text_color="teal",fg_color="gray75",hover_color="gray75", font=ctk.CTkFont(size=12, weight="bold"))
    btn_6.pack(pady=(180,0))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def abrir_formatar_cpf():
        for widget in menu_window.winfo_children():
            widget.destroy()
    
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
                keyboard.send('ctrl+c')
                texto_copiado = menu_window.clipboard_get()
                cpfs = extrair_cpfs(texto_copiado)
                displayBox.delete("1.0", tk.END)
                displayBox.insert(tk.END, '\n'.join(cpfs))
                reprocessar()
            except tk.TclError:
                status_label.configure(text="Erro ao acessar a área de transferência.", text_color="red")
                
        def reprocessar():
            try:
                texto_copiado = menu_window.clipboard_get()
                cpfs = extrair_cpfs(texto_copiado)
                displayBox.delete("1.0", tk.END)
                displayBox.insert(tk.END, '\n'.join(cpfs))
                status_label.configure(text="Exibindo lista:", text_color="#5193c2")
            except tk.TclError:
                status_label.configure(text="Erro ao acessar a área de transferência.", text_color="red")
        
        def processar_virgula():
            try:
                texto_copiado = menu_window.clipboard_get()
                cpfs = extrair_cpfs(texto_copiado)
                displayBox.delete("1.0", tk.END)
                displayBox.insert(tk.END, ',\n'.join(cpfs))
                status_label.configure(text="Virgula adicionada!", text_color="#4b9636")
            except tk.TclError:
                status_label.configure(text="Erro ao acessar a área de transferência.", text_color="red")
        def segment_button_function(value):
            if value == "Listar":
                processar_cpfs()
            elif value == "Add Virgula":
                processar_virgula()
            elif value == "Copiar":
                copiar_texto()
            elif value == "Apagar":
                limpar_resultados()
                
        def copiar_texto():
            try:
                menu_window.clipboard_clear()
                conteudo_coluna_1 = displayBox.get("1.0", tk.END).strip()
                texto_copiado = conteudo_coluna_1
                menu_window.clipboard_append(texto_copiado)
                status_label.configure(text="Texto copiado com sucesso!", text_color="#245aab")
            except tk.TclError:
                status_label.configure(text="Erro ao copiar texto", text_color="red")
                
        def limpar_resultados():
            displayBox.delete("1.0", tk.END)
            status_label.configure(text="Resultados limpos!", text_color="#ebeb4b")

        btn_1 = ctk.CTkButton(menu_window, text="Voltar", command=voltar, width=20, fg_color="teal", hover_color="darkred",height=3)
        btn_1.pack(pady=0)
        status_label = ctk.CTkLabel(menu_window, text="Formatador de CPFs", font=ctk.CTkFont(size=14), text_color="Teal",height=10)
        status_label.pack(pady=0)
        displayBox = ctk.CTkTextbox(menu_window, width=600, height=363, border_width=1, border_color="gray40",text_color="gray75")
        displayBox.pack(padx=0, pady=0)
        texto_pronto = "Para utilizar selecione o texto/lista que\ndeseja formatar e pressione Ctrl + M..."
        displayBox.insert("1.0", texto_pronto)
        keyboard.add_hotkey('ctrl+m', processar_cpfs)
        seg_button_1 = ctk.CTkSegmentedButton(menu_window,unselected_color="teal",fg_color="teal",selected_hover_color="#3291a8",unselected_hover_color="#3291a8")
        seg_button_1.pack(pady=0)
        seg_button_1.configure(values=["Listar", "Add Virgula", "Copiar","Apagar"], command=segment_button_function)
                
    menu_window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    menu_principal()
