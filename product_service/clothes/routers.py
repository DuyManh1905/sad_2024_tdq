class ClothesRouter:
    # truy vấn đọc (SELECT)
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'clothes':
            return 'mongodb'
        return None
 # truy vấn ghi (INSERT, UPDATE, DELETE)
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'clothes':
            return 'mongodb'
        return None

# cho phép quan hệ (relationship) giữa hai đối tượng (obj1 và obj2
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'clothes' and
            obj2._meta.app_label == 'clothes'
        ):
            return True
        return None

# thực hiện các migration trên database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'clothes':
            return db == 'mongodb'
        return None