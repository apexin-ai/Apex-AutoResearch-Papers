# code phi3v attention profile

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_attention_profile_20260519T174425_result.json`
- **Structured JSON:** [`25048b96e262330acd8f.json`](../../sessions/25/25048b96e262330acd8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**TracVLA-Phi3V Attention Profile (5 LIBERO-Goal tasks, 32 layers × 32 heads)**

| 层段 | instruction-dominant heads | mean text attn | 模式 |
|------|--------------------------|----------------|------|
| L0 | 3/32 | 0.2249 | image-dominant |
| **L1** | **32/32** | **0.7348** | **全 text-dominant** |
| **L2** | **32/32** | **0.7807** | **全 text-dominant** |
| L3-L8 | 0-3/32 | 0.27-0.35 | image-dominant |
| L9-L28 | 3-12/32 | 0.33-0.49 | 渐进回升 |
| L29-L31 | 17-18/32 | 0.52-0.65 | text-dominant 回升 |

注意：实际 image tokens = 313（Phi3V 动态分辨率），非预期的 144。

JSON 输出已保存至 `westd-19183:/root/autodl-tmp/vla-ssd/results/attention/phi3v_attention_profile.json`，registry 已更新为 DONE。

---
