def user_directory_path(instance, filename):
    return 'user {0}/{1}'.format(instance.user.id, filename)
     
 