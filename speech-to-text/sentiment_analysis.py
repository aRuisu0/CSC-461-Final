from api_comms import *
from record_mic import*
from translate import*

def analysis(json_name):
    with open(json_name, "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)
        
    n_pos = len(positives)
    n_neg  = len(negatives)
    n_neut = len(neutrals)

    file_name = input('Enter name for analysis text file: ') + '.txt'
    # analysis_file = os.path.join("analysis_file", file_name)

    input_file = os.path.join("sentiment_analysis", file_name)
    with open(input_file, "w") as f:
            f.write("Num positives: ")
            f.write(str(n_pos))
            f.write("\nNum negatives: ")
            f.write(str(n_neg))
            f.write("\nNum neutrals: ")
            f.write(str(n_neut))
    
    # print("Num positives:", n_pos)
    # print("Num negatives:", n_neg)
    # print("Num neutrals:", n_neut)

    # ignore neutrals here
    # r = n_pos / (n_pos + n_neg)
    # print(f"Positive ratio: {r:.3f}")
