# code multi seed rasp scripts

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi-seed-rasp-scripts_20260514T235913_result.json`
- **Structured JSON:** [`a9cd0491cb6c18fa69f1.json`](../../sessions/a9/a9cd0491cb6c18fa69f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查。

**产出**: `/root/recovery_aware_struct_prune/src/run_multi_seed_rasp.sh`

**用法**（两个 seed 可分别跑在两张 GPU 上并行）:
```bash
bash src/run_multi_seed_rasp.sh 123 0   # seed=123 on cuda:0
bash src/run_multi_seed_rasp.sh 7   1   # seed=7   on cuda:1
```

**每 seed 时间估算**（基于 7B 模型 + 单 A6000）:
| 步骤 | 估算 |
|------|------|
| Importance scoring (512 samples) | ~10-15 min |
| CKA overlap (512 samples) | ~10-15 min |
| Pruning (计算+保存) | ~2-5 min |
| GSM8K eval (N=100, max_tokens=4096) | ~30-60 min |
| **合计** | **~55-95 min / seed** |

两个 seed 并行跑（各占一张 GPU）约 1-1.5 小时全部完成。所有模型和结果写入 `/root/autodl-tmp/recovery_aware_struct_prune/`（遵守 C002 约束），GPU 限制 0/1（遵守 C001）。

---
