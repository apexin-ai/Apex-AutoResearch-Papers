# gpu exp 069 llama8b logiqa200 dryrun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-069-llama8b-logiqa200-dryrun_20260519T115202_result.json`
- **Structured JSON:** [`8c1addce592f98fd93e6.json`](../../sessions/8c/8c1addce592f98fd93e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 报告

**结果: Y（通过）**

| 项目 | 详情 |
|---|---|
| vLLM 启动时间 | ~30 秒 |
| 处理速度 | Q1: 114.4s, Q2: 24.0s, Q3: 66.7s, 平均 68.4s/问题 |
| 预估全量时间 | ~224 分钟（约 3.7 小时） |
| 3 题结果 | SICA: D(V), A(V), D(X) / SC: D(V), A(V), C(V) |

**警告（不影响运行）**:
- 部分长 prompt（>4097 tokens）的 extraction 会因 `input_tokens + max_tokens > 8192` 触发 400 错误，脚本 gracefully 跳过（3 题中出现 1 次）
- 偶有 "Empty after stripping thinking" / "No JSON found" warning，不影响最终结果

**建议的全量运行命令**:
```bash
cd /root/symb_invariant_consensus && mkdir -p results/exp069_llama8b_logiqa200

# Step 1: 启动 vLLM
CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 nohup python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8005 \
  --dtype auto --trust-remote-code --enforce-eager \
  > /tmp/vllm_exp069.log 2>&1 &

# Step 2: 确认 vLLM 就绪后运行实验
python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 \
  --api-base http://localhost:8005/v1 --model auto --seed 42 \
  --strategyqa-data data/logiqa_200.json \
  --folio-data data/empty.json --math-data data/empty.json --pw-data data/empty.json \
  --output results/exp069_llama8b_logiqa200/exp069_results.json \
  --save-intermediates 2>&1 | tee results/exp069_llama8b_logiqa200/exp069.log
```

---
