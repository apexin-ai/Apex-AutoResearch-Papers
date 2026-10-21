# paper writing method

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260517T001252_result.json`
- **Structured JSON:** [`6deb274f398541bb5bc7.json`](../../sessions/6d/6deb274f398541bb5bc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已写入 `docs/paper/sections/method.tex`，约 1500 words，包含 7 个 subsection。

关键覆盖项：
- CP 定义及 operationalization
- 6 个 metric 的精确数学定义（含 Pre-CP FPR 双定义及差异解释）
- 3 模型 + 架构/规模设计 + OpenThinker 排除理由
- 60/20/20 split（125/41/43），val 用于 threshold tuning
- HS probe: last token hidden state, layer selection = balanced_acc × crossing_rate (scheme B)
- Text baseline: all-MiniLM-L6-v2 (384-d)
- Temporal: window concatenation (W=1..25) + GRU (single/multi-layer, 3 seeds)
- Baselines: BOCPD, CUSUM, Mahalanobis

无 em-dash、无 -ing 结尾、所有缩写首次出现已定义。

---
