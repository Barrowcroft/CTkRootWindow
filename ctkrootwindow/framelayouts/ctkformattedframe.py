# Karl Jones, Dec 2023

from typing import Any

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter


class CTkFormattedFrame(CTkFrame):
    """CTkFormattedFrame

    The formatted frame class
    """

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the formatted frame

        Args:
            master (CTkFrame): master frame into which this frame is placed
        """

        #  Initialise the CTkFrame

        super().__init__(master, *args, **kwargs)  # type: ignore - call to CustomTknter

        #  Configure the frame

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_propagate(False)

        #  Set the root window's descriptors

        self._str = "CTkFormattedFrame"
        self._repr = (
            "CTkFormattedFrame (master={master}, *args={*args}, **kwargs={**kwargs})"
        )

    #  Implement some dunder functions

    def __str__(self) -> str:
        return self._str

    def __repr__(self) -> str:
        return self._repr
