# knowledge paper framing prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper_framing_prep_20260515T184035_result.json`
- **Structured JSON:** [`0b89638ec022b2c441e2.json`](../../sessions/0b/0b89638ec022b2c441e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。v2.2 → v2.3，以下是具体变更：

**[UPDATED 2026-05-15] 标记的变更点：**

1. **Claim 1 - Seed robustness**: 将原有文字描述替换为完整的 3-seed 表格（含 95% CI [99.58, 100]），更直观。新增 DeepSeek epoch1=99.83% 与 Qwen 完全一致的独立段落。

2. **Claim 3 - Calibration 完整表格**: 新增 4-condition calibration 表（ECE + Brier），关键对比：
   - exception_only: ECE=0.003, Brier=0.001
   - no_trace: ECE=0.171, Brier=0.197（57x / 197x gap）
   - 新增解读：no_trace 不仅 accuracy 低，且对错误预测过度自信

3. **Story Arc step 4**: 加入 seed robustness + calibration 双重确认。

4. **Venue Fit Risks**: 新增 Calibration 行。

5. **Reviewer Concerns**: 更新 "saturated" 回应（加入 Brier 数据和 no_trace 对比），新增 "calibration 只有 1 seed" 的预防性回应。

6. **Discussion D6 (新增)**: Calibration as secondary evidence — Brier score 提供独立于 accuracy 的 evidence dimension。

7. **v1 对比表**: 新增 Calibration 行。

Story arc 无需调整，seed robustness 和 calibration 都是 strengthening evidence，不改变核心 narrative。

---
