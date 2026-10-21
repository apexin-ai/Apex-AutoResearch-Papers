# code libero finetuned attention

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_finetuned_attention_20260519T071437_result.json`
- **Structured JSON:** [`e0324bd7e6562aaed2ca.json`](../../sessions/e0/e0324bd7e6562aaed2ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**L1 bookend attention 4 条件比较：**

| Condition | Instruction-dominant heads (/32) | Mean text attn |
|---|---|---|
| untrained | 0 | 0.0778 |
| llama2base | 9 | 0.3627 |
| openvla7b | 24 | 0.5729 |
| **libero_finetuned** | **22** | **0.5686** |

LIBERO-Goal fine-tuning基本保持了 L1 bookend pattern（22/32 vs 24/32，text_attn 0.5686 vs 0.5729）。4 条件形成单调训练轨迹：untrained → llama2base → openvla7b ≈ libero_finetuned。

**输出文件：**
- 完整结果：`/root/autodl-tmp/vla-ssd/results/libero_finetuned_attention_profile.json`
- 兼容格式：`/root/autodl-tmp/vla-ssd/results/attention/full_32layer_libero_finetuned.json`
- 日志：`/root/autodl-tmp/vla-ssd/results/libero_finetuned_attention.log`

Registry 已更新为 DONE(success)，artifact 已注册。

---
