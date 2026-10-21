# ops westd 34887 fill c4 ood

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-fill-c4-ood_20260518T084357_result.json`
- **Structured JSON:** [`22ab351bed5dc4c03337.json`](../../sessions/22/22ab351bed5dc4c03337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1** — kl50_s456_eval wikitext2_ppl = **11.8614**，已更新到 registry。

**Step 2 & 3** — 两个 C4 OOD 评估已提交并确认在跑：
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| c4_ood_kl50_s42 | cuda:0 | 12354 | RUNNING |
| c4_ood_kl50_s456 | cuda:1 | 12424 | RUNNING |

注意：路径已修正为 `/root/distill_sparse_swiglu/`（autodl-tmp 下无代码目录）。c4_ood_kl50_s456 的旧 conclusion=killed 未能清除（registry 不支持 null），但状态已推进到 RUNNING。

---
