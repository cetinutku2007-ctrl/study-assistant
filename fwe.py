def get_topics(topic_count):
    topics = []
    for i in range(1,topic_count + 1):
        all_topics = input("Lütfen konu adını giriniz: ")
        topics.append(all_topics)
    return topics