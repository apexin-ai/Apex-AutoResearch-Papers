# code unstructured pruning baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unstructured_pruning_baseline_20260519T030837_result.json`
- **Structured JSON:** [`9880cb211048fa5086e4.json`](../../sessions/98/9880cb211048fa5086e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已有**: `src/run_unstructured_baseline.py` — 手动 zeroing + 内存中 eval，不保存 pruned model

**新建**: `src/prune_unstructured.py` — 使用 `torch.nn.utils.prune.global_unstructured` 做全局 L1 magnitude pruning，保存 pruned model 到磁盘。与已有脚本的区别：
- 用 PyTorch 官方 prune API（有 mask 管理，prune.remove 永久化）
- 输出完整 HF model 到 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured/s{pct}/`
- 跳过 embed/lm_head/norm 层（与现有脚本一致）
- `--gpu` 参数控制设备

**Dry-run `--help` 通过**。

运行命令：
```bash
# 剪枝 (20% sparsity, ~5min)
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/prune_unstructured.py --sparsity 0.2 --gpu 0

# 快速验证 (100 samples GSM8K)
/root/miniconda3/bin/python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured/s20 --max_samples 100 --seed 42
```

注意：westd-29022 的 `python` 不在 PATH 里，需要用 `/root/miniconda3/bin/python`。

---
