# ops cleanup duplicate augment

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-duplicate-augment_20260514T172553_result.json`
- **Structured JSON:** [`f834a8a268883ccee7f1.json`](../../sessions/f8/f834a8a268883ccee7f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无遗留输出文件。结论明确：

## 报告

**保留进程**: PID 368343 (`augment_admissible_v2.py`)  
**被清理进程**: PID 368243 (`augment_expert_data.py`) — 已自行退出，无需手动 kill

### 为什么 v2 是正确版本

| 特性 | augment_expert_data.py (死) | augment_admissible_v2.py (活) |
|---|---|---|
| 数据源 | 2900 games (progress.json 预存) | 3553 games (直接扫 alfworld data) |
| task type 过滤 | 无 | 有 (排除 movable_recep) |
| move/put 追踪 | 无 | 有: `move=678, put=0` ✓ |
| 内置验证 | 无 validate_example | 有 validate_example |
| train/val split | 有 | 有 |
| 结束验证 | action verb check | admissible_found + move_preserved check |
| 格式匹配 RAGEN | 基本匹配 | 明确匹配 (exp019b 专用) |

关键：v2 日志显示 `put_actions=0, move_actions=678`，确认使用原始 expert data 保留 `move X to Y`，未做 put 替换。

### 当前进度

- **1000/3553** games 完成，965 条有效 SFT 数据
- 成功率: 99.2% (992 ok / 1000), 失败主要是 `validate_too_long` (27) 和 `not_won` (8)
- 速率: ~45 games/min (22 分钟处理 1000 个)
- **预估剩余: ~57 分钟**

### 输出路径

- `/root/autodl-tmp/expert_sft_v3/expert_sft_train.jsonl`
- `/root/autodl-tmp/expert_sft_v3/expert_sft_val.jsonl`

（v2 在内存中收集所有数据，最后一次性写入，当前目录为空是正常的）

### 数据污染

无。死进程没有写入任何 jsonl 文件到输出目录。唯一遗留是 `/tmp/augment_expert.log`（无害）。

---
