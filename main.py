import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os
TOKEN = os.environ.get("BOT_TOKEN", "8893438802:AAFbz9lOC4JL1lQkKPYkOIHW-pPEhGt6EXg")
print("BOT_TOKEN exists:", bool(TOKEN))
print("BOT_TOKEN length:", len(TOKEN) if TOKEN else 0)
print("BOT_TOKEN preview:", TOKEN[:10] if TOKEN else None)

logging.basicConfig(level=logging.INFO)

# ===== СТАРТ С КАРТИНКОЙ =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📅 День 1 — Модель и система", callback_data="day1")],
        [InlineKeyboardButton("📅 День 2 — Аналитика и управление", callback_data="day2")],
        [InlineKeyboardButton("📅 День 3 — Road Map и защита", callback_data="day3")],
    ]
    with open("welcome.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption="Выбери день адаптации 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def back_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📅 День 1 — Модель и система", callback_data="day1")],
        [InlineKeyboardButton("📅 День 2 — Аналитика и управление", callback_data="day2")],
        [InlineKeyboardButton("📅 День 3 — Road Map и защита", callback_data="day3")],
    ]
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))

# ===== ДЕНЬ 1 — ГЛАВНОЕ МЕНЮ =====
async def day1_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📋 Расписание дня", callback_data="day1_schedule")],
        [InlineKeyboardButton("📗 Блок 1 — Модель ImproSales", callback_data="day1_b1")],
        [InlineKeyboardButton("📗 Блок 2 — Операционная карта", callback_data="day1_b2")],
        [InlineKeyboardButton("📗 Блок 3 — Хаотичный проект", callback_data="day1_b3")],
        [InlineKeyboardButton("📗 Блок 4 — Папка проекта", callback_data="day1_b4")],
        [InlineKeyboardButton("📗 Блок 5 — Реестр материалов", callback_data="day1_b5")],
        [InlineKeyboardButton("📗 Блок 6 — Карта участников", callback_data="day1_b6")],
        [InlineKeyboardButton("📗 Блок 7 — Запрос материалов", callback_data="day1_b7")],
        [InlineKeyboardButton("📗 Блок 8 — Взаимодействие ОКК", callback_data="day1_b8")],
        [InlineKeyboardButton("📗 Блок 9 — Управленческие кейсы", callback_data="day1_b9")],
        [InlineKeyboardButton("📗 Блок 10 — Вывод дня", callback_data="day1_b10")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_main")],
    ]
    await query.edit_message_caption(caption="📅 День 1 — Модель и система\n\nВыбери блок:", reply_markup=InlineKeyboardMarkup(keyboard))

# ===== ДЕНЬ 1 — РАСПИСАНИЕ =====
async def day1_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📋 Расписание — День 1\n\n"
        "09:30–10:30 — Блок 1: Модель ImproSales\n"
        "10:30–11:20 — Блок 2: Операционная карта\n"
        "11:20–12:30 — Блок 3: Хаотичный проект\n"
        "12:30–13:00 — 🍽 Перерыв\n"
        "13:00–13:30 — Блок 4: Папка проекта\n"
        "13:30–14:20 — Блок 5: Реестр материалов\n"
        "14:20–15:00 — Блок 6: Карта участников\n"
        "15:00–15:30 — Блок 7: Запрос материалов\n"
        "15:30–16:30 — Блок 8: Взаимодействие ОКК\n"
        "16:30–17:30 — Блок 9: Управленческие кейсы\n"
        "17:30–17:45 — Блок 10: Вывод дня\n"
        "17:45–18:00 — Защита дня перед тренером"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 1 =====
async def day1_b1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b1_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b1_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 1 — Модель ImproSales\n⏰ 09:30–10:30\n\nИзучи материалы по модели ImproSales и письменно ответь на вопросы.\n\n👆 Сначала открой материалы, потом переходи к заданию.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b1_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 1\n\n"
        "Изучи в таком порядке:\n\n"
        "1️⃣ ДИ РОП — роль, KPI, дашборд, Road Map, ОКК:\n"
        "https://docs.google.com/document/d/1vZ_lbRrIqD6F24sWxpxgKGIh0uepQ8GA/edit\n\n"
        "2️⃣ Положение о KPI РОП:\n"
        "https://docs.google.com/document/d/1ruv9MhAAxzguqo77cQ-Wp6tqUmTt6cRLM6zJ_XQtHzY/edit\n\n"
        "3️⃣ Положение о грейдинговой системе:\n"
        "https://docs.google.com/document/d/1Vav4STwwQTE6um7cIA_RyC5oaYJgF1MBmTjZmhxe-Eo/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b1_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b1")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b1_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 1: Модель ImproSales\n\n"
        "Ответь письменно на 8 вопросов в Excel файле:\n\n"
        "1. Что такое «РОП в аренду» в модели ImproSales?\n"
        "2. Чем РОП ImproSales отличается от штатного РОПа клиента?\n"
        "3. За что РОП отвечает перед ImproSales?\n"
        "4. За что РОП отвечает перед клиентом?\n"
        "5. Какие ошибки РОПа могут навредить проекту и компании?\n"
        "6. Какие ключевые инструменты должен использовать РОП?\n"
        "7. Когда РОП должен подключать ОКК, бизнес-тренера, интегратора или ментора?\n"
        "8. Как ты понимаешь роль тренера в адаптации и роль ментора после адаптации?\n\n"
        "⚠️ Важно: показывай своё понимание, а не пересказ текста!"
    )
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b1")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 2 =====
async def day1_b2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b2_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 2 — Операционная карта\n⏰ 10:30–11:20\n\nМатериалы уже изучены в Блоке 1.\nПереходи сразу к заданию.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b2_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 2: Операционная карта\n\n"
        "Разложи работу РОПа по периодичности в Excel файле.\n"
        "По каждому действию укажи: зачем нужно, риск если не делать.\n\n"
        "Ежедневно:\n"
        "• Проведение планёрки\n"
        "• Контроль план/факт\n"
        "• Контроль входящих лидов\n"
        "• Контроль сделок и следующих шагов\n"
        "• Отписка в рабочие группы\n\n"
        "Еженедельно:\n"
        "• Разбор воронки\n"
        "• One-to-One с менеджерами\n"
        "• Работа с ОКК\n"
        "• Работа с отказниками\n"
        "• Контроль Road Map\n\n"
        "Ежемесячно:\n"
        "• Месячный отчёт собственнику\n"
        "• Анализ KPI РОПа\n"
        "• Актуализация Road Map\n"
        "• Ролевые тренировки с МОПами\n"
        "• Отчёт по качеству МОП"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b2")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 3 =====
