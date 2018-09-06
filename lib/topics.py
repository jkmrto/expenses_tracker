import csv
import math
from lib.sheet_handler import sheetHandler
from fuzzywuzzy import fuzz

def load_topics_from_api():
    sheet = sheetHandler().load_last_sheet()

    clean_topics = []
    for row in sheet:
        if row["resultados_tipo"] != "":
            aux = {"tipo": row["resultados_tipo"].lower(), 
                   "subtipo": row["resultados_subtipo"].lower()}
            clean_topics.append(aux)
    return clean_topics

def export_topics_to_csv(filename):

    clean_topics = load_topics_from_api()

    topics_file_handler =  open(filename, 'w', newline='') 
    fieldnames = ['tipo', 'subtipo']
    writer = csv.DictWriter(topics_file_handler, fieldnames=fieldnames)
    writer.writeheader()

    for row in clean_topics:
        writer.writerow(row)

    topics_file_handler.close()

def load_topics_from_csv(filename):

    topics_file_handler =  open(filename, 'r', newline='\n') 
    reader = csv.DictReader(topics_file_handler, delimiter=",")
    topics_dict = []
    for row in reader:
        topics_dict.append(row)

    return topics_dict

def get_topics_similarity_ratio(raw_topics, topics_to_eval):
    ratio_main_topic = fuzz.ratio(raw_topics["main"], topics_to_eval["main"])
    ratio_sub_topic = fuzz.ratio(raw_topics["sub"], topics_to_eval["sub"])
    return math.sqrt(ratio_main_topic**2 + ratio_sub_topic**2)

def set_topics_if_higher_ratio_found(raw_topics, topics_to_eval, settled_ratio, settled_topics):
    new_ratio = get_topics_similarity_ratio(raw_topics, topics_to_eval)
    if new_ratio > settled_ratio:
        return [new_ratio, topics_to_eval]
    else: 
        return [settled_ratio, settled_topics]

def find_closest_topic(raw_main_topic, raw_sub_topic, topics_available):
    matched_ratio = 0
    selected_topic = {"main": "", "sub": ""}
    for topic in topics_available:
        [matched_ratio, selected_topic] = set_topics_if_higher_ratio_found(
            raw_topics = {"main": raw_main_topic, "sub": raw_sub_topic},
            topics_to_eval = {"main": topic["tipo"], "sub": topic["subtipo"]},
            settled_ratio = matched_ratio,
            settled_topics = selected_topic
        )
    return selected_topic
  
def check_and_fix_topic_names(sheet, topics_available):
    for row in sheet:
        selected_topic = find_closest_topic(row["tipo"], row["subtipo"], topics_available)
        row["tipo"] = selected_topic["main"]
        row["subtipo"]  = selected_topic["sub"]
    return sheet