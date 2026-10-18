# analysis accum v3 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_accum_v3_results_20260519T124613_result.json`
- **Structured JSON:** [`ddc6bd29d69bdd991e83.json`](../../sessions/dd/ddc6bd29d69bdd991e83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/accum_v3/accum_v3_results_analysis.md`，registry 已更新为 DONE。

核心结果：

| 指标 | mix50 (50% human) | mix25 (25% human) | Full-replacement | Chance |
|------|-------------------|-------------------|-----------------|--------|
| 4-class acc | 69.1% | **70.1%** | 85.9% | 25% |
| d1-d3 bal acc | 58.9% | **60.3%** | — | 33% |

关键发现：
1. **Accumulation 降低信号 ~16-17pp**（vs full-replacement 85.9%），但远高于 chance（+44pp），信号未被摧毁
2. **mix25 略优于 mix50**（+1.0pp）— 反直觉。更少 human text → 更强 recursive signature → 更容易区分深度
3. **d2 是瓶颈**（~42% recall），在 d1/d3 之间的过渡区被大量混淆
4. **Pythia-1.4B 特征提取已确认**，bug 修复生效
5. 对 Discussion §6：支持 "full-replacement is upper bound" 的 claim，但需修正 "更多 human data → 更好信号" 的假设

---
