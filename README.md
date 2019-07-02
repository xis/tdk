<div align="center">
  <h1>tdk yan sanayi</h1>
   fetches meanings of turkish words from sozluk.gov.tr
</div>

## Installation
```bash
pip install tdk-fetch
```

## Usage
```python
from tdk import tdk

# create new word
word = tdk.new_word("şarap")
# prints meaning of the word
print(word.meaning())
# prints all the word's data
print(word.all_data())
```