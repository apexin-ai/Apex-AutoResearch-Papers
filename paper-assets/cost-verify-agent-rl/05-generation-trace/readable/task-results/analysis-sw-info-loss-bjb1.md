# analysis sw info loss bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sw_info_loss_bjb1_20260520T190842_result.json`
- **Structured JSON:** [`1a9957df91dd4bfcff63.json`](../../sessions/1a/1a9957df91dd4bfcff63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B run found. Both conditions completed. Here are the results:

## 结果摘要
- **Full context success rate**: 34.8% (31/89)
- **h=2 success rate**: 4.5% (4/89)
- **Delta**: **30.3 pp** (34.8% → 4.5%)
- **Episodes completed**: 89 full / 89 h=2 (identify-life-stages-2 只有 2 variations，所以总数 89 而非 90)
- **W&B run**: N/A
- **AvgScore**: full=26.7, h=2=17.4
- **Runtime**: full=5932s (66.7s/ep), h=2=2770s (31.1s/ep)

## Per-task breakdown

| Task | Full Rate | h=2 Rate | Delta |
|------|-----------|----------|-------|
| boil | 33.3% | 0.0% | -33.3 |
| change-the-state-of-matter-of | 66.7% | 0.0% | -66.7 |
| chemistry-mix | 33.3% | 0.0% | -33.3 |
| chemistry-mix-paint-secondary-color | 0.0% | 0.0% | 0 |
| chemistry-mix-paint-tertiary-color | 0.0% | 0.0% | 0 |
| find-animal | **100.0%** | 0.0% | **-100** |
| find-living-thing | **100.0%** | 0.0% | **-100** |
| find-non-living-thing | **100.0%** | **66.7%** | -33.3 |
| find-plant | 0.0% | 0.0% | 0 |
| freeze | 0.0% | 0.0% | 0 |
| grow-fruit | 0.0% | 0.0% | 0 |
| grow-plant | 0.0% | 0.0% | 0 |
| identify-life-stages-1 | 33.3% | 0.0% | -33.3 |
| identify-life-stages-2 | 0.0% | 0.0% | 0 |
| inclined-plane-determine-angle | 33.3% | 0.0% | -33.3 |
| inclined-plane-friction-named | 0.0% | 0.0% | 0 |
| inclined-plane-friction-unnamed | 66.7% | 0.0% | -66.7 |
| lifespan-longest-lived | 66.7% | 33.3% | -33.3 |
| lifespan-longest+shortest | **100.0%** | 0.0% | **-100** |
| lifespan-shortest-lived | 66.7% | 33.3% | -33.3 |
| measure-melting-known | 33.3% | 0.0% | -33.3 |
| measure-melting-unknown | 33.3% | 0.0% | -33.3 |
| melt | 0.0% | 0.0% | 0 |
| mendelian-genetics-known | 33.3% | 0.0% | -33.3 |
| mendelian-genetics-unknown | 33.3% | 0.0% | -33.3 |
| power-component | 66.7% | 0.0% | -66.7 |
| power-component-renewable | 0.0% | 0.0% | 0 |
| test-conductivity | 33.3% | 0.0% | -33.3 |
| test-conductivity-unknown | 0.0% | 0.0% | 0 |
| use-thermometer | 0.0% | 0.0% | 0 |

h=2 仅解决了 4 个 episode：find-non-living-thing ×2, lifespan-longest-lived ×1, lifespan-shortest-lived ×1。这些都是相对简单的分类/查找任务。

## Conclusion: **success**
## Reasoning: h=2 windowing 导致 success rate 从 34.8% 暴跌至 4.5%（-30.3 pp），hypothesis confirmed——step-independent 训练下的信息丢失在 ScienceWorld 上同样严重。尤其是 find-animal/find-living-thing/lifespan-longest+shortest 三个 full context 下 100% 的任务在 h=2 下直接归零，说明这些任务强依赖历史 context。

## 与 ALFWorld info loss 对比
日志中无 ALFWorld 参考数据。需从其他实验日志或 memory.md 中获取 ALFWorld 的 info loss 数据进行对比。

---
