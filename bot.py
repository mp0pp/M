import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

# رقم حساب الأدمن
ADMIN_ID = 6721093406


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في بوت إدارة القناة\n\n"
        "📢 بونصات ولفات مجانيه\n\n"
        "🤖 البوت يعمل بنجاح 🚀"
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # السماح للأدمن فقط
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ ليس لديك صلاحية استخدام لوحة الإدارة.")
        return

    keyboard = [
        [
            InlineKeyboardButton("📢 نشر منشور", callback_data="publish"),
            InlineKeyboardButton("📊 الإحصائيات", callback_data="stats"),
        ],
        [
            InlineKeyboardButton("🔗 روابط الدعوة", callback_data="invites"),
            InlineKeyboardButton("🏆 المتصدرين", callback_data="leaders"),
        ],
        [
            InlineKeyboardButton("📌 تثبيت منشور", callback_data="pin"),
            InlineKeyboardButton("🗑 حذف منشور", callback_data="delete"),
        ],
    ]

    await update.message.reply_text(
        "👑 لوحة إدارة القناة\n\n"
        "اختر العملية التي تريد تنفيذها:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # الأدمن فقط
    if query.from_user.id != ADMIN_ID:
        await query.answer("⛔ غير مسموح", show_alert=True)
        return

    if query.data == "publish":
        text = (
            "📢 نشر منشور\n\n"
            "هذه الوظيفة قيد التجهيز.\n"
            "سنضيف لاحقاً إرسال المنشور مباشرة إلى القناة."
        )

    elif query.data == "stats":
        text = (
            "📊 الإحصائيات\n\n"
            "سنضيف هنا عدد الأعضاء والإحالات وغيرها."
        )

    elif query.data == "invites":
        text = (
            "🔗 روابط الدعوة\n\n"
            "سنضيف هنا إنشاء وإدارة روابط الإحالة."
        )

    elif query.data == "leaders":
        text = (
            "🏆 المتصدرين\n\n"
            "سنضيف هنا قائمة أكثر الأشخاص إحالة."
        )

    elif query.data == "pin":
        text = (
            "📌 تثبيت منشور\n\n"
            "هذه الوظيفة قيد التجهيز."
        )

    elif query.data == "delete":
        text = (
            "🗑 حذف منشور\n\n"
            "هذه الوظيفة قيد التجهيز."
        )

    else:
        text = "❓ أمر غير معروف."

    await query.edit_message_text(text)


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN غير موجود")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
