# code temperature ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_temperature-ablation_20260517T134633_result.json`
- **Structured JSON:** [`23145562efccdadbc072.json`](../../sessions/23/23145562efccdadbc072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，所有请求返回 200 OK。K=12 traces 分 3 batch（4 per batch）生成中。

**实验已成功提交并运行：**

| 项目 | 详情 |
|------|------|
| 脚本 | `scripts/run_temperature_ablation.sh` |
| 修复 | `--max-model-len` 从 4096 改为 8192 |
| tmux session | `temp_ablation` |
| 三个 T | 0.3 → 0.5 → 1.0 串行执行 |
| 输出 | `results/temperature_ablation/temperature_ablation_T{0.3,0.5,1.0}_results.json` |
| Registry | 三个条目均已标记 RUNNING |
| 日志 | `/tmp/temperature_ablation.log` |
| 预计时长 | ~3h（每个 T 约 1h，60 题 × K=12） |

---
