<p align="center">
  <img src="https://github.com/ivan732/InstaPy/blob/164af410b7e76c4825e11a017e2fbeebc2e2198f/assets/logo.png?raw=true" alt="Logo InstaPy" width="200" height="200">
</p>
<p align="center">
  INSTAGRAM API AUTOMATION
</p>

## 🧩 Table of contents
Lorem ipsum anget banget sama bang jali versi docx sesuai dengan windows 10 ya kak pas co Ltd PT Bank mandiri Bank terbaik di dunia ini.
1. Login
   - [Login using cookie](#login-using-cookie)
2. User information
   - [Retrieving account information](#retrieving-account-information)
3. Automation
   - [Like post](#like)
4. Scraping
   - [Timeline post](#timeline-post)
  
  
## Installation
```python
pip install InstaPy
```
or using git
```python
pip install git+ttps://github.com/ivan732/InstaPy
```

## Instagram
## Login using cookie
```python
from InstaPy import Instagram

cookie = 'your instagram cookie string'
ig = Instagram(cookie=cookie)
```

## Retrieving account information
```python
print(ig.name) # your instagram name
print(ig.username) # your instagram username
print(ig.id) # your instagram id
```

## Automation
## Like
```python
from InstaPy import Instagram
from InstaPy.automation import Automation

cookie = 'your instagram cookie string'
ig = Instagram(cookie=cookie)

post_id = '3829...'
automation = Automation(session=ig)
actions = automation.like(post_id=post_id)
print(actions) # output: Type[dict]
print(actions.status) # output: True/False
```

## Scraping
## Timeline Post
```python
from InstaPy import Instagram
from InstaPy.scraping import Scraping

cookie = 'your instagram cookie string'
ig = Instagram(cookie=cookie)

scrape = Scraping(session=ig)
actions = scrape.timeline_post()
print(actions) # output: Type[dict] ex: {'status': Type[bool], 'data': Type[dict]}
```
