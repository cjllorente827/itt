from django.http import HttpResponseNotAllowed

def method_dispatch(**table):
    def invalid_method(request, *args, **kwargs):
        return HttpResponseNotAllowed(table.keys())

    def callable(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)
    
    return callable