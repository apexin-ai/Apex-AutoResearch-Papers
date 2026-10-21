# monitor westd grpo progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd_grpo_progress_20260516T133855_result.json`
- **Structured JSON:** [`be7e3de0ecd9a2def33f.json`](../../sessions/be/be7e3de0ecd9a2def33f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 个 GRPO 已崩溃退出（EXIT_CODE=1），GPU 全部空闲（0% 利用率）。**

崩溃原因：3 个为 `No space left on device`（checkpoint 写磁盘满），1 个为 `RuntimeError: unexpected pos`（同属磁盘写入损坏）。

日志每 10 step 打印一次，以下为各实验崩溃前最后记录的状态：

| exp_id | step | reward | grad_norm | frac_zero_std | 状态 |
|--------|------|--------|-----------|---------------|------|
| grpo_rasp_qwen_math | 40/100 | 0.083 | 5.59 | 0.65 | ❌ 磁盘满崩溃 |
| grpo_standard_qwen_math | 30/100 | 0.063 | 2.28 | 0.775 | ❌ 磁盘满崩溃 |
| grpo_rasp_25_qwen_math | 20/100 | 0.169 | 1.94 | 0.55 | ❌ 磁盘满崩溃 |
| grpo_standard_25_qwen_math | 20/100 | 0.163 | 3.33 | 0.40 | ❌ 磁盘满崩溃 + KL 爆炸(56.08) |

**Collapse 分析：**
- `grpo_standard_qwen_math`：frac_zero_std=0.975（step 20）→ 严重 collapse，reward 降到 0.007
- `grpo_standard_25_qwen_math`：KL=56.08（step 20），策略严重偏移
- 两个 RASP 组相对正常，但 reward 偏低

**根因：** checkpoint 写入路径可能在根分区而非 `/root/autodl-tmp/`，导致磁盘满。当前根分区 df 显示 5.1G/30G（17%），说明崩溃后文件可能已被清理或 wandb finish 释放了部分空间。需要检查训练脚本的 `output_dir` 配置是否指向数据盘。

---
