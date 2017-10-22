from vkapp.bot.models import VKUser, Blogger

def new_blogger(uid):
    vk_user = VKUser.objects.filter(vk_id=uid)
    if len(vk_user)==0:
        vk_user = VKUser(uid)
        vk_user.save()
    vk_user = VKUser.objects.get(vk_id=uid)

    blogger = Blogger.objects.filter(vk_user=vk_user)
    if len(blogger) == 0:
        blogger = Blogger(vk_user=vk_user)
        blogger.save()
    return blogger


def get_or_create_blogger(uid):
    bloggers = Blogger.objects.filter(vk_user__vk_id=uid).select_related()
    if len(bloggers) == 0:
        blogger = new_blogger(uid)
    else:
        blogger = bloggers[0]
    return blogger
