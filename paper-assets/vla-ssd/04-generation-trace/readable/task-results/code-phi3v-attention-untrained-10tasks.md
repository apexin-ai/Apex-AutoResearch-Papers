# code phi3v attention untrained 10tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_attention_untrained_10tasks_20260519T225529_result.json`
- **Structured JSON:** [`4a629b2d1e2cf24846c6.json`](../../sessions/4a/4a629b2d1e2cf24846c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE (success)。

**结果摘要**（10 tasks, untrained Phi3V）：

| Layer | n_dom | text | image |
|-------|-------|------|-------|
| L1 | 28/32 | 0.7745 | — |
| L0-L31 | 28-32/32 | ~0.60-0.77 | ~0.25-0.40 |

所有层均匀高 instruction dominance（28-32/32），无层间分化。与 5-task untrained 结果一致。

输出文件：
- `/root/autodl-tmp/vla-ssd/results/attention/phi3v_attention_untrained_10tasks.json`
- `/root/autodl-tmp/vla-ssd/results/attention/full_32layer_phi3v_untrained_10tasks.json`

---
