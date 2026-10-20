# code l1 head ablation fix

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l1_head_ablation_fix_20260517T130432_result.json`
- **Structured JSON:** [`68713e700e50e3bcf39e.json`](../../sessions/68/68713e700e50e3bcf39e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整运行已提交。

- **PID**: 891475, **tmux session**: `l1_head_ablation`
- **日志**: `~/runs/vla-ssd/l1_head_ablation.log`
- **输出**: `/root/autodl-tmp/vla-ssd/results/l1_head_ablation/results_v2.json`

三处修改总结：
1. **标签逻辑**: label 从 `task_idx` 改为 `instruction_id`(0-9)，train/test split 从 demo-based 改为 task-based (tasks 0-7 train, 8-9 test)
2. **PCA-256**: StandardScaler 之后加 `PCA(n_components=256)` 降维
3. **ablate_top5**: 新增条件 `[0, 10, 14, 22, 25]`，总共 4 个条件

50 images × 10 instructions × 4 conditions = 2000 次前向传播，预计 ~30-40 分钟。

---
