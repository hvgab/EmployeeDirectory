from django.db import models
from django.


class BaseModel(models.Model):
    """My custom model"""
    class Meta:
        abstract = True
    
    id = models.UUIDField(_("ID"), primary_key=True)


class Employee(BaseModel):
    """Employee"""
    class Meta:
        pass
    
    employee_number = models.IntegerField(_("employee-number"))
    firstname = models.CharField(_("firstname"), max_length=50)
    lastname = models.CharField(_("lastname"), max_length=50)
    phone = models.PhoneNumberField(_("phone"))
    email = models.EmailField(_("email"), max_length=320, unique=True)
    
    address_street = models.CharField(_("street"), max_length=50)
    address_postcode = models.IntegerField(_("postcode"))
    address_city = models.CharField(_("city"), max_length=50)
    
    birthdate = models.DateField(_("birthdate"), auto_now=False, auto_now_add=False)
    ssn = models.IntegerField(_("social security number"))  # TODO restrict this field
    bank_account_number = models.CharField(_("bank account number"), max_length=50)  # TODO restrict this field
    
    emergency_contacts = models.ManyToManyField("core.EmergencyContact", verbose_name=_("emergency contacts"))
    __is_employed = models.BooleanField(default=True, editable=False, help_text="Is the employee employed at the moment?")
    
    @property
    def is_employed(self):
        return self.__is_employed

    @is_employed.setter()
    def is_employed(self, bool:bool):
        self.__is_employed = bool



    def save(self):
        """Overwrite default save method."""
        # TODO: Create linked employment if Employee is new. Does a create method exist?
        pass


class Employment(BaseModel):
    """When an employee has started and quitted the firm.

        An employee could come back to work at a later time.
        Also tracks title changes on the employee
    """

    class Meta:
        pass

    title = models.CharField(_("title"), max_length=50)
    start_date = models.DateField(_("start_date"), auto_now_add=True)
    end_date = models.DateField(_("end_date"))

class EmergencyContact(models.Model):
    id = models.UUIDField(_("id"))
    name = models.CharField(_("name"), max_length=50)
    phone = models.PhoneNumberField(_("phone"))
    email = models.EmailField(_("email"), max_length=254)

    
class ExternalSystem(BaseModel):
    """external systems in use by employees"""
    slug = models.SlugField(_(""))
    name = models.CharField(_("name"), max_length=50)
    url = models.URLField(_("url"), max_length=200)

class ExternalUserAccount(BaseModel):
    """UserAccounts connected to the user.

    For easy on/off-boarding and reporting."""

    # TODO: Hvis vi legger business logikken her så kan vi kalle på APIer på de andre servicene herfra.
    # Så denne applikasjonen har ansvaret for å opprette andre brukere, men kan kalle på APIer/gRPC/sette i redis kø andre steder.
    # Så slipper man at denne applikasjonen har ansvar for andre tjenester. Denne skal kun kalle.

    employee = models.ForeignKey("core.Employee", verbose_name=_(""), on_delete=models.CASCADE)
    system = models.ForeignKey("core.ExternalSystem", verbose_name=_(""), on_delete=models.CASCADE)
    __username = models.CharField(max_length=320)
    
    @property
    def username(self):
        return self.__username

    @username.setter()
    def username(self, username):
        self.__username = username
