from django.apps import AppConfig

class QuizConfig(AppConfig):
    name = 'quiz'

    def ready(self):
        # Importing signals to apply timezone setting on every database connection
        import quiz.signals
