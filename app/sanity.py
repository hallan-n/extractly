import re


def concat(value: str, params: str):
    return value + params


def after(value: str, params: str):
    return value[value.find(params) + 1 :]


def until(value: str, params: str):
    return value[: value.find(params)]


def replace(value: str, params: str):
    return value.replace(params, "")


def case(value: str, params: str):
    case, then = params.split("|")
    if value == case:
        return then
    return value


def ignore_if(value: str, params: str):
    if value == params:
        return None
    return value


def not_contain(value: str, params: str):
    return value if not params in value else ""


def not_equal(value: str, params: str):
    return value if value != params else ""


def if_existe_text(value: str, params: str):
    return value if params in value else ""


def if_not_exist_text(value: str, params: str):
    return value if not params in value else ""


def get_date(value: str, params: str | int = 0):
    matches = re.findall(r"((\d{4}|\d{2})(\/|-|\.)){2}(\d{4}|\d{2})", value)
    return "".join(matches[int(params)]) if matches else ""


def get_cnpj(value: str, params: str | int = 0):
    matches = re.findall(r"\d{14}|\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}", value)
    return "".join(matches[int(params)]) if matches else ""


def get_cpf(value: str, params: str | int = 0):
    matches = re.findall(r"\d{11}|(\d{3}(\.)?){3}-\d{2}", value)
    return "".join(matches[int(params)]) if matches else ""


def get_cpf_cnpj(value: str, params: str | int = 0):
    matches = re.findall(
        r"(\d{14}|\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})|(\d{11}|(\d{3}(\.)?){3}-\d{2})",
        value,
    )
    return "".join(matches[int(params)]) if matches else ""


def get_first_word(value: str):
    if data := re.match(r"^\w+(\W)?", value):
        return data.group()
    return ""


def get_last_word(value: str):
    if data := re.match(r"\w+(\W)?$", value):
        return data.group()
    return ""


def get_cep(value: str, params: str | int = 0):
    matches = re.findall(r"\d{8}|\d{5}-\d{3}", value)
    return matches[int(params)] if matches else ""


def get_uf(value: str, params: str | int = 0):
    matches = re.findall(
        r"(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO)",
        value.upper(),
    )
    return matches[int(params)] if matches else ""


def get_fone(value: str, params: str):
    matches = re.findall(
        r"(\s{0,}\+\d{2}\s{0,})?(\(|\[)?\d{2}(\)|\])?(-)?\s{0,}\d{4,5}(-|\s{0,})?\d{4}",
        value,
    )
    return matches[int(params)] if matches else ""


def get_email(value: str, params: str):
    matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", value)
    return matches[int(params)] if matches else ""


def get_ddd(value: str, params: str):
    matches = re.findall(r"(?<=\()\d{2}(?=\))", value)
    return matches[int(params)] if matches else ""


def get_money(value: str, params: str):
    matches = re.findall(r"\d{1,3}([.,]\d{3})*([.,]\d{2})", value)
    return matches[int(params)] if matches else ""


def get_float(value: str, params: str):
    matches = re.findall(r"(\d{1,}[,\.]){1,}\d{1,}", value)
    return matches[int(params)] if matches else ""


def get_int(value: str, params: str = 0):
    matches = re.findall(r"\d{1,}", value)
    return matches[int(params)] if matches else ""


def regex(value: str, params: str):
    mode, rgx = params.split("|")

    match mode:
        case "get":
            return re.search(rgx, value).group() if re.search(rgx, value) else ""
        case "replace":
            return re.sub(rgx, "", value)
        case "match":
            return value if re.search(rgx, value) else ""
        case _:
            return ""


def sanity(command: str, value: str):
    commands = command.split(":")

    try:
        if len(commands) == 1:
            callback = commands[0]
            return eval(f"{callback}(value)")
        else:
            callback = commands[0]
            params = commands[1]

            return eval(f"{commands[0]}(value, params)")

    except Exception as e:
        raise Exception(f"Função Sanity não encontrado: {e}")



print(sanity("get_cpf_cnpj", "17193448765 27193448765 37193448765"))