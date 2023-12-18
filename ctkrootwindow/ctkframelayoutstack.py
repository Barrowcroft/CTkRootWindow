# Karl Jones, Dec 2023

from typing import Any, List

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter

from .framelayouts import CTkFormattedFrame, CTkFrameLayout


class CTkFrameLayoutStack(CTkFrameLayout):
    """CTkFrameLayoutStack

    The frame set class that will contain a stack of frames
    """

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        number: int = 3,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the frame stack

        Args:
            master (CTkFrame): master frame into which this frame is placed
            number (int, optional): number of frames in the stack. Defaults to 3.
        """
        #  Initilise the CTkFrameLayout

        super().__init__(master, *args, **kwargs)

        #  Initialise the frame stack

        self._frameStack: List[CTkFormattedFrame] | None = []

        #  Create the required number of frames on the stack

        for i in range(0, number):
            self._frameStack.append(CTkFormattedFrame(self, *args, **kwargs))
            self._frameStack[i].grid(row=0, column=0, padx=0, pady=0, sticky="nswe")  # type: ignore - call to CustomTknter

    def select(self, index: int) -> None:
        """select

        Brings the specified frame to the top of the stack

        Args:
            index (int): index of frame to bring to the top
        """
        self._frameStack[index].tkraise()  # type: ignore - call to CustomTknter
