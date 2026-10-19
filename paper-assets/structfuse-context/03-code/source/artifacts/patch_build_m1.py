"""Patch build_m1_training_data.py: add --embedding-mining-mode {static,dynamic}."""

path = '/root/structfuse/scripts/build_m1_training_data.py'
with open(path) as f:
    lines = f.readlines()

total = len(lines)
print(f"Original file: {total} lines")

# Verify anchors (1-indexed from grep, convert to 0-indexed)
assert '    parser.add_argument("--seed"' in lines[152], f"Line 153 mismatch: {lines[152]!r}"
assert '            # BM25' in lines[226], f"Line 227 mismatch: {lines[226]!r}"
assert '            # Track strategy divergence' in lines[232], f"Line 233 mismatch: {lines[232]!r}"
assert '    os.makedirs(args.output_dir' in lines[289], f"Line 290 mismatch: {lines[289]!r}"
assert '    print("Done!")' in lines[349], f"Line 350 mismatch: {lines[349]!r}"

# === Patch 1: Insert --embedding-mining-mode arg after --seed (line 152) ===
insert_arg = [
    '    parser.add_argument("--embedding-mining-mode", choices=["static", "dynamic"],\n',
    '                        default="static",\n',
    '                        help="static: pre-mine negatives with BM25; '\
    'dynamic: output candidate pools for training-time mining")\n',
]

# === Patch 2: Wrap BM25+pools in conditional (lines 226-230) ===
bm25_new = [
    '            if args.embedding_mining_mode == "static":\n',
    '                bm25 = compute_bm25_scores(source_files[buggy_file], all_py, source_files)\n',
    '                pools = build_candidate_pools(non_pos, bm25, full_connected, args.pool_size)\n',
    '            else:\n',
    '                pools = {}\n',
]

# === Patch 3: Guard strategy divergence (lines 232-235) ===
track_new = [
    '            if args.embedding_mining_mode == "static":\n',
    '                if set(pools["embedding"]) != set(pools["dataflow"]):\n',
    '                    stats["total_pos_diff"] += 1\n',
    '                stats["total_instances"] += 1\n',
]

# === Patch 4: Replace output section (lines 289-349) ===
output_new = []
# Build the replacement as explicit line list to avoid escaping issues
def L(s):
    """Append a line (auto-adds newline)."""
    output_new.append(s + '\n')

