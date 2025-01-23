import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .env import GOOGLE_CREDS_JSON_PATH, GOOGLE_SHEET_NAME
from src.models.sheet_model import SheetModel


class GoogleSheetClient:
    def __init__(self):
        # Настройка доступа через учетные данные
        self.__scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.__credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDS_JSON_PATH, self.__scope)
        self.__client = gspread.authorize(self.__credentials)
        # Открытие Google Sheet
        self.__spreadsheet = self.__client.open(GOOGLE_SHEET_NAME)  # Укажите имя таблицы
        self.__sheet = self.__spreadsheet.sheet1  # Выбор первого листа
        self.__data = self.update_data()

    # def get_sheet(self):
    #     return self.sheet

    def update_data(self) -> SheetModel:
        admin_username = self.__sheet.acell("B3").value
        timeout_sec = int(self.__sheet.acell("B4").value)
        active_key = int(self.__sheet.acell("B5").value)
        gpt_model = self.__sheet.acell("B12").value

        # Читаем список ключей (например, чисел) из диапазона
        keys_range = self.__sheet.range("B6:B10")
        keys = [cell.value for cell in keys_range if cell.value]

        prompt = self.__sheet.acell("B2").value

        products_info = self.__sheet.col_values(4)

        self.__data = SheetModel(
            gpt_model=gpt_model,
            admin_username=admin_username,
            timeout_sec=timeout_sec,
            active_key=active_key,
            keys=keys,
            prompt=prompt,
            products_info=products_info
        )

        return self.__data

    def get_data(self):
        return self.__data

    def set_data(self, sheet_model: SheetModel) -> None:
        """
        Записывает данные из объекта SheetModel в Google Sheets.

        :param sheet_model: Объект SheetModel с данными для записи.
        """
        # Запись отдельных полей
        self.__sheet.update_acell("B3", sheet_model.admin_username)
        self.__sheet.update_acell("B4", sheet_model.timeout_sec)
        self.__sheet.update_acell("B5", sheet_model.active_key)
        self.__sheet.update_acell("B2", sheet_model.prompt)

        # Запись списка ключей в диапазон
        keys_range = self.__sheet.range("B6:B10")
        for i, cell in enumerate(keys_range):
            # Если есть соответствующее значение, записываем его, иначе оставляем пустым
            cell.value = sheet_model.keys[i] if i < len(sheet_model.keys) else ""
        self.__sheet.update_cells(keys_range)
        self.update_data()

    def write_product_description(self, product_info: str, product_ai_description: str) -> None:
        try:
            # Find the cell containing the text
            cell = self.__sheet.find(product_info)
            self.__sheet.update_cell(cell.row, cell.col + 1, product_ai_description)

        except gspread.exceptions.CellNotFound:
            print(f"NOT FOUND IN SHEET: '{product_info}'")

google_sheet_client = GoogleSheetClient()
