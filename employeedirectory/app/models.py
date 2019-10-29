from django.db import models


class Employee(models.Model):
    """Employee"""
    class Meta:
        pass

    id = models.UUIDField(verbose_name='Employee UUID', primary_key=True)
    firstname = models.CharField()
    lastname = models.CharField()
    phone = models.CharField()  # TODO: add google phone internalization lib.
    email = models.EmailField(unique=True)
    employed = models.BooleanField(default=True, editable=False, help_text="Is the employee employed at the moment?")  # TODO: This is a property of _Employment_ status

    def save(self):
        """Overwrite default save method."""
        # TODO: Create linked employment if Employee is new. Does a create method exist?
        pass


class Employment(models.Model):
    """When an employee has started and quitted the firm.

        An employee could come back to work at a later time.
    """

    class Meta:
        pass

    id = models.UUIDField(primary_key=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()