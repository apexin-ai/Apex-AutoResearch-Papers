# ops verify 05b in mmlu irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_05b_in_mmlu_irt_20260517T062653_result.json`
- **Structured JSON:** [`280a332cc2751e82772b.json`](../../sessions/28/280a332cc2751e82772b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论确凿。** 全部 8 个 0.5B 模型都有严重 position bias：

| Model | Acc | A-rate |
|-------|-----|--------|
| d000_s123 | 42.2% | 36.7% |
| d000_s42 | 39.8% | 46.2% |
| d005_s123 | 30.0% | **81.2%** |
| d005_s42 | 32.5% | **65.1%** |
| d025_s123 | 34.7% | **64.7%** |
| d025_s42 | 28.0% | **79.8%** |
| d100_s123 | 30.6% | **71.2%** |
| d100_s42 | 23.3% | **98.3%** |

正常分布应是 ~25% per option。0.5B 的 A-rate 从 37% 到 98%，严重违反 IRT 假设。

最终回答：

1. **Stan 输入中 0.5B 是 aligned 版本吗？** → YES，但 "aligned" 仅指 prompt 格式（"The answer is X."），**不是 position bias 修正**。
2. **0.5B aligned 在 MMLU 上的 accuracy/A-rate 是否正常？** → **完全不正常**。A-rate 范围 37%-98%（正常应 ~25%）。6/8 个模型 A-rate > 64%，其中 d100_s42 达 98.3%（几乎只输出 A）。Accuracy 23-42% 看似合理但完全由 position bias 驱动。
3. **MMLU domain IRT 真的包含 0.5B 吗？** → **YES，J=21 包含全部 8 个 0.5B**（0.5B×8 + 1.5B×8 + 3B×5）。论文说 "exclude 0.5B from MMLU IRT" 与实际数据矛盾。这些带有严重 position bias 的模型进入了 IRT 拟合，会污染 item parameter 估计（把 gold=A 的 item 误判为容易、gold≠A 的误判为难）。

---
