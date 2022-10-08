import rules

@rules.predicate
def is_post_owner(user, post):
    return post.created_by == user

@rules.predicate
def has_model_level_permission(user):
    return user.has_perm('kublog.change_postone')

@rules.predicate
def has_object_level_permission(user, post):
    return user.has_perm('kublog.change_postone', post)

@rules.predicate
def is_staff(user):
    return user.is_staff

@rules.predicate
def is_superuser(user):
    return user.is_superuser

rules.add_perm('is_object_editor', is_post_owner | has_object_level_permission | is_superuser)
rules.add_perm('is_editor', has_model_level_permission | is_staff)
rules.add_perm('can_edit_user', has_object_level_permission)