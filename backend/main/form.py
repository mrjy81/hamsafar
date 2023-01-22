from django import forms
from .models import RequestClient, RequestDriver
from leaflet.forms.widgets import LeafletWidget
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class PassengerGeoForm(forms.ModelForm):

    class Meta:
        model = RequestClient
        fields = ['start_loc', 'finish_loc']
        widgets = {'start_loc': LeafletWidget(), 'finish_loc': LeafletWidget(),
                   "req_start": DatePickerInput(),
                   "req_time_start": TimePickerInput(),
                   }

    # def __init__(self, *args, **kwargs):
    #     super(PassengerGeoForm, self).__init__(*args, **kwargs)
    #     self.fields['req_start'] = JalaliDateField(label=_('date'),  # date format is  "yyyy-mm-dd"
    #                                                widget=AdminJalaliDateWidget  # optional, to use default datepicker
    #                                                )
    #     self.fields['req_finish'] = JalaliDateField(label=_('date'),  # date format is  "yyyy-mm-dd"
    #                                                 widget=AdminJalaliDateWidget  # optional, to use default datepicker
    #                                                 )

    #     # you can added a "class" to this field for use your datepicker!
    #     # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

    #     self.fields['req_start'] = SplitJalaliDateTimeField(label=_('date time'),
    #                                                         # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
    #                                                         widget=AdminSplitJalaliDateTime
    #                                                         )
    #     self.fields['req_finish'] = SplitJalaliDateTimeField(label=_('date time'),
    #                                                          # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
    #                                                          widget=AdminSplitJalaliDateTime
    #                                                          )


class DriverGeoForm(forms.ModelForm):

    class Meta:
        model = RequestDriver
        fields = ['start_loc']
        widgets = {'start_loc': LeafletWidget(),
                   "req_start": DatePickerInput(),
                   }
