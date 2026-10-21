# fix westd disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_disk_cleanup_20260516T134144_result.json`
- **Structured JSON:** [`1e54b6bf5c755209834b.json`](../../sessions/1e/1e54b6bf5c755209834b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。下面是完整报告和清理计划。

---

## 诊断结果

**数据盘 `/dev/md0`：750G 已 100% 满，仅剩 2.2M**

### 占用分布

| 目录 | 大小 | 说明 |
|------|------|------|
| grpo_rasp_qwen_math | 132G | 6 个 checkpoint (15-40) |
| grpo_standard_qwen_math | 154G | 6 个 checkpoint (10-35) |
| grpo_rasp_25_qwen_math | 100G | 5 个 checkpoint (5-25) |
| grpo_standard_25_qwen_math | 100G | 5 个 checkpoint (5-25) |
| grpo_unpruned_v2 | 46G | 1 个 checkpoint (100) |
| grpo_standard_v8_step50 | 12G | 无 checkpoint |
| pruned_* (8个) | ~80G | 禁删 |
| sft_* (9个) | ~96G | 禁删 |
| models/ | 29G | DeepSeek-R1 + Qwen2.5-Math |
| 其他 | <1G | |

### Checkpoint 完整性

| 实验 | 最新可用 checkpoint | 损坏的 checkpoint |
|------|---------------------|-------------------|
| grpo_rasp_qwen_math | **checkpoint-35** (27G, 完整) | checkpoint-40 (48K, model.safetensors 仅 40KB) |
| grpo_standard_qwen_math | **checkpoint-30** (27G, 完整) | checkpoint-35 (23G, optimizer 截断 12.2G vs 正常 15.7G, 缺 trainer_state/rng_state/scheduler) |
| grpo_rasp_25_qwen_math | **checkpoint-20** (25G, 完整) | checkpoint-25 (48K, model.safetensors 仅 40KB) |
| grpo_standard_25_qwen_math | **checkpoint-20** (25G, 完整) | checkpoint-25 (48K, model.safetensors 仅 40KB) |

### 清理计划

**Phase 1 — 删除损坏 checkpoint (~23G)**
- `grpo_rasp_qwen_math/checkpoint-40` (48K)
- `grpo_standard_qwen_math/checkpoint-35` (23G)
- `grpo_rasp_25_qwen_math/checkpoint-25` (48K)
- `grpo_standard_25_qwen_math/checkpoint-25` (48K)

**Phase 2 — 删除旧 checkpoint，每个实验仅保留最新完整的 (~366G)**
- `grpo_rasp_qwen_math`: 删 15,20,25,30 (保留 35) → ~108G
- `grpo_standard_qwen_math`: 删 10,15,20,25 (保留 30) → ~108G
- `grpo_rasp_25_qwen_math`: 删 5,10,15 (保留 20) → ~75G
- `grpo_standard_25_qwen_math`: 删 5,10,15 (保留 20) → ~75G

**预计释放 ~389G，清理后数据盘约 48% 使用率（~361G/750G）。**

确认执行？

---
