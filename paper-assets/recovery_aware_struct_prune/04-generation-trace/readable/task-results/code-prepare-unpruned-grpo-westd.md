# code prepare unpruned grpo westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-unpruned-grpo-westd_20260515T172008_result.json`
- **Structured JSON:** [`c88b6c08fe91dbc0239f.json`](../../sessions/c8/c88b6c08fe91dbc0239f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

## 准备结果

| 项目 | 状态 |
|------|------|
| **Base model** | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` (15GB, config 无 `per_layer` 属性，确认未剪枝) |
| **train_grpo_v5.py** | 已写入 westd `src/train_grpo_v5.py` (301行) + `model_utils.py` (106行) |
| **启动脚本** | `/root/autodl-tmp/recovery_aware_struct_prune/run_grpo_unpruned.sh` 已创建 |
| **磁盘** | **46GB 空闲，偏紧**。已将 `save_total_limit` 从 3 降为 2 以控制用量。峰值估算 ~40GB（2 checkpoint + final model）。勉强够用但没有余量 |
| **依赖** | trl 1.4.0, transformers 5.8.1, torch 2.11.0+cu128, bitsandbytes 0.49.2 — 全部就绪 |
| **兼容性** | `load_pruned_model` 检测到无 `per_layer_*` 属性 → 走标准 `from_pretrained` 路径。monkey-patch 同理。无阻塞 |

## 阻塞项

**无硬阻塞**。唯一风险是磁盘余量小 (~6GB buffer)。如果需要更安全的裕度，可以：
- 将 `save_total_limit` 降到 1
- 或清理 westd 上的旧数据（`sft_ablation` 占 87GB，`alpha_ablation` 占 58GB）

启动命令: `bash /root/autodl-tmp/recovery_aware_struct_prune/run_grpo_unpruned.sh`

---