async def day1_b3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b3_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b3_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 3 — Хаотичный проект\n⏰ 11:20–12:30\n\nТы входишь в учебный проект TopGlass — компания по производству стекла и зеркал.\n\n👆 Сначала изучи регламент, потом делай задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b3_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 3\n\n"
        "Изучи перед заданием:\n\n"
        "📄 Регламент внедрения РОПа в проект\n"
        "(как входить в новый проект, что собирать, какие дефициты искать)\n\n"
        "https://docs.google.com/document/d/1Bo7IPqwWtIffISl63lp9vrbO6cOima_r/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b3_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b3")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b3_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 3: Хаотичный проект\n\n"
        "Разбери вводные по учебному проекту TopGlass.\n"
        "Заполни таблицу дефицитов в Excel файле.\n\n"
        "По каждому пункту укажи:\n"
        "• Что не так\n"
        "• Критичность\n"
        "• Кто должен предоставить\n"
        "• Срок\n"
        "• Риск если не закрыть\n"
        "• Первое действие РОПа\n\n"
        "Что есть в проекте:\n"
        "📌 План продаж — есть, но без декомпозиции\n"
        "📌 Факт продаж — только за текущий месяц\n"
        "📌 Воронка — есть, но этапы размытые\n"
        "📌 Скрипты — есть старые\n"
        "📌 Мотивация менеджеров — есть устно, файла нет\n"
        "📌 Портрет клиента — нет\n"
        "📌 Конкуренты — нет\n"
        "📌 Road Map — нет\n"
        "📌 Дашборд — нет"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b3")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 4 =====
async def day1_b4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b4_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 4 — Папка проекта\n⏰ 13:00–13:30\n\n👆 Сначала изучи регламент и шаблоны, потом делай задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b4_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 4\n\n"
        "1️⃣ Регламент ведения проектной документации:\n"
        "https://docs.google.com/document/d/1T7SJFDSIs9SnTZ9ZE1fXoma_7EOKneem/edit\n\n"
        "2️⃣ Шаблоны для первичных работ:\n"
        "https://drive.google.com/drive/folders/1z38TSfrubwF0X9LAb_Fo28-eVovhbp7T"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b4")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b4_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 4: Папка проекта\n\n"
        "Собери правильную структуру папки проекта TopGlass в Excel файле.\n\n"
        "По каждой папке укажи:\n"
        "• Что должно лежать внутри\n"
        "• Зачем нужно РОПу\n"
        "• Риск если отсутствует\n\n"
        "Папки:\n"
        "📁 Адаптация\n"
        "📁 Воронка\n"
        "📁 Коммерция\n"
        "📁 Месячный отчёт\n"
        "📁 Мотивационная схема\n"
        "📁 ОКК\n"
        "📁 Портрет клиента\n"
        "📁 Прайс / КП / презентации\n"
        "📁 Скрипты\n"
        "📁 Сравнение с конкурентами\n"
        "📁 HR\n"
        "📁 Реестр материалов\n"
        "📁 Road Map\n"
        "📁 Дашборд\n"
        "📁 Архив / неактуально"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b4")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 5 =====
async def day1_b5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b5_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b5_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 5 — Реестр материалов\n⏰ 13:30–14:20\n\n👆 Сначала изучи шаблон реестра, потом делай задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b5_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 5\n\n"
        "📄 Единый реестр документов (с примером):\n"
        "https://docs.google.com/spreadsheets/d/1vrEcTUlyzWX4icnbyWyw29nuQOGYkCOz/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b5_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b5")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b5_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 5: Реестр материалов\n\n"
        "Зафиксируй все материалы проекта TopGlass в реестре.\n\n"
        "По каждому материалу укажи:\n"
        "• Статус (есть / нет / частично)\n"
        "• Критичность\n"
        "• Ответственный за предоставление\n"
        "• Срок\n"
        "• Место хранения\n\n"
        "⚠️ Фиксируй без дублей, чётко и по делу."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b5")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 6 =====
async def day1_b6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b6_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b6_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 6 — Карта участников\n⏰ 14:20–15:00\n\n👆 Сначала изучи шаблон, потом делай задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b6_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 6\n\n"
        "📄 Карта участников проекта (шаблон):\n"
        "https://docs.google.com/spreadsheets/d/1a6kfLHszgdpJ_gNuBb40imYKs7Yo3zHf/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b6_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b6")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b6_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 6: Карта участников\n\n"
        "Определи участников проекта TopGlass в Excel файле.\n\n"
        "По каждому участнику укажи:\n"
        "• Роль\n"
        "• Влияние на продажи\n"
        "• Что нужно от него\n"
        "• Риск\n"
        "• Формат взаимодействия\n\n"
        "Участники:\n"
        "👤 Собственник\n"
        "👤 Куратор проекта\n"
        "👤 Действующий руководитель\n"
        "👤 Маркетолог\n"
        "👤 HR\n"
        "👤 ОКК\n"
        "👤 Бухгалтерия\n"
        "👤 CRM-специалист\n"
        "👤 Менеджеры 1, 2, 3\n"
        "👤 Бизнес-тренер"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b6")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 7 =====
async def day1_b7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b7_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 7 — Запрос материалов\n⏰ 15:00–15:30\n\nНа основе разбора хаотичного проекта пишешь деловое сообщение собственнику TopGlass.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b7_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 7: Запрос материалов\n\n"
        "Напиши деловое сообщение собственнику TopGlass.\n\n"
        "В сообщении должно быть:\n"
        "• Какие материалы отсутствуют\n"
        "• Почему они критичны\n"
        "• Какой риск если не предоставят\n"
        "• Конкретный срок\n"
        "• Следующий шаг\n\n"
        "⚠️ Не обвиняй — фиксируй факты.\n"
        "Тон: деловой, уважительный, конкретный."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b7")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 8 =====
async def day1_b8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы для изучения", callback_data="day1_b8_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b8_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 8 — Взаимодействие с ОКК\n⏰ 15:30–16:30\n\n👆 Сначала изучи регламент РОП-ОКК, потом делай задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b8_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 8\n\n"
        "📄 Регламент РОП–ОКК:\n"
        "Скоро появится\n\n"
        "Пока ознакомься с отчётом ОКК который получишь в задании."
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day1_b8_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1_b8")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day1_b8_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 8: Взаимодействие с ОКК\n\n"
        "Ты получил отчёт от ОКК по проекту TopGlass.\n\n"
        "Ключевые выводы ОКК:\n"
        "✅ Плюсы: высокая техническая компетентность менеджеров, быстрые расчёты\n"
        "⚠️ Проблемы: клиенты пропадают после цены, нет фиксации следующего шага, слабый дожим на «я подумаю», анкетный стиль общения\n\n"
        "Ответь в Excel файле на вопросы:\n"
        "• Ключевой вывод из ОС ОКК\n"
        "• Что является главной проблемой\n"
        "• Какие задачи поставить менеджерам\n"
        "• Что изменить в коммуникации после цены\n"
        "• Как отработать фразу «я подумаю»\n"
        "• Какой контроль внедрить на неделю\n"
        "• Какой результат должен измениться через 7–14 дней"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b8")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 9 =====
