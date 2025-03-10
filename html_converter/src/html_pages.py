
import html as html_converter


class HtmlPagesConverter:

    def __init__(self, open_file):
        self.open_file = open_file
        self._find_page_breaks()

    def _find_page_breaks(self):
        """Read the file and note the positions of the page breaks
        so we can access them quickly"""
        self.breaks = [0]
        while True:
            line = self.open_file.readline()
            if not line:
                break
            if "PAGE_BREAK" in line:
                self.breaks.append(self.open_file.tell())
        self.breaks.append(self.open_file.tell())

    def get_html_page(self, page):
        """Return html page with the given number (zero indexed)"""
        page_start = self.breaks[page]
        # bug: retrieves the wrong page, should be self.breaks[page+1]
        page_end = self.breaks[page+1]
        html = ""
        self.open_file.seek(page_start)
        while self.open_file.tell() != page_end:
            line = self.open_file.readline()
            if "PAGE_BREAK" in line:
                continue
            line = line.rstrip()
            # Bug - we should escape quotes
            html = html_converter.escape(line, quote=True)
            html += "<br />"
        return html
