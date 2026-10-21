# paper 021 appendix table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_021-appendix-table_20260517T234234_result.json`
- **Structured JSON:** [`ce9ecbe0213c4f7add57.json`](../../sessions/ce/ce9ecbe0213c4f7add57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改了两个文件：

1. **`docs/paper/sections/appendix.tex`** (line ~293): 在 "Reframing the intervention target" 段落中，exp_018 讨论之后新增一段 exp_021 的跨环境验证证据。核心内容：Full-SGS 在 Cheetah 上未阻止 CIVO 初始 spike (NVE 9.94x at 45K)，但使 agent 在 ~10K steps 内自修复（sustained NVE 0.34x, eval 221.5 vs 010b 的 51.7），将 SGS 重新定性为 "enables recovery" 而非 "prevents collapse"。

2. **`paper/sections/sgs_informative_negative.md`**: 末尾新增 `\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\_021)}`，总结 021 结果并引用 D088 结论。

完整实验表中 exp_021 行已存在（line 44: `221.5 @105K, Recovery`），无需修改。

---
