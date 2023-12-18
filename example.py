# Karl Jones, Dec 2023

from customtkinter import CTkButton, CTkLabel  # type: ignore - call to CustomTknter

from ctkrootwindow import CTkFrameLayout, CTkFrameSet, CTkRootWindow

_stackSize: int = 25

# Create navigation methods


def previous():
    global _index
    _index = (_index - 1) % _stackSize
    _stack.frameStack[_index].tkraise()  # type: ignore - call to CustomTknter
    _label.configure(text=f"Predefined layout #{_index}")  # type: ignore - call to CustomTknter


def next():
    global _index
    _index = (_index + 1) % _stackSize
    _stack.frameStack[_index].tkraise()  # type: ignore - call to CustomTknter
    _label.configure(text=f"Predefined layout #{_index}")  # type: ignore - call to CustomTknter


# Create and configure the root window with predefined layout #1 (top and main).

_root: CTkRootWindow = CTkRootWindow.with_frames_from_predefined_layout(
    title="Example Predefined Layouts",
    width=800,
    height=600,
    layout=1,
    gutter=5,
    padx=(20, 20),
    pady=(20, 20),
)
if _root.frames is not None and _root.frames.main is not None:
    _root.frames.configure(fg_color="transparent")  # type: ignore - call to CustomTknter
    _root.frames.main.configure(fg_color="transparent")  # type: ignore - call to CustomTknter

# Crate a stack of subframes in frameMain.

_index: int = 0

if _root.frames is not None and _root.frames.main is not None:
    _stack: CTkFrameLayout = CTkFrameSet.with_frames_as_stack(
        master=_root.frames.main, number=_stackSize
    )
    _stack.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nwse")  # type: ignore - call to CustomTknter

    # In each subframe create a new predefined layout: layout =1 in subframe 1, and so on.

    if _stack.frameStack is not None:
        for _index, _frame in enumerate(_stack.frameStack):
            _layout = CTkFrameSet.with_predefined_frame_layout(
                _frame, layout=_index, gutter=5
            )
            _layout.grid(row=0, column=0, padx=0, pady=0, sticky="nwse")  # type: ignore - call to CustomTknter

    # Bring the first subframe to the top.

    _index = 0
    _stack.frameStack[_index].tkraise()  # type: ignore - call to CustomTknter

# Configure frameTop and create navigation buttons and label

if _root.frames is not None and _root.frames.top is not None:
    _root.frames.top.grid_columnconfigure(index=0, weight=0)
    _root.frames.top.grid_columnconfigure(index=1, weight=0)
    _root.frames.top.grid_columnconfigure(index=2, weight=1)

_button1: CTkButton = CTkButton(_root.top, text="Previous", command=previous)
_button1.grid(row=0, column=0, padx=(10, 0), pady=0, sticky="w")  # type: ignore - call to CustomTknter

_button2: CTkButton = CTkButton(_root.top, text="Next", command=next)
_button2.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="w")  # type: ignore - call to CustomTknter

_label: CTkLabel = CTkLabel(_root.top, text=f"Predefined layout #{_index}")
_label.grid(row=0, column=2, padx=(0, 15), pady=0, sticky="e")  # type: ignore - call to CustomTknter

# Continue the input loop

CTkFrameSet.with_predefined_frame_layout
_root.mainloop()  # type: ignore - call to CustomTknter
