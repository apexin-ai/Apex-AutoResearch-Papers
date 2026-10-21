# code repo level 3shot baseline prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-level-3shot-baseline-prep_20260519T024810_result.json`
- **Structured JSON:** [`5a747f90b1176dc1c4dd.json`](../../sessions/5a/5a747f90b1176dc1c4dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常。输出格式与 `eval_repo_cls.py` 一致。

**结果汇总：**

| 项目 | 信息 |
|------|------|
| 脚本路径 | `/home/sonny/exec-sim-repair-verifier/eval_3shot_baseline.py` |
| 输出目录 | `artifacts/eval_3shot/` (predictions.jsonl + summary.json) |
| 推理速度 | ~2.4 ex/s (基于 3-sample test) |
| 预估全量时间 | 9784 / 2.4 ≈ **68 分钟** (单 GPU) |
| 测试集 | 9784 per-test instances, 48 variants |

**推荐全量运行命令：**

```bash
cd /home/sonny/exec-sim-repair-verifier && \
HF_HUB_OFFLINE=1 nohup /root/miniconda3/bin/python eval_3shot_baseline.py \
    --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
    --data_dir data/swebench_full \
    --device cuda:1 \
    --max_seq_length 4096 \
    --output_dir artifacts/eval_3shot_deepseek \
    > logs/eval_3shot_deepseek.log 2>&1 &
```

脚本支持 `--resume_from N` 断点续跑，以及 `--max_samples` 用于调试。Predictions JSONL 包含 `problem_id` 和 `mutation_type` 字段，可直接与 `aggregate_variant_level.py` 对接。

---
