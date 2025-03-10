from dishka import Provider, Scope, provide

from src.services import NotificationService


class NotificationServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_notification_service(self) -> NotificationService:
        return NotificationService()
