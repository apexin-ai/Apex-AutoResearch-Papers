# code baseline mode feature

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline-mode-feature_20260514T014605_result.json`
- **Structured JSON:** [`b456e85dc94a7f688d71.json`](../../sessions/b4/b456e85dc94a7f688d71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器修改完成，验证通过。

**修改内容**（bjb1 和 bjb2 一致）：

1. **`parse_args()`** — 新增 `--baseline_mode` 参数（L68-70），choices=`["single", "mean"]`，默认 `single`
2. **`main()`** — 原来 `args.K = 1` 改为条件分支（L359-363）：
   - `single` → K=1（保持原行为）
   - `mean` → K=10（10次采样取均值）
3. **`summary` dict** — 新增 `baseline_mode` 字段（L334），记录到结果 JSON

**无需修改 `select_action_vla_only`**：该函数已实现 `k_trunc.mean(dim=0)`，K=10 时自然计算 10 次采样均值。

**用法**：
```bash
# 原 vla_only（K=1，不变）
python evaluate.py --mode vla_only --benchmark object

# K=10 mean baseline（新）
python evaluate.py --mode vla_only --baseline_mode mean --benchmark object
```

---
