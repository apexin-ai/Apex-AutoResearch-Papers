# run d025 v3 s2 minkpp recompute

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_d025_v3_s2_minkpp_recompute_20260515T210334_result.json`
- **Structured JSON:** [`552308dc51c0f507d8ab.json`](../../sessions/55/552308dc51c0f507d8ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果

**已完成：**
- 旧目录已重命名：`Qwen2.5-3B_d025_s42` → `Qwen2.5-3B_d025_s42_DEPRECATED_alpha16`
- v3 输出目录已创建：`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/`

**s2_minkpp 需要 GPU，无法作为 CPU 任务运行。** 原因：`s2_minkpp.py` 的 `compute()` 函数会：
1. 加载 target model（带 LoRA adapter）到 GPU，对所有 benchmark items 做 forward pass 计算 per-token log-probs
2. 卸载 target model，再加载 reference model（自动推断 d000 同 scale 的 adapter）做同样的 forward pass
3. 用两组 log-probs 计算 Min-K%++ score

调用命令（供 Main Agent 调度 GPU 时使用）：
```bash
cd /root/contamcal-irt-calibration/exp002 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=N python compute_signals.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter/ \
  --benchmark {mmlu,gsm8k,arc_challenge} \
  --signal s2 \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/
```
需要对 3 个 benchmark 分别运行。3B 模型需要约 7-8GB 显存（加载两次，但非同时），需要一个空闲 GPU。

---
