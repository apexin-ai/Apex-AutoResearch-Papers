# code eval hellaswag

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_hellaswag_20260517T050518_result.json`
- **Structured JSON:** [`535755753704abc1415c.json`](../../sessions/53/535755753704abc1415c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/spectral_collapse_ews/eval_hellaswag.py` 并验证通过。

功能概要：
- 手写 4-choice log-likelihood scoring，不依赖 lm-eval-harness
- 自动遍历 `gen_N/` 子目录，支持 `--gen N` 指定单代
- 离线兼容：自动设置 `TRANSFORMERS_OFFLINE=1`，数据从 HF cache 或 parquet fallback 加载
- 输出 JSON 数组到 stdout 或 `--output` 文件
- 额外参数：`--max_samples`（调试用）、`--device`、`--data_path`

用法示例：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python eval_hellaswag.py --checkpoint_dir /root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/ --batch_size 8
python eval_hellaswag.py --checkpoint_dir /root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/ --gen 0 --max_samples 100
```

---
