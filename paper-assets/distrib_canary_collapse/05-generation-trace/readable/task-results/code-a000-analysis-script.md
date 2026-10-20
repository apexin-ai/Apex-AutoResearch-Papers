# code a000 analysis script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a000_analysis_script_20260516T162214_result.json`
- **Structured JSON:** [`e861fd7041ef62ec5589.json`](../../sessions/e8/e861fd7041ef62ec5589.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整管线在 a075_s43 上验证通过，结果与预期一致（4/8 robust pairs, 5/8 perm FDR sig）。

**产出已就绪:**

| 文件 | 说明 |
|------|------|
| `/root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py` | 通用 CLI 脚本，支持 `--data_dir`, `--alpha`, `--seed`, `--dry-run` |
| `/root/autodl-tmp/distrib_canary_collapse/run_a000_batch_analysis.sh` | 一键跑 a000 两个 seed |

**a000 当前状态:** s43 和 s44 各有 gen_0~gen_5（共 5 代），训练完成到 gen_10 后执行 `bash run_a000_batch_analysis.sh` 即可。脚本会自动从 `gen_X/metrics.json` 聚合数据，无需预先生成 `all_metrics.json`。

---
