from django.urls import reverse


class MenuMixin:
    @staticmethod
    def get_menu_context_data(**kwargs):
        context = kwargs
        context["footer"] = [
            dict(title="Покупателям",
                 sub_items=[
                     dict(title="Новинки", url=reverse("home")+"#news"),
                     dict(title="Доставка", url=reverse("delivery")),
                     dict(title="Оплата", url=reverse("payment")),
                    ]
                 ),
            dict(title="Информация",
                 sub_items=[
                     dict(title="О нас", url=reverse("about")),
                     dict(title="Отзывы", url=reverse("home")+"#reviews"),
                    ]
                 ),
            dict(title="Контакты",
                 sub_items=[
                     dict(title="Вконтакте", url="#", target="blank"),
                     dict(title="Instagram", url="#", target="blank"),
                     dict(title="Telegram", url="#", target="blank"),
                    ]
                 ),
        ]
        return context
