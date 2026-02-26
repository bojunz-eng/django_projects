
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any

# Create your views here.
class MainView(LoginRequiredMixin, TemplateView):
    template_name = "solo2/index.html"

    def post(self, request, *args, **kwargs):
        field1 = request.POST.get("field1").strip()
        field2 = request.POST.get("field2").strip()
        
        context = self.get_context_data(**kwargs)
        context["result_message"] = ''.join(list(reversed(f'{field1} {field2}'.upper())))
        
        return self.render_to_response(context)
    