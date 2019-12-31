HTTP_MARK = '://'
HTTP_MARK_LEN = len(HTTP_MARK)


def remove_http_protocol(link):
    return link[link.index(HTTP_MARK) + HTTP_MARK_LEN:]