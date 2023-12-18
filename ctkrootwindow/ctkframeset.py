# Karl Jones, Dec 2023

from typing import Any, List, Optional

from customtkinter import CTk, CTkFrame  # type: ignore - call to CustomTknter

from .ctkframelayoutgrid import CTkFrameLayoutGrid
from .ctkframelayoutstack import CTkFrameLayoutStack
from .framelayouts import (
    CTkFormattedFrame,
    CTkFrameLayout,
    CTkFrameLayout0,
    CTkFrameLayout1,
    CTkFrameLayout2,
    CTkFrameLayout3,
    CTkFrameLayout4,
    CTkFrameLayout5,
    CTkFrameLayout6,
    CTkFrameLayout7,
    CTkFrameLayout8,
    CTkFrameLayout9,
    CTkFrameLayout10,
    CTkFrameLayout11,
    CTkFrameLayout12,
    CTkFrameLayout13,
    CTkFrameLayout14,
    CTkFrameLayout15,
    CTkFrameLayout16,
    CTkFrameLayout17,
    CTkFrameLayout18,
    CTkFrameLayout19,
    CTkFrameLayout20,
    CTkFrameLayout21,
    CTkFrameLayout22,
    CTkFrameLayout23,
    CTkFrameLayout24,
)


class CTkFrameSet(CTkFrameLayout):
    """CTkFrameSet

    The frame set class that will contain a set of predefined frames
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

        Initialises the frame set

        Args:
            master (CTkFrame): master frame into which this frame is placed
        """

        #  Initilise the CTkFrameLayout

        super().__init__(master, *args, **kwargs)

        #  Set the frame set's descriptors

        self._str: str = f"CTkFrameSet SHOULD NOT BE INSTANTIATED DIRECTLY"
        self._repr: str = f"CTkFrameSet SHOULD NOT BE INSTANTIATED DIRECTLY (master={master}, *args={args},  **kwargs{kwargs})"

    #  Class methods to create the frame set with optional predefined frame layouts

    @staticmethod
    def with_frames_as_grid(
        master: CTk | CTkFrame | CTkFormattedFrame,
        *args: Any,
        rows: int = 2,
        columns: int = 3,
        gutter: int = 5,
        **kwargs: Any,
    ) -> CTkFrameLayout:
        """with_frame_as_grid

        Creates a frame set that consists of a grid of frames

        Args:
            master (CTkFrame): master frame into which this frame is placed
            rows (int, optional): number of rows in the grid. Defaults to 2
            columns (int, optional): number of rows in the grid. Defaults to 3
            gutter (int, optional): gutter between frames in the grid. Defaults to 5

        Returns:
            CTkFrameLayout: this frame set that consists of a grid of frames
        """
        #  Create a frame layout with a grid of frames

        _frames: CTkFrameLayoutGrid = CTkFrameLayoutGrid(
            master, *args, rows=rows, columns=columns, gutter=gutter, **kwargs
        )

        #  Update the dunder __str__ and __repr__ string

        _frames._str = f"CTkFrameSet with_frame_grid"
        _frames._repr = f"CTkFrameSet with_frame_grid (master={master}, *args={args}, rows={rows}, columns={columns}, gutter={gutter}, **kwargs{kwargs})"

        #  Return the frame set

        return _frames

    @staticmethod
    def with_frames_as_stack(
        master: CTk | CTkFrame | CTkFormattedFrame,
        *args: Any,
        number: int = 3,
        **kwargs: Any,
    ) -> CTkFrameLayout:
        """with_frame_as_stack

        Creates a frame set that consists of a stack of frames

        Args:
            master (CTkFrame): master frame into which this frame is placed
            number (int, optional): number of frames in the stack. Defaults to 3

        Returns:
            CTkFrameLayout: this frame set that consists of a stack of frames
        """
        #  Create a frame layout with a stack of frames

        _frames: CTkFrameLayoutStack = CTkFrameLayoutStack(
            master, *args, number=number, **kwargs
        )

        #  Update the dunder __str__ and __repr__ string

        _frames._str = f"CTkFrameSet with_frame_stack"
        _frames._repr = f"CTkFrameSet with_frame_stack (master={master}, *args={args}, number={number}, **kwargs{kwargs})"

        #  Return the frame set

        return _frames

    @staticmethod
    def with_predefined_frame_layout(
        master: CTk | CTkFrame | CTkFormattedFrame,
        *args: Any,
        layout: int,
        gutter: int = 5,
        **kwargs: Any,
    ) -> CTkFrameLayout:
        """with_predefined_frame_frames

        Creates a frame set that consists of a predefined layout of frames

        Args:
            master (CTkFrame): master frame into which this frame is placed
            layout (int, optional): number of predefined layout to use
            gutter (int, optional): gutter between frames in the grid. Defaults to 5

        Returns:
            CTkFrameLayout: this frame set that consists of a grid of frames
        """
        #  Create the appropriate layout of frames for the frame set

        match layout:
            case 0:
                _frames: CTkFrameLayout = CTkFrameLayout0(
                    master,
                    *args,
                    **kwargs,
                )
            case 1:
                _frames: CTkFrameLayout = CTkFrameLayout1(
                    master, *args, gutter=gutter, **kwargs
                )
            case 2:
                _frames: CTkFrameLayout = CTkFrameLayout2(
                    master, *args, gutter=gutter, **kwargs
                )
            case 3:
                _frames: CTkFrameLayout = CTkFrameLayout3(
                    master, *args, gutter=gutter, **kwargs
                )
            case 4:
                _frames: CTkFrameLayout = CTkFrameLayout4(
                    master, *args, gutter=gutter, **kwargs
                )
            case 5:
                _frames: CTkFrameLayout = CTkFrameLayout5(
                    master, *args, gutter=gutter, **kwargs
                )
            case 6:
                _frames: CTkFrameLayout = CTkFrameLayout6(
                    master, *args, gutter=gutter, **kwargs
                )
            case 7:
                _frames: CTkFrameLayout = CTkFrameLayout7(
                    master, *args, gutter=gutter, **kwargs
                )
            case 8:
                _frames: CTkFrameLayout = CTkFrameLayout8(
                    master, *args, gutter=gutter, **kwargs
                )
            case 9:
                _frames: CTkFrameLayout = CTkFrameLayout9(
                    master, *args, gutter=gutter, **kwargs
                )
            case 10:
                _frames: CTkFrameLayout = CTkFrameLayout10(
                    master, *args, gutter=gutter, **kwargs
                )
            case 11:
                _frames: CTkFrameLayout = CTkFrameLayout11(
                    master, *args, gutter=gutter, **kwargs
                )
            case 12:
                _frames: CTkFrameLayout = CTkFrameLayout12(
                    master, *args, gutter=gutter, **kwargs
                )
            case 13:
                _frames: CTkFrameLayout = CTkFrameLayout13(
                    master, *args, gutter=gutter, **kwargs
                )
            case 14:
                _frames: CTkFrameLayout = CTkFrameLayout14(
                    master, *args, gutter=gutter, **kwargs
                )
            case 15:
                _frames: CTkFrameLayout = CTkFrameLayout15(
                    master, *args, gutter=gutter, **kwargs
                )
            case 16:
                _frames: CTkFrameLayout = CTkFrameLayout16(
                    master, *args, gutter=gutter, **kwargs
                )
            case 17:
                _frames: CTkFrameLayout = CTkFrameLayout17(
                    master, *args, gutter=gutter, **kwargs
                )
            case 18:
                _frames: CTkFrameLayout = CTkFrameLayout18(
                    master, *args, gutter=gutter, **kwargs
                )
            case 19:
                _frames: CTkFrameLayout = CTkFrameLayout19(
                    master, *args, gutter=gutter, **kwargs
                )
            case 20:
                _frames: CTkFrameLayout = CTkFrameLayout20(
                    master, *args, gutter=gutter, **kwargs
                )
            case 21:
                _frames: CTkFrameLayout = CTkFrameLayout21(
                    master, *args, gutter=gutter, **kwargs
                )
            case 22:
                _frames: CTkFrameLayout = CTkFrameLayout22(
                    master, *args, gutter=gutter, **kwargs
                )
            case 23:
                _frames: CTkFrameLayout = CTkFrameLayout23(
                    master, *args, gutter=gutter, **kwargs
                )
            case 24:
                _frames: CTkFrameLayout = CTkFrameLayout24(
                    master, *args, gutter=gutter, **kwargs
                )
            case _:
                _frames: CTkFrameLayout = CTkFrameLayout0(
                    master, *args, gutter=gutter, **kwargs
                )

        #  Return the frame set

        return _frames
