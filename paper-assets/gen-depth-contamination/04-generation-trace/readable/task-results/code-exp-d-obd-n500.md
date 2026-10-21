# code exp D obd n500

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_obd_n500_20260515T102324_result.json`
- **Structured JSON:** [`6af08e246b8d4e47073a.json`](../../sessions/6a/6af08e246b8d4e47073a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EXP-D 完成。结果：

**OBD-LightGBM 在 N=500 子集上的 5-class accuracy: 45.6% ± 2.4% (95% CI: [39.4%, 51.8%])**

| 方法 | N | 5-class Accuracy |
|------|---|-----------------|
| OBD-LightGBM | 500 | 45.6% ± 2.4% |
| GPT-5.5 | 500 | 33.2% |
| Claude Opus 4.6 | 500 | 33.1% |
| OBD-LightGBM (full) | 25,000 | 45.4% |

注意：之前报告的 38.6% 是 6-class (depths 0-5) 准确率。本次为公平比较使用 5-class (depths 0-4)，与 LLM baseline 一致，得到 full 准确率 45.4%。在匹配样本量 N=500 时，OBD 仍显著高于两个 LLM baseline 约 12 个百分点。

输出已保存至 `artifacts/exp_D_obd_n500.json`，脚本在 `scripts/exp_D_obd_n500.py`。

---
