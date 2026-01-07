# Git Upload Instructions

## Quick Commands to Upload Everything to GitHub

```bash
# 1. Navigate to your repository
cd /path/to/agi-metaverse-tbca

# 2. Initialize git (if not already done)
git init

# 3. Add remote (if not already done)
git remote add origin https://github.com/nechesov/agi-metaverse-tbca.git

# 4. Create directory structure
mkdir -p demo
mkdir -p datasets/math datasets/legal datasets/qa datasets/economic
mkdir -p docs
mkdir -p src/llm src/logic src/blockchain src/cognitive_loop
mkdir -p experiments
mkdir -p configs
mkdir -p scripts
mkdir -p results

# 5. Copy all files from this package to your repository
# (Copy the files from github_files/ directory to corresponding locations)

# Main files (root):
cp github_files/README.md .
cp github_files/LICENSE .
cp github_files/CITATION.cff .
cp github_files/requirements.txt .
cp github_files/.gitignore .

# Demo:
cp github_files/demo/simple_demo.py demo/

# Datasets:
cp github_files/datasets/README.md datasets/
cp github_files/datasets/math/sample_tasks.jsonl datasets/math/

# Documentation:
cp github_files/docs/INSTALLATION.md docs/

# 6. Create placeholder files for structure
touch src/__init__.py
touch src/llm/__init__.py
touch src/logic/__init__.py
touch src/blockchain/__init__.py
touch src/cognitive_loop/__init__.py

# 7. Create a simple README for empty directories
echo "# Source Code" > src/README.md
echo "# Experiments" > experiments/README.md
echo "# Scripts" > scripts/README.md

# 8. Stage all files
git add .

# 9. Commit
git commit -m "Initial commit: Minimal working version for IEEE Access paper

- Added README with project overview and quick start
- Added MIT LICENSE
- Added requirements.txt with all dependencies
- Added CITATION.cff for proper citation
- Added simple demo (works without API keys)
- Added sample datasets (5 tasks per domain)
- Added installation guide
- Created directory structure for full implementation
"

# 10. Push to GitHub
git push -u origin main

# If branch is 'master' instead of 'main':
# git push -u origin master
```

## What Gets Uploaded

### Root Files (7 files)
- ✅ README.md (main project documentation)
- ✅ LICENSE (MIT license)
- ✅ CITATION.cff (citation metadata)
- ✅ requirements.txt (Python dependencies)
- ✅ .gitignore (ignore rules)

### Demo (1 file)
- ✅ demo/simple_demo.py (working demo without API keys)

### Datasets (2 files)
- ✅ datasets/README.md (dataset documentation)
- ✅ datasets/math/sample_tasks.jsonl (5 sample math tasks)

### Documentation (1 file)
- ✅ docs/INSTALLATION.md (installation guide)

### Directory Structure (8 directories)
- ✅ src/ (source code - empty for now)
- ✅ experiments/ (experiment scripts - empty for now)
- ✅ configs/ (configuration files - empty for now)
- ✅ scripts/ (utility scripts - empty for now)
- ✅ results/ (gitignored, for local results)

**Total**: ~12 files + directory structure

## After Upload

### Verify on GitHub

1. Go to: https://github.com/nechesov/agi-metaverse-tbca
2. Check that files are visible
3. Check that README displays correctly
4. Test clone and demo:
   ```bash
   # Fresh clone
   git clone https://github.com/nechesov/agi-metaverse-tbca.git test-clone
   cd test-clone
   
   # Install and run
   pip install -r requirements.txt
   python demo/simple_demo.py
   ```

### Next Steps

1. **Add to paper**: Update Appendix A with repository URL
2. **Optional**: Add more sample datasets
3. **Optional**: Add experiment scripts
4. **Optional**: Add source code implementation

## File Size Check

Before uploading, check file sizes:

```bash
# Check all files
find . -type f -size +100M

# GitHub has 100MB file size limit
# If any file is >100MB, add to .gitignore or use Git LFS
```

## Git LFS (if needed for large files)

If you have files >100MB (e.g., model checkpoints):

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.pth"
git lfs track "*.ckpt"

# Add .gitattributes
git add .gitattributes

# Commit and push
git commit -m "Add Git LFS for large files"
git push
```

## Troubleshooting

### Issue: "fatal: remote origin already exists"

```bash
# Remove existing remote
git remote remove origin

# Add again
git remote add origin https://github.com/nechesov/agi-metaverse-tbca.git
```

### Issue: "error: failed to push some refs"

```bash
# Pull first (if remote has changes)
git pull origin main --allow-unrelated-histories

# Then push
git push origin main
```

### Issue: File too large

```bash
# Add to .gitignore
echo "large_file.bin" >> .gitignore

# Remove from git
git rm --cached large_file.bin

# Commit
git commit -m "Remove large file"
```

## Summary

**Minimal upload** (what we're doing):
- 12 essential files
- Working demo
- Sample datasets
- Documentation
- Directory structure

**Time**: 5-10 minutes
**Size**: <1 MB
**Status**: ✅ Ready for paper submission

This gives reviewers/readers enough to:
1. Understand the project
2. Run a demo
3. See sample data
4. Know how to install

Full implementation can be added later!
