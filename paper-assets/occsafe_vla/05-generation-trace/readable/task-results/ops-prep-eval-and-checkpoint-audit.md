# ops prep eval and checkpoint audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_eval_and_checkpoint_audit_20260523T192953_result.json`
- **Structured JSON:** [`ed88711ed08e0a58f262.json`](../../sessions/ed/ed88711ed08e0a58f262.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。总结：

### 任务 1: Eval 命令

3 个 eval 命令已写入 memory.md，使用正确的 `--pretrained_checkpoint` 参数（用户模板中的 `--vla_path` 是错的）。脚本默认值已匹配训练配置，不需要额外指定 `--num_images_in_input` 等参数。

- **reverse_cutoff_s0_eval** → GPU 2，50K checkpoint 待生成（当前到 40K）
- **cutoff_25k_s0_eval** → GPU 3，50K checkpoint 待生成（当前到 40K）
- **vanilla_retrain_s0_eval** → GPU 2（reverse_cutoff 完后），50K checkpoint 已存在

### 任务 2: Checkpoint 审计

| 条件 | 50K (seed 42) | 状态 |
|------|--------------|------|
| vanilla_retrain_s0 | ✅ westd-34685 | 可用 |
| full_occ_retrain_s0 | ✅ westd-34685 | 可用 |
| ablation_random_occ_s0 | ❌ | westd-10894 上已删除 |
| ablation_occ_detach_s0 | ❌ | westd-10894 上已删除 |
| depth_s0 | ❌ | westd-34685 上已删除 |

**缺失 3 个条件**：random_occ_s0、detach_s0、depth_s0 的 seed 42 checkpoint 均在 eval 后被磁盘清理删除。如需 same-round 梯度分析，需重训这 3 个。s2 版本（seed 44）的 random_occ 和 detach 在 westd-34685 上仍有 50K checkpoint 可用。

---
