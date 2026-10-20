# code batch analysis script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch_analysis_script_20260519T011324_result.json`
- **Structured JSON:** [`b09c7a19f7f1435f55df.json`](../../sessions/b0/b09c7a19f7f1435f55df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常，输出格式符合要求。

**已完成**：`/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py` 已部署到 westd-17855 并通过 dry-run 验证（用 `a010_s43_bf16` 数据，11 gens，~4s 完成）。

功能概要：
- `--exp_dir` 读取 `all_metrics.json`，计算 8 指标 drift%
- 5 方法 × 8 对（canary: token_entropy/ece × diversity: distinct_1/2/3/mauve），含 BH FDR 校正
- K>=4 consensus 计数；`--null_dirs` 可选开启完整 MMCT
- 单模块失败不影响其他模块，缺失数据处理已覆盖

实验完成后用法：
```bash
python batch_analysis.py --exp_dir results/alpha_sweep/a005_s42_fp32_v3_d080
```

---
