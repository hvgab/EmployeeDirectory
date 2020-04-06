from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from django.utils import timezone

class BaseModel(models.Model):
    """My custom model"""
    class Meta:
        abstract = True
    
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4(), editable=False)


class Employee(BaseModel):
    """Employee"""
    class Meta:
        pass
    
    employee_number = models.IntegerField(_("employee-number"))
    firstname = models.CharField(_("firstname"), max_length=50)
    lastname = models.CharField(_("lastname"), max_length=50)
    phone = models.CharField(_("phone"), max_length=50)
    email = models.EmailField(_("email"), max_length=320, unique=True)
    
    address_street = models.CharField(_("street"), max_length=50)
    address_postcode = models.IntegerField(_("postcode"))
    address_city = models.CharField(_("city"), max_length=50)
    
    birthdate = models.DateField(_("birthdate"), auto_now=False, auto_now_add=False)
    ssn = models.IntegerField(_("social security number"))  # TODO restrict this field
    bank_account_number = models.CharField(_("bank account number"), max_length=50)  # TODO restrict this field
    
    is_employed = models.BooleanField(default=True, editable=False, help_text="Is the employee employed at the moment?")

    def __str__(self):
        return f"{self.employee_number}: {self.firstname} {self.lastname}"
    

    def save(self, *args, **kwargs):
        """Overwrite default save method."""
        # TODO: Create linked employment if Employee is new. Does a create method exist?
        super(Employee, self).save(*args, **kwargs)


class Employment(BaseModel):
    """When an employee has started and quitted the firm.

        An employee could come back to work at a later time.
        Also tracks title changes on the employee
    """

    class Meta:
        pass
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name="employments")
    jobtitle = models.CharField(_("title"), max_length=50)
    start_date = models.DateField(_("start_date"), default=timezone.now)
    end_date = models.DateField(_("end_date"), blank=True, null=True)

    def save(self, *args, **kwargs):
        # TODO: if end_date is null, or in the future, set employee.is_employed to True, else False.
        super(Employment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.jobtitle} ({self.start_date} - {self.end_date})"
    

class EmergencyContact(BaseModel):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(_("name"), max_length=50)
    phone = models.CharField(_("phone"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)

    def __str__(self):
        return f"{self.name}, {self.phone}"
    
class ExternalSystem(BaseModel):
    """external systems in use by employees"""
    slug = models.SlugField(_("slug"), unique=True, max_length=15)
    name = models.CharField(_("name"), max_length=50)
    url = models.URLField(_("url"), max_length=200)

    def __str__(self):
        return self.name
    

class ExternalUserAccount(BaseModel):
    """UserAccounts connected to the user.

    For easy on/off-boarding and reporting."""

    # TODO: Hvis vi legger business logikken her så kan vi kalle på APIer på de andre servicene herfra.
    # Så denne applikasjonen har ansvaret for å opprette andre brukere, men kan kalle på APIer/gRPC/sette i redis kø andre steder.
    # Så slipper man at denne applikasjonen har ansvar for andre tjenester. Denne skal kun kalle.

    employee = models.ForeignKey("core.Employee", on_delete=models.CASCADE)
    system = models.ForeignKey("core.ExternalSystem", on_delete=models.CASCADE)
    username = models.CharField(max_length=320)
    
    def __str__(self):
        return f'{self.employee.firstname} {self.employee.lastname}, {self.system.name}, {self.username}'
    