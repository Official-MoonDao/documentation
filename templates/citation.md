---
tags: citations
title: {{title}}
authors: {{authors}}
year: {{date | format('YYYY')}}
type: {{itemType}}
---
link:: {{url}}
extra:: {{extra}}

# {{title}}

> [!note] Formatted Bibliography
> {{bibliography}}

{% if abstractNote %}
### Abstract
{{abstractNote}}
{% endif %}

{% if attachments %}
{% for item in attachments %}
{%if path!{{pdfLink}}
{% endif %}
## Annotations
{% for annotation in annotations %}
{% if annotation.annotatedText %}

> {{annotation.annotatedText}}
> {% endif %}
> {% if annotation.comment %}
> {{annotation.comment}}
{% endif %}
{% endfor %}