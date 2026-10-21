# paper p1c instruct writeup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1c-instruct-writeup_20260515T175016_result.json`
- **Structured JSON:** [`9a54da882647686e5dda.json`](../../sessions/9a/9a54da882647686e5dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更内容：

**discussion.tex** — 新增 `\paragraph{Instruct tuning degrades depth signal.}` (3句)：
- OLMo-2-1B-Instruct LOGO F1=0.338 vs base 0.763；Qwen3-0.6B chat F1=0.667 vs base 0.816
- 推测 instruct tuning 改变 token 分布使 depth features 失效，机制待明确
- 以此 justify scope 限定为 base model

**limitations.tex** — 第一段补充了 OLMo instruct 和 Qwen3 chat 的具体 F1 数值及 length confound 问题，替换了原来纯定性的表述。

两个文件已同步到 `docs/paper/`。未在 results 主文中添加内容，未使用 "inverted DDR"/"significantly" 措辞。

---
