# code 72b inference script

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b_inference_script_20260522T130940_result.json`
- **Structured JSON:** [`52775ae80ab581624500.json`](../../sessions/52/52775ae80ab581624500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Watchdog 运行中，当前 27/37 shards。

---

## 汇总

### 1. 推理命令

```bash
cd /root/nlp_variance_gtheory
PYTHONPATH=/root/nlp_variance_gtheory python -m src.inference.run_experiment \
    --design design_matrix_exp003_72b.csv \
    --items data/mmlu_items_exp001.json \
    --benchmark mmlu \
    --precision bfloat16 \
    --gpu-id 0 \
    --tensor-parallel 4 \
    --output results/exp003_scale_72b_mmlu.jsonl
```

### 2. Dry-run 验证结果

全部通过：
- 模型路径 → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-72B-Instruct` ✓
- 实验设计 → 288 conditions (2 temps × 6 prompts × 6 seeds × 4 orderings) ✓
- VLLMRunner `tensor_parallel_size` 参数存在 ✓
- Design matrix 验证 ✓ (288 条件, 仅含 72B, temps=[0.0, 0.7])

### 3. Watchdog 状态

旧 watchdog_v2 已于 19:39 过期退出。已部署新 `watchdog_72b.sh` (PID 255068)，每 3 分钟检查 shard 数量，37/37 齐全后自动启动推理。最长等待 12 小时。

### 4. 预估推理时间

| 模型 | 耗时 | 吞吐 (toks/s output) |
|------|------|---------------------|
| 3B (TP=1, 1GPU) | 13 min | ~1,287 |
| 7B (TP=1, 1GPU) | 23.5 min | ~690 |
| **72B (TP=4, 4GPU)** | **~60-90 min** | est. ~200-350 |

72B 推理估计 1-1.5 小时。TP=4 把 72B 参数分到 4 卡（每卡 ~18B，类似 7B 单卡），但 all-reduce 通信开销使实际速度约为 7B 的 1/3-1/2。

**下载进度**：27/37 shards，当前 shard 30 (71%)、32 (43%)、33 (17%) 下载中。速度 ~400KB/s，预计剩余 ~5-8 小时完成下载。

---
