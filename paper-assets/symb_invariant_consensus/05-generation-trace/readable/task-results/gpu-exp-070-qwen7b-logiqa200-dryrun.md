# gpu exp 070 qwen7b logiqa200 dryrun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-070-qwen7b-logiqa200-dryrun_20260519T115213_result.json`
- **Structured JSON:** [`009fc7c88ae67fba29a8.json`](../../sessions/00/009fc7c88ae67fba29a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 报告

**状态: PASS**

| 项目 | 结果 |
|------|------|
| dry-run 通过 | **Y** |
| vLLM 启动 | 已有实例在 port 8002 运行（Qwen2.5-7B-Instruct, cuda:2, enforce-eager + FLASHINFER_SAMPLER=0） |
| 处理速度 | 问题 0: 20.2s, 问题 1: 13.0s, 平均 ~16.6s/题 |
| ETA (200题) | ~55 min |
| 2/2 正确 | SICA=100%, SC=100% |
| 报错/警告 | 无 |

**注意事项:**
- cuda:2 上已有 vLLM (port 8002) 运行 Qwen2.5-7B-Instruct，无需重新启动
- `run_logiqa.py` 也存在（exp-069 用它跑 Mistral LogiQA），但 dry-run 用了你指定的 `run_full_mvp.py --strategyqa-data`
- port 8002 的 vLLM 没设 `--max-model-len 8192`（默认 32768），不影响功能

**建议的全量运行命令:**
```bash
cd /root/symb_invariant_consensus
python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 \
  --api-base http://localhost:8002/v1 --model auto --seed 42 \
  --strategyqa-data data/logiqa_200.json \
  --folio-data data/empty.json --math-data data/empty.json --pw-data data/empty.json \
  --output results/exp070_qwen7b_logiqa200/exp070_results.json \
  --save-intermediates 2>&1 | tee results/exp070_qwen7b_logiqa200/exp070_run.log
```

---
