# code t20 analysis script prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_t20_analysis_script_prep_20260520T151115_result.json`
- **Structured JSON:** [`df9adf73a41982faaf50.json`](../../sessions/df/df9adf73a41982faaf50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写好：

**`scripts/t20_post_analysis.py`** — 单实验分析+验证：
- 先检查 gen_0..gen_20 的 metrics.json 完整性
- 调用服务器上的 `run_5method_analysis_d102.py` 跑 D120 5-method lead-lag
- 从输出 JSON 提取 `perm_granger_fdr_forward_sig` 作为 observed PermG count
- 与 `t20_predictions_locked.json` 对应 α 的 `predicted_permg_count` / `rate_95ci` 对比
- 输出验证 JSON 到 `artifacts/t20_verify_a{alpha}_s{seed}.json`

**`scripts/t20_batch_verify.sh`** — 批量运行所有 5 个 α：
- 遍历 α∈{0.45, 0.50, 0.60, 0.75, 1.00}
- 检查 `results/t20/a{alpha}_s42_fp32/gen_20/metrics.json` 存在才运行（跳过未完成的）
- 汇总 PASS/FAIL/SKIP 计数

关键路径映射：
- 实验数据：`/root/autodl-tmp/distrib_canary_collapse/results/t20/a{XXX}_s42_fp32/`
- 分析脚本：`/root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py`（在项目根目录，不在 scripts/ 下）
- 5method 输出：`{exp_dir}/analysis/5method_leadlag.json`

使用时需要先把这两个脚本同步到 17855 的 `$PROJ/scripts/` 下，然后 `bash scripts/t20_batch_verify.sh`。

---
