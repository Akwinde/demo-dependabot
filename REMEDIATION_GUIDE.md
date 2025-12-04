# Secret Remediation Guide

## Immediate Action Items

### 1. Revoke Exposed Credentials (URGENT)

#### AWS Access Key
```bash
# Use AWS CLI to deactivate the key
aws iam update-access-key --access-key-id AKIA1234567890TEST --status Inactive --user-name <USERNAME>

# Then delete it
aws iam delete-access-key --access-key-id AKIA1234567890TEST --user-name <USERNAME>

# Generate a new access key pair
aws iam create-access-key --user-name <USERNAME>
```

#### GitHub Personal Access Token
1. Go to https://github.com/settings/tokens
2. Find the exposed token
3. Click "Delete" to revoke it
4. Generate a new token with minimal required scopes

### 2. Remove Secrets from Repository

The following files contain secrets and should be removed:
- `creds.txt` - Contains AWS Access Key ID
- `test.txt` - Contains GitHub Personal Access Token

**DO NOT** simply delete these files in a new commit, as they will remain in Git history.

#### Option A: Remove from current commit only (if not pushed to remote)
```bash
git rm creds.txt test.txt
git commit --amend -m "Remove credential files"
```

#### Option B: Remove from Git history (if already pushed)
```bash
# Using git filter-repo (recommended)
git filter-repo --path creds.txt --invert-paths
git filter-repo --path test.txt --invert-paths

# Force push to remote (WARNING: This rewrites history)
git push origin --force --all
```

#### Option C: Use BFG Repo-Cleaner
```bash
# Download BFG from https://rtyley.github.io/bfg-repo-cleaner/
java -jar bfg.jar --delete-files creds.txt
java -jar bfg.jar --delete-files test.txt
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push origin --force --all
```

### 3. Verify Removal
```bash
# Check that files are gone
git log --all --full-history -- creds.txt
git log --all --full-history -- test.txt

# Search for any remaining secrets
git grep "AKIA" $(git rev-list --all)
git grep "ghp_" $(git rev-list --all)
```

## Prevention Measures

### 1. Enable GitHub Secret Scanning
1. Go to repository Settings > Code security and analysis
2. Enable "Secret scanning"
3. Enable "Push protection" to prevent secrets from being pushed

### 2. Install Git Hooks
```bash
# Install git-secrets
brew install git-secrets  # macOS
# or download from: https://github.com/awslabs/git-secrets

# Set up git-secrets for the repository
cd /path/to/repo
git secrets --install
git secrets --register-aws
git secrets --add 'ghp_[0-9a-zA-Z]{36}'
```

### 3. Use Environment Variables
Instead of committing credentials:

```python
# main.py - Example
import os

# Get credentials from environment
aws_key = os.environ.get('AWS_ACCESS_KEY_ID')
github_token = os.environ.get('GITHUB_TOKEN')
```

```bash
# Set locally (not committed)
export AWS_ACCESS_KEY_ID="your-key-here"
export GITHUB_TOKEN="your-token-here"
```

### 4. Use Secrets Management
- **For local development:** Use `.env` files (add to .gitignore)
- **For CI/CD:** Use GitHub Secrets
- **For production:** Use AWS Secrets Manager, HashiCorp Vault, etc.

## Audit Steps

### Check AWS Activity
```bash
# Review CloudTrail logs
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=Username,AttributeValue=<USERNAME> \
  --start-time 2025-01-01 \
  --end-time 2025-12-04
```

### Check GitHub Activity
1. Go to https://github.com/settings/security-log
2. Review recent activity for suspicious actions
3. Check repository audit log (Settings > Logs)

## Best Practices Going Forward

1. **Never commit secrets** - Always use environment variables or secret managers
2. **Use .gitignore** - Prevent credential files from being tracked
3. **Enable security features** - Use GitHub's secret scanning and push protection
4. **Regular audits** - Periodically scan for exposed secrets
5. **Least privilege** - Grant minimal necessary permissions to credentials
6. **Rotate regularly** - Change credentials on a regular schedule
7. **Monitor usage** - Set up alerts for unusual credential usage

## Resources

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [git-secrets](https://github.com/awslabs/git-secrets)
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
- [AWS Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
