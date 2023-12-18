#  Karl Jones, Dec 2023

from typing import Any, List, Optional, Self, Tuple

from customtkinter import CTk  # type: ignore - call to CustomTknter

from .ctkframeset import CTkFrameSet
from .framelayouts import CTkFormattedFrame, CTkFrameLayout


class CTkRootWindow(CTk):
    """CTkRootWindow

    The root window class that will contain a set of predefined frames
    """

    @property
    def frames(self) -> Optional[CTkFrameLayout]:
        """frames

        The 'frames' property exposes the predefined frame set
        It may be None

        Returns:
            Optional[CTkFrameSet]: frame set
        """
        return self._frames

    @property
    def frameGrid(self) -> Optional[List[List[CTkFormattedFrame]]]:
        """frameGrid

        The 'frameGrid' property exposes the predefined two-dimensional grid of frames
        It may be None:

        Returns:
            Optional[List[List[CTkFormattedFrame]]]: two-dimensional grid of frames
        """
        if self._frames is not None:
            return self._frames.frameGrid
        else:
            return None

    @property
    def frameStack(self) -> Optional[List[CTkFormattedFrame]]:
        """frameStack

        The 'frameStack' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[List[CTkFormattedFrame]] | None: the stack of frames
        """
        if self._frames is not None:
            return self._frames.frameStack
        else:
            return None

    @property
    def top(self) -> Optional[CTkFormattedFrame]:
        """top

        The 'top' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[CTkFormattedFrame] | None: the stack of frames
        """

        if self._frames is not None:
            return self._frames.top
        else:
            return None

    @property
    def bottom(self) -> Optional[CTkFormattedFrame]:
        """bottom

        The 'bottom' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: the stack of frames
        """

        if self._frames is not None:
            return self._frames.bottom
        else:
            return None

    @property
    def left(self) -> Optional[CTkFormattedFrame]:
        """left

        The 'left' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]]: stack of frames
        """

        if self._frames is not None:
            return self._frames.left
        else:
            return None

    @property
    def right(self) -> Optional[CTkFormattedFrame]:
        """right

        The 'right' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: the stack of frames
        """

        if self._frames is not None:
            return self._frames.right
        else:
            return None

    @property
    def main(self) -> Optional[CTkFormattedFrame]:
        """main

        The 'main' property exposes the predefined stack of frames
        It may be None:

        Returns:
            Optional[CTkFormattedFrame]: the stack of frames
        """

        if self._frames is not None:
            return self._frames.main
        else:
            return None

    def __init__(
        self,
        *args: Any,
        title: str,
        width: int,
        height: int,
        xpos: Optional[float] = None,
        ypos: Optional[float] = None,
        **kwargs: Any,
    ) -> None:
        """__init__

        Initialises the root window

        Args:
            title (str): title of the root window
            width (int): width of the root window
            height (int): height of the root window
            xpos (Optional[int | None], optional): x position of the window. Defaults to None
            ypos (Optional[int | None], optional): y position of the window. Defaults to None
        """

        #  Initialise the CTk object

        super().__init__(*args, **kwargs)  # type: ignore - call to CustomTknter

        #  Configure the root window

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.title(title)

        #  Center the root window in x if xpos is not set

        _xpos: float = (
            (self.winfo_screenwidth() / 2) - (width / 2) if xpos is None else xpos
        )

        #  Center the root window in y if ypos is not set

        _ypos: float = (
            (self.winfo_screenheight() / 2) - (height / 2) if ypos is None else ypos
        )

        #  Set size and position of window

        self.geometry(f"{width}x{height}+{int(_xpos)}+{int(_ypos)}")

        #  Initialise the 'frames' property

        self._frames: Optional[CTkFrameLayout] = None

        #  Set the root window's descriptors

        self._str: str = f'CTkRootWindow "{title}"'
        self._repr: str = f"CTkRootWindow (*args={args},  **kwargs{kwargs})"

    #  Implement some dunder functions

    def __str__(self) -> str:
        return self._str

    def __repr__(self) -> str:
        return self._repr

    #  Class methods to create the root winodw with optional predefined frame layouts

    @classmethod
    def with_frames_as_grid(
        cls,
        *args: Any,
        title: str,
        width: int,
        height: int,
        rows: int = 2,
        columns: int = 3,
        gutter: int = 5,
        xpos: Optional[float] = None,
        ypos: Optional[float] = None,
        padx: Optional[Tuple[int, int]] = (0, 0),
        pady: Optional[Tuple[int, int]] = (0, 0),
        **kwargs: Any,
    ) -> Self:
        """with_frames_as_grid

        Creates a root window with a frame set that consists of a grid of frames

        Args:
            title (str): title of the root window
            width (int): width of the root window
            height (int): height of the root window
            rows (int, optional): number of rows in the grid. Defaults to 2
            columns (int, optional): number of columns in the grid. Defaults to 3
            gutter (Optional[int], optional): gutter between frames in the grid. Defaults to 5
            xpos (Optional[int | None], optional): x position of the window. Defaults to None
            ypos (Optional[int | None], optional): y position of the window. Defaults to None
            padx (Optional[Tuple[int, int]], optional): x poadding around the whole frame set. Defaults to (0, 0)
            pady (Optional[Tuple[int, int]], optional): y padding around the whole frame set. Defaults to (0, 0)

        Returns:
            Self: this root winodw with a frame set that consists of a grid of frames
        """

        #  Create an instance of the root window

        _rootWindow: Self = cls(
            *args,
            title=title,
            width=width,
            height=height,
            xpos=xpos,
            ypos=ypos,
            **kwargs,
        )

        #  Create the frame set

        _rootWindow._frames = CTkFrameSet.with_frames_as_grid(
            _rootWindow, rows=rows, columns=columns, gutter=gutter
        )

        #  Add the frame set to the root window

        _rootWindow._frames.grid(row=0, column=0, padx=padx, pady=pady, sticky="nswe")  # type: ignore - call to CustomTknter

        #  Update the dunder __repr__ string

        _rootWindow._repr = f'CTkRootWindow with_frame_as_grid (*args={args}, title="{title}", width={width}, height={height}, rows={rows}, columns={columns}, gutter={gutter}, padx={padx}, pady={pady}, **kwargs{kwargs})'

        #  Return this root window

        return _rootWindow

    @classmethod
    def with_frames_as_stack(
        cls,
        *args: Any,
        title: str,
        width: int,
        height: int,
        number: int = 3,
        xpos: Optional[float] = None,
        ypos: Optional[float] = None,
        padx: Optional[Tuple[int, int]] = (0, 0),
        pady: Optional[Tuple[int, int]] = (0, 0),
        **kwargs: Any,
    ) -> Self:
        """with_frames_as_stack

        Creates a root window with a frame set that consists of a stack of frames

        Args:
            title (str): title of the root window
            width (int): width of the root window
            height (int): height of the root window
            number (int, optional): number of frames in the stack. Defaults to 3.
            xpos (Optional[int | None], optional): x position of the window. Defaults to None
            ypos (Optional[int | None], optional): y position of the window. Defaults to None
            padx (Optional[Tuple[int, int]], optional): x poadding around the whole frame set. Defaults to (0, 0)
            pady (Optional[Tuple[int, int]], optional): y padding around the whole frame set. Defaults to (0, 0)

        Returns:
            Self: this root winodw with a frame set
        """

        #  Create an instance of the root window

        _rootWindow: Self = cls(
            *args,
            title=title,
            width=width,
            height=height,
            xpos=xpos,
            ypos=ypos,
            **kwargs,
        )

        #  Create the frame set

        _rootWindow._frames = CTkFrameSet.with_frames_as_stack(
            _rootWindow, number=number
        )

        #  Add the frame set to the root window

        _rootWindow._frames.grid(row=0, column=0, padx=padx, pady=pady, sticky="nswe")  # type: ignore - call to CustomTknter

        #  Update the dunder __repr__ string

        _rootWindow._repr = f'CTkRootWindow with_frame_as_stack (*args={args}, title="{title}", number={number}, padx={padx}, pady={pady}, **kwargs{kwargs})'

        #  Return this root window

        return _rootWindow

    @classmethod
    def with_frames_from_predefined_layout(
        cls,
        *args: Any,
        title: str,
        width: int,
        height: int,
        layout: int,
        gutter: int = 5,
        xpos: Optional[float] = None,
        ypos: Optional[float] = None,
        padx: Optional[Tuple[int, int]] = (0, 0),
        pady: Optional[Tuple[int, int]] = (0, 0),
        **kwargs: Any,
    ) -> Self:
        """with_frames_from_predefined_layout

        Creates a root window with a frame set that consists of a predefined layout
        Layouts are number from 0 to 24

        Args:
            title (str): title of the root window
            width (int): width of the root window
            height (int): height of the root window
            layout (int): number of predefined layout to use
            gutter (Optional[int], optional): gutter between frames in the layout. Defaults to 5
            xpos (Optional[int | None], optional): x position of the window. Defaults to None
            ypos (Optional[int | None], optional): y position of the window. Defaults to None
            padx (Optional[Tuple[int, int]], optional): x poadding around the whole frame set. Defaults to (0, 0)
            pady (Optional[Tuple[int, int]], optional): y padding around the whole frame set. Defaults to (0, 0)

        Returns:
            Self: this root winodw with a frame set
        """

        #  Create an instance of the root window

        _rootWindow: Self = cls(
            *args,
            title=title,
            width=width,
            height=height,
            xpos=xpos,
            ypos=ypos,
            **kwargs,
        )

        #  Create the frame set

        _rootWindow._frames = CTkFrameSet.with_predefined_frame_layout(
            _rootWindow, layout=layout, gutter=gutter
        )

        #  Add the frame set to the root window

        _rootWindow._frames.grid(row=0, column=0, padx=padx, pady=pady, sticky="nswe")  # type: ignore - call to CustomTknter

        #  Update the dunder __repr__ string

        _rootWindow._repr = f'CTkRootWindow with_predefined_frame_layout (*args={args}, title="{title}", width={width}, height={height}, layout={layout}, gutter={gutter}, padx={padx}, pady={pady}, **kwargs{kwargs})'

        #  Return this root window

        return _rootWindow
