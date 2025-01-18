#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
from code.logic.appmain import main
import sys
import os

# Add the root directory to the Python path so you can import project modules.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # If no command-line arguments provided, run the main program (main.py).
        main()

    elif sys.argv[1] == "test":
        # If the argument "test" is provided, run the test suite using pytest.
        import pytest

        # Run the three pytest files in the root directory.
        pytest.main(["test_mainapp.py", "test_dialogs.py", "test_background.py"])
    else:
        print("Usage: python project.py [test]")
