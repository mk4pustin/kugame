class Settings:
    level_number = 1
    cell_size = 80

    @staticmethod
    def change_level(level):
        Settings.level_number = level

    @staticmethod
    def change_size(size):
        Settings.cell_size = size
