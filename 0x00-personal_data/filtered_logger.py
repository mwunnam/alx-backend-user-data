#!/usr/bin/env python3
''' log message obfuscating '''
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: [str],
                separator: str) -> str:
    '''Log message obfuscating '''
    pattern = (
        rf"(?<={re.escape(separator)})"
        rf"(?P<field>{'|'.join(map(re.escape, fields))})"
        rf"=(?P<value>[^;]*)(?={re.escape(separator)}|$)"
    )
    return re.sub(pattern, lambda m: f"{m.group('field')}={redaction}", message)
