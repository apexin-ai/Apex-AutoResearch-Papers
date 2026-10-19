"""Patch training/train.py: add --dynamic-mining and candidate pool re-encoding."""

path = '/root/structfuse/training/train.py'
with open(path) as f:
    lines = f.readlines()

total = len(lines)
print(f"Original file: {total} lines")

# Verify anchors (0-indexed)
assert 'p.add_argument("--embeddings-file"' in lines[471], f"Line 472 mismatch: {lines[471]!r}"
assert 'for epoch in range(args.num_epochs):' in lines[344], f"Line 345 mismatch: {lines[344]!r}"
assert '# P2b:' in lines[345], f"Line 346 mismatch: {lines[345]!r}"
assert 'def _save_checkpoint' in lines[422], f"Line 423 mismatch: {lines[422]!r}"

# Also find the miner setup end and the blank line after it
# Line 322 (0-idx): miner = build_miner(
# Need to find where this call ends (closing paren)
miner_start = 321  # 0-indexed for line 322
miner_end = None
paren_depth = 0
for j in range(miner_start, min(miner_start + 10, total)):
    for ch in lines[j]:
        if ch == '(':
            paren_depth += 1
        elif ch == ')':
            paren_depth -= 1
            if paren_depth == 0:
                miner_end = j
                break
    if miner_end is not None:
        break
assert miner_end is not None, "Could not find end of build_miner() call"
print(f"miner call ends at line {miner_end + 1}")

# Find the blank line after miner_end to insert candidate pool loading
insert_pool_after = miner_end + 1  # line after the closing )

# === Patch 1: Add CLI args after --embeddings-file (line 471) ===
new_args = [
    '    p.add_argument("--dynamic-mining", action="store_true",\n',
    '                   help="Re-mine negatives each epoch using current encoder")\n',
    '    p.add_argument("--candidate-pool-file", default=None,\n',
    '                   help="candidate_pools.jsonl from build_m1_training_data.py --embedding-mining-mode dynamic")\n',
]

# === Patch 2: Insert candidate pool loading after miner setup ===
pool_loading = [
    '\n',
    '    # Load candidate pools for dynamic mining\n',
    '    candidate_pools = None\n',
    '    if getattr(args, "dynamic_mining", False):\n',
    '        if not args.candidate_pool_file:\n',
    '            raise ValueError("--candidate-pool-file required when --dynamic-mining is set")\n',
    '        candidate_pools = {}\n',
    '        with open(args.candidate_pool_file) as f:\n',
    '            for line in f:\n',
    '                if line.strip():\n',
    '                    entry = json.loads(line)\n',
    '                    candidate_pools[entry["instance_id"]] = entry\n',
    '        if accelerator.is_main_process:\n',
    '            print(f"Loaded {len(candidate_pools)} candidate pools for dynamic mining")\n',
]

# === Patch 3: Modify epoch loop start (replace lines 345-350) ===
# Original lines 345-350 (0-indexed):
#   345: # P2b: negatives pre-mined per strategy...
#   346: if accelerator.is_main_process:
#   347:     print(f"[Epoch {epoch+1}] Using pre-mined negatives...")
#   348: (blank)
#   349: (blank)
#   350: accelerator.wait_for_everyone()
# Let me verify these lines
print(f"Line 346: {lines[345]!r}")
print(f"Line 347: {lines[346]!r}")
print(f"Line 348: {lines[347]!r}")
print(f"Line 349: {lines[348]!r}")
print(f"Line 350: {lines[349]!r}")
print(f"Line 351: {lines[350]!r}")

# Find the exact range: from P2b comment to accelerator.wait_for_everyone()
epoch_block_start = 345  # P2b comment
epoch_block_end = None
for j in range(epoch_block_start, min(epoch_block_start + 10, total)):
    if 'accelerator.wait_for_everyone()' in lines[j]:
        epoch_block_end = j
        break
assert epoch_block_end is not None, "Could not find accelerator.wait_for_everyone()"
print(f"Epoch block: lines {epoch_block_start+1}-{epoch_block_end+1}")

epoch_new = [
    '        if getattr(args, "dynamic_mining", False) and candidate_pools is not None:\n',
    '            if accelerator.is_main_process:\n',
    '                print(f"[Epoch {epoch+1}] Dynamic mining: re-encoding candidates...")\n',
    '            mined = _mine_dynamic_negatives(\n',
    '                model=accelerator.unwrap_model(model),\n',
    '                tokenizer=tokenizer,\n',
    '                candidate_pools=candidate_pools,\n',
    '                train_ds=train_ds,\n',
    '                num_negatives=args.num_negatives,\n',
    '                max_seq_length=args.max_seq_length,\n',
    '                device=accelerator.device,\n',
    '            )\n',
    '            train_ds.refresh_negatives(mined)\n',
    '            if accelerator.is_main_process:\n',
    '                print(f"  Mined negatives for {len(mined)} queries")\n',
    '        else:\n',
    '            if accelerator.is_main_process:\n',
    '                print(f"[Epoch {epoch+1}] Using pre-mined negatives ({args.hard_negative_strategy})...")\n',
    '\n',
]

