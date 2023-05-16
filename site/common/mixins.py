
class DataMixin:
    # def get_user_context(self, **kwargs):
    #     context = kwargs
    #     user_menu = menu.copy()
    #
    #     if not self.request.user.is_authenticated:
    #         user_menu.pop(1)
    #
    #     context['menu'] = user_menu
    #     return context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
