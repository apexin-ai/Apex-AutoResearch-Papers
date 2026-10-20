# code d063 val sweep prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d063-val-sweep-prep_20260514T082906_result.json`
- **Structured JSON:** [`61bc528412f354db5f9e.json`](../../sessions/61/61bc528412f354db5f9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**eval 脚本**: `eval_repo_cls.py` 已支持 `--split val`（L260），无需修改。

**Val set**: `swebench_val.jsonl`, 9335 samples, majority baseline **75.88%**（pass=7083, fail=2252）。

**已有 val 结果 (home, seed123)**:
| Ckpt | Val Acc | Val F1_macro |
|------|---------|-------------|
| 200 | 62.51% | 55.54 |
| 400 | 80.72% | 67.03 |
| 600 | 76.78% | 66.81 |
| **800** | **81.81%** | **69.14** |
| 1000 | 运行中 | — |

Val best = ckpt-800, 而 test best = ckpt-600，验证了 D063 的问题。

**GPU 状态**: westd 4 卡全满（GPU 0/1 CWM eval ~02:30 UTC May 15 完成，GPU 2/3 8B 训练）。Home GPU 被 seed123 ckpt-1000 val eval 占用（~30min 内完成）。

**待执行**: 6 个 val sweep 命令（P1: v5-conda 3 ckpts + 8b-conda 3 ckpts）已写入 artifact `d063_val_sweep_plan.md`（art_20260514_d9af88），等 westd GPU 0 释放后执行。

---
