class MultipleProxyMiddleware:
    COUNT = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.COUNT += 1
        if not self.COUNT % 5:
            self.COUNT = 0
            res = self.get_response(request)
            text = ""
            slug = ""
            for i in res.context_data:
                if 1040 <= ord(i) <= 1103:
                    slug += i
                else:
                    text += slug[::-1] + i
                    slug = ""
            text += slug[::-1]
            res.context_data = text
            return res
        return self.get_response(request)
