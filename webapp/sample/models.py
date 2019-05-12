from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumField
from enumfields import Enum

class SystemUserRole(Enum):
    SYS_ADMIN       = "SYS_ADMIN"
    SYS_USER        = "SYS_USER"

class Common(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL,
                    null=True, db_index=True, editable=False,
                    on_delete=models.SET_NULL, related_name="%(class)s_created")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                    null=True, db_index=True, editable=False,
                    on_delete=models.SET_NULL, related_name="%(class)s_modified")

    class Meta:
        abstract = True
        app_label = "sample"

class Company(Common):
    name        = models.CharField(max_length=256, db_index=True, unique=True)
    email       = models.EmailField(db_index=True)
    phone       = models.CharField(max_length=20, blank=True, null=True)
    address_1   = models.CharField(max_length=256, blank=True, null=True)
    address_2   = models.CharField(max_length=256, blank=True, null=True)
    street      = models.CharField(max_length=256, blank=True, null=True)
    city        = models.CharField(max_length=256, blank=True, null=True)
    state       = models.CharField(max_length=256, blank=True, null=True)
    zipcode     = models.CharField(max_length=20, blank=True, null=True)
    country     = models.CharField(max_length=256, blank=True, null=True)
    logo_url    = models.TextField(blank=True, null=True)

    class Meta:
        app_label = "sample"

    def __str__(self):
        return "{}".format(self.name)

    @property
    def full_address(self):
        address_line = ""
        address_line += self.address_1 if self.address_1 else ""
        address_line += ", {}".format(self.address_2) if self.address_2 else ""
        address_line += ", {}".format(self.street) if self.street else ""
        address_line += ", {}".format(self.city) if self.city else ""
        address_line += ", {}".format(self.state) if self.state else ""
        address_line += ", {}".format(self.country) if self.country else ""
        address_line += ", {}".format(self.zipcode) if self.zipcode else ""
        return address_line

class User(Common, AbstractUser):
    email           = models.EmailField(_("email address"), unique=True)
    company         = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    system_role     = EnumField(SystemUserRole, default=SystemUserRole.SYS_USER, blank=True, null=True)
    registered      = models.BooleanField(default=False, db_index=True)
    avatar          = models.CharField(max_length=1024, blank=True, null=True)
    display_name    = models.CharField(max_length=128, blank=True, null=True)
    job_title       = models.CharField(max_length=256, blank=True, null=True)
    department      = models.CharField(max_length=256, blank=True, null=True)
    phone           = models.CharField(max_length=32, blank=True, null=True)
    address_1       = models.CharField(max_length=256, blank=True, null=True)
    address_2       = models.CharField(max_length=256, blank=True, null=True)
    street          = models.CharField(max_length=64, blank=True, null=True)
    city            = models.CharField(max_length=64, blank=True, null=True)
    state           = models.CharField(max_length=64, blank=True, null=True)
    zipcode         = models.CharField(max_length=32, blank=True, null=True)
    country         = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        app_label = "sample"

    @property
    def full_address(self):
        address_line = ""
        address_line += self.address_1 if self.address_1 else ""
        address_line += ", {}".format(self.address_2) if self.address_2 else ""
        address_line += ", {}".format(self.street) if self.street else ""
        address_line += ", {}".format(self.city) if self.city else ""
        address_line += ", {}".format(self.state) if self.state else ""
        address_line += ", {}".format(self.country) if self.country else ""
        address_line += ", {}".format(self.zipcode) if self.zipcode else ""
        return address_line

