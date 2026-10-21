# ops westb cuda1 pruning or download

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-cuda1-pruning-or-download_20260516T044351_result.json`
- **Structured JSON:** [`6b9a999ec5480703861a.json`](../../sessions/6b/6b9a999ec5480703861a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## Qwen2.5-Math-7B 下载状态：进行中

- 正在下载 `model-00003-of-00004.safetensors`（3.65GB，速度 ~800KB/s）
- 已完成 3/4 个 safetensors 文件（shard 1、2、4 已下载，shard 3 在临时目录中下载中）
- 已占用 15GB 磁盘空间
- **预计剩余时间**：shard 3 正在写入中，按当前速度估计还需数十分钟到一两小时完成剩余部分

## 25% sparsity 剪枝可行性：**可行**

所需资源全部就绪：
- **模型**：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`（~14.2GB，完整，含 config.json）
- **importance scores**：`/root/recovery_aware_struct_prune/results/importance_scores.pt`
- **CKA scores**：`/root/recovery_aware_struct_prune/results/cka_scores.pt`
- **prune.py** 支持 `--sparsity 0.25`（默认 0.35）

剪枝命令格式：
```bash
python /root/recovery_aware_struct_prune/src/prune.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path /root/recovery_aware_struct_prune/results/importance_scores.pt \
  --cka_path /root/recovery_aware_struct_prune/results/cka_scores.pt \
  --mode rasp \
  --sparsity 0.25 \
  --alpha 1.0 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 \
  --dtype bfloat16
```

## 建议

Qwen2.5-Math-7B 下载未完成，按 Director 指令应先用 DeepSeek-R1-Distill-Qwen-7B 做 25% sparsity 剪枝。等待确认是否启动。

---
