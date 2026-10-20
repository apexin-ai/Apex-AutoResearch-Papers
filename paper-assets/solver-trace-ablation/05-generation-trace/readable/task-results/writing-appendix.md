# writing appendix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_appendix_20260514T194249_result.json`
- **Structured JSON:** [`7f999c27b4018c686857.json`](../../sessions/7f/7f999c27b4018c686857.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写好了。`appendix.tex` 包含三个章节：

- **Appendix A (Experimental Setup)**: Table A1 列出所有超参数（Qwen3-4B, GRPO K=8, lr=1e-6, batch=4×2=8, 500/1000 steps, BF16, 3 seeds, FOLIO 500/100, 6 reward conditions）。注明了 s43 sampling eval 的例外。
- **Appendix B (Hacking Mode Definitions)**: 7 种 hacking mode 各有定义、FOL/Prolog 伪代码示例、ISR 交互说明、prevalence 数据。
- **Appendix C (Per-Seed Detailed Results)**: 两张 `table*`（FOL Table A2 + Prolog Table A3），涵盖所有 exp\_id 的 PR/ISR\*/H7/H1/Genuine，含 3-seed mean±std 和脚注说明 Prolog classifier 误导性问题。

`paper.tex` 已添加 `\input{appendix}`。

---
