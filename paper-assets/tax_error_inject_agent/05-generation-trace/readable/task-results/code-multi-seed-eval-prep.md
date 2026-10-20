# code multi seed eval prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi-seed-eval-prep_20260514T182339_result.json`
- **Structured JSON:** [`47b7492e19111da9230d.json`](../../sessions/47/47b7492e19111da9230d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**创建了** `scripts/run_multiseed_eval.sh`：
- 用法：`bash scripts/run_multiseed_eval.sh vanilla 0`
- 自动发现 seed=42（无后缀目录）+ seed=0/7/123（带后缀目录）的最新 checkpoint
- 输出命名与 `analyze_multiseed.py` 一致（seed42 → `v4_{type}_eval.json`，其他 → `v4_{type}_seed{N}_eval.json`）
- 已有结果自动跳过（删除文件可重跑）

**`scripts/aggregate_multiseed.py` 无需创建**——已有 `scripts/analyze_multiseed.py`，功能更完整（bootstrap CI、paired permutation test、per-task-type breakdown）。eval 完后直接运行：
```bash
python scripts/analyze_multiseed.py
```

当前 checkpoint 状态：seed0 有 checkpoint-1090，seed7 有 checkpoint-545（可能还在训练），seed123 尚无 checkpoint。

---
