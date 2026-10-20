"""Patch 3: Fix multi-file patch support in apply_patch_to_get_fixed."""

filepath = "/root/trace_distill_repair/run_phase3_repair.py"
with open(filepath, "r") as f:
    content = f.read()

# Replace get_fixed_code_direct's patch application section
# to copy ALL changed files to temp dir before patching
old_patch_section = '''    instances = load_phase3_instances()
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

new_patch_section = '''    instances = load_phase3_instances()
    inst = instances.get(instance_key)
    if not inst or not inst.get("ground_truth_patch"):
        return ""
    patch_text = inst["ground_truth_patch"]
    changed_files = inst.get("changed_files", [])
    if not changed_files:
        return ""
    target_file = changed_files[0]
    buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
    with tempfile.TemporaryDirectory() as tmpdir:
        for cf in changed_files:
            src = os.path.join(buggy_dir, cf)
            if not os.path.isfile(src):
                continue
            dst = os.path.join(tmpdir, cf)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(src) as f:
                data = f.read()
            with open(dst, "w") as f:
                f.write(data)
        target_path = os.path.join(tmpdir, target_file)
        if not os.path.isfile(target_path):
            return ""
        proc = subprocess.run(
            ["patch", "-p1", "--no-backup-if-mismatch"],
            input=patch_text,
            capture_output=True, text=True,
            cwd=tmpdir,
        )
        if proc.returncode == 0 and os.path.isfile(target_path):
            with open(target_path) as f:
                return f.read()
        logger.warning("patch apply failed for %s (rc=%d): %s",
                        instance_key, proc.returncode, proc.stderr[:300])
    return ""'''

assert old_patch_section in content, "old_patch_section not found!"
content = content.replace(old_patch_section, new_patch_section, 1)

with open(filepath, "w") as f:
    f.write(content)

print("PATCH 3 APPLIED SUCCESSFULLY")
print(f"New file size: {len(content)} chars, {content.count(chr(10))} lines")