async def day1_b9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b9_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 9 — Управленческие кейсы\n⏰ 16:30–17:30\n\nРеши 3 жизненных кейса из работы РОПа.\nПокажи стержень, инициативу и способность держать давление.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b9_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 9: Управленческие кейсы\n\n"
        "По каждому кейсу напиши: решение, первые 3 действия, риски.\n\n"
        "Кейс 1 — Тяжёлый собственник:\n"
        "Собственник TopGlass резко пишет что РОП ничего не меняет, денег нет, команда не верит. Требует результат завтра.\n\n"
        "Кейс 2 — Старички подрывают авторитет:\n"
        "Два опытных менеджера говорят команде «очередной РОП пришёл учить, но ничего не понимает в стекле». Новички начинают слушать их.\n\n"
        "Кейс 3 — Действовать без информации:\n"
        "Клиент ждёт действий, данные не предоставлены, собственник торопит, менеджеры говорят разное, времени на диагностику нет."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b9")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== БЛОК 10 =====
async def day1_b10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day1_b10_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day1")],
    ]
    await query.edit_message_caption(
        caption="📗 Блок 10 — Вывод дня\n⏰ 17:30–17:45\n\nПосле этого — защита перед тренером в 17:45.\n\nПо итогу дня также изучи оргструктуру ImproSales:\nhttps://docs.google.com/document/d/1a4-ZfENS1R7yBM_MYx2wlRflWxsI2qtWb0sJZ5KBbvM/edit",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day1_b10_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 10: Вывод дня\n\n"
        "Сформируй итоговый вывод по первому дню.\nНапиши 7–10 предложений в Excel файле.\n\n"
        "Ответь на вопросы:\n"
        "• Что я понял о роли РОПа ImproSales?\n"
        "• Какие документы критичны перед стартом проекта?\n"
        "• Какие риски если проект не структурирован?\n"
        "• Что я понял по взаимодействию с ОКК?\n"
        "• Какие первые действия РОП должен сделать перед выходом на клиента?\n"
        "• Где мне нужна дополнительная ясность?\n"
        "• Что бы я изменил?\n\n"
        "⚠️ Тренер должен увидеть самоанализ и управленческую зрелость."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day1_b10")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== ДЕНЬ 2 =====
async def day2_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📋 Расписание дня", callback_data="day2_schedule")],
        [InlineKeyboardButton("📊 Блок 1 — Изучение кейса TopGlass", callback_data="day2_b1")],
        [InlineKeyboardButton("📊 Блок 2 — Расчёт плана", callback_data="day2_b2")],
        [InlineKeyboardButton("📊 Блок 3 — Анализ дефицита", callback_data="day2_b3")],
        [InlineKeyboardButton("📊 Блок 4 — Анализ воронки", callback_data="day2_b4")],
        [InlineKeyboardButton("📊 Блок 5 — Определение КЭВ", callback_data="day2_b5")],
        [InlineKeyboardButton("📊 Блок 6 — Потенциал сделок", callback_data="day2_b6")],
        [InlineKeyboardButton("📊 Блок 7 — План 72 часа", callback_data="day2_b7")],
        [InlineKeyboardButton("📊 Блок 8 — Планёрка", callback_data="day2_b8")],
        [InlineKeyboardButton("📊 Блок 9 — Кейсы по МОП", callback_data="day2_b9")],
        [InlineKeyboardButton("📊 Блок 10 — One-to-One", callback_data="day2_b10")],
        [InlineKeyboardButton("📊 Блок 11 — Ролевка", callback_data="day2_b11")],
        [InlineKeyboardButton("📊 Блок 12 — Вечерний отчёт", callback_data="day2_b12")],
        [InlineKeyboardButton("📊 Блок 13 — Вывод дня", callback_data="day2_b13")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_main")],
    ]
    await query.edit_message_caption(caption="📅 День 2 — Аналитика и управление\n\nВыбери блок:", reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📋 Расписание — День 2\n\n"
        "09:00–09:30 — Блок 1: Изучение кейса TopGlass\n"
        "09:30–10:30 — Блок 2: Расчёт плана\n"
        "10:30–11:15 — Блок 3: Анализ дефицита\n"
        "11:15–12:00 — Блок 4: Анализ воронки\n"
        "12:00–12:30 — Блок 5: Определение КЭВ\n"
        "12:30–13:00 — 🍽 Перерыв\n"
        "13:00–13:45 — Блок 6: Потенциал сделок\n"
        "13:45–14:30 — Блок 7: План 72 часа\n"
        "14:30–15:00 — Блок 8: Планёрка\n"
        "15:00–15:45 — Блок 9: Кейсы по МОП\n"
        "15:45–16:15 — Блок 10: One-to-One\n"
        "16:15–16:45 — Блок 11: Ролевка\n"
        "16:45–17:15 — Блок 12: Вечерний отчёт\n"
        "17:15–17:35 — Блок 13: Вывод дня\n"
        "17:35–18:00 — Защита дня перед тренером"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b1_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b1_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 1 — Изучение кейса TopGlass\n⏰ 09:00–09:30\n\nИзучи вводные по проекту и зафикcируй первичную ситуацию.\n\n👆 Сначала материалы, потом задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b1_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 1\n\n"
        "1️⃣ Положение о KPI РОП:\n"
        "https://docs.google.com/document/d/1ruv9MhAAxzguqo77cQ-Wp6tqUmTt6cRLM6zJ_XQtHzY/edit\n\n"
        "2️⃣ Методология поиска дефицита:\n"
        "https://docs.google.com/document/d/1hmYbyEjV_8B3HCbhUZ_7LBeHChXeMEhc/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b1_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b1")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b1_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 1: Изучение кейса\n\n"
        "📊 Вводные TopGlass:\n"
        "• План месяца: 25 000 000 ₸\n"
        "• Факт на 10-й день: 8 000 000 ₸\n"
        "• Осталось дней: 12\n"
        "• Чек B2C: 60 000 ₸ | Чек B2B: 250 000 ₸\n"
        "• Конверсия: 25% (цель 35%)\n"
        "• Лидов: 160 (в работе 120, некачественных 40)\n\n"
        "Ответь в Excel файле:\n"
        "• Где проект по план/факту?\n"
        "• Какие первые признаки отставания?\n"
        "• Какие данные считать в первую очередь?\n"
        "• Гипотеза по основной проблеме?\n"
        "• Какие риски из запроса собственника?"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b1")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b2_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 2 — Расчёт плана\n⏰ 09:30–10:30\n\nМатериалы уже изучены в Блоке 1.\nПереходи к расчётам.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b2_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 2: Расчёт плана\n\n"
        "Посчитай в Excel файле:\n\n"
        "• % выполнения плана = факт / план\n"
        "• Остаток до плана = план - факт\n"
        "• Нужный дневной темп = остаток / 12 дней\n"
        "• Продаж B2C нужно = остаток / 60 000\n"
        "• Продаж B2B нужно = остаток / 250 000\n"
        "• Лидов при текущей конверсии 25%\n"
        "• Лидов при целевой конверсии 35%\n"
        "• Доля некачественных лидов\n\n"
        "⚠️ На выходе: таблица расчёта + короткий вывод за счёт чего закрывать дефицит."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b2")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b3_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 3 — Анализ дефицита\n⏰ 10:30–11:15\n\nОпредели главные причины отставания проекта.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b3_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 3: Анализ дефицита\n\n"
        "Разбери каждую зону в Excel файле:\n\n"
        "• Количество лидов — 160 за 10 дней\n"
        "• Качество лидов — 40 из 160 некачественные\n"
        "• Передача в работу — 120 из 160\n"
        "• Конверсия — 25% vs цель 35%\n"
        "• Средний чек B2C — 60 000 ₸\n"
        "• Средний чек B2B — 250 000 ₸\n"
        "• B2C/B2B микс — чеки сильно отличаются\n"
        "• Обработка и дожим — клиенты пропадают после цены\n\n"
        "По каждой зоне: гипотеза → что проверить → первое действие\n\n"
        "⚠️ На выходе: 2-3 главные причины отставания."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b3")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b4_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 4 — Анализ воронки\n⏰ 11:15–12:00\n\n👆 Сначала материалы, потом задание.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b4_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 4\n\n"
        "📄 Стандарт работы РОП ImproSales (ДИ РОП):\n"
        "https://docs.google.com/document/d/1vZ_lbRrIqD6F24sWxpxgKGIh0uepQ8GA/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b4")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b4_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 4: Анализ воронки\n\n"
        "Разбери воронку TopGlass в Excel файле.\n\n"
        "По каждому этапу: что не работает → почему влияет на деньги → действие РОПа\n\n"
        "Этапы:\n"
        "• Входящий лид\n"
        "• Квалификация\n"
        "• Консультация\n"
        "• Замер / КЭВ\n"
        "• КП / расчёт\n"
        "• Согласование\n"
        "• Оплата\n"
        "• Отказ\n"
        "• Повторное касание\n"
        "• B2B-процесс\n\n"
        "⚠️ Известные проблемы: клиенты пропадают после цены, замеры нестабильны, B2B = B2C."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b4")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b5_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 5 — Определение КЭВ\n⏰ 12:00–12:30\n\nОпредели ключевой этап воронки для B2C и B2B.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b5_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 5: Определение КЭВ\n\n"
        "Ответь в Excel файле:\n\n"
        "• Какой КЭВ для B2C?\n"
        "• Почему этот этап влияет на оплату?\n"
        "• Какой КЭВ для B2B?\n"
        "• Почему B2B нельзя вести как B2C?\n"
        "• Что должен делать менеджер чтобы довести до КЭВ?\n"
        "• Как РОП контролирует КЭВ?\n"
        "• Какая метрика показывает движение к оплате?\n\n"
        "⚠️ КЭВ — это этап после которого клиент с высокой вероятностью платит."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b5")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b6_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 6 — Потенциал сделок\n⏰ 13:00–13:45\n\nРасставь приоритеты по 8 клиентам TopGlass.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b6_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 6: Потенциал сделок\n\n"
        "Расставь приоритеты A/B/C и определи действия:\n\n"
        "Клиент 1 — B2C — 480 000 ₸ — получил КП, думает\n"
        "Клиент 2 — B2B — 1 800 000 ₸ — запросил условия партнёрства\n"
        "Клиент 3 — B2C — 220 000 ₸ — сказал дорого после цены\n"
        "Клиент 4 — B2B — 2 500 000 ₸ — нужна встреча с ЛПР\n"
        "Клиент 5 — B2C — 90 000 ₸ — не отвечает после расчёта\n"
        "Клиент 6 — B2B — 1 200 000 ₸ — сравнивает с конкурентом\n"
        "Клиент 7 — B2C — 350 000 ₸ — готов на замер, дата не назначена\n"
        "Клиент 8 — B2B — 3 000 000 ₸ — есть потребность, нет КП\n\n"
        "По каждому: приоритет → действие → срок → нужен ли РОП?"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b6")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b7_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 7 — План 72 часа\n⏰ 13:45–14:30\n\nСформируй план стабилизации TopGlass на 3 дня.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b7_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 7: План 72 часа\n\n"
        "Заполни таблицу в Excel файле.\n"
        "По каждому блоку: проблема → действие → ответственный → срок → метрика\n\n"
        "Блоки плана:\n"
        "• План/факт\n"
        "• B2B-потенциал\n"
        "• B2C-дожим\n"
        "• КЭВ / замеры\n"
        "• Конверсия\n"
        "• Возражение «дорого»\n"
        "• Менеджеры\n"
        "• Повторные касания\n"
        "• Контроль дня\n\n"
        "⚠️ Не общие слова — конкретные действия с цифрами и сроками."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b7")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b8_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b8_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 8 — Планёрка\n⏰ 14:30–15:00\n\nПодготовь повестку утренней планёрки для TopGlass.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b8_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 8\n\n"
        "📄 Регламент One-to-One:\n"
        "https://docs.google.com/document/d/1VkMWD3gXZO_8FVRJ2azLwq20SorFe8M7ggS9K__E5HY/edit\n\n"
        "📄 Тренинг по возражениям «Дорого»:\n"
        "https://docs.google.com/document/d/1SU3JbG0gBma_e5YNQWh5mlfnHHG5D9GV/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b8_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b8")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b8_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 8: Планёрка\n\n"
        "Подготовь повестку в Excel файле.\n\n"
        "Блоки планёрки:\n"
        "• Открытие\n"
        "• План/факт\n"
        "• Дефицит до плана\n"
        "• Фокус дня\n"
        "• Приоритетные B2B-сделки\n"
        "• Приоритетные B2C-сделки\n"
        "• КЭВ / замеры\n"
        "• Задачи по менеджерам\n"
        "• Повторные касания\n"
        "• Фиксация контроля\n\n"
        "По каждому блоку: что говорит РОП → задача команде → ожидаемый результат"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b8")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b9_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 9 — Кейсы по МОП\n⏰ 15:00–15:45\n\nРеши 6 управленческих кейсов по менеджерам.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b9_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 9: Кейсы по МОП\n\n"
        "По каждому кейсу: проблема → как проверить → решение → задача → контроль → риск\n\n"
        "Кейс 1: «Лиды плохие, продавать нечего»\n"
        "Кейс 2: Отправляет цену и ждёт пока клиент сам вернётся\n"
        "Кейс 3: Не предлагает замер — «клиент сам спросит»\n"
        "Кейс 4: Продаёт только через скидку\n"
        "Кейс 5: Не разделяет подход к B2B и B2C\n"
        "Кейс 6: Сильный менеджер но хаотичный — не фиксирует договорённости"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b9")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b10_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b10_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 10 — One-to-One\n⏰ 15:45–16:15\n\nПодготовь индивидуальную встречу с менеджером.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b10_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 10\n\n"
        "📄 Регламент One-to-One встречи:\n"
        "https://docs.google.com/document/d/1VkMWD3gXZO_8FVRJ2azLwq20SorFe8M7ggS9K__E5HY/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b10_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b10")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b10_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 10: One-to-One\n\n"
        "Подготовь план встречи с менеджером который отправляет цену и не ведёт клиента.\n\n"
        "Заполни в Excel:\n"
        "• Цель встречи\n"
        "• Какая проблема разбирается\n"
        "• Вопросы менеджеру\n"
        "• Обратная связь от РОПа\n"
        "• Задачи после встречи\n"
        "• Срок проверки\n"
        "• Ожидаемое изменение поведения\n"
        "• Как будет проверено выполнение"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b10")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b11_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b11_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 11 — Ролевка\n⏰ 16:15–16:45\n\nПодготовь сценарий ролевой тренировки.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b11_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 11\n\n"
        "📄 Шаблон ролевой тренировки:\n"
        "https://docs.google.com/document/d/1OHOTH7krPhAtONUtkmNVmPdIieyf0RFDlMc1DOSRS5E/edit\n\n"
        "📄 Тренинг «Дорого»:\n"
        "https://docs.google.com/document/d/1SU3JbG0gBma_e5YNQWh5mlfnHHG5D9GV/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b11_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b11")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b11_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 11: Ролевка\n\n"
        "Тема: «Цена отправлена — клиент говорит дорого / думает / пропадает»\n\n"
        "Подготовь сценарий в Excel:\n"
        "• Цель тренировки\n"
        "• Роль клиента\n"
        "• Роль менеджера\n"
        "• Вводная ситуация\n"
        "• Типовые реплики клиента\n"
        "• Правильная логика ответа менеджера\n"
        "• Как перевести к следующему шагу\n"
        "• Критерии оценки менеджера\n"
        "• Что фиксирует РОП после ролевки"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b11")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Материалы", callback_data="day2_b12_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b12_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 12 — Вечерний отчёт\n⏰ 16:45–17:15\n\nНапиши управленческий отчёт по TopGlass.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b12_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 12\n\n"
        "📄 Вечерний отчёт — стандарт (ВРВ):\n"
        "https://docs.google.com/spreadsheets/d/1e9ZXqvx7wNIsYX2giLVUMiLjD4edwrmScosD5WuNjlw/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day2_b12_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2_b12")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b12_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 12: Вечерний отчёт\n\n"
        "Напиши отчёт в Excel файле по структуре:\n\n"
        "• План месяца\n"
        "• Текущий факт\n"
        "• % выполнения\n"
        "• Дефицит\n"
        "• Ключевая причина отставания\n"
        "• Действия на 72 часа\n"
        "• Приоритетные сделки\n"
        "• Что будет сделано с менеджерами\n"
        "• Риски\n"
        "• Задачи на завтра\n\n"
        "⚠️ На выходе — финальный текст отчёта целиком."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b12")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day2_b13(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day2_b13_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day2")],
    ]
    await query.edit_message_caption(
        caption="📊 Блок 13 — Вывод дня\n⏰ 17:15–17:35\n\nПосле этого — защита перед тренером в 17:35.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day2_b13_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 13: Вывод дня\n\n"
        "Напиши вывод 7–10 предложений в Excel файле.\n\n"
        "Ответь на вопросы:\n"
        "• Где в TopGlass основная проблема?\n"
        "• Что нужно исправить в первую очередь?\n"
        "• Что может дать быстрый денежный эффект?\n"
        "• Какие действия вынести в Road Map на 30 дней?\n"
        "• Какие риски остаются даже после плана 72 часа?\n\n"
        "⚠️ Тренер должен увидеть управленческую логику и конкретику."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day2_b13")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== ДЕНЬ 3 =====
# ===== ДЕНЬ 3 =====
async def day3_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📋 Расписание дня", callback_data="day3_schedule")],
        [InlineKeyboardButton("📘 Блок 1 — Досье TopGlass", callback_data="day3_b1")],
        [InlineKeyboardButton("📘 Блок 2 — Анализ досье", callback_data="day3_b2")],
        [InlineKeyboardButton("📘 Блок 3 — Анализ конкурентов", callback_data="day3_b3")],
        [InlineKeyboardButton("📘 Блок 4 — Анализ SMM", callback_data="day3_b4")],
        [InlineKeyboardButton("📘 Блок 5 — Мотивация МОП", callback_data="day3_b5")],
        [InlineKeyboardButton("📘 Блок 6 — Road Map 30 дней", callback_data="day3_b6")],
        [InlineKeyboardButton("📘 Блок 7 — Soft: Собственник", callback_data="day3_b7")],
        [InlineKeyboardButton("📘 Блок 8 — Soft: Менеджер", callback_data="day3_b8")],
        [InlineKeyboardButton("📘 Блок 9 — Soft: Приоритеты", callback_data="day3_b9")],
        [InlineKeyboardButton("📘 Блок 10 — Критические кейсы", callback_data="day3_b10")],
        [InlineKeyboardButton("📘 Блок 11 — Защита Road Map", callback_data="day3_b11")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_main")],
    ]
    await query.edit_message_caption(caption="📅 День 3 — Road Map и защита\n\nВыбери блок:", reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📋 Расписание — День 3\n\n"
        "09:00–09:30 — Блок 1: Досье TopGlass\n"
        "09:30–10:10 — Блок 2: Анализ досье\n"
        "10:10–10:50 — Блок 3: Анализ конкурентов\n"
        "10:50–11:40 — Блок 4: Анализ SMM\n"
        "11:40–12:30 — Блок 5: Мотивация МОП\n"
        "12:30–13:00 — 🍽 Перерыв\n"
        "13:00–14:10 — Блок 6: Road Map 30 дней\n"
        "14:10–14:40 — Блок 7: Soft: Собственник\n"
        "14:40–15:10 — Блок 8: Soft: Менеджер\n"
        "15:10–15:40 — Блок 9: Soft: Приоритеты\n"
        "15:40–16:40 — Блок 10: Критические кейсы\n"
        "16:40–17:10 — Блок 11: Подготовка защиты\n"
        "17:10–17:40 — Защита Road Map\n"
        "17:40–18:00 — Итоговый портрет РОПа"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b1_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 1 — Досье TopGlass\n⏰ 09:00–09:30\n\nИзучи досье и зафикcируй ключевые вводные, проблемы и ограничения.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b1_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 1: Досье TopGlass\n\n"
        "📋 Ключевые вводные:\n"
        "• Компания: производство стекла и зеркал под заказ\n"
        "• B2C чек: 60 000 ₸ | B2B чек: 250 000 ₸\n"
        "• План: 25 000 000 ₸ | Факт (10й день): 8 000 000 ₸\n"
        "• Команда: 3 менеджера (сильный/дисциплинированный/слабый)\n\n"
        "❗️ Проблемы:\n"
        "• Слабое объяснение ценности после цены\n"
        "• Клиенты пропадают после КП\n"
        "• Замеры нестабильны\n"
        "• B2B обрабатывают как B2C\n"
        "• Причины отказов общие\n"
        "• ОКК без фокуса от РОПа\n"
        "• Нет Road Map и актуальных скриптов\n\n"
        "Зафикcируй пометки по досье в Excel файле."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b1")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b2_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 2 — Анализ досье\n⏰ 09:30–10:10\n\nВыдели проблемы, гипотезы, риски и быстрые действия.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b2_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 2: Анализ досье\n\n"
        "Заполни таблицу анализа в Excel файле.\n\n"
        "По каждой проблеме укажи:\n"
        "• Проблема\n"
        "• Гипотеза причины\n"
        "• Риск если не решить\n"
        "• Быстрое действие РОПа\n"
        "• Данные которых не хватает\n\n"
        "⚠️ На выходе: связка проблема → действие → результат."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b2")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b3_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 3 — Анализ конкурентов\n⏰ 10:10–10:50\n\nСравни TopGlass с двумя конкурентами и выведи действия для Road Map.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b3_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 3: Анализ конкурентов\n\n"
        "Найди двух конкурентов TopGlass в Алматы и заполни таблицу.\n\n"
        "Параметры сравнения:\n"
        "• Позиционирование\n"
        "• Скорость ответа\n"
        "• Цена\n"
        "• Упаковка КП\n"
        "• B2C подход\n"
        "• B2B подход\n"
        "• Доверие / кейсы\n"
        "• Сервис / замер\n\n"
        "По каждому параметру: TopGlass vs Конкурент 1 vs Конкурент 2 → вывод → действие для Road Map\n\n"
        "Итог: главный риск для TopGlass + что усилить."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b3")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 SMM отчёт", callback_data="day3_b4_mat")],
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 4 — Анализ SMM\n⏰ 10:50–11:40\n\nПроанализируй рекламный отчёт и подготовь рекомендации собственнику.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b4_mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📖 Материалы — Блок 4\n\n"
        "📄 SMM отчёт TopGlass за март:\n"
        "https://docs.google.com/document/d/1ukSqK59pjsOXRr1ZnXyhypxyDCHyKewq/edit"
    )
    keyboard = [
        [InlineKeyboardButton("✅ Перейти к заданию", callback_data="day3_b4_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3_b4")],
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b4_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 4: Анализ SMM\n\n"
        "Изучи отчёт и заполни таблицу в Excel файле.\n\n"
        "Задачи:\n"
        "• Отдели лиды от трафика\n"
        "• Найди сильные и слабые кампании\n"
        "• Рассчитай стоимость обращения по направлениям\n"
        "• Определи что масштабировать, что отключить\n\n"
        "На выходе:\n"
        "• Таблица анализа SMM\n"
        "• Рекомендации собственнику: что делать с рекламой\n\n"
        "⚠️ Смотри на связку маркетинг → продажи, а не только на рекламные цифры."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b4")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b5_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 5 — Мотивация МОП\n⏰ 11:40–12:30\n\nРазработай систему нематериальной мотивации на 30 дней.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b5_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 5: Мотивация МОП\n\n"
        "Заполни план в Excel файле.\n\n"
        "По каждому направлению укажи:\n"
        "• Проблема / зачем нужно\n"
        "• Конкретное действие РОПа\n"
        "• Как внедрить\n"
        "• Периодичность\n"
        "• Метрика эффекта\n"
        "• Риск / ограничение\n\n"
        "Направления мотивации:\n"
        "• Вовлечённость\n"
        "• Дисциплина\n"
        "• Фокус на КЭВ\n"
        "• Качество дожима\n"
        "• Командный дух\n\n"
        "Итог: 5-7 конкретных инструментов в единую систему.\n"
        "Вывод: какие 2-3 дадут самый быстрый эффект и почему?"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b5")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b6_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 6 — Road Map 30 дней\n⏰ 13:00–14:10\n\nСобери Road Map по итогам досье, Дня 2, конкурентов, SMM и мотивации.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b6_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 6: Road Map 30 дней\n\n"
        "Заполни Road Map в Excel файле.\n\n"
        "По каждому блоку укажи:\n"
        "• Блок (маркетинг / воронка / команда / ОКК / скрипты и т.д.)\n"
        "• Цель\n"
        "• Гипотеза / проблема\n"
        "• Конкретное действие\n"
        "• Ответственный\n"
        "• Срок\n"
        "• Приоритет A/B/C\n"
        "• Метрика успеха\n"
        "• Плановый результат\n\n"
        "⚠️ Не общие слова — конкретные действия с цифрами, сроками и метриками.\n"
        "Road Map будешь защищать перед тренером!"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b6")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b7_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 7 — Soft: Собственник\n⏰ 14:10–14:40\n\nРеши кейс коммуникации с собственником под давлением.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b7_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 7: Soft: Собственник\n\n"
        "💬 Кейс:\nСобственник пишет: «Лиды есть, менеджеры работают, но кассы нет. "
        "Мне не нужны таблицы — мне нужны деньги. Что вы конкретно сделаете за 3 дня?»\n\n"
        "Ответь в Excel файле:\n"
        "• Как признать проблему без оправданий\n"
        "• Какие факты и цифры использовать\n"
        "• Что обещаешь за 72 часа\n"
        "• Какие риски обозначаешь\n"
        "• Что просишь от собственника\n\n"
        "Итог: готовый текст ответа собственнику.\n\n"
        "⚠️ Не оправдывайся — говори фактами и действиями."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b7")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b8_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 8 — Soft: Менеджер\n⏰ 14:40–15:10\n\nПодготовь обратную связь менеджеру.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b8_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 8: Soft: Менеджер\n\n"
        "💬 Кейс:\nМенеджер говорит: «Я всё сделал: цену отправил. "
        "Если клиенту надо — сам вернётся. Не хочу давить, а то уйдёт.»\n\n"
        "Ответь в Excel файле:\n"
        "• В чём управленческая проблема\n"
        "• Какую обратную связь дашь\n"
        "• Какие вопросы задашь менеджеру\n"
        "• Какую задачу поставишь\n"
        "• Срок проверки\n"
        "• Какое изменение поведения ожидается\n\n"
        "Итог: готовая формулировка обратной связи.\n\n"
        "⚠️ Баланс: требовательность + конкретика + уважение."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b8")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b9_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 9 — Soft: Приоритеты\n⏰ 15:10–15:40\n\nРасставь приоритеты в ситуации одновременных срочных задач.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b9_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 9: Soft: Приоритеты\n\n"
        "💬 Кейс:\nОдновременно: собственник требует отчёт, менеджер просит скидку "
        "по крупной сделке, ОКК прислал критичную ошибку, два клиента ждут ответа, "
        "команда просит провести планёрку. Время ограничено.\n\n"
        "Ответь в Excel файле:\n"
        "• Расположи задачи по приоритету\n"
        "• Что сделаешь лично\n"
        "• Что делегируешь\n"
        "• Что отложишь и почему\n"
        "• Какие риски проконтролируешь\n"
        "• Как сообщишь собственнику и команде\n\n"
        "⚠️ Покажи управленческую логику — не распыляйся."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b9")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b10_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 10 — Критические кейсы\n⏰ 15:40–16:40\n\nРеши 8 сложных управленческих ситуаций.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b10_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 10: Критические кейсы\n\n"
        "По каждому кейсу: действия → кого подключить → что зафиксировать → что нельзя делать → риск\n\n"
        "Кейс 1: Массовый саботаж — 2-3 менеджера отказываются от новых правил\n"
        "Кейс 2: Эпидемия больничных — несколько МОП заболели, план горит\n"
        "Кейс 3: Отпуска в один период — несколько МОП просят одновременно\n"
        "Кейс 4: Ежемесячные больничные у одного сотрудника\n"
        "Кейс 5: Старички подрывают авторитет РОПа публично\n"
        "Кейс 6: Сотрудник на рабочем месте в состоянии опьянения\n"
        "Кейс 7: Сотрудница сообщает о беременности\n"
        "Кейс 8: Признаки воровства — клиенты уходят, оплата мимо компании\n\n"
        "⚠️ В юридически чувствительных ситуациях — не действуй самовольно!\n"
        "Эскалируй к руководству / HR / юристу."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b10")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

async def day3_b11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✅ Задание", callback_data="day3_b11_task")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="day3")],
    ]
    await query.edit_message_caption(
        caption="📘 Блок 11 — Защита Road Map\n⏰ 16:40–17:40\n\nПодготовь аргументацию и защити Road Map перед тренером.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def day3_b11_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "✅ Задание — Блок 11: Защита Road Map\n\n"
        "Подготовь тезисы защиты в Excel файле.\n\n"
        "Вопросы тренера на защите:\n"
        "• Какая главная проблема TopGlass?\n"
        "• Почему выбранный КЭВ является ключевым?\n"
        "• Какие 3 действия дадут быстрый денежный эффект?\n"
        "• Что в Road Map самое приоритетное и почему?\n"
        "• Какие задачи нельзя откладывать?\n"
        "• Какие риски по команде самые опасные?\n"
        "• Что контролируешь ежедневно?\n"
        "• Что согласовываешь с руководством / HR / юристом?\n"
        "• Какие зоны передаёшь ментору после адаптации?\n\n"
        "⚠️ После защиты тренер формирует твой итоговый портрет РОПа.\n"
        "Это финал адаптации — покажи управленческую зрелость! 💪"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="day3_b11")]]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

