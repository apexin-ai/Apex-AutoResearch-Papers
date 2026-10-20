# analysis text ablation check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_text-ablation-check_20260521T064051_result.json`
- **Structured JSON:** [`d312ceef3503e3991497.json`](../../sessions/d3/d312ceef3503e3991497.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成，registry 已更新为 DONE，cron 已清除。

## T_ext Ablation 结果汇总

| T_ext | SICA Acc (%) | SC Acc (%) | Δ vs SC (pp) | McNemar p | #Constraints |
|-------|-------------|-----------|-------------|-----------|-------------|
| 0.1   | 57.35       | 55.88     | **+1.47**   | 0.5811    | 69.3        |
| **0.3** | **59.31** | 54.41     | **+4.90**   | **0.0129** | 68.8       |
| 0.5   | 56.37       | 55.88     | +0.49       | 1.0000    | 68.2        |
| 0.7   | 53.43       | 55.88     | -2.45       | 0.3018    | 67.3        |
| 1.0   | 55.39       | 55.88     | -0.49       | 1.0000    | 65.2        |

**关键发现**：
- **T_ext=0.3 是最优值**，SICA 59.31%，比 SC +4.9pp，McNemar p=0.013（显著）
- 低温（0.1）有小幅提升但不显著；高温（0.7, 1.0）反而略降
- 约束数量随 T_ext 升高而减少（69.3→65.2），高温提取更发散导致去重后约束更少
- 假设"T_ext 不影响 SICA"被推翻——温度确实显著影响效果，低温提取更一致的约束有利于共识

---
