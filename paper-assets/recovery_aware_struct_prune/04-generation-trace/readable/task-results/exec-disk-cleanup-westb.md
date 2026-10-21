# exec disk cleanup westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_disk_cleanup_westb_20260517T045152_result.json`
- **Structured JSON:** [`2bb185fdfd73efcc625e.json`](../../sessions/2b/2bb185fdfd73efcc625e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已重启并在运行中。

## 汇报

| 项目 | 结果 |
|------|------|
| **checkpoint 删除** | `/grpo_stage2_rasp_20_v9/checkpoint-10` 已删除 |
| **可用空间** | `/root/autodl-tmp` 43G 可用（250G 总，83% 使用） |
| **scoring_ablation_batch 状态** | 已重启，PID 676366 |
| **失败原因** | 非磁盘问题。`model_utils.py:load_pruned_model()` 读取属性名 `per_layer_num_heads` / `per_layer_num_kv_heads`，但 config.json 保存的是 `per_layer_num_attention_heads` / `per_layer_num_key_value_heads`，导致 per-layer attention 调整被跳过，模型维度不匹配 |
| **修复** | 已将 `model_utils.py` 第 31-32 行属性名修正为 `per_layer_num_attention_heads` / `per_layer_num_key_value_heads` |
| **tmux session** | `scoring_ablation`，当前正在执行 magnitude Step 1/4 (Pruning) |

---
