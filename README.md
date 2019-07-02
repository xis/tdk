<div align="center">
  <h1>tdk yan sanayi</h1>
   fetches meanings of turkish words from sozluk.gov.tr
</div>

## Installation
```bash
pip install tdk-w
```

## Usage
```python
from tdk import new_word

# create new word
word = new_word("şarap")
# prints meaning of the word
print(word.meaning())
# prints all the word's data
print(word.all_data())
```