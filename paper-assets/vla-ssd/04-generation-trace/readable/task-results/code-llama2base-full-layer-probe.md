# code llama2base full layer probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama2base_full_layer_probe_20260517T063130_result.json`
- **Structured JSON:** [`44de1a23659ae0a916fd.json`](../../sessions/44/44de1a23659ae0a916fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Llama2base 全层 profile 结果：

| Layer Range | Accuracy |
|---|---|
| L0 | 10% (chance) |
| L1 | 80.2% |
| L2-L4 | 98.7% → 99.5% |
| L5-L31 | 99.8%-100% (saturated) |

关键发现：llama2base 从 L5 开始就接近饱和（99.9-100%），L9-L31 全部维持在 99.8-100%，没有出现像 untrained 条件那样的衰减。

结果已保存至 `/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/llama2base_full_layer_classification.json`。

---
