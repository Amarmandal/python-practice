import re
from pathlib import Path
from collections import Counter

log_mapping = {
    'debug': 0, 
    'info': 5, 
    'warn': 10, 
    'error': 15, 
    'critical': 20
}

def parse_log(filepath, min_severity):
    with open(filepath, 'r', encoding='utf-8') as f: 
        for line in f: 
            strip_line = line.strip()

            token = re.findall(r'\[(.*?)\]', strip_line)

            token_order = log_mapping[token[1].lower()]
            min_order = log_mapping[min_severity.lower()]

            if token_order >= min_order: 
                yield {'component': token[2], 'severity': token[1].upper()}



def aggregate_logs(log_generator):
    return Counter(log['component'] for log in log_generator)


def main(): 
    base_dir = Path.cwd()

    log_generator = parse_log(base_dir / "data" / "log.txt", "Error")

    print(dict(aggregate_logs(log_generator)))

if __name__ == "__main__":
    main()

