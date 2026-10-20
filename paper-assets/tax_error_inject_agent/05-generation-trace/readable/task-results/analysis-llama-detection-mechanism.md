# analysis llama detection mechanism

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-detection-mechanism_20260516T091859_result.json`
- **Structured JSON:** [`d3bed77ac6670c32d6ab.json`](../../sessions/d3/d3bed77ac6670c32d6ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**Detection 指标不可信，不应作为论文 contribution。**

1. **LLaMA 的 38 个 "detection" 全部是假阳性** — 100% 仅匹配 "go back"（ALFWorld 正常导航用语），没有一个真正表达了错误意识（如 wrong/error/strange/missing）
2. **Qwen detection=0% 是评估 artifact** — `recovery.py:227` 传入 `enable_thinking=False`，Qwen3 不生成 `&lt;think>` 文本，heuristic 无词可匹配。与检测能力无关
3. **LLaMA vs Qwen 差异完全由输出格式决定** — LLaMA 遵循 prompt 生成 `&lt;think>` 标签 → 导航语言被误匹配；Qwen 跳过 `&lt;think>` → 永远不触发

建议从论文中移除 detection_rate，聚焦 recovery rate 作为核心指标。

---
