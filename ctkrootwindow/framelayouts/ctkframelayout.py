# Karl Jones, Dec 2023

from typing import Any, List, Optional

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter

from .ctkformattedframe import CTkFormattedFrame


class CTkFrameLayout(CTkFormattedFrame):
    """CTkFrameLayout

    The frame layout class that will contain a number of frames in a predefined layout
    """

    @property
    def frameGrid(self) -> Optional[List[List[CTkFormattedFrame]]]:
        """frameGrid

        The 'frameGrid' property exposes the predefined two-dimensional grid of frames
        It may be None:

        Returns:
            Optional[List[List[CTkFormattedFrame]]: two-dimensional grid of frames
        """
        return self._frameGrid

    @property
    def frameStack(self) -> Optional[List[CTkFormattedFrame]]:
        """frameStack

        The 'frameStack' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[List[CTkFormattedFrame]]: the stack of frames
        """
        return self._frameStack

    @property
    def top(self) -> Optional[CTkFormattedFrame]:
        """top

        The 'top' property exposes the top frame
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: top frame
        """
        return self._top

    @property
    def bottom(self) -> Optional[CTkFormattedFrame]:
        """bottom

        The 'bottom' property exposes the bottom frame
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: bottom frame
        """
        return self._bottom

    @property
    def left(self) -> Optional[CTkFormattedFrame]:
        """left

        The 'left' property exposes the left frame
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: left frame
        """
        return self._left

    @property
    def right(self) -> Optional[CTkFormattedFrame]:
        """right

        The 'right' property exposes the right frame
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: right frame
        """
        return self._right

    @property
    def main(self) -> Optional[CTkFormattedFrame]:
        """main

        The 'main' property exposes the main frame
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: main frame
        """
        return self._main

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the frame layout

        Args:
            master (CTkFrame): master frame into which this frame layout is placed
        """

        #  Initialise the CTkFormattedFrame

        super().__init__(master, *args, **kwargs)

        #  Initialise the properties

        self._frameGrid: Optional[List[List[CTkFormattedFrame]]] = None
        self._frameStack: Optional[List[CTkFormattedFrame]] = None
        self._top: Optional[CTkFormattedFrame] = None
        self._bottom: Optional[CTkFormattedFrame] = None
        self._left: Optional[CTkFormattedFrame] = None
        self._right: Optional[CTkFormattedFrame] = None
        self._main: Optional[CTkFormattedFrame] = None

        #  Set the frame layout's descriptors

        self._str = "CTkFrameLayout"
        self._repr = (
            "CTkFrameLayout (master={master}, *args={*args}, **kwargs={**kwargs})"
        )
