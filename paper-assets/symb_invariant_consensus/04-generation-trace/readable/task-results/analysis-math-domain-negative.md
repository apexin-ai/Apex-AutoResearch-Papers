# analysis math domain negative

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math_domain_negative_20260516T012213_result.json`
- **Structured JSON:** [`2122e4022e54347b4d6d.json`](../../sessions/21/2122e4022e54347b4d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact `art_20260516_778777`，路径：`artifacts/_project/report/math_domain_negative_analysis.md`。

内容覆盖：
- **证据汇总表**：4 个实验的完整数据（题数、温度、multi-candidate rate、SICA-SC gap），所有数字标注 registry exp_id 来源
- **根因分析**：CoT 确定性、temperature 无效（0.7/0.9/1.0 三梯度验证）、MaxSAT exclusion 在单候选下退化为 no-op（exclusion_rate=38.7% 但无法改变结果）
- **方法论含义**：SICA 的价值前提（需要 multi-candidate rate > 0）、数学域作为不适用域的定位、三个解法方向
- **论文价值**：domain boundary analysis 的定位、与 SC 文献的 model calibration 讨论、建议呈现为 §5.3 独立小节

---
