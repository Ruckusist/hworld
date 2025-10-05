# Hworld

A collection of tools and utilities built in the spirit of Unix philosophy: do one thing well, compose with other tools, and keep things simple and modular.

## Project Philosophy

- **Python First**: We prefer Python classes and keep functions small.
- **Clean Code**: 4-space indentation, CamelCase naming, double quotes, 79-character lines.
- **Self-Contained**: Build our own tools rather than relying on external dependencies where possible.
- **Unix Inspired**: Think in terms of pipes, filters, and composable components.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Ruckusist/hworld.git
   cd hworld
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Run the tool:
   ```bash
   hworld
   ```

## Development

- Follow the coding standards outlined in `.github/copilot-instructions.md`
- Keep functions and files small
- Work in complete sections
- Always credit changes in the changelog

## Contributing

1. Create a proposal in `.github/proposals/`
2. Implement changes following project conventions
3. Update the changelog
4. Submit a pull request

## License

[Add license information here]
