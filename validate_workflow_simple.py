#!/usr/bin/env python3
"""
Simple GitHub Actions workflow validator using only standard library
"""
import re
import sys

def validate_workflow(file_path):
    """Validate GitHub Actions workflow file"""

    print(f"Validating GitHub Actions workflow: {file_path}")
    print("=" * 60)

    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"✗ File not found: {file_path}")
        return False

    errors = []
    warnings = []
    checks_passed = []

    # Check 1: File is not empty
    if not content.strip():
        errors.append("Workflow file is empty")
        return False

    checks_passed.append("File is not empty")

    # Check 2: Basic YAML syntax - no tabs (YAML doesn't allow tabs)
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if '\t' in line:
            errors.append(f"Line {i}: Tabs are not allowed in YAML, use spaces")

    if not any('\t' in line for line in lines):
        checks_passed.append("No tabs found (YAML uses spaces)")

    # Check 3: Required fields present
    if not re.search(r'^on:', content, re.MULTILINE):
        errors.append("Missing required 'on:' field (workflow triggers)")
    else:
        checks_passed.append("Has 'on:' field (workflow triggers)")

    if not re.search(r'^jobs:', content, re.MULTILINE):
        errors.append("Missing required 'jobs:' field")
    else:
        checks_passed.append("Has 'jobs:' field")

    if not re.search(r'^name:', content, re.MULTILINE):
        warnings.append("Missing 'name:' field (recommended)")
    else:
        checks_passed.append("Has 'name:' field")

    # Check 4: Permissions syntax
    if re.search(r'^permissions:', content, re.MULTILINE):
        checks_passed.append("Has 'permissions:' field")

        # Check for valid permission keys
        valid_perms = ['actions', 'checks', 'contents', 'deployments',
                      'id-token', 'issues', 'discussions', 'packages',
                      'pages', 'pull-requests', 'repository-projects',
                      'security-events', 'statuses']

        perm_section = re.search(r'permissions:(.*?)(?=\n\S|\Z)', content, re.DOTALL)
        if perm_section:
            for perm in valid_perms:
                if re.search(rf'^\s+{perm}:\s*(read|write)', perm_section.group(1), re.MULTILINE):
                    checks_passed.append(f"Permission '{perm}' configured correctly")

    # Check 5: Jobs structure
    jobs_match = re.search(r'jobs:(.*?)(?=\n\S|\Z)', content, re.DOTALL)
    if jobs_match:
        jobs_content = jobs_match.group(1)

        # Find all job names (indented keys under jobs)
        job_names = re.findall(r'^\s+(\w+):', jobs_content, re.MULTILINE)
        if job_names:
            checks_passed.append(f"Found {len(job_names)} job(s): {', '.join(job_names)}")

            # Check each job has runs-on
            for job_name in job_names:
                job_pattern = rf'{job_name}:(.*?)(?=^\s+\w+:|$)'
                job_match = re.search(job_pattern, jobs_content, re.MULTILINE | re.DOTALL)
                if job_match:
                    job_def = job_match.group(1)
                    if not re.search(r'runs-on:', job_def):
                        errors.append(f"Job '{job_name}' missing required 'runs-on:' field")
                    else:
                        checks_passed.append(f"Job '{job_name}' has 'runs-on'")

                    if re.search(r'steps:', job_def):
                        checks_passed.append(f"Job '{job_name}' has 'steps'")
        else:
            errors.append("No jobs defined under 'jobs:' field")

    # Check 6: Action versions
    action_uses = re.findall(r'uses:\s+([^\s]+)', content)
    if action_uses:
        checks_passed.append(f"Found {len(action_uses)} action(s)")
        for action in action_uses:
            if '@' in action:
                checks_passed.append(f"Action '{action}' has version specified")
            else:
                warnings.append(f"Action '{action}' should specify a version (e.g., @v4)")

    # Check 7: Common GitHub Actions patterns
    if re.search(r'actions/checkout@v', content):
        checks_passed.append("Uses actions/checkout (standard practice)")

    if re.search(r'actions/upload-pages-artifact@v', content):
        checks_passed.append("Uses actions/upload-pages-artifact")

    if re.search(r'actions/deploy-pages@v', content):
        checks_passed.append("Uses actions/deploy-pages")

    # Check 8: No deprecated actions (common ones)
    deprecated_actions = {
        'actions/checkout@v1': 'Use @v4 instead',
        'actions/checkout@v2': 'Use @v4 instead',
        'actions/setup-node@v1': 'Use @v4 instead',
    }

    for deprecated, suggestion in deprecated_actions.items():
        if deprecated in content:
            warnings.append(f"Using deprecated action '{deprecated}' - {suggestion}")

    # Print results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if errors:
        print(f"\n✗ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")

    if warnings:
        print(f"\n⚠ WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")

    if checks_passed:
        print(f"\n✓ CHECKS PASSED ({len(checks_passed)}):")
        for check in checks_passed:
            print(f"  - {check}")

    print("\n" + "=" * 60)
    if not errors:
        print("✓ VALIDATION SUCCESSFUL!")
        print("✓ Workflow syntax is valid and follows GitHub Actions conventions")
    else:
        print(f"✗ VALIDATION FAILED with {len(errors)} error(s)")
    print("=" * 60)

    return len(errors) == 0

if __name__ == '__main__':
    success = validate_workflow('.github/workflows/deploy.yml')
    sys.exit(0 if success else 1)
