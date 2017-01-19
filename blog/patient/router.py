class PatientRouter(object):
    """
    A router to control all database operations on models in the
    patient application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to patient database.
        """
        if model._meta.app_label == 'patient':
            return 'patient'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to patient database.
        """
        if model._meta.app_label == 'patient':
            return 'patient'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the patient app is involved.
        """
        if obj1._meta.app_label == 'patient' or \
           obj2._meta.app_label == 'patient':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the patient app only appears in the 'patient'
        database.
        """
        if app_label == 'patient':
            return db == 'patient'
        return None