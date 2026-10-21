# extract 16pair d111 direction

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_16pair_d111_direction_20260520T022901_result.json`
- **Structured JSON:** [`59b2881ecf2d0799f9ae.json`](../../sessions/59/59b2881ecf2d0799f9ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成：`artifacts/pythia410m_s42_a100_16pair_d111.md`

结果：
- 10 个唯一 pair（2 canary × 5 downstream），来自 westd-19828 的三个分析文件
- **naive_fwd: 2/10**（ece→perplexity, ece→mauve）
- **diff_fwd: 2/10**（token_entropy→perplexity, ece→perplexity）
- 6/10 distinct 类 pair 的 naive/diff 均为负 lag（canary 信号实际领先 downstream），但按 D111 strict rule (lag>0) 判定为非 forward
- permG_fdr 在 6 个 distinct pair 上显著，mauve/perplexity pair 均不显著
- TY 结果因 d_max 取值不同而分歧较大（leadlag 文件 d_max=2 导致 df_resid=1，8pair 文件 d_max=0/1 更可靠）

---
