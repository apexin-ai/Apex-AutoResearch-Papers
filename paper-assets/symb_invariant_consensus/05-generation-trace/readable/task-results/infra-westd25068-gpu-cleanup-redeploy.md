# infra westd25068 gpu cleanup redeploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd25068-gpu-cleanup-redeploy_20260518T195006_result.json`
- **Structured JSON:** [`5b2d0a94d4798ce53933.json`](../../sessions/5b/5b2d0a94d4798ce53933.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 dry-run 完成。以下是最终部署命令。

---

## 实验 A: ICL Oracle (exp-044b)
- GPU: cuda:0, Port: 8000, Model: Qwen2.5-14B-Instruct
- Dry-run: **PASS** — 在 Qwen2.5-14B 上成功处理了 folio 问题，33s/题

```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp044b_icl_oracle_qwen14b && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp044b.log 2>&1 & sleep 120 && python -u run_icl_oracle.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --data data/folio_full.json --output results/exp044b_icl_oracle_qwen14b/results.json --save-intermediates 2>&1 | tee results/exp044b_icl_oracle_qwen14b/exp044b.log"
```

## 实验 B: Mistral-7B PW-600 (exp-046)
- GPU: cuda:2, Port: 8002, Model: Mistral-7B-Instruct-v0.3
- Dry-run: **PASS** — 成功完成 2 题 ProofWriter，SICA=50%, SC=0%

```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp046_mistral_7b_pw600 && CUDA_VISIBLE_DEVICES=2 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8002 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp046.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/proofwriter_full.json --folio-data data/empty.json --output results/exp046_mistral_7b_pw600/exp046_results.json --save-intermediates 2>&1 | tee results/exp046_mistral_7b_pw600/exp046.log"
```

## 实验 C: Backward Verification (exp-045b)
- GPU: cuda:3, Port: 8003, Model: Qwen2.5-14B-Instruct
- Dry-run: **PASS** — 在 Qwen2.5-14B 上成功完成 2 题 backward verification

```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp045b_backward_qwen14b && CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8003 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp045b.log 2>&1 & sleep 120 && python -u backward_verification.py --api-base http://localhost:8003/v1 --model auto --k 12 --data data/folio_full.json --output results/exp045b_backward_qwen14b/results.json --seed 42 --temperature 0.7 2>&1 | tee results/exp045b_backward_qwen14b/exp045b.log"
```

---

### 补充信息

**exp-045 v1 结果**：已完成但使用了**错误模型** (Qwen2.5-7B 而非 14B)。BV accuracy=53.9% vs SC baseline=75.0% (delta=-21.1pp)，数据无效。结果在 `results/exp05_backward_verification/`。

**exp-034 状态**：GPU 1 上 Qwen2.5-14B ProofWriter 正常运行中 (116/600)，未受影响。

**GPU 当前状态**：GPU 0/2/3 已清空，可立即部署。

---
