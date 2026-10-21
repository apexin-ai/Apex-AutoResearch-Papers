# code fix inference speedup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_inference_speedup_20260516T215142_result.json`
- **Structured JSON:** [`518891f33b98cc4bc519.json`](../../sessions/51/518891f33b98cc4bc519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Benchmark 已成功启动，正在加载 Dense 模型权重 (94%)。数据集使用了本地缓存。

**修复内容：**
- `benchmark_inference.py` 第 17-19 行原来对所有模型用 `AutoModelForCausalLM.from_pretrained()`
- 新增 `from model_utils import load_pruned_model` 导入（带 `sys.path` 修正）
- `benchmark_model()` 新增 `is_pruned` 参数：`True` 时调用 `load_pruned_model()` 处理非均匀 MLP 维度，`False` 时保持原 `from_pretrained` 逻辑
- Dense 模型 `is_pruned=False`，rasp_20/standard_20 为 `is_pruned=True`

**运行状态：**
- tmux session: `inference_bench`
- GPU: cuda:1 (CUDA_VISIBLE_DEVICES=1)
- 配置: 50 prompts × 512 max_new_tokens × 3 models
- 预计完成时间: ~20-30 分钟（每模型 ~7-10 min）
- 结果输出: `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark.json`
- 日志: `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log`

可用 `tmux capture-pane -t inference_bench -p -S -100` 查看进度。

---
