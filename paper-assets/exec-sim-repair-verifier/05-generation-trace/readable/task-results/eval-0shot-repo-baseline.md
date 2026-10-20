# eval 0shot repo baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_0shot-repo-baseline_20260517T230923_result.json`
- **Structured JSON:** [`5243cf07cefa938177ef.json`](../../sessions/52/5243cf07cefa938177ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，汇总：

| 项目 | 值 |
|---|---|
| **脚本路径** | `/home/sonny/exec-sim-repair-verifier/run_0shot_repo_level.py` |
| **tmux session** | `0shot-repo-baseline` |
| **PID** | 3929211 |
| **数据** | 9784 samples, pass=7138 / fail=2646 |
| **模型** | Qwen3-8B, thinking=disabled, attn=sdpa |
| **截断** | 0 samples truncated（到 400 条为止） |
| **unparseable** | 0% |
| **running accuracy** | ~52.8%（400 samples 时） |
| **处理速度** | ~10 samples/sec |
| **预计总时间** | ~16-17 分钟（ETA ~954s） |

前 400 条 accuracy 约 52.8%，0% unparseable，符合 0-shot baseline 的预期（远低于 fine-tuned CLS 的 74-85%）。

---
