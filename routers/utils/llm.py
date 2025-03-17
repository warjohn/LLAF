from openai import OpenAI

class OpenAIClient:
    client = OpenAI(api_key="")
    client_2 = OpenAI(api_key = '')
    
    @classmethod
    def get_assistant_ids(cls):
        """Метод для получения списка ID ассистентов."""
        my_assistants = cls.client.beta.assistants.list(
            order="desc",
            limit="20",
        )
        return [assistant.id for assistant in my_assistants]

    @classmethod
    def create_thread(cls):
        """Метод для создания нового треда."""
        return cls.client.beta.threads.create()

    @classmethod
    def send_message(cls, thread_id, content):
        """Метод для отправки сообщения в тред."""
        return cls.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content
        )

    @classmethod
    def run_assistant(cls, thread_id, assistant_index):
        """Метод для запуска ассистента и получения статуса выполнения."""
        ass_id = cls.get_assistant_ids()
        print(ass_id)
        run = cls.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=ass_id[assistant_index],
        )
        return run

    @classmethod
    def get_thread_messages(cls, thread_id):
        """Метод для получения сообщений в треде."""
        messages = cls.client.beta.threads.messages.list(
            thread_id=thread_id
        )
        return messages.data[0].content[0].text.value if messages.data else None

    @classmethod
    def get_thread_messages_third(cls, thread_id):
        """Метод для получения сообщений в треде."""
        messages = cls.client_2.beta.threads.messages.list(
            thread_id=thread_id
        )
        return messages.data[0].content[0].text.value if messages.data else None

    @classmethod
    def process_thread(cls, content, assistant_index):
        """Главный метод для создания треда, отправки сообщения и получения ответа ассистента."""
        thread = cls.create_thread()
        cls.send_message(thread.id, content)
        run = cls.run_assistant(thread.id, assistant_index)
        print('run', run)
        if run.status == 'completed':
            response = cls.get_thread_messages(thread.id)
            print(response)
            return response
        else:
            print(run.status)
            return "Error"
     
    @classmethod    
    def process_thread_third(cls, content):
        thread = cls.client_2.beta.threads.create()
        cls.client_2.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=content
        )
        run = cls.client_2.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id='',
        )
        print('run', run)
        if run.status == 'completed':
            response = cls.get_thread_messages_third(thread.id)
            print(response)
            return response
        else:
            print(run.status)
            return "Error"
        pass

#   OpenAIClient.process_thread("Привет расскажи всё, что знаешь о модели yolo?", 0)
