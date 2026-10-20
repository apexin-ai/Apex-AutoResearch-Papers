# code recovery paired training script

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-paired-training-script_20260515T165257_result.json`
- **Structured JSON:** [`1c0ff97929b1578517bb.json`](../../sessions/1c/1c0ff97929b1578517bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都能正常执行。训练脚本正确提示需要先跑 prepare 脚本生成数据——这是预期行为，因为 recovery_paired.jsonl 还在生成中。

**已创建的脚本：**

1. **`scripts/prepare_recovery_paired_data.py`** — 数据准备：
   - 读取 `data/recovery_paired/recovery_paired.jsonl` + `sft_vanilla_v4.jsonl`
   - 3 种模式：`full`（错误前缀+恢复）、`recovery_only`（仅恢复）、`inject_only`（仅错误前缀）
   - Fixed-size 设计，保持总量 = vanilla 数据量（4358），按比例替换
   - 支持 `--ratios 10,25,50` 一次生成多个比例
   - 含数据验证（拒绝 DRY_RUN 占位符）和统计输出
   - `--stats-only` 可只看统计不写文件

2. **`scripts/run_recovery_paired_sft.sh`** — 训练启动：
   - 参数：`--seed`, `--mode`, `--ratio`, `--epochs`, `--lr`, `--lora-rank`, `--dry-run`
   - 自动构建数据路径和实验名（如 `v4_full_recovery_inject25_s42`）
   - 训练参数与现有 dose-response 实验一致
   - 数据文件不存在时给出明确错误提示

**数据生成完毕后的使用流程：**
```bash
# 1. 准备数据（3 种模式 × 3 种比例）
python scripts/prepare_recovery_paired_data.py --mode full --ratios 10,25,50
python scripts/prepare_recovery_paired_data.py --mode recovery_only --ratios 10,25,50

# 2. 启动训练
bash scripts/run_recovery_paired_sft.sh --seed 42 --mode full --ratio 25
```

---
