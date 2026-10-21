# analysis phase diagram t20 a075 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t20_a075_s43_fp32_20260522T122202_result.json`
- **Structured JSON:** [`8a14bcff2819fe27617d.json`](../../sessions/8a/8a14bcff2819fe27617d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**s43 与 s42 完全一致，cross-seed validation SUCCESS。**

| 指标 | s43 | s42 | 匹配 |
|------|-----|-----|------|
| PermG_fwd_fdr | **6/8** | 6/8 | Exact |
| PermG_rev_fdr | **0/8** | 0/8 | Exact |
| DiffXCorr_fdr_fwd | **8/8** | 7/8 | +1 |
| Threshold_3sigma | **6/8** | 6/8 | Exact |
| K>=3 robust pairs | **6/8** | 6/8 | Exact |

- PermG 方向性 6/0 保持（forward causation robust to seed）
- 同样的 2 个 mauve pair 为 non-detection（mauve 仅漂移 +5%，信号太弱）
- TY 从 5/8 降到 3/8，符合 C003 预期（TY seed-unstable）
- 6/8 ceiling 在 T=20 alpha=0.75 的第 2 个 seed 得到确认

产出文件：
- 分析报告: `artifacts/phase_diagram_t20_a075_s43_fp32_analysis.md`
- 5-method JSON: `artifacts/phase_diagram_t20_a075_s43_fp32/data/5method_leadlag.json`
- Registry metrics dict 在报告末尾，可直接用于 `update_registry`

---
