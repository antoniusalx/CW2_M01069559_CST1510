# Copilot Instructions for CW2_M01069559_CST1510

## Project Overview
This is a CST1510 coursework project (Module M01069559). Currently contains a minimal Python setup with `test.py` as the starting point. The project is likely a data analysis or computational assignment given the naming convention.

## Architecture & Structure
- **`test.py`**: Entry point for the project. Currently a minimal placeholder.
- **`.git/`**: Version control repository with initial commit.

This is an early-stage project. As you develop, maintain clear separation between:
- **Data processing logic**: Core algorithms and data transformations
- **Test suite**: Unit/integration tests (expand beyond `test.py`)
- **Utilities**: Helper functions and shared code

## Development Workflow

### Running & Testing
```bash
# Run the main script
python test.py

# To add tests, follow Python conventions:
# - Create test files with `test_*.py` naming
# - Use unittest or pytest for test execution
```

### Key Conventions to Follow
1. **Python Style**: Follow PEP 8 for consistency
2. **Testing**: Create separate test files; don't mix tests and implementation
3. **Git Commits**: Use clear, descriptive commit messages referencing the coursework context
4. **Dependencies**: If adding external packages, maintain a `requirements.txt` file

## Integration Points & Dependencies
- Currently has no external dependencies (pure Python)
- When adding packages, document them in `requirements.txt`
- For data processing coursework, common dependencies might be: `numpy`, `pandas`, `matplotlib`

## Patterns & Conventions
- This appears to be a **coursework submission** - maintain clarity for academic evaluation
- Start with small, well-documented functions
- Use type hints for function parameters where applicable
- Include docstrings explaining algorithm logic

## Quick Start for AI Agents
1. Read `test.py` first to understand existing structure
2. When implementing features, create focused functions with single responsibilities
3. Add unit tests in `test_*.py` files as features are implemented
4. Update `requirements.txt` if new packages are needed
