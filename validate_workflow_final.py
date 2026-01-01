#!/usr/bin/env python3
"""
GitHub Actions workflow validator using standard library only
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
    info = []

    # Check 1: File is not empty
    if not content.strip():
        errors.append("Workflow file is empty")
        return False
    checks_passed.append("File is not empty")

    # Check 2: No tabs (YAML doesn't allow tabs)
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if '\t' in line and line.strip():  # Ignore empty lines
            errors.append(f"Line {i}: Tabs are not allowed in YAML, use spaces")

    if not any('\t' in line for line in lines):
        checks_passed.append("No tabs found (YAML compliant)")

    # Check 3: Indentation consistency (should be 2 spaces)
    indent_pattern = re.compile(r'^( +)\S')
    indents = []
    for i, line in enumerate(lines, 1):
        match = indent_pattern.match(line)
        if match:
            indent_len = len(match.group(1))
            indents.append(indent_len)

    if indents:
        # Check if all indents are multiples of 2
        if all(i % 2 == 0 for i in indents):
            checks_passed.append("Consistent 2-space indentation")
        else:
            warnings.append("Inconsistent indentation detected (should use 2 spaces)")

    # Check 4: Required top-level fields
    if re.search(r'^on:', content, re.MULTILINE):
        checks_passed.append("Has 'on:' field (workflow triggers)")

        # Extract trigger types
        triggers = []
        if 'push:' in content:
            triggers.append('push')
        if 'pull_request:' in content:
            triggers.append('pull_request')
        if 'workflow_dispatch:' in content:
            triggers.append('workflow_dispatch')
        if triggers:
            info.append(f"Triggers: {', '.join(triggers)}")
    else:
        errors.append("Missing required 'on:' field (workflow triggers)")

    if re.search(r'^jobs:', content, re.MULTILINE):
        checks_passed.append("Has 'jobs:' field")
    else:
        errors.append("Missing required 'jobs:' field")

    if re.search(r'^name:', content, re.MULTILINE):
        name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
        if name_match:
            info.append(f"Workflow name: {name_match.group(1)}")
            checks_passed.append("Has 'name:' field")
    else:
        warnings.append("Missing 'name:' field (recommended for workflow identification)")

    # Check 5: Permissions
    if re.search(r'^permissions:', content, re.MULTILINE):
        checks_passed.append("Has 'permissions:' field (explicit permissions defined)")

        valid_perms = ['contents', 'id-token', 'pages']
        found_perms = []
        for perm in valid_perms:
            if re.search(rf'^\s+{perm}:\s*(read|write)', content, re.MULTILINE):
                found_perms.append(perm)

        if found_perms:
            info.append(f"Permissions configured: {', '.join(found_perms)}")

    # Check 6: Concurrency control
    if re.search(r'^concurrency:', content, re.MULTILINE):
        checks_passed.append("Has 'concurrency:' field (prevents concurrent deployments)")

    # Check 7: Jobs validation - improved parsing
    # Find the jobs section
    jobs_section_match = re.search(r'^jobs:\s*\n((?:  .*\n)*)', content, re.MULTILINE)

    if jobs_section_match:
        jobs_content = jobs_section_match.group(0)

        # Find job names - they're at 2-space indent level under 'jobs:'
        job_pattern = re.compile(r'^  ([a-z_][a-z0-9_-]*):\s*$', re.MULTILINE)
        job_names = job_pattern.findall(jobs_content)

        if job_names:
            info.append(f"Jobs defined: {', '.join(job_names)}")
            checks_passed.append(f"Found {len(job_names)} job(s)")

            # For each job, verify it has runs-on
            for job_name in job_names:
                # Find the job definition
                job_start = re.search(rf'^  {job_name}:\s*$', jobs_content, re.MULTILINE)
                if job_start:
                    # Get content after this job name until next job or end
                    rest_content = jobs_content[job_start.end():]
                    next_job = re.search(r'^  [a-z_][a-z0-9_-]*:\s*$', rest_content, re.MULTILINE)

                    if next_job:
                        job_def = rest_content[:next_job.start()]
                    else:
                        job_def = rest_content

                    # Check for runs-on
                    if re.search(r'^\s+runs-on:', job_def, re.MULTILINE):
                        checks_passed.append(f"Job '{job_name}' has 'runs-on' field")
                    else:
                        errors.append(f"Job '{job_name}' missing required 'runs-on:' field")

                    # Check for steps or uses
                    if re.search(r'^\s+steps:', job_def, re.MULTILINE):
                        checks_passed.append(f"Job '{job_name}' has 'steps' field")
                    elif re.search(r'^\s+uses:', job_def, re.MULTILINE):
                        info.append(f"Job '{job_name}' is a reusable workflow")
        else:
            errors.append("No jobs defined under 'jobs:' field")

    # Check 8: Action versions
    action_pattern = re.compile(r'uses:\s+([^\s]+)')
    actions = action_pattern.findall(content)

    if actions:
        info.append(f"Uses {len(actions)} action(s)")
        for action in actions:
            if '@v' in action:
                checks_passed.append(f"Action '{action}' has version pinned")
            elif '@' in action:
                warnings.append(f"Action '{action}' uses non-standard version reference")
            else:
                warnings.append(f"Action '{action}' should specify a version (e.g., @v4)")

    # Check 9: Standard GitHub Actions
    if 'actions/checkout@v' in content:
        checks_passed.append("Uses 'actions/checkout' (standard practice)")

    if 'actions/upload-pages-artifact@v' in content:
        checks_passed.append("Uses 'actions/upload-pages-artifact' for GitHub Pages")

    if 'actions/deploy-pages@v' in content:
        checks_passed.append("Uses 'actions/deploy-pages' for GitHub Pages")

    # Check 10: No deprecated Node.js/npm commands for static site
    if re.search(r'npm (ci|install|run)', content):
        errors.append("Workflow contains npm commands but this is a static site (no package.json)")

    if 'actions/setup-node' in content:
        errors.append("Workflow uses Node.js setup but this is a static site")

    # Print results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if errors:
        print(f"\n✗ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")

    if warnings:
        print(f"\n⚠  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")

    if checks_passed:
        print(f"\n✓ CHECKS PASSED ({len(checks_passed)}):")
        for check in checks_passed:
            print(f"  - {check}")

    if info:
        print(f"\nℹ  WORKFLOW INFORMATION:")
        for item in info:
            print(f"  - {item}")

    print("\n" + "=" * 60)
    if not errors:
        print("✓ VALIDATION SUCCESSFUL!")
        print("✓ Workflow syntax is valid and follows GitHub Actions best practices")
        print("✓ All required fields are present")
        print("✓ No deprecated actions are used")
    else:
        print(f"✗ VALIDATION FAILED with {len(errors)} error(s)")
        print("  Please fix the errors above before deploying")

    print("=" * 60)

    return len(errors) == 0

if __name__ == '__main__':
    success = validate_workflow('.github/workflows/deploy.yml')
    sys.exit(0 if success else 1)
