import numpy as np


class Grid:
    def __init__(self, rows: int, columns: int, bombcount: int):
        self.rows: int = rows
        self.columns: int = columns
        self.values: np.ndarray = np.ones((rows, columns)) * -1
        self.remaining_values: np.ndarray = self.values.copy()
        self.flags: np.ndarray = np.zeros_like(self.values)
        self.bombcount: int = bombcount

    def get_save(self) -> np.ndarray:
        filled_pos = np.where(self.remaining_values == 0)

        full_mask = np.zeros_like(self.flags, dtype=bool)
        for pos in zip(filled_pos[0], filled_pos[1]):
            mask = self.neighborhood_mask(pos[0], pos[1])
            full_mask += mask

        # positions where the mask is true and no flag placed
        save_pos = np.where(np.logical_and(full_mask, self.flags != True))

        return np.vstack(save_pos).T

    def neighborhood_mask(self, row: int, column: int) -> np.ndarray:
        mask = np.zeros_like(self.flags, dtype=bool)
        bottom = max(0, row - 1)
        top = min(self.rows, row + 2)

        left = max(0, column - 1)
        right = min(self.columns, column + 2)

        mask[bottom:top, left:right] = True
        mask[row, column] = False

        return mask

    def set_value(self, row: int, column: int, value: int) -> None:
        self.values[row, column] = value

        # update remaining
        mask = self.neighborhood_mask(row, column)
        self.remaining_values[row, column] = value - np.sum(self.flags[mask])

    def set_flag(self, row: int, column: int) -> None:
        self.flags[row, column] = True

        # update remaining
        mask = self.neighborhood_mask(row, column)
        self.remaining_values[mask] -= 1

    def __repr__(self) -> str:
        return f"values:\n{self.values}\nflags:\n{self.flags}\nremaining:\n{self.remaining_values}"
