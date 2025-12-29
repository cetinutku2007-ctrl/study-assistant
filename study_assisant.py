print("Akıllı Çalışma Asistanı v0.1")

def get_user_input():
    class_name = str(input("Lütfen ders adını giriniz: "))
    daily_hours = int(input("Lütfen günlük kaç saat çalıştığınızı giriniz: "))
    days = int(input("Lütfen kaç gün çalıştığınızı giriniz: "))
    return class_name, daily_hours, days

def calculate_total_hours(daily_hours, days):
    total_hours= daily_hours * days
    return total_hours

def get_topic_count():
    topic_count = int(input("Lütfen konu sayısını giriniz: " ))
    if topic_count == 0:
        return 0
    else:
        return topic_count

def calculate_hours_per_topic(total_hours, topic_count):
    hours_per_topic = total_hours / topic_count
    return hours_per_topic


def main():
    class_name, daily_hours, days= get_user_input()
    total= calculate_total_hours(daily_hours, days)
    print(f"Toplamda {total} saat çalışmışsınız!")
    topics = get_topic_count()
    hour_per_topic = calculate_hours_per_topic(total, topics)
    print(f"Her konuya {hour_per_topic:.2f} saat çalışmışsınız!")

main()

