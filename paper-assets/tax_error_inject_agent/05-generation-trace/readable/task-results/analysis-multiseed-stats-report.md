# analysis multiseed stats report

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-stats-report_20260514T214945_result.json`
- **Structured JSON:** [`5af23aaaa5f072c715f6.json`](../../sessions/5a/5af23aaaa5f072c715f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册完成。关键发现需要注意：

**原 "3.3x variance" claim 需要修正** — 实际计算结果是 **10.4x**（TaxEI variance 0.0111 vs Vanilla 0.001064）。原始 3.3x 可能是 SD ratio（0.1054/0.0326 ≈ 3.2x），论文中应明确用哪个指标。

核心统计结论：

| Claim | 状态 | 关键数据 |
|-------|------|---------|
| TaxEI 无 clean-eval 优势 | ✅ 支持 | seed=0 显著差于 Vanilla (p=0.0053) |
| TaxEI 无 recovery 优势 | ✅ 支持 | 所有 pairwise p > 0.38 |
| TaxEI 增大方差 | ⚠️ 描述性支持 | 10.4x variance ratio，但仅 2 vs 3 seeds |
| Random ≥ TaxEI | ✅ 支持 | 方向一致，但无显著差异 |
| 无检测能力 | ✅ 强支持 | 0% detection across all conditions |
| 研究 underpowered | ✅ 支持 | MDE = h=0.409 (需 ~20pp 差异)，power 仅 0.32 |

产出文件在服务器 `/root/autodl-tmp/tax_error_inject_agent/analysis/` 目录：
- `multiseed_stats.py` — 分析脚本
- `multiseed_report.md` — 完整报告

---
