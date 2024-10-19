## Repo for storing bbox of country boundaries 

### Get bbox [here](./bbox.json)

### Get Country Name and ISO3 CSV [here](./globalboundaries.csv) 


### Get programmatically  


```python
import requests
import json 


bbox_global = json.dumps(requests.get("https://raw.githubusercontent.com/kshitijrajsharma/global-boundaries-bbox/refs/heads/main/bbox.json").json())
print(bbox_global)
```


### Source and attribution : 

https://www.geoboundaries.org/globalDownloads.html