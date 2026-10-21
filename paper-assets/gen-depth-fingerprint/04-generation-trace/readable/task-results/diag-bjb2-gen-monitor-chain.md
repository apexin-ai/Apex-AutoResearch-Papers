# diag bjb2 gen monitor chain

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-gen-monitor-chain_20260518T071956_result.json`
- **Structured JSON:** [`0cd10b9f0e88c7966ac8.json`](../../sessions/0c/0cd10b9f0e88c7966ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两条自动链均已就位，正在等待生成进程结束。

---

## 汇总

### 生成进度
| 任务 | Session | PID | GPU | 进度 | 预估剩余 |
|------|---------|-----|-----|------|----------|
| Qwen t=0.9 | tc_phase3 | 2067 | GPU 0 (42%, 4.0G) | **927/996** (93%) | ~14 min |
| Llama instruct | exp054_resume | 3103 | GPU 2 (65%, 6.9G) | **944/995** (95%) | ~7 min |

### GPU 状态
- GPU 0: Qwen 生成中 (3968 MiB)
- GPU 1: **空闲** → Qwen 特征提取将用此 GPU
- GPU 2: Llama 生成中 (6916 MiB)
- GPU 3: **空闲** → Llama 特征提取将用此 GPU

### 自动链设置
**tc_phase3:chain** — 等 PID 2067 结束 → `CUDA_VISIBLE_DEVICES=1 python extract_features.py --input data/qwen3-1.7b-t09/generations_shard0.jsonl --output data/features_qwen3-1.7b-t09.csv --device cuda:0`

**exp054_resume:chain** — 等 PID 3103 结束 → `CUDA_VISIBLE_DEVICES=3 python extract_features.py --input data/llama-3.2-3b-instruct/generations_shard0.jsonl --output data/features_llama-3.2-3b-instruct.csv --device cuda:0` → `python eval_exp054_instruct_llama.py`

注意：Qwen 的旧 features CSV（2413 条）将被完整数据重新提取覆盖。`$(date)` 在 echo 中被提前展开了（纯装饰，不影响实际命令执行）。

---
