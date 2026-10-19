# research paper outline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-outline-prep_20260515T044605_result.json`
- **Structured JSON:** [`da999e17fd7f826dee7f.json`](../../sessions/da/da999e17fd7f826dee7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备忘录已写入 `artifacts/spatial_analysis_prep.md` 并注册（art_20260515_b9f79e）。

核心发现：

- **当前数据倾向 Scenario C**（obs_only 57.5% > perdof 42.0%），但 obs_only 仅 4/10 tasks，排序可能翻转
- **Scenario B 是最稳健的 fallback**——只要 CRM vs argmin-only ≥5pp 即可支撑，不依赖 variant 排序
- **Magnitude control (norm=1.42→0% vs norm=0.1→42-57.5%)** 在所有 scenario 下都是独立 contribution，建议升级为论文 "second punch"
- **裁决最低数据**: spatial + object 均完成全 10 tasks + Fisher exact test p<0.05
- 预计 May 16 spatial 完成后可初步选择 narrative，May 17-19 锁定

---
