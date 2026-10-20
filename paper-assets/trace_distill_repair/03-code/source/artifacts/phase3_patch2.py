"""Patch 2: Fix buggy_code retrieval in run_instance to use changed_files fallback."""

filepath = "/root/trace_distill_repair/run_phase3_repair.py"
with open(filepath, "r") as f:
    content = f.read()

# In run_instance(), after getting buggy_code, add fallback to read correct file
old_buggy_code = '    buggy_code = get_buggy_code(instance_key)\n    fixed_code = get_fixed_code_direct(instance_key)'
new_buggy_code = '''    buggy_code = get_buggy_code(instance_key)
    if len(buggy_code) < 500:
        p3inst = load_phase3_instances().get(instance_key, {})
        changed = p3inst.get("changed_files", [])
        if changed:
            alt_path = os.path.join(
                WORKSPACE, "instances", instance_key, "buggy", changed[0]
            )
            if os.path.isfile(alt_path):
                with open(alt_path) as f:
                    alt_code = f.read()
                if len(alt_code) > len(buggy_code):
                    buggy_code = alt_code
    fixed_code = get_fixed_code_direct(instance_key)'''

assert old_buggy_code in content, "old_buggy_code not found!"
content = content.replace(old_buggy_code, new_buggy_code, 1)

# Also fix the dry-run buggy_code retrieval
old_dryrun_buggy = '            buggy_code = get_buggy_code(key)\n            fixed_code = get_fixed_code_direct(key)'
new_dryrun_buggy = '''            buggy_code = get_buggy_code(key)
            if len(buggy_code) < 500:
                p3i_bc = load_phase3_instances().get(key, {})
                changed_bc = p3i_bc.get("changed_files", [])
                if changed_bc:
                    alt_path = os.path.join(
                        WORKSPACE, "instances", key, "buggy", changed_bc[0]
                    )
                    if os.path.isfile(alt_path):
                        with open(alt_path) as _f:
                            alt_code = _f.read()
                        if len(alt_code) > len(buggy_code):
                            buggy_code = alt_code
            fixed_code = get_fixed_code_direct(key)'''

assert old_dryrun_buggy in content, "old_dryrun_buggy not found!"
content = content.replace(old_dryrun_buggy, new_dryrun_buggy, 1)

with open(filepath, "w") as f:
    f.write(content)

print("PATCH 2 APPLIED SUCCESSFULLY")
print(f"New file size: {len(content)} chars, {content.count(chr(10))} lines")
