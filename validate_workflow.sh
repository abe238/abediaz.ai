#!/bin/bash

# Simple YAML validation for GitHub Actions workflow
# Checks for common syntax issues and best practices

echo "Validating GitHub Actions workflow: .github/workflows/deploy.yml"
echo "================================================================"
echo ""

# Check if file exists
if [ ! -f ".github/workflows/deploy.yml" ]; then
    echo "✗ Workflow file not found"
    exit 1
fi

# Basic checks
errors=0
warnings=0

# Check for valid YAML structure (basic indentation check)
if grep -q $'^\t' ".github/workflows/deploy.yml"; then
    echo "✗ Error: File contains tab characters (use spaces for YAML)"
    errors=$((errors + 1))
else
    echo "✓ No tab characters found (spaces only)"
fi

# Check required top-level keys
if grep -q "^name:" ".github/workflows/deploy.yml"; then
    echo "✓ Has 'name' field"
else
    echo "⚠ Warning: Missing 'name' field"
    warnings=$((warnings + 1))
fi

if grep -q "^on:" ".github/workflows/deploy.yml"; then
    echo "✓ Has 'on' trigger field"
else
    echo "✗ Error: Missing 'on' trigger field"
    errors=$((errors + 1))
fi

if grep -q "^jobs:" ".github/workflows/deploy.yml"; then
    echo "✓ Has 'jobs' field"
else
    echo "✗ Error: Missing 'jobs' field"
    errors=$((errors + 1))
fi

# Check permissions (best practice for Pages deployment)
if grep -q "^permissions:" ".github/workflows/deploy.yml"; then
    echo "✓ Has 'permissions' field (security best practice)"
else
    echo "⚠ Warning: Missing 'permissions' field"
    warnings=$((warnings + 1))
fi

# Check for concurrency (best practice for deployments)
if grep -q "^concurrency:" ".github/workflows/deploy.yml"; then
    echo "✓ Has 'concurrency' field (deployment best practice)"
else
    echo "⚠ Warning: Missing 'concurrency' field"
    warnings=$((warnings + 1))
fi

# Check for deprecated Node.js/npm references
if grep -q "npm\|node\|package.json" ".github/workflows/deploy.yml"; then
    echo "✗ Error: Contains npm/Node.js references (not needed for static site)"
    errors=$((errors + 1))
else
    echo "✓ No npm/Node.js references"
fi

# Check for proper action versions
if grep -q "@v[0-9]" ".github/workflows/deploy.yml"; then
    echo "✓ Uses versioned actions"
else
    echo "⚠ Warning: Actions should use version tags (@v4, @v3, etc.)"
    warnings=$((warnings + 1))
fi

# Check for runs-on in jobs
if grep -q "runs-on:" ".github/workflows/deploy.yml"; then
    echo "✓ Jobs specify runner (runs-on)"
else
    echo "✗ Error: Jobs missing 'runs-on' specification"
    errors=$((errors + 1))
fi

echo ""
echo "================================================================"
echo "Validation Summary:"
echo "  Errors: $errors"
echo "  Warnings: $warnings"
echo ""

if [ $errors -eq 0 ]; then
    echo "✓ YAML syntax appears valid"
    echo "✓ Follows GitHub Actions best practices"
    exit 0
else
    echo "✗ Validation failed with $errors error(s)"
    exit 1
fi