# ===== ЗАПУСК =====
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(back_main, pattern="^back_main$"))
    app.add_handler(CallbackQueryHandler(day1_menu, pattern="^day1$"))
    app.add_handler(CallbackQueryHandler(day1_schedule, pattern="^day1_schedule$"))
    app.add_handler(CallbackQueryHandler(day1_b1, pattern="^day1_b1$"))
    app.add_handler(CallbackQueryHandler(day1_b1_mat, pattern="^day1_b1_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b1_task, pattern="^day1_b1_task$"))
    app.add_handler(CallbackQueryHandler(day1_b2, pattern="^day1_b2$"))
    app.add_handler(CallbackQueryHandler(day1_b2_task, pattern="^day1_b2_task$"))
    app.add_handler(CallbackQueryHandler(day1_b3, pattern="^day1_b3$"))
    app.add_handler(CallbackQueryHandler(day1_b3_mat, pattern="^day1_b3_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b3_task, pattern="^day1_b3_task$"))
    app.add_handler(CallbackQueryHandler(day1_b4, pattern="^day1_b4$"))
    app.add_handler(CallbackQueryHandler(day1_b4_mat, pattern="^day1_b4_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b4_task, pattern="^day1_b4_task$"))
    app.add_handler(CallbackQueryHandler(day1_b5, pattern="^day1_b5$"))
    app.add_handler(CallbackQueryHandler(day1_b5_mat, pattern="^day1_b5_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b5_task, pattern="^day1_b5_task$"))
    app.add_handler(CallbackQueryHandler(day1_b6, pattern="^day1_b6$"))
    app.add_handler(CallbackQueryHandler(day1_b6_mat, pattern="^day1_b6_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b6_task, pattern="^day1_b6_task$"))
    app.add_handler(CallbackQueryHandler(day1_b7, pattern="^day1_b7$"))
    app.add_handler(CallbackQueryHandler(day1_b7_task, pattern="^day1_b7_task$"))
    app.add_handler(CallbackQueryHandler(day1_b8, pattern="^day1_b8$"))
    app.add_handler(CallbackQueryHandler(day1_b8_mat, pattern="^day1_b8_mat$"))
    app.add_handler(CallbackQueryHandler(day1_b8_task, pattern="^day1_b8_task$"))
    app.add_handler(CallbackQueryHandler(day1_b9, pattern="^day1_b9$"))
    app.add_handler(CallbackQueryHandler(day1_b9_task, pattern="^day1_b9_task$"))
    app.add_handler(CallbackQueryHandler(day1_b10, pattern="^day1_b10$"))
    app.add_handler(CallbackQueryHandler(day1_b10_task, pattern="^day1_b10_task$"))
    app.add_handler(CallbackQueryHandler(day2_menu, pattern="^day2$"))
    app.add_handler(CallbackQueryHandler(day3_menu, pattern="^day3$"))
    app.add_handler(CallbackQueryHandler(day2_schedule, pattern="^day2_schedule$"))
    app.add_handler(CallbackQueryHandler(day2_b1, pattern="^day2_b1$"))
    app.add_handler(CallbackQueryHandler(day2_b1_mat, pattern="^day2_b1_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b1_task, pattern="^day2_b1_task$"))
    app.add_handler(CallbackQueryHandler(day2_b2, pattern="^day2_b2$"))
    app.add_handler(CallbackQueryHandler(day2_b2_task, pattern="^day2_b2_task$"))
    app.add_handler(CallbackQueryHandler(day2_b3, pattern="^day2_b3$"))
    app.add_handler(CallbackQueryHandler(day2_b3_task, pattern="^day2_b3_task$"))
    app.add_handler(CallbackQueryHandler(day2_b4, pattern="^day2_b4$"))
    app.add_handler(CallbackQueryHandler(day2_b4_mat, pattern="^day2_b4_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b4_task, pattern="^day2_b4_task$"))
    app.add_handler(CallbackQueryHandler(day2_b5, pattern="^day2_b5$"))
    app.add_handler(CallbackQueryHandler(day2_b5_task, pattern="^day2_b5_task$"))
    app.add_handler(CallbackQueryHandler(day2_b6, pattern="^day2_b6$"))
    app.add_handler(CallbackQueryHandler(day2_b6_task, pattern="^day2_b6_task$"))
    app.add_handler(CallbackQueryHandler(day2_b7, pattern="^day2_b7$"))
    app.add_handler(CallbackQueryHandler(day2_b7_task, pattern="^day2_b7_task$"))
    app.add_handler(CallbackQueryHandler(day2_b8, pattern="^day2_b8$"))
    app.add_handler(CallbackQueryHandler(day2_b8_mat, pattern="^day2_b8_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b8_task, pattern="^day2_b8_task$"))
    app.add_handler(CallbackQueryHandler(day2_b9, pattern="^day2_b9$"))
    app.add_handler(CallbackQueryHandler(day2_b9_task, pattern="^day2_b9_task$"))
    app.add_handler(CallbackQueryHandler(day2_b10, pattern="^day2_b10$"))
    app.add_handler(CallbackQueryHandler(day2_b10_mat, pattern="^day2_b10_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b10_task, pattern="^day2_b10_task$"))
    app.add_handler(CallbackQueryHandler(day2_b11, pattern="^day2_b11$"))
    app.add_handler(CallbackQueryHandler(day2_b11_mat, pattern="^day2_b11_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b11_task, pattern="^day2_b11_task$"))
    app.add_handler(CallbackQueryHandler(day2_b12, pattern="^day2_b12$"))
    app.add_handler(CallbackQueryHandler(day2_b12_mat, pattern="^day2_b12_mat$"))
    app.add_handler(CallbackQueryHandler(day2_b12_task, pattern="^day2_b12_task$"))
    app.add_handler(CallbackQueryHandler(day2_b13, pattern="^day2_b13$"))
    app.add_handler(CallbackQueryHandler(day2_b13_task, pattern="^day2_b13_task$"))
    app.add_handler(CallbackQueryHandler(day3_menu, pattern="^day3$"))
    app.add_handler(CallbackQueryHandler(day3_schedule, pattern="^day3_schedule$"))
    app.add_handler(CallbackQueryHandler(day3_b1, pattern="^day3_b1$"))
    app.add_handler(CallbackQueryHandler(day3_b1_task, pattern="^day3_b1_task$"))
    app.add_handler(CallbackQueryHandler(day3_b2, pattern="^day3_b2$"))
    app.add_handler(CallbackQueryHandler(day3_b2_task, pattern="^day3_b2_task$"))
    app.add_handler(CallbackQueryHandler(day3_b3, pattern="^day3_b3$"))
    app.add_handler(CallbackQueryHandler(day3_b3_task, pattern="^day3_b3_task$"))
    app.add_handler(CallbackQueryHandler(day3_b4, pattern="^day3_b4$"))
    app.add_handler(CallbackQueryHandler(day3_b4_mat, pattern="^day3_b4_mat$"))
    app.add_handler(CallbackQueryHandler(day3_b4_task, pattern="^day3_b4_task$"))
    app.add_handler(CallbackQueryHandler(day3_b5, pattern="^day3_b5$"))
    app.add_handler(CallbackQueryHandler(day3_b5_task, pattern="^day3_b5_task$"))
    app.add_handler(CallbackQueryHandler(day3_b6, pattern="^day3_b6$"))
    app.add_handler(CallbackQueryHandler(day3_b6_task, pattern="^day3_b6_task$"))
    app.add_handler(CallbackQueryHandler(day3_b7, pattern="^day3_b7$"))
    app.add_handler(CallbackQueryHandler(day3_b7_task, pattern="^day3_b7_task$"))
    app.add_handler(CallbackQueryHandler(day3_b8, pattern="^day3_b8$"))
    app.add_handler(CallbackQueryHandler(day3_b8_task, pattern="^day3_b8_task$"))
    app.add_handler(CallbackQueryHandler(day3_b9, pattern="^day3_b9$"))
    app.add_handler(CallbackQueryHandler(day3_b9_task, pattern="^day3_b9_task$"))
    app.add_handler(CallbackQueryHandler(day3_b10, pattern="^day3_b10$"))
    app.add_handler(CallbackQueryHandler(day3_b10_task, pattern="^day3_b10_task$"))
    app.add_handler(CallbackQueryHandler(day3_b11, pattern="^day3_b11$"))
    app.add_handler(CallbackQueryHandler(day3_b11_task, pattern="^day3_b11_task$"))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()