# Copilot Instructions

This file provides guidelines for using GitHub Copilot and Copilot Chat in this repository.

## How to Use Copilot
- Use Copilot to generate code suggestions, documentation, and tests.
- Review all Copilot-generated code for correctness and security before merging.
- Use Copilot Chat for troubleshooting, refactoring, and code explanations.

## Best Practices
- Always validate Copilot suggestions with manual review and testing.
- Prefer Copilot for boilerplate, repetitive tasks, and documentation generation.
- Do not commit sensitive information or credentials suggested by Copilot.
- Use clear prompts to get the best results from Copilot Chat.

## Package Management
- Every time you import a Python package or add a package to a requirements.txt or pyproject.toml, use the safety-mcp to check if the version you have chosen is secure and is the latest version of the package. Make sure you always use the latest_secure_version (returned by safety-mcp) for any package.
- If a package already exists in a codebase, and a user asks you to check it for vulnerabilities, use the safety-mcp and evaluate whether there are any secure versions in the same major version and acknowledge these options. Additionally, inform the user of the latest secure version of the package.

## Troubleshooting
- If Copilot suggestions are incorrect, provide more context or clarify your prompt.
- For environment or dependency issues, use Copilot Chat to get step-by-step help.

## Security & Privacy
- Do not use Copilot to generate or handle secrets, passwords, or private keys.
- Remove any Copilot-generated sensitive data before committing.

## Feedback
- Report issues or improvement suggestions for Copilot usage in this repository to the maintainers.

---
_Last updated: August 8, 2025_
