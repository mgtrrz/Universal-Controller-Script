
# Contributing

Note that documentation is only of overarching designs and how-tos. Code in
the project is documented using docstring, and will be displayed inline by
most code editors.

## Getting Started

1.  Set up the project as per the [main instructions](../setup.md), but instead
    of cloning the project directly,
    [create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
    where your work can be done without the risk of breaking the project. When
    your work is done, you can create a pull request to merge your improvements
    into the main project. Make sure you clone the project recursively.
2.  Install [Python](https://www.python.org/downloads/) (if you're on Windows,
    on MacOS it is built in)
3.  Open the repository in your editor of choice. I've ensured it works well with
    [VS Code](https://code.visualstudio.com), but others should be fine too.
4.  Install any recommended extensions if you are in VS Code
5.  Open a terminal in the repository folder and create a Python
    [virtual environment](https://docs.python.org/3/library/venv.html). This will
    keep the project's dependencies separate from any other ones you have
    installed, ensuring nothing can get broken. Run `python -m venv .venv`.
6.  When VS Code or your editor prompts you to activate the virtual environment,
    do so.
7.  Activate the virtual environment in your terminal (refer to the virtual
    environment documentation linked above). In VS Code you can just restart your
    terminal.
8.  Install the project dependencies. Run `pip install -r requirements.txt`.
9.  Ensure that your coding environment is functioning correctly by running the
    code from your editor. If all your dependencies are set up correctly, it
    will start up, print the welcome message then exit.
10. Get familiar with the project's [style guidelines](style.md)

## Contributing Docs
* [Style guide](style.md)
* [Plugins](plugins.md)
* [Devices](devices.md)
* [Control surfaces](controlsurface.md)
* [Control matchers](controlmatcher.md)
* [Control events](controlevent.md)
* [Device shadows](deviceshadow.md)
* [Control shadows](controlshadow.md)
* [Event filters](eventfilter.md)
* [Event patterns](eventpattern.md)
* [Mapping strategies](mappingstrategy.md)
* [Value strategies](valuestrategy.md)
* [Performance profiling](performance.md)
