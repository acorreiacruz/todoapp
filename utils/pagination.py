# flake8: noqa
import math
from django.core.paginator import Paginator


def criar_range_de_paginacao(range_de_paginas, quantidade_de_paginas, pagina_atual):
    meio_do_range = math.ceil(quantidade_de_paginas / 2)
    inicio_do_range = pagina_atual - meio_do_range
    fim_do_range = pagina_atual + meio_do_range
    total_de_paginas = len(range_de_paginas)


    inicio_do_range_offset = abs(inicio_do_range) if inicio_do_range < 0 else 0

    if inicio_do_range < 0:
        inicio_do_range = 0
        fim_do_range += inicio_do_range_offset

    if fim_do_range >= total_de_paginas:
        inicio_do_range -= abs(fim_do_range - total_de_paginas)

    return {
        "range_de_paginas": range_de_paginas[inicio_do_range:fim_do_range],
        "pagina_atual": pagina_atual,
        "total_de_paginas": total_de_paginas,
        "primeira_pagina_fora_do_range": pagina_atual > meio_do_range,
        "ultima_pagina_fora_do_range": fim_do_range < total_de_paginas
    }


def criar_paginacao(request, queryset, per_page, quantidade_de_paginas=5):
    try:
        pagina_atual = int(request.GET.get('page', 1))
    except ValueError:
        pagina_atual = 1

    paginator = Paginator(queryset, per_page)
    pagina_objeto = paginator.get_page(pagina_atual)
    range_de_paginacao = criar_range_de_paginacao(
        paginator.page_range,
        quantidade_de_paginas,
        pagina_atual
    )

    return pagina_objeto, range_de_paginacao