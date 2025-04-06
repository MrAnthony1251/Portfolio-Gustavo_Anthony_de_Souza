import requests
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import PhotoImage
from PIL import Image, ImageTk

class ConversorDeMoedas:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas Avançado")
        self.root.geometry("800x600")           
        self.api_key = os.getenv("MrAnthony1251")
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.moedas = []
        self.favoritos = []
        self.carregar_favoritos()
        self.carregar_moedas()
        self.configurar_interface() 
    
        
        
        
    def carregar_moedas(self):
        """Carrega as moedas disponíveis da API"""
        try:
            resposta = requests.get(f"{self.base_url}USD")
            dados = resposta.json()
            self.moedas = list(dados['rates'].keys())
        except:
            self.moedas = ["USD", "EUR", "GBP", "JPY", "CAD"]
        
    def carregar_favoritos(self):
        """Carrega os pares de moedas favoritos do arquivo"""
        try:
            with open("favoritos.json", "r") as f:
                self.favoritos = json.load(f)
        except:
            self.favoritos = []
            
            
    def salvar_favoritos(self):
        """Salva os pares favoritos no arquivo"""
        with open("favoritos.json", "w") as f:             
            json.dump(self.favoritos, f)
            
    def obter_taxa_cambio(self, moeda_origem, moeda_destino):
        """Obtém a taxa de câmbio em tempo real"""
        try:
            resposta = requests.get(f"{self.base_url}{moeda_origem}")
            dados = resposta.json()
            return dados['rates'][moeda_destino]
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao obter taxas: {str(e)}")
            return None
        
    def obter_historico_taxas(self, moeda, dias=30):
        """Obtém taxas históricas (simplificadas)"""
        data_fim = datetime.now()
        data_inicio = data_fim - timedelta(days=dias)
        datas = []
        taxas = []
        
        
        
        for i in range(dias):
            data = data_inicio + timedelta(days=i)
            datas.append(data.strftime("%Y-%m-%d"))
            import random
            taxas.append(1.0 + random.uniform(-0.1,  0.1))
        
        return datas, taxas
    
    def configurar_interface(self):
        """Configura a interface gráfica"""
        
        self.root.set_theme("equilux")
        
        
        frame_principal = ttk.Frame(self.root, padding=20)
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        
        ttk.Label(frame_principal, text="Valor:").grid(row=0, column=0, sticky="w")
        self.entrada_valor = ttk.Entry(frame_principal)
        self.entrada_valor.grid(row=0, column=1, sticky="ew")
        
        
        
        ttk.Label(frame_principal, text="De:").grid(row=1, column=0, sticky="w")
        self.moeda_origem = ttk.Combobox(frame_principal, values=self.moedas)
        self.moeda_origem.grid(row=1, column=1, sticky="ew")
        self.moeda_origem.set("USD")
        
        
        
        ttk.Label(frame_principal, text="Para:").grid(row=2, column=0, sticky="w")
        self.moeda_destino = ttk.Combobox(frame_principal, values=self.moedas)
        self.moeda_destino.grid(row=2, column=1, sticky='ew')
        self.moeda_destino.set("EUR")
        
        
        botao_converter = ttk.Button(frame_principal, text="Converter", command=self.converter) 
        botao_converter.grid(row=3, column=0, columnspan=2, pady=10)
        
        
        self.rotulo_resultado = ttk.Label(frame_principal, text="", font=("Arial", 14))
        self.rotulo_resultado.grid(row=4, column=0, columnspan=2 )
        
        
        ttk.Label(frame_principal, text="Favoritos:").grid(row=5, column=0, sticky="w")
        self.var_favorito = tk.StringVar()
        self.menu_favoritos = ttk.Combobox(frame_principal, textvariable=self.var_favorito, values=self.favoritos)
        self.menu_favoritos.grid(row=5, column=1, sticky="ew")
        self.menu_favoritos.bind("<<ComboboxSelected>>", self.carregar_favorito)
        
        
        
        botao_adicionar = ttk.Button(frame_principal, text="Adicionar Favorito", command=self.adicionar_favorito)
        botao_adicionar.grid(row=6, column=0, pady=5)
        
        
        botao_remover = ttk.Button(frame_principal, text="Remover favorito", command=self.remover_favorito)
        botao_remover.grid(row=6, column=1, pady=5)
        
        
        botao_historico = ttk.Button(frame_principal, text="Ver Dados Históricos", command=self.mostrar_historico)
        botao_historico.grid(row=7, column=0, columnspan=2, pady=10)
        
        frame_principal.columnconfigure(1, weight=1)
        frame_principal.rowconfigure(7, weight=1)
        
    def converter(self):
        """Realiza a conversão de moedas"""
        try:
            valor = float(self.entrada_valor.get())
            moeda_origem = self.moeda_origem.get()
            moeda_destino = self.moeda_destino.get()
            
            taxa = self.obter_taxa_cambio(moeda_origem, moeda_destino)
            if taxa:
                resultado = valor * taxa
                self.rotulo_resultado.config(text=f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido")
            
            
    def adicionar_favorito(self):
        """Adiciona o par atual aos favoritos"""
        par = f"{self.moeda_origem.get()}-{self.moeda_destino.get()}"
        if par not in self.favoritos:
            self.favoritos.append(par)
            self.salvar_favoritos()
            self.menu_favoritos['values'] = self.favoritos
            messagebox.showinfo("Sucesso", "Adicionado aos favoritos!")
            
    def carregar_favorito(self, event):
        """Carrega um par favorito"""
        selecionado = self.var_favorito.get()
        if selecionado: 
            moeda_origem, moeda_destino = selecionado.split('-')
            self.moeda_origem.set(moeda_origem)
            self.moeda_destino.set(moeda_destino)
            
            
    def remover_favorito(self):
        selecionado = self.var_favorito.get()
        if selecionado in self.favoritos:
            self.favoritos.remove(selecionado)
            self.salvar_favoritos()
            self.menu_favoritos['values'] = self.favoritos
            messagebox.showinfo("Sucesso", "Favorito removido!")
    
    
    
    
    
    def mostrar_historico(self):
        """Mostra as taxas históricas em uma nova Janela"""
        moeda = self.moeda_origem.get()
        if not moeda:
            messagebox.showerror("Erro", "Selecione uma moeda primeiro")
            return
        moeda = self.moeda_origem.get()
        datas, taxas = self.obter_historico_taxas(moeda)
        
        
        
        
        figura = plt.Figure(figsize=(8, 4), dpi=100)
        ax = figura.add_subplot(111)
        ax.plot(datas, taxas, marker='o', linestyle='-', color='b')
        ax.set_title(f"Taxas Históricas para {moeda}")
        ax.set_xlabel("Data", labelpad=10)
        ax.set_ylabel("Taxa de Câmbio", labelpad=10)
        plt.setp(ax.get_xticklabels(), rotation= 45, ha='right')
        
        
        plt.xticks(rotation=45)
        
        ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.4f'))
        
        
        
        figura.autofmt_xdate()
        
        
        
        janela_historico = tk.Toplevel(self.root)
        janela_historico.title(f"Taxas Históricas - {moeda}")
        
        canvas = FigureCanvasTkAgg(figura, master=janela_historico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
     
    




if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = ConversorDeMoedas(root)
    root.mainloop()



        
        
        
    
    
        
        
        
        
    
        
        
        
        
        

    
        
        
