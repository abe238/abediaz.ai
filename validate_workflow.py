#!/usr/bin/env python3
"""
Validate GitHub Actions workflow syntax
"""
import yaml
import sys
import os

def validate_yaml_syntax(file_path):
    """Check if YAML file has valid syntax"""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        print(f"✓ YAML syntax is valid for {file_path}")
        return data
    except yaml.YAMLError as e:
        print(f"✗ YAML syntax error in {file_path}:")
        print(f"  {e}")
        return None

def validate_github_actions_schema(data, file_path):
    """Validate GitHub Actions workflow structure"""
    errors = []
    warnings = []

    # Check required top-level fields
    if 'name' not in data:
        warnings.append("Missing 'name' field (recommended)")

    if 'on' not in data:
        errors.append("Missing required 'on' field")

    if 'jobs' not in data:
        errors.append("Missing required 'jobs' field")
    elif not isinstance(data['jobs'], dict) or len(data['jobs']) == 0:
        errors.append("'jobs' must be a non-empty dictionary")

    # Validate permissions
    if 'permissions' in data:
        valid_permissions = ['actions', 'checks', 'contents', 'deployments',
                           'id-token', 'issues', 'discussions', 'packages',
                           'pages', 'pull-requests', 'repository-projects',
                           'security-events', 'statuses']
        for perm in data['permissions']:
            if perm not in valid_permissions:
                warnings.append(f"Unknown permission: {perm}")

    # Validate jobs
    if 'jobs' in data and isinstance(data['jobs'], dict):
        for job_name, job_data in data['jobs'].items():
            if not isinstance(job_data, dict):
                errors.append(f"Job '{job_name}' must be a dictionary")
                continue

            # Check required job fields
            if 'runs-on' not in job_data:
                errors.append(f"Job '{job_name}' missing required 'runs-on' field")

            # Validate steps
            if 'steps' in job_data:
                if not isinstance(job_data['steps'], list):
                    errors.append(f"Job '{job_name}': 'steps' must be a list")
                else:
                    for idx, step in enumerate(job_data['steps']):
                        if not isinstance(step, dict):
                            errors.append(f"Job '{job_name}', step {idx}: must be a dictionary")
                        elif 'uses' not in step and 'run' not in step:
                            errors.append(f"Job '{job_name}', step {idx}: must have either 'uses' or 'run'")

    return errors, warnings

def check_action_versions(data):
    """Check if actions use specific versions (not latest)"""
    recommendations = []

    if 'jobs' in data and isinstance(data['jobs'], dict):
        for job_name, job_data in data['jobs'].items():
            if 'steps' in job_data and isinstance(job_data['steps'], list):
                for idx, step in enumerate(job_data['steps']):
                    if isinstance(step, dict) and 'uses' in step:
                        action = step['uses']
                        if '@' not in action:
                            recommendations.append(
                                f"Job '{job_name}', step {idx}: Action '{action}' should specify a version"
                            )

    return recommendations

def main():
    workflow_file = '.github/workflows/deploy.yml'

    if not os.path.exists(workflow_file):
        print(f"✗ Workflow file not found: {workflow_file}")
        sys.exit(1)

    print(f"Validating GitHub Actions workflow: {workflow_file}")
    print("=" * 60)

    # Step 1: Validate YAML syntax
    data = validate_yaml_syntax(workflow_file)
    if data is None:
        sys.exit(1)

    # Step 2: Validate GitHub Actions schema
    errors, warnings = validate_github_actions_schema(data, workflow_file)

    # Step 3: Check action versions
    recommendations = check_action_versions(data)

    # Report results
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

    if recommendations:
        print(f"\n💡 RECOMMENDATIONS ({len(recommendations)}):")
        for rec in recommendations:
            print(f"  - {rec}")

    if not errors and not warnings:
        print("\n✓ All checks passed! Workflow is valid.")
    elif not errors:
        print("\n✓ No errors found. Workflow is valid (with warnings/recommendations).")
    else:
        print(f"\n✗ Validation failed with {len(errors)} error(s).")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("WORKFLOW SUMMARY")
    print("=" * 60)
    if 'name' in data:
        print(f"Name: {data['name']}")
    if 'on' in data:
        print(f"Triggers: {', '.join(data['on'].keys()) if isinstance(data['on'], dict) else data['on']}")
    if 'jobs' in data:
        print(f"Jobs: {', '.join(data['jobs'].keys())}")
    print("=" * 60)

if __name__ == '__main__':
    main()
