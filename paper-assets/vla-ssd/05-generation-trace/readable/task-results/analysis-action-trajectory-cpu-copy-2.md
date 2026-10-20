# analysis action trajectory cpu

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_trajectory_cpu_20260519T184457_result.json`
- **Structured JSON:** [`e4a4b42705fef2ac6ec1.json`](../../sessions/e4/e4a4b42705fef2ac6ec1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**Temporal Coherence**
- Instruction ablation 的 per-dim CV 显著低于 control（1.298 vs 2.744, Wilcoxon p=0.016），说明 instruction head ablation 造成的扰动更系统化/结构化
- Demo-level lag-1 autocorrelation：instruction = -0.201, control = 0.026，但 Mann-Whitney 检验不显著（p=0.42），因为 n=5 per group 统计力不足
- 原始逐步 action 数据未保存，无法计算真正的 step-to-step autocorrelation

**Per-Head Effect Size Bootstrap (B=1000)**
- Instruction heads: per-head d = 0.027, 95% CI [0.023, 0.030]
- Control heads: per-head d = 0.051, 95% CI [0.040, 0.057]
- **CI 不重叠**，差异 CI [0.017, 0.028] 排除零
- Control heads 每头贡献 1.87x 更大的 action disruption，但 instruction heads 通过集体效应（24 vs 8 heads）实现更大总效应

输出文件：`/root/autodl-tmp/vla-ssd/results/action_trajectory_cpu_analysis.json`

---
