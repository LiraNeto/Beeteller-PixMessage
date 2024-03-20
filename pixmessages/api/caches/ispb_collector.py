from django.core.cache import cache

max_collectors = 5


def check_ispb_limit(ispb):
    lock_key = f'{ispb}_lock'
    with cache.lock(lock_key):
        try:
            qty_colecttor = cache.get(ispb)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            print(template.format(type(ex).__name__, ex.args))
            return False

        if qty_colecttor is None:
            qty_colecttor = 0

        print(f'Quantidade de coletores para o ispb {ispb}: {qty_colecttor}')
        if qty_colecttor >= max_collectors:
            return False
        qty_colecttor += 1
        cache.set(ispb, qty_colecttor)
    return True


def stop_collecting(ispb):
    lock_key = f'{ispb}_lock'
    with cache.lock(lock_key):
        qty_colecttor = cache.get(ispb)

        if qty_colecttor is None:
            qty_colecttor = 0
        if qty_colecttor > 0:
            qty_colecttor -= 1

        print(f'Quantidade de coletores para o ispb {ispb}: {qty_colecttor}')
        cache.set(ispb, qty_colecttor)
