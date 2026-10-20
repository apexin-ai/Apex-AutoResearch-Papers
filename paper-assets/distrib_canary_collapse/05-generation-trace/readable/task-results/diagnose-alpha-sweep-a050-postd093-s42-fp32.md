# diagnose alpha sweep a050 postd093 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha_sweep_a050_postd093_s42_fp32_20260520T033207_result.json`
- **Structured JSON:** [`5b9ef293ae0166e6e01a.json`](../../sessions/5b/5b9ef293ae0166e6e01a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**确认结果：**
- EXIT_CODE=0，训练正常完成
- gen_0 ~ gen_10 共 11 个 generation 目录完整，all_metrics.json 和 analysis_results.json 均存在
- 日志末尾为 "All metrics saved" + "Sentinel written"，无 error
- `checkpoint_path` → `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_postd093_s42_fp32/gen_10/checkpoint`
- `log_path` → `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_postd093_s42_fp32/train.log`

日志内容与 conclusion=success (PermG=6/8) 一致，无异常。

---
