# ssh fix mcmc n17 scripts

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-mcmc-n17-scripts_20260524T093235_result.json`
- **Structured JSON:** [`c4264fcbee5b44c022d3.json`](../../sessions/c4/c4264fcbee5b44c022d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个修复完成并验证通过：

| Fix | 文件 | 状态 |
|-----|------|------|
| 1 | `run_exp003_n17.py` | `CUDA_VISIBLE_DEVICES = "0,3"` |
| 2 | `run_n17_downstream.py` | `JUDGMENT_DIR_N17` → `exp003/judgment_data_n17` |
| 3 | `evaluation.py` | `arena_correlation` 支持 `exclude_models` + `ARENA_NAME_MAPPING` |
| 4 | `bootstrap_delta_tau.py` | 数据驱动（从 idata coords 读模型名）+ qwen3-8b 排除 + N=8 后向兼容 |
| 5 | `run_n17_downstream.py` | `run_bootstrap()` 通过 symlink `output_003b→output_n17` 调用修复后的脚本 |
| 6 | 语法检查 + import 验证 + functional test | 全部通过 |

Judge eval 完成后可直接执行：
```bash
cd /root/gated_mfrm_judge_bias/exp003
python run_exp003_n17.py --judgment-dir ./judgment_data_n17 --exposure-csv ../exp002/results/exposure_scores.csv --output-dir ./output_n17
python run_n17_downstream.py
```

---
