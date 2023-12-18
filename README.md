# CTkRootWindow and CTkFrameSet
A simple class to create CTk root window with a number of optional predefined frame layouts.

NOTE: CustomTkinter seems to cause problems with strict type checking - I have had to make liberal use of "# type: ignore".

### CTkRootWindow

CTkRootWindow is a subclass of CTk. 

The CTkRootWindow can be instantiated directly, for example:

```
_root: CTkRootWindow = CTkRootWindow(
    title="Example Predefined Layouts",
    width=800,
    height=600,
    padx=(20, 20),
    pady=(20, 20),
)
```

### CTkRootWindow.with_frames_as_grid


The CTkRootWindow can also be instantiated using one of the class methods to return a root window with a predefined layout of frames. For example the following will return a CTkRootWindow with a grid of frames which consists of two rows and three columns:


```
_root: CTkRootWindow = CTkRootWindow.with_frames_as_grid(
    title="Example Predefined Layouts",
    width=800,
    height=600,
    rows=2,
    columns=3
    gutter=5,
    padx=(20, 20),
    pady=(20, 20),
)
```

The set of frames is exposed by the 'frameGrid' property.

### CTkRootWindow.with_frames_as_stack

The CTkRootWindow can also be instantiated using one of the class methods to return a root window with a predefined layout of frames. For example the following will return a CTkRootWindow with a stack of five frames:


```
_root: CTkRootWindow = CTkRootWindow.with_frames_as_stack(
    title="Example Predefined Layouts",
    width=800,
    height=600,
    number=15,
    gutter=5,
    padx=(20, 20),
    pady=(20, 20),
)
```
The set of frames is exposed by the 'frameStack' property.

### CTkRootWindow.with_frames_from_predefined_layout

The CTkRootWindow can also be instantiated using one of the class methods to return a root window with a predefined layout of frames. There are twenty five predefined layout numbered from 0 to 24. For example the following will return a CTkRootWindow with predefined layout #1:


```
_root: CTkRootWindow = CTkRootWindow.with_frames_from_predefined_layout(
    title="Example Predefined Layouts",
    width=800,
    height=600,
    layout=1,
    gutter=5,
    padx=(20, 20),
    pady=(20, 20),
)
```

The predefined layouts consist of an arrangemnt of up to five frames. These are exposed in the properties 'top', 'bottom', 'left', 'right' and 'main.' Frames not used in any particular layout will remain as None.

### CTkFrameSet

If a new root window is not required the CTkFrameSet can be used to create a set of frames within an existing window.

Usage is simlar to CTkRootWindowand the predefined layouts consist of an arrangemnt of up to five frames. These are exposed in the properties 'top', 'bottom', 'left', 'right' and 'main.' Frames not used in any particular layout will remain as None.

Unlike the CTkRootWindow the CTkrameSet should only be instantiated using one of the class methods. The class methods are:

CTkFrameSet.with_frame_as_grid
CTkFrameSet.with_frame_as_stack
CTkFrameSet.with_predefined_frame_layout

For example:

```
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
_root.frames.configure(fg_color="transparent")
_root.frames.main.configure(fg_color="transparent")

# Crate a stack of subframes in frameMain.

_stack: CTkFrameSet = CTkFrameSet.with_frames_as_stack(
    master=_root.frames.main, number=_stackSize
)
_stack.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nwse")
```

### Example

The CTkRootWindow package includes a script, example.py which demontrates the twenty-five different frame layouts.