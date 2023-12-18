# Karl Jones, Dec 2023

from typing import Any

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter

from .ctkformattedframe import CTkFormattedFrame
from .ctkframelayout import CTkFrameLayout


class CTkFrameLayout2(CTkFrameLayout):
    """CTkFrameLayout2

    The frame layout class that will contain a number of frames in a predefined layout
    """

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        gutter: int = 5,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the frame layout

        Args:
            master (CTkFrame): master frame into which this frame layout is placed
            gutter (Optional[int], optional): gutter between frames in the layout. Defaults to 5
        """

        #  Initialise the CTkFrameLayout

        super().__init__(master, *args, **kwargs)

        #  Configure the frame layout

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=0)

        #  Initialise the frames that makeup the layout
        #  Other frames will still be None

        self._main = CTkFormattedFrame(self)
        self._main.grid(row=0, column=0, padx=0, pady=(0, gutter), sticky="nsew")  # type: ignore - call to CustomTknter

        self._bottom = CTkFormattedFrame(self, height=50)
        self._bottom.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")  # type: ignore - call to CustomTknter

        #  Set the frame layout's descriptors

        self._str = "CTkFrameLayout2"
        self._repr = (
            "CTkFrameLayout2 (master={master}, *args={*args}, **kwargs={**kwargs})"
        )
