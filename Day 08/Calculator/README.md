# Task 8 – Simple CLI Calculator
 AI-Driven Development – 30-Day Challenge

## 📝 Overview
For this task, we built a **Simple CLI Calculator** using **SpecKitPlus**, following 5 core commands. The calculator was created by following these steps:

1. `/sp.constitution` – Defined the project idea and scope: *"Simple calculator with basic operations"*
2. `/sp.specify` – Defined input and output: *"calculator: input expr (string) → output result (number)"*
3. `/sp.plan` – Planned the logic: *"take expression, validate, evaluate, return number"*
4. `/sp.tasks` – Broke down the tasks:
   1. Receive input
   2. Validate expression
   3. Evaluate safely
   4. Return result
5. `/sp.implement` – Implemented the calculator using the above plan

##  How It Was Built
The calculator was created by following these steps:

### Initialize SpecKitPlus project
specify init calculator

cd calculator

### Execute the 5 core commands in the prompt to define & implement the calculator
/sp.constitution "simple calculator with basic operations"

/sp.specify "calculator: input expr (string) output result number"

/sp.plan "take expression validate evaluate return number"

/sp.tasks "1 receive input 2 validate expression 3 evaluate safely 4 return result"

/sp.implement "implement calculator in five core commands"

## Project Structure

```
.
├── .gitignore
├── CLAUDE.md
├── README.md
├── requirements.txt
├── .claude/
│   └── commands/
│       ├── sp.adr.md
│       ├── sp.analyze.md
│       ├── sp.checklist.md
│       ├── sp.clarify.md
│       ├── sp.constitution.md
│       ├── sp.git.commit_pr.md
│       ├── sp.implement.md
│       ├── sp.phr.md
│       ├── sp.plan.md
│       ├── sp.specify.md
│       └── sp.tasks.md
├── .git/...
├── .specify/
│   ├── memory/
│   │   └── constitution.md
│   ├── scripts/
│   │   └── powershell/
│   │       ├── check-prerequisites.ps1
│   │       ├── common.ps1
│   │       ├── create-new-feature.ps1
│   │       ├── setup-plan.ps1
│   │       └── update-agent-context.ps1
│   └── templates/
│       ├── adr-template.md
│       ├── agent-file-template.md
│       ├── checklist-template.md
│       ├── phr-template.prompt.md
│       ├── plan-template.md
│       ├── spec-template.md
│       └── tasks-template.md
├── .venv/
│   ├── Include/...
│   ├── Lib/...
│   └── Scripts/...
├── history/
│   └── prompts/
│       ├── 001-calculator-app/
│       ├── calculator-app/
│       │   ├── 0003-create-simple-calculator-app-specification.spec.prompt.md
│       │   └── 0004-generate-simple-calculator-app-tasks.tasks.prompt.md
│       └── constitution/
│           └── 0002-update-simple-calculator-app-constitution.constitution.prompt.md
├── specs/
│   └── 001-calculator-app/
│       ├── plan.md
│       ├── spec.md
│       ├── tasks.md
│       └── checklists/
│           └── requirements.md
├── src/
│   ├── __init__.py
│   ├── calculator_core.py
│   ├── display_manager.py
│   ├── input_parser.py
│   ├── main.py
│   ├── utils.py
│   └── __pycache__/
└── tests/
    ├── __init__.py
    ├── integration/
    │   └── test_full_workflow.py
    └── unit/
        ├── test_calculator_core.py
        └── test_input_parser.py
```

## Getting Started

### Prerequisites

- `pip` for package installation

### Installation

   ```bash
   specify init Calculator
   cd Calculator
   ```
## execute 5 core commands using SpecKitPlus as described above.   
1. /sp.constitution "simple calculator with basic operations"  
2. /sp.specify "calculator: input expr (string) output result number"  
3. /sp.plan "take expression validate evaluate return number"  
4. /sp.tasks "1 receive input 2 validate expression 3 evaluate safely 4 return result"  
5. /sp.implement "implement calculator in five core commands"     

## Usage

To run the calculator, execute the `main.py` script from the `src` directory:

```bash
python src/main.py
```

This will start the CLI calculator which can perform basic operations: +, -, *, /
