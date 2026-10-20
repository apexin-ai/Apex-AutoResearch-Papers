# code fix instruction retention v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_instruction_retention_v2_20260521T030923_result.json`
- **Structured JSON:** [`38e60515f9c21710751a.json`](../../sessions/38/38e60515f9c21710751a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动完成，摘要：

**修复 1：`--seed` 参数**
- 新增 `import random`（L27）
- argparse 加 `--seed`，默认 42
- L378-381：模型加载前设 `random.seed` / `np.random.seed` / `torch.manual_seed` / `torch.cuda.manual_seed_all`
- seed 值写入输出 JSON 的 args 字段

**修复 2：按 category 分组报告**
- L121-139：`CATEGORY_MAP` 硬编码 18 个 check_fn → 4 个 category 的映射
- `compute_summary` 中每个 beta 新增 `per_category` 字段，含各 category 的 overall_rate 和 late_turn_rate
- 跨 beta 新增 `per_category_comparison`，含每个 category 的 late-turn rate delta
- 终端 summary 输出新增分 category 表格（category / β=0 / β=3 / Δ）

---
