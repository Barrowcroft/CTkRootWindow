# Karl Jones, Dec 2023

from typing import Any, List, Tuple

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter

from .framelayouts import CTkFormattedFrame, CTkFrameLayout


class CTkFrameLayoutGrid(CTkFrameLayout):
    """CTkFrameLayoutGrid

    The frame set class that will contain a grid of frames
    """

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        rows: int = 2,
        columns: int = 3,
        gutter: int = 5,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the frame grid

        Args:
            master (CTkFrame): master frame into which this frame is placed
            rows (int, optional): number of rows in the grid. Defaults to 2
            columns (int, optional): number of rows in the grid. Defaults to 3
            gutter (int, optional): gutter between frames in the grid. Defaults to 5
        """
        #  Initilise the CTkFrameLayout

        super().__init__(master, *args, **kwargs)

        #  Initialise the frame grid

        self._frameGrid: List[List[CTkFormattedFrame]] | None = []

        #  Create the grid of frames

        for _row in range(0, rows):
            _y_padding: Tuple[int, int] = (0, gutter) if (_row < rows - 1) else (0, 0)

            self._frameGrid.append([])
            self.grid_rowconfigure(index=_row, weight=1)

            for _column in range(0, columns):
                _x_padding: Tuple[int, int] = (
                    (0, gutter) if (_column < columns - 1) else (0, 0)
                )

                self.grid_columnconfigure(index=_column, weight=1)
                self._frameGrid[_row].append(CTkFormattedFrame(self))

                self._frameGrid[_row][_column].grid(  # type: ignore - call to CustomTknter
                    row=_row,
                    column=_column,
                    padx=_x_padding,
                    pady=_y_padding,
                    sticky="nsew",
                )
