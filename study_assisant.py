print("Akıllı Çalışma Asistanı v0.1")

def get_user_input():
    class_name = (input("Lütfen ders adını giriniz: "))
    daily_hours = int(input("Lütfen günlük kaç saat çalıştığınızı giriniz: "))
    days = int(input("Lütfen kaç gün çalıştığınızı giriniz: "))
    return class_name, daily_hours, days

def calculate_total_hours(daily_hours, days):
    total_hours= daily_hours * days
    return total_hours

def get_topic_count():
    while True:
        topic_count = int(input("Lütfen konu sayısını giriniz: "))
        if topic_count == 0 or topic_count < 0:
            print("Lütfen sıfırdan büyük bir sayı giriniz")
            continue
        else:
            return topic_count
def calculate_hours_per_topic(total_hours, topic_count):
    hours_per_topic = total_hours / topic_count
    return hours_per_topic

def get_topics(topic_count):
    topics = []
    for i in range(1,topic_count + 1):
        all_topics = input("Lütfen konu adını giriniz: ")
        topics.append(all_topics)
    return topics

def print_study_plan(topics, hours_per_topic):
    for topic in topics:
        print(f"{topic} konusuna {hours_per_topic:.2f} saat çalışmışsınız!")

def save_study_plan_to_file(class_name, total_hours, topics, hours_per_topic):
    with open("study_plan.txt", "w", encoding="utf-8") as file:
        file.write(f"Ders: {class_name}\n")
        file.write(f"Toplam süre: {total_hours} saat\n\n")

        for topic in topics:
            file.write(f"{topic} → {hours_per_topic:.2f} saat\n")

def main():
    class_name, daily_hours, days= get_user_input()
    total= calculate_total_hours(daily_hours, days)
    print(f"Toplamda {total} saat çalışmışsınız!")
    topics_counts = get_topic_count()
    hour_per_topic = calculate_hours_per_topic(total, topics_counts)
    print(f"Her konuya {hour_per_topic:.2f} saat çalışmışsınız!")
    topics = get_topics(topics_counts)
    print_study_plan(topics, hour_per_topic)
    save_study_plan_to_file(class_name, total, topics, hour_per_topic)


main()

