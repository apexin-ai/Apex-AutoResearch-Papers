# code d062 analysis regime patch

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_analysis_regime_patch_20260516T114733_result.json`
- **Structured JSON:** [`2e60c4a659e9f716d664.json`](../../sessions/2e/2e60c4a659e9f716d664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改总结：

**新增常量**：`SEED_REGIME`（seed→regime映射）、`COMPARABLE_SEEDS = ["s43", "s44"]`

**改动点**：

| 函数 | 变更 |
|------|------|
| `build_summary_table` | `mean` → `mean_all` + `mean_comparable`（仅s43+s44） |
| `print_summary_table` | 表头显示 regime 标注，数据列增加 mean_all/mean_cmp 两列，底部添加 NOTE |
| `write_summary_csv` | 重构为长格式，增加 `regime` 列（3ep/p0 / 2ep/p2），含 mean_all 和 mean_comparable 汇总行 |
| `stratified_analysis` | 输出分为 `all_seeds` 和 `comparable_only` 两组，复用 `_compute_effects` 辅助函数 |
| `bootstrap_ci` | 每个 config 增加 `regime` 字段；pairwise 分为 `pairwise_all_seeds` 和 `pairwise_comparable` |
| `main` | bootstrap 打印增加 regime 标签和双版本 pairwise 输出 |

**dry-run 结果**（6/14 文件，`--partial`）：
- Summary table 正确显示 s42=[3ep/p0]、s43/s44=[2ep/p2]、两种 mean、NOTE 备注
- CSV 含 `regime` 列，值正确
- stratified.json 含 `all_seeds` / `comparable_only` 两组 + `regime_note`
- bootstrap.json 含 config 级 `regime`、`pairwise_all_seeds` / `pairwise_comparable` 两组

---
