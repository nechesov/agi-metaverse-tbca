# AGI-Powered Metaverse: Task-Based Cognitive Architecture

[![Paper](https://img.shields.io/badge/Paper-IEEE%20Access-blue)](https://ieeexplore.ieee.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

Official implementation of **"The AGI-Powered Metaverse: A Decentralized Task-Based Cognitive Architecture"** submitted to IEEE Access (2026).

**Author**: Andrey Nechesov (Novosibirsk State University)

---

## 🎯 Quick Start (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/nechesov/agi-metaverse-tbca.git
cd agi-metaverse-tbca

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run demo task
python demo/simple_demo.py
```

**Expected output**:
```
Task: "Sarah buys 5 notebooks at $3 each and some pens at $2 each, spending $25. How many pens?"
Answer: 5 pens
Confidence: 0.931
Status: ✓ VALIDATED
```

---

## 📊 Paper Results Reproduction

Our system achieves the following results on 800 evaluation tasks:

| Domain | Accuracy | Confidence | Gap Resolution |
|--------|----------|------------|----------------|
| Legal | 89.3% ± 1.2% | 0.876 | 21% |
| Math | 85.0% ± 1.5% | 0.875 | 28% |
| QA | 87.5% ± 1.1% | 0.869 | 19% |
| Economic | 84.0% ± 1.8% | 0.862 | 25% |

All results from the paper can be reproduced using the scripts in [`experiments/`](experiments/).

---

## 🏗️ Architecture Overview

Three-layer hybrid system combining:

1. **LLM Layer**: GPT-4, Claude 3 Opus, or Llama 3.1 70B for hypothesis generation
2. **Logic Layer**: Z3 SMT solver + Neo4j knowledge graph for symbolic validation
3. **Blockchain Layer**: Multi-layer blockchain (Hyperledger Fabric + Tendermint + PoW) for decentralized knowledge storage

```
┌─────────────────────────────────────────────────────┐
│                    Task Input                        │
└───────────────────┬─────────────────────────────────┘
                    │
         ┌──────────▼──────────┐
         │   LLM Generator     │  GPT-4, Claude, Llama
         │   (Hypotheses)      │  → 3-5 candidates
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │   Logic Engine      │  Z3 + Neo4j
         │   (Validation)      │  → Confidence p ≥ θ?
         └──────────┬──────────┘
                    │
              ┌─────┴─────┐
              │           │
          p ≥ θ?      p < θ?
              │           │
    ┌─────────▼─┐    ┌────▼──────────┐
    │ Validated │    │ Gap Resolution │
    └─────┬─────┘    │ (Knowledge     │
          │          │  Retrieval)    │
          │          └────┬───────────┘
          │               │
          │          ┌────▼───────┐
          │          │ Re-validate│
          │          └────┬───────┘
          │               │
    ┌─────▼───────────────▼─┐
    │   Blockchain Storage   │  L1/L2/L3
    │   (Knowledge Base)     │  
    └────────────────────────┘
```

---

## 📦 Installation

### System Requirements

**Minimum**:
- Python 3.10+
- 16 GB RAM
- 10 GB disk space

**For full experiments** (optional):
- 4× NVIDIA GPUs (for Llama 3.1)
- 128 GB RAM
- Neo4j database
- Blockchain nodes

### Setup

1. **Clone repository**:
```bash
git clone https://github.com/nechesov/agi-metaverse-tbca.git
cd agi-metaverse-tbca
```

2. **Create virtual environment**:
```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure API keys** (for LLM experiments):

Create `configs/api_keys.env`:
```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
# Llama 3.1: No API key needed (self-hosted)
```

**Note**: For demo, API keys are optional (uses mock LLM).

---

## 🧪 Running Experiments

### Quick Demo (No API Keys Required)

```bash
python demo/simple_demo.py
```

Uses mock LLM and pre-built knowledge base.

### Single Domain Experiment

```bash
# Legal reasoning (requires OpenAI API key)
python experiments/legal_reasoning.py --tasks 10 --model gpt-4

# Math reasoning
python experiments/math_reasoning.py --tasks 10 --model gpt-4
```

### Full Paper Reproduction

```bash
# Run all 800 tasks (takes ~72 hours)
./scripts/run_all_experiments.sh

# Results saved to: results/full_results.csv
```

**Note**: Full reproduction requires API keys and significant compute time (~72h + $800 in API costs).

---

## 📁 Repository Structure

```
agi-metaverse-tbca/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
│
├── demo/                     # Quick demos
│   ├── simple_demo.py       # 5-minute demo (no API keys)
│   └── interactive_demo.py  # Interactive CLI
│
├── src/                      # Source code
│   ├── llm/                 # LLM clients
│   ├── logic/               # Logic engine (Z3 + Neo4j)
│   ├── blockchain/          # Blockchain integration
│   └── cognitive_loop/      # Main cognitive loop
│
├── experiments/              # Experiment scripts
│   ├── legal_reasoning.py
│   ├── math_reasoning.py
│   ├── qa_reasoning.py
│   └── economic_reasoning.py
│
├── datasets/                 # Evaluation datasets
│   ├── legal/               # 200 legal tasks
│   ├── math/                # 200 math tasks
│   ├── qa/                  # 200 QA tasks
│   └── economic/            # 200 economic tasks
│
├── configs/                  # Configuration files
│   ├── api_keys.env         # API keys (not in git)
│   └── hyperparameters.yaml # Model hyperparameters
│
├── scripts/                  # Utility scripts
│   ├── run_all_experiments.sh
│   └── setup_dependencies.sh
│
├── docs/                     # Documentation
│   ├── INSTALLATION.md      # Detailed setup guide
│   ├── ARCHITECTURE.md      # System architecture
│   └── EXPERIMENTS.md       # Experiment instructions
│
└── results/                  # Experiment results (gitignored)
```

---

## 📚 Datasets

All 800 evaluation tasks are included in this repository under `datasets/`:

- **Legal**: 200 tasks (ContractNLI + custom disputes)
- **Math**: 200 tasks (GSM8K word problems)  
- **QA**: 200 tasks (Natural Questions)
- **Economic**: 200 tasks (custom financial scenarios)

Each dataset includes:
- Task text
- Ground truth answer
- Domain metadata
- Difficulty level

**Format**: JSON files, one task per line.

**Example** (`datasets/math/tasks.jsonl`):
```json
{"id": "math_142", "task": "Sarah buys 5 notebooks at $3 each...", "answer": "5", "difficulty": "medium"}
```

---

## 🔬 Key Features

### 1. Formal Theorem & Proof (Section III.3)

**Theorem 1 (Confidence Monotonicity)**: Knowledge enrichment monotonically increases hypothesis confidence.

Formally proved with complexity analysis: O((n+k)² log(n+k))

### 2. Gap Resolution Protocol (Section IV.3)

Automatically identifies and resolves knowledge gaps:
- Missing premises: 45% of gaps
- Low-confidence rules: 30%
- Ambiguous terms: 18%
- Complex chains: 7%

Convergence: 96% success rate after 5 iterations.

### 3. Multi-Layer Blockchain (Section IV.4)

Addresses blockchain trilemma:
- **L1 (Fast)**: 2500 TPS, 298ms latency
- **L2 (Logic)**: 1200 TPS, 612ms latency  
- **L3 (Master)**: 15 TPS, 4min blocks

Overall score: 72/100 (+60% vs single-layer)

---

## 📖 Citation

If you use this code or datasets, please cite our paper:

```bibtex
@article{nechesov2025agi,
  title={The AGI-Powered Metaverse: A Decentralized Task-Based Cognitive Architecture},
  author={Nechesov, Andrey},
  journal={IEEE Access},
  year={2025},
  note={Under review}
}
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📧 Contact

**Andrey Nechesov**
- Email: nechesov@gmail.com
- Institution: Novosibirsk State University
- GitHub: [@nechesov](https://github.com/nechesov)

---

## 🙏 Acknowledgments

This work was supported by a grant for research centers, provided by the Ministry of Economic Development of the Russian Federation in accordance with the subsidy agreement with the Novosibirsk
State University dated April 17, 2025 No. 139-15-2025-006: IGK 000000C313925P3S0002..

Special thanks to reviewers for valuable feedback that significantly improved this work.

---

## 📊 Project Status

- [x] Paper submitted to IEEE Access
- [x] Code repository public
- [x] Datasets included
- [x] Demo available
- [ ] Paper accepted (under review)
- [ ] Extended experiments (future work)

---

## 🔗 Links

- **Paper**: [IEEE Xplore](https://ieeexplore.ieee.org/) (upon acceptance)
- **Datasets**: Included in this repository
- **Documentation**: See [`docs/`](docs/) folder
- **Issues**: [GitHub Issues](https://github.com/nechesov/agi-metaverse-tbca/issues)

---

**Last Updated**: January 2026
