from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry

@receiver(post_save)
def update_document(sender, **kwargs):
    app_label = sender._meta.app_label
    model_name = sender_meta.model_name
    instance = kwargs['instance']

    print(app_label)
    print(model_name)
    print(instance)

    if app_label == 'pin':
        if model_name == 'board':
            instances = instance.board.all()
            for _instance in instances:
                registry.update(_instance)

@receiver(post_delete)
def delete_document(sender, **kwargs):
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'pin':
        if model_name == 'board':
            instances = instance.board.all()
            for _instance in instances:
                registry.delete(_instance, raise_on_error=False)