class PlaceholderMixin:
    def add_placeholder(self):
        for field_name, field in self.fields.items():
            placeholder = field.label or field_name.replace('_', ' '.capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder()
