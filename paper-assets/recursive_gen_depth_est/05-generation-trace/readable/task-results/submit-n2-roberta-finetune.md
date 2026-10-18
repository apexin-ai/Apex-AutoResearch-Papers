# submit n2 roberta finetune

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_n2_roberta_finetune_20260515T121826_result.json`
- **Structured JSON:** [`dad796d0a97d27e3f98f.json`](../../sessions/da/dad796d0a97d27e3f98f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，loss 稳步下降。

**完成总结：**
- `n2_roberta_finetune_001` 已在 gpu-6000pro-2 的 cuda:1 上启动（PID 235750）
- 首次提交因 model.safetensors 文件损坏失败，已通过 hf-mirror 重新下载完整模型（476MB）后重新提交
- 超参数与 DeBERTa 完全一致：epochs=3, batch_size=16, lr=2e-5, max_len=512, 5-fold CV, seed=42
- Fold 1 训练中，step 400/1000，loss 从 1.44 降至 ~0.84
- 5-fold × 3 epochs 预计总时间 ~2-3 小时

---
