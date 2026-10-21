# code sampling support implementation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sampling_support_implementation_20260516T192301_result.json`
- **Structured JSON:** [`87b673c716b2ddfdb73b.json`](../../sessions/87/87b673c716b2ddfdb73b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器完全一致。不是 git 仓库所以跳过 commit。

---

**完成。** 修改了 `run_constrained_extraction.py`，改动摘要：

| 位置 | 改动 |
|------|------|
| 第 617-618 行 | 新增 `--temperature` (default=0.0) 和 `--top_p` (default=1.0) CLI 参数 |
| 第 418 行 | `run_single_pass` 签名增加 `sampling_kwargs=None` |
| 第 436-437 行 | `gen_kwargs.update(sampling_kwargs)` 在 logits_processor 之前 |
| 第 466 行 | `run_s2_two_pass` 签名增加 `sampling_kwargs=None` |
| 第 486-487 行 | Pass 1 generate 前 `gen_kwargs_p1.update(sampling_kwargs)` |
| 第 545-546 行 | Pass 2 generate 前 `gen_kwargs_p2.update(sampling_kwargs)` |
| 第 708-710 行 | main() 中构建 `sampling_kwargs` dict（仅 temperature>0 时启用 sampling） |
| 第 723, 729 行 | 调用两个函数时传入 `sampling_kwargs` |

**generate() 完整参数列表**（sampling 模式）：`input_ids`, `attention_mask`, `max_new_tokens`, `do_sample=True`, `temperature`, `top_p`, `logits_processor=[grammar_proc, type_constraint_proc]`

默认行为不变（temperature=0 → greedy, `sampling_kwargs=None`），logits_processor 始终生效。

---
