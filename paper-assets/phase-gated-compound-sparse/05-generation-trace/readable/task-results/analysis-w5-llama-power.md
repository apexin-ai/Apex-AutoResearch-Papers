# analysis w5 llama power

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_llama_power_20260515T130442_result.json`
- **Structured JSON:** [`ae261a3460dc6ee6dd90.json`](../../sessions/ae/ae261a3460dc6ee6dd90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**Phase-gated effect（importance masking）**：power=1.0，n=10 即可检测，n=49 绰绰有余。

**Importance vs random 差异**：d=0.19–0.34（small），n=49 时 power 仅 0.26–0.63，全部欠功效。需 n=72–215 才能达到 80% power。

这为论文中将 LLaMA 结果定位为 "qualitative confirmation of phase-gated pattern" 提供了统计依据：核心的 phase-gated 效应检测力充足，但样本量不足以可靠区分两种 masking 策略的差异。

交付物：
- 服务器 JSON：`analysis_output/w5_llama_power_analysis.json`
- 本地报告：`artifacts/w5_llama_power/report.md`
- 分析脚本：`w5_llama_power_analysis.py`（已含文件头注释）

---
