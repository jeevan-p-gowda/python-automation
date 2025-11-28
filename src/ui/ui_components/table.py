from playwright.sync_api import Page


class Table:
    def __init__(self, __page: Page, locator: str):
        self.__page = __page
        self.__table = __page.locator(locator)
        self.__header_row = "thead tr"
        self.__header = "th"
        self.__rows = self.__table.locator("tbody tr")
        self.__table_data = "td"

    def get_columns(self):
        header_row = self.__table.locator(f"thead tr:nth-child({self.__table.locator(self.__header_row).count()})")
        return header_row.locator(self.__header)

    def get_body_rows(self):
        return self.__rows

    def get_all_rows(self):
        return self.__rows.all()

    def get_column_header(self, column_name: str):
        columns = self.get_columns()
        headers = columns.all()
        for header in headers:
            if header.text_content() == column_name:
                return header

    def get_column_index(self, column_name: str):
        columns = self.get_columns()
        headers = columns.all_text_contents()
        return headers.index(lambda x: column_name in x) + 1

    def get_data_matched_row(self, table_data: str):
        all_rows = self.get_all_rows()
        for row in all_rows:
            texts = row.locator(self.__table_data).all_text_contents()
            for text in texts:
                if text == table_data:
                    return row

    def get_data_matched_rows(self, table_data: str):
        all_rows = self.get_all_rows()
        matched_rows = []
        for row in all_rows:
            texts = row.locator(self.__table_data).all_text_contents()
            for text in texts:
                if text == table_data:
                    matched_rows.append(row)
        return matched_rows

    def get_data_for_matched_rows(self, table_data: str, column_name: str):
        column_data: list[str] = []
        index = self.get_column_index(column_name)
        matched_rows = self.get_data_matched_rows(table_data)
        for matched_row in matched_rows:
            data = matched_row.locator(f"td:nth-child({index})").text_content()
            if isinstance(data, str):
                column_data.append(data)
            else:
                raise Exception(f"Alien found {data}")
        return column_data

    def get_data_for_matched_row(self, table_data: str, column_name: str):
        index = self.get_column_index(column_name)
        matched_row = self.get_data_matched_row(table_data)
        data = matched_row.locator(f"td:nth-child({index})").text_content()
        return data
