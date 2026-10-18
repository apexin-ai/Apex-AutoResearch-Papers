# ops prep qwen compounding sweep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_qwen_compounding_sweep_20260515T181040_result.json`
- **Structured JSON:** [`6026dfd9c7be00716e36.json`](../../sessions/60/6026dfd9c7be00716e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预验证完成。汇总：

### 验证结果

| 项目 | 状态 | 详情 |
|------|------|------|
| Qwen 模型 | **OK** | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/` — layers=28, kv_heads=4 |
| Qwen profiles | **OK** | `/root/ratekv/qwen_float32_profiles.json` (19KB, model_name=Qwen2.5-7B, 有 `profiles` key) |
| `ppl_profiles_hires.json` | 存在但无 model_name 字段 — 不是 Qwen 专用 |
| `qwen_ppl_profiles_hires.json` | **不存在** |
| `run_k_ablation.py` | **OK** | 4051 bytes, 接受 `--model --profiles --gpu --k_values --budget --output` |

### 提交命令

```
exp_id: qwen_compounding_sweep
server: westd-37397
command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/ratekv/run_k_ablation.py --model /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/ --profiles /root/ratekv/qwen_float32_profiles.json --gpu cuda:0 --k_values 0,2,4,8,16,32,64,128,256 --budget 0.25 --output /root/ratekv/artifacts/qwen_compounding_sweep_results.json
gpu: cuda:0
```

---
