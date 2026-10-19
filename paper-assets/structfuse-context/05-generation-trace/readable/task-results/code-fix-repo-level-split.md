# code fix repo level split

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_repo_level_split_20260512T212539_result.json`
- **Structured JSON:** [`8d4bf05ec2ec987cbf0d.json`](../../sessions/8d/8d4bf05ec2ec987cbf0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成汇报

### 1. Diff

**修改前** (instance-level random split):
```python
balanced = []
for rid, insts in by_repo_inst.items():
    if len(insts) > args.max_per_repo:
        random.shuffle(insts)
        insts = insts[:args.max_per_repo]
    balanced.extend(insts)
random.shuffle(balanced)

split = int(0.8 * len(balanced))
train_base = balanced[:split]
val_base = balanced[split:]
```

**修改后** (repo-level split):
```python
all_repos = sorted(by_repo_inst.keys())
random.shuffle(all_repos)
split_idx = int(len(all_repos) * 0.8)
train_repos = set(all_repos[:split_idx])
val_repos = set(all_repos[split_idx:])

train_base = []
val_base = []
for rid in all_repos:
    insts = by_repo_inst[rid]
    if len(insts) > args.max_per_repo:
        random.shuffle(insts)
        insts = insts[:args.max_per_repo]
    if rid in train_repos:
        train_base.extend(insts)
    else:
        val_base.extend(insts)
random.shuffle(train_base)
random.shuffle(val_base)
```

### 2. Dry-run 验证结果

- **Repo isolation**: Train 8 repos, Val 2 repos, **Overlap 0 — NO LEAK**
- **三策略 MD5 不同**:
  - random: `908a71b9...` (126.1MB)
  - embedding: `0f831053...` (151.5MB)
  - dataflow: `c6c3ccf1...` (139.2MB)

### 3. Split 统计

| | Repos | Instances |
|---|---|---|
| Train | 8 | 1338 |
| Val | 2 | 220 |
| Total | 10 | 1558 |

---
