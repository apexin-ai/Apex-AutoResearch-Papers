# code ctrl contam eval run

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ctrl-contam-eval-run_20260520T184651_result.json`
- **Structured JSON:** [`46e1d68036c5fe5b1eb3.json`](../../sessions/46/46e1d68036c5fe5b1eb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### exp-ctrl-contam-pilot 结果

| Condition | Acc | Acc_seen | Acc_unseen | lz* | Δlz* | Cohen's d | Mem_frac |
|-----------|-----|----------|------------|-----|------|-----------|----------|
| clean_s1 | 0.679 | — | 0.679 | 8.01 | +1.03 | — | — |
| clean_s2 | 0.679 | — | 0.679 | 5.94 | -1.03 | — | — |
| **contam_15** | 0.731 | **0.824** | 0.715 | 3.00 | **-3.97** | **-3.85** | 0.38 |
| **contam_50** | 0.764 | **0.805** | 0.724 | 5.45 | **-1.53** | **-1.48** | 0.29 |

Baseline lz\* mean = 6.98, std = 1.03

**关键发现：**
- 两个 clean 条件 accuracy 几乎一致（0.679），验证了实验稳定性
- **contam_15 的 Δlz\* = -3.97, Cohen's d = -3.85**——极强信号，seen items 的 lz\* 降至 0.45（接近 IRT 预期），而 unseen 仍为 3.13
- contam_50 效应反而弱于 contam_15（d=-1.48 vs -3.85），可能因 50% 污染抬高了整体 θ 估计，使 seen items 的 aberrance 被部分吸收
- memorization fraction: contam_15=0.38, contam_50=0.29，均低于假设的 0.5 阈值——模型记住了约 30-38% 的 seen items 的答案

Registry 和 artifact 已更新。

---
