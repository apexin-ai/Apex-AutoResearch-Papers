# fix score quality robustness

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_score-quality-robustness_20260516T104432_result.json`
- **Structured JSON:** [`6f9a073bf313aa20ebae.json`](../../sessions/6f/6f9a073bf313aa20ebae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Quick Probe 已正常启动，正在生成中。

### 总结

1. **score.py 修复内容**：
   - 空/纯空白 response 在送 ArmoRM 前直接赋 0.0 分
   - batch forward 外层加 `try-except (ValueError, RuntimeError)`，失败时 fallback 逐条打分
   - 逐条打分仍失败的样本赋 0.0

2. **ArmoRM tokenizer**：使用 Llama3 chat template（`<|start_header_id|>`, `<|eot_id|>` 等），gating token 依赖 `<|eot_id|>` 存在于 tokenized 序列中

3. **验证通过**：空 response 得分 0.0，正常 response 得分正常（~0.07-0.10）

4. **Quick Probe 已启动**：PID 497183，已加载 2000 prompts，正在生成（16/2000）

---
