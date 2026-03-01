from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import os

def generate_pdf_report(data, output_filename="report.pdf"):
    """
    Генерирует красивый PDF-отчёт из данных
    
    Args:
        data: словарь с данными для отчёта
        output_filename: имя выходного PDF файла
    """
    
    # Загружаем шаблон
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("report_template.html")
    
    # Подготавливаем данные для графика (высота столбцов)
    max_rt = max(s['rt'] for s in data['sessions'])
    for session in data['sessions']:
        # Нормализуем высоту столбцов (макс. высота 150px)
        session['bar_height'] = int((session['rt'] / max_rt) * 150)
    
    # Добавляем вычисляемые поля
    data['max_rt'] = max_rt
    data['min_rt'] = min(s['rt'] for s in data['sessions'])
    data['improvement'] = abs(data['first_session_rt'] - data['last_session_rt'])
    
    # Рендерим HTML
    html_out = template.render(data)
    
    # Создаём PDF
    HTML(string=html_out).write_pdf(output_filename)
    print(f"PDF успешно создан: {output_filename}")

# Пример использования с вашими данными
if __name__ == "__main__":
    
    # ВАШИ ДАННЫЕ - просто замените эти значения
    report_data = {
        # Основная информация
        "user_id": "67",
        "report_date": "28.02.2026",
        "report_time": "19:06",
        "total_sessions": 2,
        
        # Средние показатели
        "avg_rt": 292.2,
        "avg_accuracy": 65.8,
        "avg_variability": 40.7,
        "avg_misses": 20.5,
        "avg_false_alarms": 0.0,
        
        # Изменения
        "rt_change": 2.7,  # в процентах
        "accuracy_change": -34.1,  # в процентах
        "variability_trend": "Стабильность снижается",
        
        # Последняя сессия
        "last_session_date": "2026-02-28",
        "last_session_time": "12:19:42",
        "last_session_rt": 288.2,
        "last_session_accuracy": 31.7,
        "last_session_misses": 41,
        "last_session_false_alarms": 0,
        "last_session_variability": 19.1,
        
        # Данные для графика (все сессии)
        "sessions": [
            {
                "number": 1,
                "rt": 296,
                "date_short": "28 фев",
                "date_full": "2026-02-28"
            },
            {
                "number": 2,
                "rt": 288,
                "date_short": "28 фев",
                "date_full": "2026-02-28"
            }
        ],
        
        # Для статистики графика
        "first_session_rt": 296,
        "last_session_rt": 288,
    }
    
    # Генерируем PDF
    generate_pdf_report(report_data, "reaction_report.pdf")