# static_code_analysis_PES2UG23CS290
# Reflection

### Q1: Which issues were the easiest to fix, and which were the hardest? Why?
- **Easiest to fix**: The **string formatting** issue was the easiest fix, as it just required switching to f-strings. The **blank line errors** were also easy to address by adding the necessary blank lines between functions and class definitions.
- **Hardest to fix**: The **global statement** was the most difficult to fix because it required refactoring the way `stock_data` was handled across functions. It required a more structured approach to return and pass data rather than relying on a global variable.

### Q2: Did the static analysis tools report any false positives? If so, describe one example.
- There were **no false positives** reported by the tools. All flagged issues were valid and contributed to improving the quality and safety of the code.

### Q3: How would you integrate static analysis tools into your actual software development workflow?
- I would integrate static analysis tools like Pylint, Flake8, and Bandit into the **continuous integration (CI) pipeline** to ensure that every code change is checked for style violations, bugs, and security vulnerabilities before being merged into the main branch.
- Additionally, I would use these tools locally by setting up pre-commit hooks to catch issues before committing code changes.

### Q4: What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- **Code quality**: The code is now more **robust** with proper error handling and input validation. For example, adding checks for non-integer quantities in `add_item` ensures that invalid input does not break the program.
- **Readability**: The use of f-strings, proper docstrings for functions, and better spacing between functions makes the code much easier to read and follow.
- **Maintainability**: The removal of the `global` statement and refactoring of functions to handle stock data more explicitly improves the **maintainability** of the code, making it easier to extend and debug.
- **Security**: The removal of `eval()` reduces security risks, as `eval()` can execute arbitrary code if the input is not properly sanitized.

