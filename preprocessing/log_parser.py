import re

def parse_build_log(log_text):
    pattern = r"(process_start|file_write|process_end|curl|chmod|exit)"
    tokens = re.findall(pattern, log_text)
    return tokens
