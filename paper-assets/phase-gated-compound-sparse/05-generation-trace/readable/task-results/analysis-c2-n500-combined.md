# analysis c2 n500 combined

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2_n500_combined_20260515T075415_result.json`
- **Structured JSON:** [`0246abe101ead75d5eda.json`](../../sessions/02/0246abe101ead75d5eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**产出文件：**
- 服务器：`/root/autodl-tmp/pacs/analysis_n500_results.json` — 完整统计结果（含跨模型比较）
- 服务器：`/root/autodl-tmp/pacs/analysis_output/n500_unified.json` + `.csv` — 基础统计
- Artifact：`n500_statistics_summary.md` (art_20260515_029b96)
- Registry：`c2_n500_deepseek` 和 `c2_qw_n500_r3` → DONE/success，metrics 已填入

**核心结论：**

| 发现 | 详情 |
|------|------|
| Importance 单调递增 | 两模型均 ρ=1.0, p=0.0417（4级排列检验地板） |
| Phase 依赖 | low >> mid >> high，所有 p < 1e-38 |
| Random s015/s020 | NS（两模型一致） |
| Random s025 | DS bonf_p=0.029, QW bonf_p=3.2e-10（D063 confirmed） |
| Imp/Rand 比率 | DS 15–39×, QW 2.7–20× |
| 跨模型 | DS importance 2.7–5.9× > QW; QW random s025/s030 反而大于 DS |
| D064 anomaly | n=500 resolved，所有 d_z reliable |
| Qwen mid-null | 45.2%（effective_n=274），远高于 DS 10.2% |

---
