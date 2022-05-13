from django import forms
from .models import History
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class TestForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['birth'] = JalaliDateField(label=('birth'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        # self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )

class TimeForm(forms.Form):
    first = forms.CharField(max_length=200)
    second = forms.CharField(max_length=200)
    def __init__(self,*args,**kwargs):
        super(TimeForm,self).__init__(*args,**kwargs)
        self.fields['first'] = JalaliDateField(label=('first'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['second'] = JalaliDateField(label=('second'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )