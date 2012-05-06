django-quotes
=============

Random quotes for django

Install
-------

    $ pip install -e git://github.com/numerodix/django-quotes.git#egg=django-quotes

Then add:

```python
INSTALLED_APPS = (
    ..
    'quotes',
    ..
)
```

How to use
----------

{% load get_random_quote %}

<div id="random_quote">
    {% get_random_quote %}
</div>
