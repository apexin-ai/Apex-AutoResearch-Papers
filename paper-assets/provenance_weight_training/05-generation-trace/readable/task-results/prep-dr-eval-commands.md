# prep dr eval commands

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_dr_eval_commands_20260524T225433_result.json`
- **Structured JSON:** [`7905676eca530bd6d55c.json`](../../sessions/79/7905676eca530bd6d55c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/dr_eval_commands.sh`，9 条 eval 命令（3 实验 × 3 数据集）。

**当前训练进度**：
| 实验 | GPU | 进度 | `final/` 存在 |
|------|-----|------|--------------|
| q03 | cuda:3 | ~999/6103 (16%) | 否 |
| q05 | cuda:2 | ~3499/8477 (41%) | 否 |
| q07 | cuda:1 | ~499/6103 (8%) | 否 |

**关键确认**：
- eval 脚本无 `--stride`/`--fp16` 参数（stride 硬编码为 max_length//2，autocast 内置）
- 结果输出到 `${RESULTS_DIR}/` 需先 `mkdir -p` 创建目录
- 每个 eval 约 5-8 分钟（基于历史 ~5M tokens, 单 GPU）
- 三个实验都还远未完成，q05 最快大约还需 ~5-6 小时

---
