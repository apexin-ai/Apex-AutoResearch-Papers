# ops llama70b mmlu priority

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_mmlu_priority_20260523T161601_result.json`
- **Structured JSON:** [`3994b9338dfba1a59f7c.json`](../../sessions/39/3994b9338dfba1a59f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 项目 | 状态 |
|------|------|
| Kill 进程 | 334256 (force killed) + 335537 + 5个子进程 — 全部清除 |
| GSM8K 输出 | `llama70b_gsm8k.jsonl` 已删除 |
| exp_llama70b 目录 | 仅剩 `design_llama70b_gsm8k.csv` + `design_llama70b_mmlu.csv`，无 JSONL 输出 |
| MMLU-only 脚本 | `/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_mmlu_only.py` — `BENCHMARKS = ["mmlu"]` |
| tmux session | `exp_llama70b` 已清理 |
| GPU 状态 | 4x H800 全部空闲（0 MiB / 97887 MiB） |

**启动命令**（通过 submit_training_job 提交）：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp_llama70b/run_llama70b_mmlu_only.py
```

**预计运行时间**：288 conditions × ~73s ≈ **5.8 小时**（单 benchmark MMLU only）。

---
