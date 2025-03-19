from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler

TOKEN = "7986044887:AAGKRw8_EGIQQRf-r4dqe0bFDsf7aZvnaQQ"

# Función para responder al comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy un bot que repite lo que dices. ¡Escríbeme algo!")

# Función de Echo: Responde con el mismo mensaje que recibecd
async def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    await update.message.reply_text(f"Tú dijiste: {user_text}")

# Configuración del bot
app = Application.builder().token(TOKEN).build()

# Agregar manejadores (Handlers)
app.add_handler(CommandHandler("start", start))  # Maneja el comando /start
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Maneja cualquier mensaje de texto

# Iniciar el bot en modo polling (escucha mensajes constantemente)
print("🤖 Bot de Echo iniciado...")
app.run_polling()
