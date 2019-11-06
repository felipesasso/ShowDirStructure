# ShowDirStructure
Returns dictionary structure containing all the directories and size of each file under each directory.

Usage:
```python
python show_dir_structure.py
```
Output sample:
```python
python show_dir_structure.py
{
    'api': {
        'settings.py': 3385, 
        'urls.py': 200, 
        'wsgi.py': 383},
    'db.sqlite3': 135168,
    'manage.py': 535,
    'music': {
        'admin.py': 116,
        'apps.py': 85,
        'migrations': {
            '0001_initial.py': 548},
        'models.py': 281,
        'serializers.py': 193,
        'tests.py': 1319,
        'urls.py': 144,
        'views.py': 273
}