# === Patch 4: Add _mine_dynamic_negatives function before _save_checkpoint (line 422) ===
mine_func = []
def L(s):
    mine_func.append(s + '\n')

L('')
L('@torch.no_grad()')
L('def _mine_dynamic_negatives(model, tokenizer, candidate_pools, train_ds,')
L('                            num_negatives, max_seq_length, device):')
L('    """Re-encode candidates with current model, select top-k hardest negatives per query."""')
L('    model.eval()')
L('')
L('    # Group training samples by instance_id to encode candidates once per instance')
L('    iid_to_samples = {}')
L('    for idx, sample in enumerate(train_ds.samples):')
L('        qid = sample["query_id"]')
L('        iid = qid.split("::", 1)[0]')
L('        iid_to_samples.setdefault(iid, []).append(sample)')
L('')
L('    mined = {}')
L('    for iid, samples in iid_to_samples.items():')
L('        if iid not in candidate_pools:')
L('            continue')
L('')
L('        pool = candidate_pools[iid]')
L('        cand_files = [c["file"] for c in pool["candidates"]]')
L('        cand_texts = [c["content"] for c in pool["candidates"]]')
L('        gold_set = set(pool.get("gold_files", []))')
L('')
L('        if not cand_files:')
L('            continue')
L('')
L('        # Encode all candidates for this instance once')
L('        cand_embs = []')
L('        enc_batch = 32')
L('        for bi in range(0, len(cand_texts), enc_batch):')
L('            batch = cand_texts[bi:bi + enc_batch]')
L('            enc = tokenizer(batch, truncation=True, max_length=max_seq_length,')
L('                           padding=True, return_tensors="pt")')
L('            enc = {k: v.to(device) for k, v in enc.items()}')
L('            emb = model.encode(enc["input_ids"], enc["attention_mask"])')
L('            cand_embs.append(emb)')
L('        cand_embs = torch.cat(cand_embs, dim=0)  # (N, D), already L2-normalized')
L('')
L('        for sample in samples:')
L('            query_id = sample["query_id"]')
L('            query_text = sample["query_tokens"]')
L('            query_file = query_id.split("::", 1)[1] if "::" in query_id else ""')
L('            pos_id = sample.get("pos_id", "")')
L('            pos_file = pos_id.split("::", 1)[1] if "::" in pos_id else ""')
L('')
L('            q_enc = tokenizer(query_text, truncation=True, max_length=max_seq_length,')
L('                              padding=True, return_tensors="pt")')
L('            q_enc = {k: v.to(device) for k, v in q_enc.items()}')
L('            q_emb = model.encode(q_enc["input_ids"], q_enc["attention_mask"])  # (1, D)')
L('')
L('            # Cosine similarity (embeddings already L2-normalized by encode())')
L('            sims = (q_emb @ cand_embs.T).squeeze(0)  # (N,)')
L('            sorted_idx = sims.argsort(descending=True).cpu().tolist()')
L('')
L('            exclude = gold_set | {query_file, pos_file}')
L('            selected = []')
L('            for ci in sorted_idx:')
L('                if len(selected) >= num_negatives:')
L('                    break')
L('                f = cand_files[ci]')
L('                if f not in exclude:')
L('                    selected.append((iid + "::" + f, float(sims[ci])))')
L('')
L('            mined[query_id] = selected')
L('')
L('    model.train()')
L('    return mined')
L('')
L('')

# === Apply patches in a single pass ===
new_lines = []
i = 0
while i < total:
    if i == insert_pool_after:
        # Insert candidate pool loading after miner call
        new_lines.append(lines[i])  # keep the original line (blank or next code)
        new_lines.extend(pool_loading)
        i += 1
    elif i == epoch_block_start:
        # Replace epoch block start
        new_lines.extend(epoch_new)
        i = epoch_block_end  # skip to accelerator.wait_for_everyone() (keep it)
    elif i == 422:  # Before _save_checkpoint
        new_lines.extend(mine_func)
        new_lines.append(lines[i])  # keep _save_checkpoint line
        i += 1
    elif i == 471:  # --embeddings-file arg
        new_lines.append(lines[i])
        new_lines.extend(new_args)
        i += 1
    else:
        new_lines.append(lines[i])
        i += 1

with open(path, 'w') as f:
    f.writelines(new_lines)
print(f"Patched train.py: {total} -> {len(new_lines)} lines")