L('    os.makedirs(args.output_dir, exist_ok=True)')
L('')
L('    if args.embedding_mining_mode == "dynamic":')
L('        pool_path = os.path.join(args.output_dir, "candidate_pools.jsonl")')
L('        with open(pool_path, "w") as f:')
L('            for iid, rd in repo_data.items():')
L('                buggy = rd["buggy_file"]')
L('                pos_set = set(rd["valid_pos"])')
L('                non_pos = [fp for fp in rd["source_files"]')
L('                           if fp != buggy and fp not in pos_set]')
L('                entry = {')
L('                    "instance_id": iid,')
L('                    "buggy_file": buggy,')
L('                    "gold_files": rd["valid_pos"],')
L('                    "candidates": [{"file": fp, "content": rd["source_files"][fp]}')
L('                                   for fp in non_pos],')
L('                    "dataflow_connected": list(rd["full_connected"]),')
L('                }')
L('                f.write(json.dumps(entry, ensure_ascii=False) + "\\n")')
L('        print(f"candidate_pools: {len(repo_data)} instances -> {pool_path}")')
L('')
L('        train_instances = []')
L('        for inst in train_base:')
L('            iid = inst["iid"]')
L('            rd = repo_data[iid]')
L('            pos_set = set(rd["valid_pos"])')
L('            non_pos = [fp for fp in rd["source_files"]')
L('                       if fp != inst["query_file"] and fp not in pos_set]')
L('            train_instances.append({')
L('                "query_id": iid + "::" + inst["query_file"],')
L('                "query_tokens": rd["source_files"][inst["query_file"]],')
L('                "pos_id": iid + "::" + inst["pos_file"],')
L('                "pos_tokens": rd["source_files"][inst["pos_file"]],')
L('                "pos_dataflow_distance": 1,')
L('                "neg_candidates": [iid + "::" + f for f in non_pos],')
L('                "candidate_tokens": {iid + "::" + f: rd["source_files"].get(f, "") for f in non_pos},')
L('            })')
L('')
L('        dyn_path = os.path.join(args.output_dir, "train_dynamic.jsonl")')
L('        with open(dyn_path, "w") as f:')
L('            for inst in train_instances:')
L('                f.write(json.dumps(inst, ensure_ascii=False) + "\\n")')
L('        print(f"dynamic: {len(train_instances)} train -> {dyn_path}")')
L('')
L('        val_instances = []')
L('        for inst in val_base:')
L('            iid = inst["iid"]')
L('            rd = repo_data[iid]')
L('            pos_set = set(rd["valid_pos"])')
L('            non_pos = [fp for fp in rd["source_files"]')
L('                       if fp != inst["query_file"] and fp not in pos_set]')
L('            val_instances.append({')
L('                "query_id": iid + "::" + inst["query_file"],')
L('                "query_tokens": rd["source_files"][inst["query_file"]],')
L('                "pos_id": iid + "::" + inst["pos_file"],')
L('                "pos_tokens": rd["source_files"][inst["pos_file"]],')
L('                "pos_dataflow_distance": 1,')
L('                "neg_candidates": [iid + "::" + f for f in non_pos],')
L('                "candidate_tokens": {iid + "::" + f: rd["source_files"].get(f, "") for f in non_pos},')
L('            })')
L('')
L('        val_path = os.path.join(args.output_dir, "val.jsonl")')
L('        with open(val_path, "w") as f:')
L('            for inst in val_instances:')
L('                f.write(json.dumps(inst, ensure_ascii=False) + "\\n")')
L('        print(f"val: {len(val_instances)} -> {val_path}")')
L('')
L('    else:')
L('        for strategy in ["random", "embedding", "dataflow"]:')
L('            instances = []')
L('            for inst in train_base:')
L('                iid = inst["iid"]')
L('                rd = repo_data[iid]')
L('                pool = rd["pools"][strategy]')
L('')
L('                instances.append({')
L('                    "query_id": iid + "::" + inst["query_file"],')
L('                    "query_tokens": rd["source_files"][inst["query_file"]],')
L('                    "pos_id": iid + "::" + inst["pos_file"],')
L('                    "pos_tokens": rd["source_files"][inst["pos_file"]],')
L('                    "pos_dataflow_distance": 1,')
L('                    "neg_candidates": [iid + "::" + f for f in pool],')
L('                    "candidate_tokens": {iid + "::" + f: rd["source_files"].get(f, "") for f in pool},')
L('                })')
L('')
L('            path = os.path.join(args.output_dir, f"train_{strategy}.jsonl")')
L('            with open(path, "w") as f:')
L('                for inst in instances:')
L('                    f.write(json.dumps(inst, ensure_ascii=False) + "\\n")')
L('            print(f"{strategy}: {len(instances)} train -> {path}")')
L('')
L('        val_instances = []')
L('        for inst in val_base:')
L('            iid = inst["iid"]')
L('            rd = repo_data[iid]')
L('            pool = rd["pools"]["random"]')
L('')
L('            val_instances.append({')
L('                "query_id": iid + "::" + inst["query_file"],')
L('                "query_tokens": rd["source_files"][inst["query_file"]],')
L('                "pos_id": iid + "::" + inst["pos_file"],')
L('                "pos_tokens": rd["source_files"][inst["pos_file"]],')
L('                "pos_dataflow_distance": 1,')
L('                "neg_candidates": [iid + "::" + f for f in pool],')
L('                "candidate_tokens": {iid + "::" + f: rd["source_files"].get(f, "") for f in pool},')
L('            })')
L('')
L('        val_path = os.path.join(args.output_dir, "val.jsonl")')
L('        with open(val_path, "w") as f:')
L('            for inst in val_instances:')
L('                f.write(json.dumps(inst, ensure_ascii=False) + "\\n")')
L('        print(f"val: {len(val_instances)} -> {val_path}")')
L('')
L('    graph_path = os.path.join(args.output_dir, "dataflow_graph.json")')
L('    with open(graph_path, "w") as f:')
L('        json.dump(dataflow_graph, f)')
L('    print(f"Dataflow graph: {len(dataflow_graph)} entries -> {graph_path}")')
L('')
L('    import hashlib')
L('    if args.embedding_mining_mode == "static":')
L('        for s in ["random", "embedding", "dataflow"]:')
L('            p = os.path.join(args.output_dir, f"train_{s}.jsonl")')
L('            sz = os.path.getsize(p) / 1024 / 1024')
L('            h = hashlib.md5(open(p, "rb").read()).hexdigest()')
L('            print(f"  {s}: {sz:.1f}MB, md5={h}")')
L('    else:')
L('        p = os.path.join(args.output_dir, "train_dynamic.jsonl")')
L('        sz = os.path.getsize(p) / 1024 / 1024')
L('        h = hashlib.md5(open(p, "rb").read()).hexdigest()')
L('        print(f"  dynamic: {sz:.1f}MB, md5={h}")')
L('        pp = os.path.join(args.output_dir, "candidate_pools.jsonl")')
L('        psz = os.path.getsize(pp) / 1024 / 1024')
L('        ph = hashlib.md5(open(pp, "rb").read()).hexdigest()')
L('        print(f"  pools: {psz:.1f}MB, md5={ph}")')
L('    print(f"  val: {os.path.getsize(val_path)/1024/1024:.1f}MB")')
L('    print("Done!")')

# === Apply patches in a single pass ===
new_lines = []
i = 0
while i < total:
    if i == 152:  # --seed arg line
        new_lines.append(lines[i])
        new_lines.extend(insert_arg)
        i += 1
    elif i == 226:  # BM25 section start
        new_lines.extend(bm25_new)
        i = 231  # skip 5 lines (226-230 inclusive)
    elif i == 232:  # strategy divergence section
        new_lines.extend(track_new)
        i = 236  # skip 4 lines (232-235 inclusive)
    elif i == 289:  # output section start
        new_lines.extend(output_new)
        i = 350  # skip to after line 349 (print("Done!"))
    else:
        new_lines.append(lines[i])
        i += 1

with open(path, 'w') as f:
    f.writelines(new_lines)
print(f"Patched build_m1_training_data.py: {total} -> {len(new_lines)} lines")
