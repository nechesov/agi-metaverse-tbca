# Installation Guide

Step-by-step instructions for setting up the AGI-Powered Metaverse system.

## Quick Start (5 minutes)

For a quick demo without full installation:

```bash
# 1. Clone
git clone https://github.com/nechesov/agi-metaverse-tbca.git
cd agi-metaverse-tbca

# 2. Install minimal dependencies
pip install numpy z3-solver click colorama

# 3. Run demo (no API keys needed)
python demo/simple_demo.py
```

---

## Full Installation

### System Requirements

**Minimum** (for demo and basic experiments):
- Operating System: Linux, macOS, or Windows
- Python: 3.10 or higher
- RAM: 8 GB
- Disk Space: 5 GB

**Recommended** (for full paper reproduction):
- Operating System: Ubuntu 22.04 LTS
- Python: 3.10.12
- RAM: 32 GB
- Disk Space: 100 GB
- GPU: NVIDIA GPU with 24GB VRAM (optional, for Llama 3.1)

### Step 1: Clone Repository

```bash
git clone https://github.com/nechesov/agi-metaverse-tbca.git
cd agi-metaverse-tbca
```

### Step 2: Create Virtual Environment

#### Linux / macOS

```bash
# Create virtual environment
python3.10 -m venv venv

# Activate
source venv/bin/activate
```

#### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

This installs:
- Core libraries (NumPy, Pandas, SciPy)
- Logic engine (Z3 solver)
- LLM clients (OpenAI, Anthropic) - optional
- Utilities (Click, TQDM, etc.)

### Step 4: Configure API Keys (Optional)

For experiments with real LLMs, you need API keys.

#### Create configuration file

```bash
# Create configs directory
mkdir -p configs

# Create API keys file
cat > configs/api_keys.env << EOF
# OpenAI (for GPT-4)
OPENAI_API_KEY=sk-your-key-here

# Anthropic (for Claude 3)
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Llama 3.1 (self-hosted, no key needed)
# LLAMA_ENDPOINT=http://localhost:8000
EOF
```

#### Get API keys

- **OpenAI GPT-4**: https://platform.openai.com/api-keys
- **Anthropic Claude**: https://console.anthropic.com/

**Important**: Never commit `api_keys.env` to git! It's already in `.gitignore`.

### Step 5: Verify Installation

```bash
# Test Python packages
python -c "import z3, numpy, click; print('✓ Dependencies OK')"

# Run demo (no API keys needed)
python demo/simple_demo.py
```

Expected output:
```
╔══════════════════════════════════════════════════════════════════════╗
║  AGI-Powered Metaverse: Task-Based Cognitive Architecture           ║
║  Simple Demo (No API Keys Required)                                 ║
╚══════════════════════════════════════════════════════════════════════╝
...
RESULT: ✓ VALIDATED
Answer: 5 pens
Final Confidence: 0.931
```

---

## Optional Components

### Neo4j Database (for full experiments)

The full system uses Neo4j for the knowledge graph.

#### Using Docker

```bash
# Pull Neo4j image
docker pull neo4j:5.11-community

# Run Neo4j
docker run -d \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:5.11-community

# Wait for startup
sleep 30

# Verify
curl http://localhost:7474
```

#### Manual Installation

See: https://neo4j.com/docs/operations-manual/current/installation/

### Llama 3.1 (self-hosted)

For experiments without API costs, you can self-host Llama 3.1.

#### Requirements
- NVIDIA GPU with 24GB+ VRAM
- CUDA 12.1+

#### Setup

```bash
# Install vLLM
pip install vllm==0.5.1

# Download model (requires HuggingFace account)
# This is ~70GB download
huggingface-cli download meta-llama/Meta-Llama-3.1-70B-Instruct

# Run vLLM server
vllm serve meta-llama/Meta-Llama-3.1-70B-Instruct \
  --port 8000 \
  --tensor-parallel-size 4

# Test
curl http://localhost:8000/v1/models
```

---

## Troubleshooting

### Issue: `ImportError: No module named 'z3'`

**Solution**: Install Z3 solver
```bash
pip install z3-solver==4.12.2.0
```

### Issue: API key not found

**Solution**: Make sure `configs/api_keys.env` exists and contains valid keys.

```bash
# Check file exists
ls -la configs/api_keys.env

# Load in shell (for testing)
export OPENAI_API_KEY=sk-...
```

### Issue: Out of memory

**Solution**: Reduce batch size or use smaller model

For Llama 3.1, use quantized version:
```bash
pip install auto-gptq
# Use 4-bit quantized model instead
```

### Issue: Permission denied on Linux

**Solution**: Make scripts executable
```bash
chmod +x scripts/*.sh
chmod +x demo/*.py
```

### Issue: Windows path errors

**Solution**: Use forward slashes or raw strings
```python
# Instead of: "configs\api_keys.env"
# Use: "configs/api_keys.env"
```

---

## Verifying Your Installation

Run these checks to ensure everything is working:

### 1. Python version
```bash
python --version
# Should show: Python 3.10.x or higher
```

### 2. Dependencies
```bash
pip list | grep -E "z3-solver|numpy|openai"
# Should show installed versions
```

### 3. Demo script
```bash
python demo/simple_demo.py
# Should run without errors and show validated result
```

### 4. Sample experiment (optional, requires API key)
```bash
# Set API key
export OPENAI_API_KEY=sk-...

# Run small test
python experiments/math_reasoning.py --tasks 5 --model gpt-4
# Should complete successfully
```

---

## Next Steps

After successful installation:

1. ✅ Run demo: `python demo/simple_demo.py`
2. ✅ Read architecture: `docs/ARCHITECTURE.md`
3. ✅ Try experiments: `experiments/README.md`
4. ✅ Explore datasets: `datasets/README.md`

---

## Getting Help

If you encounter issues:

1. Check [GitHub Issues](https://github.com/nechesov/agi-metaverse-tbca/issues)
2. Read `docs/TROUBLESHOOTING.md` (if available)
3. Contact: nechesov@gmail.com

---

**Installation Complete!** 🎉

You're ready to reproduce the paper results or extend the system.
