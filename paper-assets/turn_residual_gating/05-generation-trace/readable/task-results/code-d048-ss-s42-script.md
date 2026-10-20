# code d048 ss s42 script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_ss_s42_script_20260522T093349_result.json`
- **Structured JSON:** [`7000bcaedd43f072e4fc.json`](../../sessions/70/7000bcaedd43f072e4fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并验证。汇总：

### 创建完成

| 脚本 | 路径 |
|------|------|
| 训练脚本 | `scripts/d048_ss_s42.sh` |
| Eval 模板 | `scripts/d048_eval_template.sh` |

### 参数验证

| 检查项 | 结果 |
|--------|------|
| `train_phase2_v8b.py` 所有参数 | 全部匹配 ✓ |
| `--ss-max-ratio` 默认值 | 0.5（脚本显式设 0.3）✓ |
| `--ss-warmup-steps` 默认值 | 0（未指定，用默认）✓ |
| 模型路径 | 存在 ✓ |
| 数据路径 `data/ultrachat_8k/` | 存在 ✓ |
| `runs/d048_ss_s42` | 不存在（无覆盖风险）✓ |

### Eval 模板调整说明

原模板中 `--eval-data` 参数不存在，已改为 `eval_phase2_gar.py` 的实际参数：
- `--eval-data` → `--conversations-path data/ultrachat_eval_heldout.json`
- 添加了 `--gate-profile` 用于记录 per-turn gate 值
- 其他可用参数：`--gar-variant {ours,dongre}`、`--ar-from-fixed`、`--max-turns`（按需添加）

---
