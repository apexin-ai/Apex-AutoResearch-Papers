"""Patch run_phase3_repair.py to fix get_fixed_code_direct and buggy_file."""
import re

filepath = "/root/trace_distill_repair/run_phase3_repair.py"
with open(filepath, "r") as f:
    content = f.read()

# 1. Add subprocess and tempfile imports
content = content.replace(
    "import re\nimport time",
    "import re\nimport subprocess\nimport tempfile\nimport time",
    1,
)

# 2. Add helper functions before get_fixed_code_direct
new_helpers = '''

_PHASE3_INSTANCES_CACHE = None

def load_phase3_instances() -> Dict[str, dict]:
    global _PHASE3_INSTANCES_CACHE
    if _PHASE3_INSTANCES_CACHE is not None:
        return _PHASE3_INSTANCES_CACHE
    path = os.path.join(PIPELINE_OUTPUT, "phase3_instances.json")
    if not os.path.isfile(path):
        _PHASE3_INSTANCES_CACHE = {}
        return _PHASE3_INSTANCES_CACHE
    with open(path) as f:
        instances = json.load(f)
    _PHASE3_INSTANCES_CACHE = {inst["instance_id"]: inst for inst in instances}
    return _PHASE3_INSTANCES_CACHE


def apply_patch_to_get_fixed(buggy_content: str, diff_text: str, filename: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        rel_dir = os.path.dirname(filename)
        if rel_dir:
            os.makedirs(os.path.join(tmpdir, rel_dir), exist_ok=True)
        full_path = os.path.join(tmpdir, filename)
        with open(full_path, "w") as f:
            f.write(buggy_content)
        proc = subprocess.run(
            ["patch", "-p1", "--no-backup-if-mismatch"],
            input=diff_text,
            capture_output=True, text=True,
            cwd=tmpdir,
        )
        if proc.returncode == 0 and os.path.isfile(full_path):
            with open(full_path) as f:
                return f.read()
        logger.warning("patch apply failed (rc=%d): %s", proc.returncode, proc.stderr[:300])
    return ""

'''

content = content.replace(
    "\ndef get_fixed_code_direct(instance_key: str) -> str:\n",
    new_helpers + "def get_fixed_code_direct(instance_key: str) -> str:\n",
    1,
)

# 3. Replace get_fixed_code_direct body
old_body = '''def get_fixed_code_direct(instance_key: str) -> str:
    """Get fixed code from workspace without triggering git checkout."""
    fixed_dir = os.path.join(WORKSPACE, "instances", instance_key, "fixed")
    if not os.path.isdir(fixed_dir):
        return ""
    setup = BugsInPySetup(WORKSPACE)
    parts = instance_key.rsplit("_", 1)
    project, bug_id = parts[0], int(parts[1])
    bug_dir = os.path.join(WORKSPACE, "BugsInPy", "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    buggy_file = bug_info.get("buggy_file", "")
    if buggy_file:
        path = os.path.join(fixed_dir, buggy_file)
        if os.path.isfile(path):
            with open(path) as f:
                return f.read()
    return setup._find_main_python_file(fixed_dir)'''

new_body = '''def get_fixed_code_direct(instance_key: str) -> str:
    """Get fixed code from workspace or generate from ground_truth_patch."""
    fixed_dir = os.path.join(WORKSPACE, "instances", instance_key, "fixed")
    if os.path.isdir(fixed_dir):
        setup = BugsInPySetup(WORKSPACE)
        parts = instance_key.rsplit("_", 1)
        project, bug_id = parts[0], int(parts[1])
        bug_dir = os.path.join(WORKSPACE, "BugsInPy", "projects", project, "bugs", str(bug_id))
        bug_info = setup._read_bug_info(bug_dir)
        buggy_file = bug_info.get("buggy_file", "")
        if buggy_file:
            path = os.path.join(fixed_dir, buggy_file)
            if os.path.isfile(path):
                with open(path) as f:
                    return f.read()
        result = setup._find_main_python_file(fixed_dir)
        if result:
            return result

    instances = load_phase3_instances()
    inst = instances.get(instance_key)
    if not inst or not inst.get("ground_truth_patch"):
        return ""
    patch_text = inst["ground_truth_patch"]
    changed_files = inst.get("changed_files", [])
    if not changed_files:
        return ""
    buggy_file = changed_files[0]
    buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
    buggy_path = os.path.join(buggy_dir, buggy_file)
    if not os.path.isfile(buggy_path):
        return ""
    with open(buggy_path) as f:
        buggy_content = f.read()
    return apply_patch_to_get_fixed(buggy_content, patch_text, buggy_file)'''

