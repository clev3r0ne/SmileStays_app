from django.shortcuts import redirect


class IfNotOwnerRedirectMixin():

    def get(self, request, *args, **kwargs):
        object = super().get_object()
        if self.request.user != object.user:
            return redirect('index')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        object = super().get_object()
        if self.request.user != object.user:
            return redirect('index')

        return super().post(request, *args, **kwargs)