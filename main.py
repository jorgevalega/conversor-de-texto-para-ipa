import customtkinter as ctk
import eng_to_ipa as ipa
import pyttsx3

# Configuração de aparência
ctk.set_appearance_mode('dark')

# Inicialização do mecanismo de síntese de voz
engine = pyttsx3.init()

# Configurar voz em inglês e ajustar velocidade
def configurar_voz_ingles():
    for voice in engine.getProperty('voices'):
        if 'en' in voice.languages or 'English' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 120)  # Ajustar velocidade da fala (padrão é cerca de 200)

configurar_voz_ingles()

# Funcionalidade principal
def converter_para_ipa():
    texto_digitado = entrada_texto.get()
    texto_ipa = ipa.convert(texto_digitado)
    texto_original_label.configure(text=texto_digitado, text_color='white')
    resultado_ipa_label.configure(text=texto_ipa, text_color='green')
    entrada_texto.delete(0, 'end')

def ouvir_pronuncia():
    texto_para_falar = texto_original_label.cget("text")
    if texto_para_falar:
        engine.say(texto_para_falar)
        engine.runAndWait()

# Janela principal
app = ctk.CTk()
app.title('Conversor de Texto para IPA')
app.geometry('600x250')

# Rótulos e campo de entrada
rotulo_texto = ctk.CTkLabel(app, text='Texto para converter:')
rotulo_texto.pack(pady=5)

entrada_texto = ctk.CTkEntry(app, placeholder_text='Digite seu texto aqui', width=500)
entrada_texto.pack(pady=10)

# Botões
botao_converter = ctk.CTkButton(app, text='Converter para IPA', command=converter_para_ipa)
botao_converter.pack(pady=10)

botao_ouvir = ctk.CTkButton(app, text='Ouvir Pronúncia', command=ouvir_pronuncia)
botao_ouvir.pack(pady=10)

# Rótulos de saída
texto_original_label = ctk.CTkLabel(app, text='')
texto_original_label.pack(pady=0)

resultado_ipa_label = ctk.CTkLabel(app, text='')
resultado_ipa_label.pack(pady=0)

# Executar o aplicativo
app.mainloop()
