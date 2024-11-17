import customtkinter as ctk
import keyboard
import re
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
formatadorcpf = ctk.CTk("gray15")
formatadorcpf.title("SindauTools")
formatadorcpf.geometry("242x425")
formatadorcpf.resizable(False, False)

modo_lista = True

# -------------------------------------------------------------------
def abrir_formatar_cpf():
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

    def atualizar_contador():
        texto = displayBox.get("1.0", tk.END).strip()
        linhas = texto.count('\n') if texto else 0 
        contador_label.configure(text=f"CPFs: {linhas+1}")
    def automatico():
        try:
            formatadorcpf.geometry("242x425")
            keyboard.send('ctrl+c')
            texto_copiado = formatadorcpf.clipboard_get()
            cpfs = extrair_cpfs(texto_copiado)
            keyboard.send('ctrl+c')
            texto_copiado = formatadorcpf.clipboard_get()
            cpfs = extrair_cpfs(texto_copiado)
            displayBox.delete("1.0", tk.END)
            displayBox.insert(tk.END, '\n'.join(cpfs))
            status_label.configure(text="Lista gerada.", text_color="#5193c2")

            atualizar_contador()

        except tk.TclError:
            status_label.configure(text="Erro ao acessar a área de transferência.", text_color="red")
    def alternar_exibicao():
        global modo_lista
        try:
            formatadorcpf.geometry("242x425")
            texto_copiado = formatadorcpf.clipboard_get()
            cpfs = extrair_cpfs(texto_copiado)
            displayBox.delete("1.0", tk.END)

            if modo_lista:
                formatadorcpf.geometry("242x425")
                displayBox.insert(tk.END, '\n'.join(cpfs))
                status_label.configure(text="Lista gerada.", text_color="#5193c2")
            else:
                formatadorcpf.geometry("484x425")
                displayBox.insert(tk.END, ','.join(cpfs))
                status_label.configure(text="Texto único gerado.", text_color="#5193c2")

            atualizar_contador()
            modo_lista = not modo_lista

        except tk.TclError:
            status_label.configure(text="Erro ao acessar a área de transferência.", text_color="red")

    def copiar_texto():
        try:
            formatadorcpf.clipboard_clear()
            conteudo_coluna_1 = displayBox.get("1.0", tk.END).strip()
            texto_copiado = conteudo_coluna_1
            formatadorcpf.clipboard_append(texto_copiado)
            status_label.configure(text="Texto copiado com sucesso!", text_color="#5193c2")
        except tk.TclError:
            status_label.configure(text="Erro ao copiar texto", text_color="red")

    def limpar_resultados():
        displayBox.delete("1.0", tk.END)
        atualizar_contador()
        status_label.configure(text="Resultados limpos!", text_color="#ebeb4b")

    label = ctk.CTkLabel(formatadorcpf, text="Formatador de CPFs", font=ctk.CTkFont(size=13, weight="bold"), width=2000, fg_color="gray35")
    label.pack(pady=0)
    status_label = ctk.CTkLabel(formatadorcpf, text="", font=ctk.CTkFont(size=10), height=12)
    status_label.pack(pady=0)
    displayBox = ctk.CTkTextbox(formatadorcpf, width=600, height=360, border_width=1, border_color="gray40")
    displayBox.pack(padx=0, pady=0)
    texto_pronto = "Selecione um texto, em qualquer janela,\ncontendo CPFs e pressione Ctrl + M..."
    displayBox.insert("1.0", texto_pronto)
    keyboard.add_hotkey('ctrl+m', automatico)
    btn_frame = ctk.CTkFrame(formatadorcpf, fg_color="gray14", width=242)
    btn_frame.pack(pady=(0, 0))
    btn_1 = ctk.CTkButton(btn_frame, text="Formatar", width=50, command=alternar_exibicao, text_color="white", hover_color="#103454", border_width=1, border_color="gray20", font=ctk.CTkFont(size=12, weight="bold"))
    btn_1.grid(row=0, column=1, padx=(0, 0))
    btn_2 = ctk.CTkButton(btn_frame, text="Copiar", width=50, command=copiar_texto, text_color="white", fg_color="gray23",hover_color="#103454", border_width=1, border_color="gray20", font=ctk.CTkFont(size=12, weight="bold"))
    btn_2.grid(row=0, column=2, padx=(0, 0))
    btn_3 = ctk.CTkButton(btn_frame, text="Apagar", width=50, command=limpar_resultados, text_color="white", fg_color="gray23", hover_color="darkred", border_width=1, border_color="gray20", font=ctk.CTkFont(size=12, weight="bold"))
    btn_3.grid(row=0, column=3, padx=(0, 0))
    contador_label = ctk.CTkLabel(btn_frame, text="CPFs: 0", font=ctk.CTkFont(size=12, weight="bold"), text_color="white")
    contador_label.grid(row=0, column=0, padx=(0, 0))

    formatadorcpf.mainloop()
if __name__ == "__main__":
    abrir_formatar_cpf()