from django.db import models


class Employee(models.Model):
    """Employee"""
    class Meta:
        pass

    id = models.UUIDField(verbose_name='Employee UUID', primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)  # TODO: add google phone internalization lib.
    email = models.EmailField(unique=True)
    employed = models.BooleanField(default=True, editable=False, help_text="Is the employee employed at the moment?")  # TODO: This is a property of _Employment_ status

    def save(self):
        """Overwrite default save method."""
        # TODO: Create linked employment if Employee is new. Does a create method exist?
        pass


class Employment(models.Model):
    """When an employee has started and quitted the firm.

        An employee could come back to work at a later time.
        Also tracks title changes on the employee
    """

    class Meta:
        pass

    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

class ExternalUserAccount(models.Model):
    """UserAccounts connected to the user.

    For easy on/off-boarding and reporting."""

    # TODO: Hvis vi legger business logikken her så kan vi kalle på APIer på de andre servicene herfra.
    # Så denne applikasjonen har ansvaret for å opprette andre brukere, men kan kalle på APIer/gRPC/sette i redis kø andre steder.
    # Så slipper man at denne applikasjonen har ansvar for andre tjenester. Denne skal kun kalle.

    EXTERNAL_TYPE_CHOICE = (
        ('AD', 'Active Directory'),
        ('TMG', 'Telemagic'),
        ('GPC', 'PureCloud'),
        ('EMAIL', 'E-Mail'),
    )

    employee = models.ForeignKey('Employee')
    main_type = models.ChoiceField(EXTERNAL_TYPE_CHOICE)
    sub_type = models.CharField(max_length=10)
    __username = models.CharField(max_length=320)
    
    @property
    def username(self):
        return self.__username

    @username.setter()
    def username(self, username):
        self.__username = username
