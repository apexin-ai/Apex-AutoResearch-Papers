# ssh fewnerd report and v4 verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewnerd_report_and_v4_verify_20260521T144647_result.json`
- **Structured JSON:** [`ae96ba02d17d9f122197.json`](../../sessions/ae/ae96ba02d17d9f122197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇总结果：

---

## 1. v4 FewNERD 数据路径确认

`recompute_alpha_crit_unified.py` 通过 `--input` 参数接收路径，不硬编码数据集名。脚本读取的是 `output/fewnerd_mf4v2_seed{42,123,456}/samples.jsonl`，全部在 autodl-5090 上。

## 2. v4 数值验证：全部匹配

| Seed | Metric | v4 表值 | Recompute | 匹配 |
|------|--------|---------|-----------|------|
| s42 | greedy | 0.7913 | 0.7913 | ✓ |
| s42 | mv_strict | 0.7580 | 0.7580 | ✓ |
| s42 | oracle | 0.8803 | 0.8803 | ✓ |
| s42 | δ(degen) | 9.1% | 9.1% | ✓ |
| s123 | greedy | 0.7908 | 0.7908 | ✓ |
| s123 | mv_strict | 0.7645 | 0.7645 | ✓ |
| s123 | oracle | 0.8899 | 0.8899 | ✓ |
| s123 | δ(degen) | 9.2% | 9.2% | ✓ |
| s456 | greedy | 0.7915 | 0.7915 | ✓ |
| s456 | mv_strict | 0.7689 | 0.7689 | ✓ |
| s456 | oracle | 0.8855 | 0.8855 | ✓ |
| s456 | δ(degen) | 8.1% | 8.1% | ✓ |

## 3. s123 report.json 已生成

通过 `run_mvp_pilot.py --skip_sampling` 从现有 samples.jsonl 重新计算。report 已写入 `output/fewnerd_mf4v2_seed123/report.json`（1697 bytes），verdict = MARGINAL，格式与 s42/s456 一致。

## 4. v3 retries 状态

- `output/fewnerd_mf4v2_seed42_v3/` 和 `output/fewnerd_mf4v2_seed123_v3/` **不存在**
- 无相关进程运行

v3 retries 未启动或从未创建。如果 v4 (mf4v2) 数据已经完整且数值已验证，建议**不再启动 v3 retries**。

---
