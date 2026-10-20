# ops westd disk check and cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_check_and_cleanup_20260517T191719_result.json`
- **Structured JSON:** [`215034afa687c2b94695.json`](../../sessions/21/215034afa687c2b94695.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 磁盘状态
| 总量 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| 750G | 746G | 4.5G | 100% |

### 2. sft_cka_only_20
**存在**，12G，传输时间 May 18 03:14。剩余 4.5G >= 2GB，按指令保留，未删除。

### 3. 大目录分布 + 清理建议

| 目录 | 大小 | 状态/建议 |
|------|------|-----------|
| `outputs/alpha_ablation/` | 127G | **最大清理候选**。含 11 个 checkpoint（6 个 sft + 5 个 pruned，各 12G）。如果 ablation 实验已完成且结果已记录，可释放 127G |
| `grpo_unpruned_v2/` | 46G | GRPO 训练产物，确认是否仍需要 |
| `grpo_standard_qwen_math/` | 38G | GRPO checkpoint |
| `grpo_rasp_rlvr_20_qwen_math/` | 38G | GRPO checkpoint |
| `grpo_rasp_qwen_math/` | 38G | GRPO checkpoint |
| `grpo_standard_25_qwen_math/` | 36G | GRPO checkpoint |
| `grpo_standard_25/` | 36G | GRPO checkpoint |
| `grpo_rasp_25_qwen_math/` | 36G | GRPO checkpoint |
| `grpo_rasp_25/` | 36G | GRPO checkpoint |
| `sft_unpruned_baseline/` | 15G | baseline 模型 |
| 各 sft/pruned 模型 (×8) | ~12G 每个 | 当前实验模型 |

**关键发现**：
- **GRPO 相关目录共占 ~300G**（8 个目录），是空间大户
- **alpha_ablation 占 127G**，如实验已完成是最高优先清理目标
- 仅清理 alpha_ablation 即可释放 127G，磁盘使用率降至 82%

**建议优先级**：
1. `outputs/alpha_ablation/` (127G) — 如果结果已记录到论文/wandb
2. GRPO 系列 (~300G) — 确认哪些实验已完成、结果已提取
3. `sft_cka_only_20` (12G) — 如果 westb 上有原件且不再需要 westd 副本

---
