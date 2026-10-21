# ssh plan012 clip download v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan012-clip-download-v2_20260516T011834_result.json`
- **Structured JSON:** [`5f0423b611f161456792.json`](../../sessions/5f/5f0423b611f161456792.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- 权重路径：`/root/vla-ssd/checkpoints/clip-vit-large-patch14/`
- 下载方式：ModelScope（HuggingFace 直连 xet 超时，代理无法解决）
- 验证通过：`CLIPModel` 加载成功，427.6M params，vision hidden size 1024
- 提取脚本用法：`python scripts/extract_features_clip.py --model_path /root/vla-ssd/checkpoints/clip-vit-large-patch14`

---
