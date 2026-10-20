# code phi3v attention untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_attention_untrained_20260519T174812_result.json`
- **Structured JSON:** [`adad4c522531d1363fdb.json`](../../sessions/ad/adad4c522531d1363fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果总结：

**Phi3V Untrained Attention Profile — 假设被否定**

| | Untrained (base Phi-3-instruct) | Trained (TracVLA-Phi3V) |
|---|---|---|
| L1 dominant heads | **28/32** | 32/32 |
| L1 mean_text_attn | **0.7745** | 0.7348 |

VLA 训练仅增加 4 个 dominant heads (28→32)，mean_text_attn 反而略降。与 OpenVLA 的 0→24 形成鲜明对比。

原因：Phi-3-mini-4k-**instruct** 已经过 instruction tuning，L1 的 instruction-dominant routing 大部分是从 instruction tuning 继承的，不是 VLA 训练学到的。OpenVLA 用的是 Llama-2 **base**（未经 instruction tuning），所以 untrained=0。

脚本：`westd-19183:/root/vla-ssd/scripts/phi3v_attention_profile_untrained.py`
结果：`westd-19183:/root/autodl-tmp/vla-ssd/results/attention/phi3v_untrained_attention_profile.json`
Registry: `phi3v_attention_untrained` → DONE (negative)

---
