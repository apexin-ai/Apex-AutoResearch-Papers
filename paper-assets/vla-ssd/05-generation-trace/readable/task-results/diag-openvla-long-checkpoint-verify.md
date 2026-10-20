# diag openvla long checkpoint verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_openvla_long_checkpoint_verify_20260521T164207_result.json`
- **Structured JSON:** [`1cbebb0354f1f3a57ec0.json`](../../sessions/1c/1cbebb0354f1f3a57ec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：Checkpoint 正确

日志第 4 行明确记录：

```
[23:37:59] Checkpoint: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10
```

**脚本配置和实际加载都是 OFT checkpoint (`openvla-7b-oft-finetuned-libero-10`)，没有用错。**

对比三个 suite 的 trained checkpoint：

| Suite | TRAINED_CKPT |
|-------|-------------|
| Long | `openvla-7b-oft-finetuned-libero-10` (OFT) |
| Object | `openvla-7b-finetuned-libero-object` |
| Goal | （脚本不存在，可能命名不同） |

Long suite 的 L1 attention 只有 14/32 instruction-dominant 不是 checkpoint 错误导致的，需要从其他角度解释（如 long-horizon 任务本身的特性）。

---
