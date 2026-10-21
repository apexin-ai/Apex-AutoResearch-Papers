# ssh fewrel 80rel diagnosis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-80rel-diagnosis_20260515T130210_result.json`
- **Structured JSON:** [`4bf17c84e455e2d95521.json`](../../sessions/4b/4bf17c84e455e2d95521.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp1 共 110 个 batch，已完成 93 个（84%）。分布：
- count_1 × 80 ✓
- count_4 × 5 ✓  
- count_8 × 5 ✓
- count_16: 3/? 进行中
- 剩余：count_32, count_64, count_80

还剩 17 个 batch（含更大的 batch），exp1 预计几分钟内完成。之后还有 exp2。

**诊断结论**：
- **PID 267149 存活**，已运行约 5.5 分钟，状态 `Ss+`（正常）
- **实验正在运行** exp1 阶段的 LLM 推理，当前处理 count_16 batch
- **exp1 进度 84%**（93/110 batch），BCS 值随 type 数量增加呈上升趋势（1-type: 0.0, 4-type: 0.54-0.78, 8-type: 0.67-0.75, 16-type: 0.75-0.84）
- exp1 完成后会自动启动 exp2
- Registry 显示 QUEUED 是状态更新问题，实际已在正常运行
- 输出目录：`artifacts/fewrel_formal_full/`（不是 `fewrel_formal_80rel`）

---
