# code exp 046 mistral pw600 prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-046-mistral-pw600-prep_20260518T193046_result.json`
- **Structured JSON:** [`1c2626d2b7dc1e529709.json`](../../sessions/1c/1c2626d2b7dc1e529709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Port 8002 空闲，run_full_mvp.py 参数确认无误。

由于 vLLM 启动测试需要先加载模型到 GPU 2（约 60s），且会实际占 GPU 显存，我直接准备最终命令，跳过加载测试（GPU 2 有 97GB 显存，Mistral-7B 绰绰有余，且同模型已在 GPU 0 上成功运行）。

---

## C001 Dry-Run 结果

| 检查项 | 状态 |
|--------|------|
| 模型文件 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/` | 完整（3 shards + tokenizer） |
| 数据 `proofwriter_full.json` | 存在，6001 行 |
| `empty.json` | 存在 |
| 输出目录 | 已创建 |
| Port 8002 | 空闲 |
| GPU 2 | 空闲（0 MiB / 97887 MiB） |
| `run_full_mvp.py` 参数 | 验证通过 |

## 与原计划的变更

- **cuda:1 → cuda:2**（cuda:1 被 exp-034 占用）
- **port 8001 → port 8002**（port 8001 被 exp-034 占用）

## 最终部署命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp046_mistral_7b_pw600 && CUDA_VISIBLE_DEVICES=2 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8002 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp046.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/proofwriter_full.json --folio-data data/empty.json --output results/exp046_mistral_7b_pw600/exp046_results.json --save-intermediates 2>&1 | tee results/exp046_mistral_7b_pw600/exp046.log"
```

确认后我来执行。

---
