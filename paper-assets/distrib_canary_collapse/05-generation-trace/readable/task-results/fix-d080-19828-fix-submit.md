# fix d080 19828 fix submit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d080_19828_fix_submit_20260519T001857_result.json`
- **Structured JSON:** [`191e5616606c99b8367f.json`](../../sessions/19/191e5616606c99b8367f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

### D080 执行结果

| 项目 | 结果 |
|------|------|
| **iterative_train.py 修复** | ✅ 2 处 `else None` → `else torch.float32`，md5: `a51bddbed6f1bdf79051283d5238fd19` |
| **scale_14b metrics** | ✅ gen_0→10 完整。token_entropy -24.4%, distinct_3 -49.8%, perplexity +78.6%, mauve -28.2%, ece 0.007→0.153 |
| **SmolLM3 dtype** | `bfloat16` — 不受 D080 bug 影响 |
| **GPT-2m dtype** | config 为 `None`（默认 float32 加载）— 修复后显式传 float32，正确 |
| **GPT-2m 提交** | ✅ PID 407859, tmux session `gen_gpt2m_a100_s43_fp32`, cuda:0 |

**无异常发现。** SmolLM3 在 cuda:1 正常运行（bfloat16 路径不受影响），GPT-2m 已在 cuda:0 启动。

---
