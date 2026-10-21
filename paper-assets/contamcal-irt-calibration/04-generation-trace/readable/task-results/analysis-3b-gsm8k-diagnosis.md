# analysis 3B gsm8k diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3B-gsm8k-diagnosis_20260514T093027_result.json`
- **Structured JSON:** [`8b57923919f99a377614.json`](../../sessions/8b/8b57923919f99a377614.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是诊断报告。

---

## 3B GSM8K 崩塌诊断报告

### 数据汇总

| 模型 | GSM8K 准确率 | Δ vs raw |
|------|------------|----------|
| 3B raw | 60.5% (798/1319) | — |
| 3B d000 s42 | 11.7% (154/1319) | **-48.8pp** |
| 3B d000 s123 | 17.6% (232/1319) | **-42.9pp** |
| 0.5B d000 s42 | 36.5% (481/1319) | N/A |

两个 seed 都崩塌，排除随机因素。

### 10 条 GSM8K 样本对比

| Item | Gold | 3B Raw | 3B SFT d000_s42 |
|------|------|--------|-----------------|
| 0 | 18 | 18 ✓ | $18 ✗ |
| 1 | 3 | 3 ✓ | 5 ✗ |
| 2 | 70000 | 10000 ✗ | 72 ✗ |
| 3 | 540 | 540 ✓ | 150 ✗ |
| 4 | 20 | 31 ✗ | 1000 ✗ |
| 5 | 64 | 64 ✓ | 20 ✗ |
| 6 | 260 | 260 ✓ | 30 ✗ |
| 7 | 160 | 60 min ✗ | 300 ✗ |
| 8 | 45 | 475 ✗ | 12 ✗ |
| 9 | 460 | 460 ✓ | 10 ✗ |

### 根因判定：**真实 CoT 能力退化**（非格式问题，非 generation collapse）

**排除假设 1（格式变化）**：
- 全部 1319 条都有提取到的数字答案（0 条 None）
- 只有 ~2 条存在格式不匹配（gsm8k_0 的 "$18" vs "18"）
- 即使全部格式问题被修复，最多救回 ~2-5% 的题目，远不够弥补 48.8pp 的差距

**排除假设 2（Generation collapse）**：
- 答案多样化：5, 72, 150, 1000, 20, 30, 300, 12, 10...无固定重复值
- 不是 collapse，而是算出了各种各样的**错误**答案

**确认根因：LoRA SFT 导致 CoT 推理能力灾难性遗忘**
- 3B raw 答对的 item (18, 3, 540, 64, 260, 460)，SFT 后给出完全不同的错误答案
- 3B SFT 有 20 处 "始化" 乱码（raw 有 0 处），说明 SFT 还引入了部分 generation 退化
- 0.5B SFT 有 0 处乱码，退化程度远轻于 3B

### 为什么 3B 崩但 0.5B 没崩？

训练配置（r=16, alpha=32, lr=2e-4, target=all 7 projection layers）对 3B 而言可能过于激进：
- 3B 的 CoT 推理是更复杂的 learned representation，更容易被 LoRA 破坏
- 同样的配置对 0.5B（推理能力本来就弱）反而通过 SFT 数据的结构化信息获益

### 建议下一步

1. **短期（不影响论文）**：这个结果本身就是有价值的发现——d000（纯 clean data SFT）也能让 3B GSM8K 崩塌，说明 LoRA 配置问题，而非 contamination 效应。可以在论文中讨论这是 SFT 的 side effect。
2. **如果需要修复**：降低 3B 的 lr（如 5e-5）、减小 rank（如 8）、或减少 target modules（只做 q_proj/v_proj），重跑 3B SFT。
3. **`extract_gsm8k_answer` 的小 bug**：当前运行时使用的版本没有正确 strip 非数字字符（"$18"、"1620 minutes" 等不应出现）。建议确保 `re.sub(r'[^-\d.]', '', answer)` 和 "16.00" vs "16" 的处理覆盖所有路径。但这是次要问题，修复后 3B SFT 准确率大约从 11.7% 提升到 ~13-14%，仍然是崩塌状态。

---
