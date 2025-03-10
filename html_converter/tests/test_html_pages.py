import io

from html_pages import HtmlPagesConverter

def test_access_last_page_of_2():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
""")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"

def test_access_second_page_of_3():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
    converter = HtmlPagesConverter(fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"

def test_convert_quotes():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
"page two"
PAGE_BREAK
page three
""")
    converter = HtmlPagesConverter(fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "&quot;page two&quot;<br />"
#
#
# def test_convert_quotes():
#     fake_file = io.StringIO("quote: ' ")
#     converter = HtmlPagesConverter(open_file=fake_file)
#     converted_text = converter.get_html_page(0)
#     assert converted_text == "quote: &#x27;<br />"
#
#
# def test_access_second_page():
#     fake_file = io.StringIO("""\
# page one
# PAGE_BREAK
# page two
# PAGE_BREAK
# page three
# """)
#     converter = HtmlPagesConverter(open_file=fake_file)
#     converted_text = converter.get_html_page(1)
#     assert converted_text == "page two<br />"
