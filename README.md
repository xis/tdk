<div align="center">
  <h1>tdk yan sanayi</h1>
   fetchs meanings of turkish words from sozluk.gov.tr
</div>

## Installation
```bash
pip install tdk_w
```

## Usage
```python
import tdk
# prints just meaning of the word - returns array
print(tdk.search("şarap"))
# prints all the word's data - returns json
print(tdk.search_all_data("şarap"))
```