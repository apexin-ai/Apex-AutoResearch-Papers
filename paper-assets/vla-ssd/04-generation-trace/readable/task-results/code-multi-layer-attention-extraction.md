# code multi layer attention extraction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_layer_attention_extraction_20260517T063232_result.json`
- **Structured JSON:** [`7ee1939581963de4a7e1.json`](../../sessions/7e/7ee1939581963de4a7e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。结果摘要：

## 多层 Attention Distribution 结果

| Condition | Layer | n_text_dominant | n_image_dominant | n_bos_dominant | mean_text | mean_image | mean_bos |
|-----------|-------|-----------------|------------------|----------------|-----------|------------|----------|
| **trained** | L8 | 4/32 | 0/32 | 21/32 | 0.4678 | 0.0315 | 0.5009 |
| **trained** | L16 | 10/32 | 1/32 | 12/32 | 0.4840 | 0.1053 | 0.4107 |
| **trained** | L31 | **19/32** | 1/32 | 3/32 | **0.5628** | 0.1333 | 0.3039 |
| **untrained** | L8 | 0/32 | **32/32** | 0/32 | 0.0790 | **0.9138** | 0.0072 |
| **untrained** | L16 | 0/32 | **32/32** | 0/32 | 0.0918 | **0.9015** | 0.0067 |
| **untrained** | L31 | 0/32 | **32/32** | 0/32 | 0.0757 | **0.9183** | 0.0059 |
| **llama2base** | L8 | 8/32 | 0/32 | 10/32 | 0.4878 | 0.0344 | 0.4779 |
| **llama2base** | L16 | **25/32** | 0/32 | 7/32 | **0.6017** | 0.0335 | 0.3648 |
| **llama2base** | L31 | 8/32 | 0/32 | 20/32 | 0.3485 | 0.0716 | 0.5800 |

关键发现：

1. **Trained model**: instruction attention 随层深递增（L8→L16→L31: 4→10→19 heads dominant），最终层 L31 有 19/32 heads 以 instruction 为主导，mean_text=0.56
2. **Untrained (random)**: 所有层所有 32 heads 都是 image-dominant（~91% attention to image），text 几乎为零——无任何 language grounding
3. **Llama2base**: L16 表现出最强 text attention（25/32 heads, mean=0.60），但 L31 反而回退到 BOS dominant（20/32 heads）——说明 Llama-2 base 有一定的 text processing 能力但 pattern 不同于 trained model

结果已保存至 `/root/autodl-tmp/vla-ssd/results/attention/multi_layer_attention_summary.json`。

---
