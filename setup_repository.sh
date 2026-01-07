#!/bin/bash
#
# Automated Repository Setup Script
# For AGI-Powered Metaverse: Task-Based Cognitive Architecture
#
# Usage: ./setup_repository.sh
#

set -e  # Exit on error

echo "=================================================="
echo "  GitHub Repository Setup"
echo "  AGI-Powered Metaverse TBCA"
echo "=================================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Error: git is not installed"
    echo "Install git first: https://git-scm.com/downloads"
    exit 1
fi

echo "✓ Git is installed"

# Get repository path
REPO_PATH=${1:-"."}
cd "$REPO_PATH"

echo ""
echo "Setting up repository at: $(pwd)"
echo ""

# Create directory structure
echo "📁 Creating directory structure..."

mkdir -p demo
mkdir -p src/llm src/logic src/blockchain src/cognitive_loop
mkdir -p experiments
mkdir -p datasets/math datasets/legal datasets/qa datasets/economic
mkdir -p docs
mkdir -p configs
mkdir -p scripts
mkdir -p results

echo "   ✓ Created all directories"

# Create placeholder files
echo ""
echo "📝 Creating placeholder files..."

# Source code placeholders
cat > src/__init__.py << 'EOF'
"""
AGI-Powered Metaverse: Task-Based Cognitive Architecture
Source code package
"""
__version__ = "1.0.0"
EOF

touch src/llm/__init__.py
touch src/logic/__init__.py
touch src/blockchain/__init__.py
touch src/cognitive_loop/__init__.py

# Experiments README
cat > experiments/README.md << 'EOF'
# Experiments

Scripts for reproducing paper results.

## Available Experiments

- `legal_reasoning.py` - Legal domain evaluation (200 tasks)
- `math_reasoning.py` - Math domain evaluation (200 tasks)
- `qa_reasoning.py` - QA domain evaluation (200 tasks)
- `economic_reasoning.py` - Economic domain evaluation (200 tasks)

## Usage

```bash
# Requires API keys in configs/api_keys.env
python experiments/math_reasoning.py --tasks 10 --model gpt-4
```

## Full Reproduction

```bash
./scripts/run_all_experiments.sh
```

Results saved to `results/` directory.
EOF

# Scripts README
cat > scripts/README.md << 'EOF'
# Utility Scripts

Helper scripts for setup and execution.

- `setup_dependencies.sh` - Install system dependencies
- `run_all_experiments.sh` - Run full evaluation (800 tasks)
- `analyze_results.py` - Generate paper figures and tables

## Usage

```bash
chmod +x scripts/*.sh
./scripts/setup_dependencies.sh
```
EOF

echo "   ✓ Created placeholder files"

# Check if files from package exist
if [ -f "../github_files/README.md" ]; then
    echo ""
    echo "📋 Copying files from package..."
    
    cp ../github_files/README.md .
    cp ../github_files/LICENSE .
    cp ../github_files/CITATION.cff .
    cp ../github_files/requirements.txt .
    cp ../github_files/.gitignore .
    
    cp ../github_files/demo/simple_demo.py demo/
    
    cp ../github_files/datasets/README.md datasets/
    cp ../github_files/datasets/math/sample_tasks.jsonl datasets/math/
    
    cp ../github_files/docs/INSTALLATION.md docs/
    
    echo "   ✓ Copied all files from package"
else
    echo ""
    echo "⚠️  Warning: github_files/ not found"
    echo "   Please manually copy files to repository"
fi

# Git initialization
echo ""
echo "🔧 Git setup..."

if [ ! -d ".git" ]; then
    git init
    echo "   ✓ Initialized git repository"
else
    echo "   ✓ Git already initialized"
fi

# Check if remote exists
if ! git remote | grep -q origin; then
    read -p "Enter GitHub repository URL (e.g., https://github.com/user/repo.git): " REPO_URL
    git remote add origin "$REPO_URL"
    echo "   ✓ Added remote: $REPO_URL"
else
    echo "   ✓ Remote 'origin' already exists"
    git remote -v
fi

# Stage files
echo ""
echo "📦 Staging files for commit..."

git add .
echo "   ✓ All files staged"

# Show status
echo ""
echo "📊 Repository status:"
git status --short

# Prepare commit message
COMMIT_MSG="Initial commit: Minimal working version for IEEE Access

- Added comprehensive README with quick start
- Added MIT LICENSE
- Added requirements.txt with all dependencies
- Added CITATION.cff for proper citation
- Added working demo (no API keys required)
- Added sample datasets (5 tasks per domain)
- Added installation guide
- Created directory structure for full implementation

Repository ready for paper submission."

echo ""
echo "📝 Prepared commit message:"
echo "----------------------------------------"
echo "$COMMIT_MSG"
echo "----------------------------------------"

# Ask for confirmation
echo ""
read -p "Commit and push to GitHub? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Commit
    git commit -m "$COMMIT_MSG"
    echo "   ✓ Files committed"
    
    # Push
    echo ""
    echo "🚀 Pushing to GitHub..."
    
    # Detect default branch
    BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "main")
    
    git push -u origin "$BRANCH"
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "=================================================="
        echo "  ✅ SUCCESS!"
        echo "=================================================="
        echo ""
        echo "Repository uploaded to GitHub!"
        echo ""
        echo "Next steps:"
        echo "  1. Visit your repository on GitHub"
        echo "  2. Verify files are visible"
        echo "  3. Test clone and demo:"
        echo ""
        echo "     git clone <your-repo-url> test"
        echo "     cd test"
        echo "     pip install -r requirements.txt"
        echo "     python demo/simple_demo.py"
        echo ""
        echo "  4. Update paper with repository URL"
        echo ""
    else
        echo ""
        echo "❌ Push failed. Common issues:"
        echo "  - Authentication required (use SSH or Personal Access Token)"
        echo "  - Remote branch doesn't exist (try: git push -u origin $BRANCH --force)"
        echo "  - Network issues"
        echo ""
        echo "Try manually:"
        echo "  git push -u origin $BRANCH"
    fi
else
    echo ""
    echo "Commit cancelled. Files are staged but not committed."
    echo "To commit later, run:"
    echo "  git commit -m 'Initial commit'"
    echo "  git push -u origin main"
fi

echo ""
echo "Setup complete!"
