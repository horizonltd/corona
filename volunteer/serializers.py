from rest_framework import serializers
from .import models



class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class VolunteerSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = models.Volunteer
        fields = [
            # 'entryID',
            'first_Name',
            'middle_Name',
            'surname',
            'dob',
            'sex',
            'state',
            'lga',
            'ward',
            'polling_Unit',
            'geolocation',
            'prepared_State_of_To_Be_Involved',
            'prepared_Start_DateTobeInvolved',
            'prepared_EndDate_To_be_Involved',
            'prepared_Days_To_be_Involved',
            'email',
            'phone_Number',
            'date_Of_Entry',
            'picture',
            'qualification',
            'specialization',
            'profession',
        ]
        #This help to view the level of hidden relationship
        depth=1

class ReportCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportCase
        fields = [
            'first_Name',
            'middle_Name',
            'surname',
            'sex',
            'state',
            'lga',
            'ward',
            'polling_Unit',
            'geolocation',
            'email',
            'phone_Number',
            'description',
            'reportDate',
        ]
        #This help to view the level of hidden relationship
        depth=1








