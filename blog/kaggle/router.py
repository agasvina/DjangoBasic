class KaggleRouter(object):
    """
    A router to control all database operations on models in the
    kaggle application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to kaggle database.
        """
        if model._meta.app_label == 'kaggle':
            return 'kaggle'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to kaggle database.
        """
        if model._meta.app_label == 'kaggle':
            return 'kaggle'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the kaggle app is involved.
        """
        if obj1._meta.app_label == 'kaggle' or \
           obj2._meta.app_label == 'kaggle':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the kaggle app only appears in the 'kaggle'
        database.
        """
        if app_label == 'kaggle':
            return db == 'kaggle'
        return None