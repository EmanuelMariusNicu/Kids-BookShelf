from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = "checkout"
    verbose_name = 'checko_ut'

    def ready(self):
        import checkout.signals