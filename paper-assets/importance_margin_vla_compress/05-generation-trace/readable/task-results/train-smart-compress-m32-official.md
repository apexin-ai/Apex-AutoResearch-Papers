# train smart compress m32 official

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m32_official_20260519T015833_result.json`
- **Structured JSON:** [`0cc9e06d3b49f899c1e6.json`](../../sessions/0c/0cc9e06d3b49f899c1e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行中。

**总结：**

1. **下载了 2 个模型**：`HuggingFaceVLA/smolvla_libero` (official checkpoint) 和 `HuggingFaceTB/SmolVLM2-500M-Instruct` (VLM backbone)，通过 hf-mirror.com 绕过直连限制
2. **兼容性验证**：
   - Official 架构差异：expert_width=0.5 (vs 0.75), num_expert_layers=-1 (vs 0), VLM=SmolVLM2-500M-Instruct (vs Video-Instruct)
   - Hidden size 相同 (960)，compressor 完全兼容
   - Trainable params: 119.6M / 627.1M (19.08%)
3. **创建配置** `configs/smart_compress_m32_official.yaml`：继承 base config，覆盖 pretrained 路径指向 official checkpoint
4. **训练已启动**：cqa1-33015 GPU cuda:3, PID=742207
   - Step 0→350, loss 正常（1.29→0.31）, sps=4.1
   - 日志：`logs/train_smart_compress_m32_official.log`
5. **Registry 已更新**：exp_id=`train_smart_compress_m32_official`, status=RUNNING

---
