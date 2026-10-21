import re

# ---- Patch run_bootstrap_loo.py ----
with open('/root/autodl-tmp/struct_self_consist_ie/run_bootstrap_loo.py') as f:
    code = f.read()

# 1. Add filter_gold_nonempty after load_instances function
old_load = '''def load_instances(path):
    insts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                insts.append(json.loads(line))
    return insts'''

new_load = '''def load_instances(path):
    insts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                insts.append(json.loads(line))
    return insts

def filter_gold_nonempty(instances):
    """Filter out instances where gold entities list is empty."""
    return [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]'''

code = code.replace(old_load, new_load)

# 2. Patch Part 1: bootstrap CI loading
old_part1_load = '''        i8 = load_instances(ds["n8"])
        i16 = load_instances(ds["n16"])
        print(f"  N=8: {len(i8)} inst ({len(i8[0]['samples'])} samp/inst)")
        print(f"  N=16: {len(i16)} inst ({len(i16[0]['samples'])} samp/inst)")'''

new_part1_load = '''        i8_raw = load_instances(ds["n8"])
        i16_raw = load_instances(ds["n16"])
        i8 = filter_gold_nonempty(i8_raw)
        i16 = filter_gold_nonempty(i16_raw)
        print(f"  N=8: {len(i8)} inst (filtered {len(i8_raw)-len(i8)} gold_empty, {len(i8[0]['samples'])} samp/inst)")
        print(f"  N=16: {len(i16)} inst (filtered {len(i16_raw)-len(i16)} gold_empty, {len(i16[0]['samples'])} samp/inst)")'''

code = code.replace(old_part1_load, new_part1_load)

# 3. Patch Part 2: LOO-SJ loading
old_part2_load = '''            insts = load_instances(path)
            res = compute_loo_sj_analysis(insts)'''

new_part2_load = '''            insts_raw = load_instances(path)
            insts = filter_gold_nonempty(insts_raw)
            print(f"  Loaded {len(insts)} inst (filtered {len(insts_raw)-len(insts)} gold_empty)")
            res = compute_loo_sj_analysis(insts)'''

code = code.replace(old_part2_load, new_part2_load)

with open('/root/autodl-tmp/struct_self_consist_ie/run_bootstrap_loo.py', 'w') as f:
    f.write(code)
print("Patched run_bootstrap_loo.py")

# ---- Patch run_loo_v2.py ----
with open('/root/autodl-tmp/struct_self_consist_ie/run_loo_v2.py') as f:
    code2 = f.read()

# 1. Add filter_gold_nonempty after load_instances
old_load2 = '''def load_instances(path):
    insts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line: insts.append(json.loads(line))
    return insts'''

new_load2 = '''def load_instances(path):
    insts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line: insts.append(json.loads(line))
    return insts

def filter_gold_nonempty(instances):
    """Filter out instances where gold entities list is empty."""
    return [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]'''

code2 = code2.replace(old_load2, new_load2)

# 2. Patch main loading
old_loo_load = '''            insts = load_instances(path)
            res = loo_sj_analysis(insts)'''

new_loo_load = '''            insts_raw = load_instances(path)
            insts = filter_gold_nonempty(insts_raw)
            print(f"  Loaded {len(insts)} inst (filtered {len(insts_raw)-len(insts)} gold_empty)")
            res = loo_sj_analysis(insts)'''

code2 = code2.replace(old_loo_load, new_loo_load)

with open('/root/autodl-tmp/struct_self_consist_ie/run_loo_v2.py', 'w') as f:
    f.write(code2)
print("Patched run_loo_v2.py")
