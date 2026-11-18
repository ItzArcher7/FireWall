class Text:

    @staticmethod
    def reverse(value):
        return str(value)[::-1]

    @staticmethod
    def count_words(value):
        return len(str(value).split())

    @staticmethod
    def is_empty(value):
        return not str(value).strip()

    @staticmethod
    def capitalize(value):
        return str(value).capitalize()