assert old_body in content, "old_body not found in content!"
content = content.replace(old_body, new_body, 1)

# 4. Modify run_instance buggy_file fallback
old_bf = '    buggy_file = info.get("bug_info", {}).get("buggy_file", "")\n'
new_bf = '''    buggy_file = info.get("bug_info", {}).get("buggy_file", "")
    if not buggy_file:
        p3inst = load_phase3_instances().get(instance_key, {})
        changed = p3inst.get("changed_files", [])
        if changed:
            buggy_file = changed[0]
'''
assert old_bf in content, "old_bf not found!"
content = content.replace(old_bf, new_bf, 1)

# 5. Enhance dry-run
old_dryrun = '''    if args.dry_run:
        print(f"\\n=== Phase 3 Dry Run ===")
        print(f"Instances: {len(all_keys)}")
        print(f"Conditions: {active_conditions}")
        print(f"Total API calls: {len(all_keys) * len(active_conditions)}")
        print(f"\\nInstances:")
        for key in all_keys:
            ns = len(structural_scores_map[key])
            nl = len(line_scores_map.get(key, []))
            nsk = sum(1 for s in structural_scores_map[key] if s.get("label") == "keep")
            nlk = sum(1 for s in line_scores_map.get(key, []) if s.get("label") == "keep")
            print(f"  {key}: structural={ns} (keep={nsk}), line={nl} (keep={nlk})")
        return'''

new_dryrun = '''    if args.dry_run:
        print(f"\\n=== Phase 3 Dry Run ===")
        print(f"Instances: {len(all_keys)}")
        print(f"Conditions: {active_conditions}")
        print(f"Total API calls: {len(all_keys) * len(active_conditions)}")
        print(f"\\nInstances:")
        for key in all_keys:
            ns = len(structural_scores_map[key])
            nl = len(line_scores_map.get(key, []))
            nsk = sum(1 for s in structural_scores_map[key] if s.get("label") == "keep")
            nlk = sum(1 for s in line_scores_map.get(key, []) if s.get("label") == "keep")
            buggy_code = get_buggy_code(key)
            fixed_code = get_fixed_code_direct(key)
            info = get_instance_info(key)
            bf = info.get("bug_info", {}).get("buggy_file", "")
            if not bf:
                p3i = load_phase3_instances().get(key, {})
                bf = (p3i.get("changed_files") or [""])[0]
            tc = info.get("test_command", "")
            print(f"  {key}: structural={ns} (keep={nsk}), line={nl} (keep={nlk})")
            print(f"    buggy_code={len(buggy_code)} chars, fixed_code={len(fixed_code)} chars")
            print(f"    buggy_file={bf}, test_cmd={'yes' if tc else 'NO'}")
            if not fixed_code:
                print(f"    WARNING: fixed_code is EMPTY")
            if not bf:
                print(f"    WARNING: buggy_file is EMPTY")
        return'''

assert old_dryrun in content, "old_dryrun not found!"
content = content.replace(old_dryrun, new_dryrun, 1)

with open(filepath, "w") as f:
    f.write(content)

print("PATCH APPLIED SUCCESSFULLY")
print(f"New file size: {len(content)} chars, {content.count(chr(10))} lines")
