from django.forms import widgets
from django.utils.safestring import mark_safe

class CustomPictureImageFieldWidget(widgets.FileInput):

    def render(self, name, value, attrs=None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)
        img_html = ''
        
        # Check if value exists and has a URL
        if value and hasattr(value, 'url'):
            img_html = mark_safe(
                f'<img src="{value.url}" width="200" style="display:block; margin-left:150px; margin-bottom:10px;" />'
            )
        
        return mark_safe(f'{img_html}{default_html}')
