from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


def extract_dict(data, extracted={}):
    for k, v in data.items():
        if isinstance(v, dict):
            extract_dict(v)
        elif v:
            extracted[k] = v
    return extracted


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key,
                self.secret_key,
                calling_format=self.calling_format,
                host='s3-ap-south-1.amazonaws.com')
        return self._connection
