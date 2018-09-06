from lib import topics
import settings

if __name__ == "__main__":
    topics.export_topics_to_csv(settings.topics_file)