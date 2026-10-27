import json
from pathlib import Path

root = Path(__file__).parent
bank = json.loads((root / 'questions.json').read_text())
template = (root / 'template.html').read_text()
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'index.html').write_text(template.replace('__QUESTION_DATA__', json.dumps(bank, ensure_ascii=False)))
