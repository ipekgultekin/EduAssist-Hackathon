import random

def generate_weekly_plan(goal: str):
    days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    plan = f"🎯 Hedef: {goal}\n\n"
    for day in days:
        topic = random.choice([
            "Konu tekrarı + 10 test",
            "Yeni konu öğrenimi",
            "Zor soru çözümü",
            "Mini deneme + analiz",
            "Eksik konu çalışması",
            "Video izleme + not çıkarma"
        ])
        plan += f"📅 {day}: {topic}\n"
    return plan