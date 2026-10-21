# fix domain gamma n24 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_domain_gamma_n24_rerun_20260516T170033_result.json`
- **Structured JSON:** [`58a390e1bf4e6d7e4e9f.json`](../../sessions/58/58a390e1bf4e6d7e4e9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 已启动，正常运行中。

**根因**：/tmp 积累了 5.9G 旧 Stan CSV 文件，根分区只剩 6.9G。第 2 个 domain（Social_Sciences）采样时 /tmp 写满，chains 1 和 4 报 "Operation not permitted"。

**修复**：
1. 清理 /tmp 旧文件（释放 5.7G）
2. `TMPDIR=/root/autodl-tmp/tmp` 让 Stan 写到数据盘

**v3 运行状态**：
- PID: **818742**
- Log: `/root/autodl-tmp/exp006/mmlu_domain_gamma_n24_v3.log`
- Output: `/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24_v3/`
- N=21 models（3 个 3B 模型无 RRF entry 被跳过）
- 7 domains 串行，预计总时长 ~80-100 min
- `adapt_delta=0.95`, `max_treedepth=12`（脚本默认值）
- RRF 使用最新版：`rrf_full_n_latest/exposure_scores.json`

---
