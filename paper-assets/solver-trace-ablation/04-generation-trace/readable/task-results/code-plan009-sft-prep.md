# code plan009 sft prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-sft-prep_20260514T105249_result.json`
- **Structured JSON:** [`26155ceac54fa12b16cd.json`](../../sessions/26/26155ceac54fa12b16cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查 `save_total_limit` 问题——当前 train_sft.py 设了 `save_total_limit=3`，按 C003 约束应改为 1。

汇总报告：

### Plan009 SFT Baseline 准备状态

| 项目 | 状态 | 详情 |
|------|------|------|
| **SFT 训练脚本** | 已存在 | `/root/solver-trace-ablation/scripts/train_sft.py`，使用 TRL `SFTTrainer`，chat 格式 |
| **训练数据 GT 字段** | 有 | `fol_premises`（list[str]）+ `fol_conclusion`（str）字段齐全，脚本已实现格式化 |
| **Qwen2.5-1.5B** | **未下载** | 只有 Qwen3-4B 和 Qwen2.5-0.5B，需要下载 1.5B |
| **TRL SFTTrainer** | 可用 | 脚本中 `from trl import SFTConfig, SFTTrainer`，环境已装 TRL |
| **eval_sta.py 兼容性** | 兼容 | 接受 `--model_path` 指向任意 HF checkpoint，与模型无关 |

### 需要的准备工作

1. **下载 Qwen2.5-1.5B 模型** — 磁盘剩余 37GB，模型约 3GB，空间充足。建议用 ModelScope 下载到 `/root/autodl-tmp/models/Qwen2.5-1.5B`

2. **修复 train_sft.py 的 `save_total_limit`** — 当前设为 3，按 C003 约束必须改为 1，防止磁盘耗尽

3. **其他** — 数据格式无需转换，eval 管线直接兼容，无其他阻塞项

是否现在执行模型下载和脚本修复？

---
