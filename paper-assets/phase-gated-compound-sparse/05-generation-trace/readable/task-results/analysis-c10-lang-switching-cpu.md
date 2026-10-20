# analysis c10 lang switching cpu

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c10_lang_switching_cpu_20260516T031532_result.json`
- **Structured JSON:** [`b402cd56bb7904d1d0d8.json`](../../sessions/b4/b402cd56bb7904d1d0d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰，JSON 已保存。

## Language Switching Analysis (DS MATH-500, gen_snippet)

| Sparsity | N | CN (switch) | EN | Mixed | Switch Rate | CN Acc | EN Acc |
|----------|---|-------------|-----|-------|-------------|--------|--------|
| dense (0%) | 50 | 0 | 50 | 0 | 0.0% | N/A | 52.0% |
| s015 (15%) | 50 | 2 | 48 | 0 | 4.0% | 0.0% | 37.5% |
| s030 (30%) | 50 | 20 | 30 | 0 | 40.0% | 10.0% | 10.0% |

### 趋势总结

1. **Language switching 随 sparsity 单调递增**：dense 0% → s015 4% → s030 40%。30% sparsity 下近半数响应切换为中文。

2. **中文响应准确率极低**：s030 中文回答仅 10.0% 正确率（2/20），远低于 dense 英文 52%。这表明 language switching 不仅是表面现象，伴随着推理质量严重下降。

3. **英文响应也在劣化**：s015 英文 37.5% → s030 英文 10.0%，说明 sparsity 对英文推理能力也有破坏，但 language switching 是额外的失败模式。

4. **s015 是关键拐点**：仅 2 条中文切换但两条全错，此时英文准确率已从 52% 降至 37.5%。

结果已保存至 `/root/autodl-tmp/pacs/results_c10_lang_cpu.json`。150 样本覆盖 3 个 sparsity 水平（s020/s025 因无 gen_snippet 被排除）。

---
