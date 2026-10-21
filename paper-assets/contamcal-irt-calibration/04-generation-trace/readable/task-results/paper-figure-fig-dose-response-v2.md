# paper figure fig dose response v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_dose_response_v2_20260516T200738_result.json`
- **Structured JSON:** [`184219eeaa587e6b2f78.json`](../../sessions/18/184219eeaa587e6b2f78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成了 `fig_dose_response.pdf` / `.png`，已注册为 `art_20260516_34d427`。

图表要点：
- 1×3 subplots (ARC-Challenge / GSM8K / MMLU)，三个尺度全部实线
- Error bars 为两种子 min-max range；3B GSM8K d005 异常点用空心标记
- 3B GSM8K d000 已排除并标注 SFT degradation；MMLU 0.5B 区域有 position bias 浅红底
- ARC 标注 0.5B forgetting (−17pp) + 1.5B/3B near-immune；GSM8K 标注 3B inflation

---
