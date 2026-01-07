# Evaluation Datasets

This directory contains the evaluation datasets used in the paper.

## Dataset Overview

Total: **800 tasks** across 4 domains

| Domain | Tasks | Source | Format |
|--------|-------|--------|--------|
| Legal | 200 | ContractNLI + Custom | JSONL |
| Math | 200 | GSM8K | JSONL |
| QA | 200 | Natural Questions | JSONL |
| Economic | 200 | Custom | JSONL |

## Directory Structure

```
datasets/
├── legal/
│   └── sample_tasks.jsonl      # 5 sample tasks (full: 200)
├── math/
│   └── sample_tasks.jsonl      # 5 sample tasks (full: 200)
├── qa/
│   └── sample_tasks.jsonl      # 5 sample tasks (full: 200)
└── economic/
    └── sample_tasks.jsonl      # 5 sample tasks (full: 200)
```

## File Format

Each `.jsonl` file contains one task per line in JSON format:

```json
{
  "id": "math_001",
  "task": "Task description text...",
  "answer": "Expected answer",
  "domain": "math",
  "difficulty": "medium",
  "steps": 3
}
```

### Fields

- **id**: Unique task identifier (`{domain}_{number}`)
- **task**: Natural language task description
- **answer**: Ground truth answer
- **domain**: One of: `legal`, `math`, `qa`, `economic`
- **difficulty**: One of: `easy`, `medium`, `hard`
- **steps**: Number of reasoning steps required

## Full Datasets

**Note**: Only sample tasks (5 per domain) are included in this repository for demonstration purposes.

The full 800-task evaluation set used in the paper is available upon request:
- Legal: 200 tasks (ContractNLI license: CC BY-SA 4.0)
- Math: 200 tasks (GSM8K license: MIT)
- QA: 200 tasks (Natural Questions license: CC BY-SA 3.0)
- Economic: 200 tasks (Custom, license: CC BY 4.0)

**To request full datasets**: Contact nechesov@gmail.com

## Using the Datasets

### Load a dataset

```python
import jsonlines

# Load tasks
tasks = []
with jsonlines.open('datasets/math/sample_tasks.jsonl') as reader:
    for task in reader:
        tasks.append(task)

print(f"Loaded {len(tasks)} tasks")
```

### Run evaluation

```python
# See experiments/ for full evaluation scripts
from experiments.math_reasoning import evaluate_math

results = evaluate_math(tasks, model="gpt-4")
```

## Dataset Statistics

### Legal Domain (200 tasks)
- Contract fulfillment: 80 tasks
- Breach identification: 60 tasks
- Liability determination: 40 tasks
- Remedies calculation: 20 tasks

### Math Domain (200 tasks)
- Arithmetic (2-3 steps): 80 tasks
- Arithmetic (4-5 steps): 80 tasks
- Arithmetic (6+ steps): 40 tasks
- Algebraic: 60 tasks
- Geometric: 40 tasks

### QA Domain (200 tasks)
- Factoid questions: 120 tasks
- Multi-hop reasoning: 50 tasks
- Temporal reasoning: 30 tasks

### Economic Domain (200 tasks)
- Investment recommendations: 80 tasks
- Risk assessment: 60 tasks
- Portfolio optimization: 40 tasks
- Market trend analysis: 20 tasks

## Ground Truth

All tasks include verified ground truth answers:
- Legal: Annotated by 2 legal experts (Cohen's κ = 0.89)
- Math: GSM8K original annotations
- QA: Natural Questions short answers
- Economic: 3 financial analyst consensus

## Citations

If you use these datasets, please cite the original sources:

**ContractNLI**:
```bibtex
@inproceedings{koreeda2021contractnli,
  title={ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts},
  author={Koreeda, Yuta and Manning, Christopher D},
  booktitle={Findings of EMNLP 2021},
  year={2021}
}
```

**GSM8K**:
```bibtex
@article{cobbe2021gsm8k,
  title={Training Verifiers to Solve Math Word Problems},
  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and others},
  journal={arXiv preprint arXiv:2110.14168},
  year={2021}
}
```

**Natural Questions**:
```bibtex
@article{kwiatkowski2019natural,
  title={Natural Questions: a Benchmark for Question Answering Research},
  author={Kwiatkowski, Tom and Palomaki, Jennimaria and Redfield, Olivia and others},
  journal={Transactions of the ACL},
  year={2019}
}
```

## License

- Legal tasks: CC BY-SA 4.0 (ContractNLI) + CC BY 4.0 (Custom)
- Math tasks: MIT (GSM8K)
- QA tasks: CC BY-SA 3.0 (Natural Questions)
- Economic tasks: CC BY 4.0 (Custom)
