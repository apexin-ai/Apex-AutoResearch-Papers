# infra exp 050 mistral icl cuda2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp-050-mistral-icl-cuda2_20260518T204914_result.json`
- **Structured JSON:** [`4a8b4a9ed31bc5e48714.json`](../../sessions/4a/4a8b4a9ed31bc5e48714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-050 部署成功，实验正在运行。**

状态：
- **GPU cuda:2**: 97% 利用率，87965/97887 MiB 显存占用
- **进度**: 3/199（刚开始，ETA ~51 min，avg 15.6s/problem）
- 前两题结果：folio_0 SICA=True(✓) SC=True(✓)，folio_1 SICA=Unknown(✓) SC=Unknown(✓)

**需注意两个问题：**

1. **Context length overflow**: 部分问题的 ICL prompt（4415 tokens）+ max_tokens（4096）= 8511 > max-model-len 8192。vLLM 会拒绝这些请求。脚本有 retry 逻辑但如果 prompt 本身超长则无法恢复。
2. **"Empty after stripping thinking" 警告**: Mistral-7B 部分 trace 的 extraction 失败，可能影响 SICA 约束质量。

context length 问题可能需要调低 `--max-tokens`（比如 2048）或提高 `--max-model-len`。是否需要现在干预？

---

**exp-049 状态**: tmux session 不存在，cuda:3 空闲，部署失败。

---
