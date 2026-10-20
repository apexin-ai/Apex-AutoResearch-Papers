# code exp17 mlm fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp17-mlm-fix_20260519T234304_result.json`
- **Structured JSON:** [`2f46a8150bcc0cb2cafc.json`](../../sessions/2f/2f46a8150bcc0cb2cafc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在正常训练。

**根因**: `train_classifier.py` 的 `treatment` mode（line 57）用 `torch.load("model.pt")` 加载 checkpoint，但 `train_deberta_mlm.py` 用 HuggingFace `save_pretrained()` 保存为 `model.safetensors` 格式，文件名不匹配导致 `FileNotFoundError`。

**修复**: 和 exp16 一样，Stage 2 改用 `--mode baseline --model_name &lt;mlm_checkpoint_path>`，通过 `AutoModel.from_pretrained()` 加载（原生支持 safetensors）。

**启动确认**:
- `exp17_mlm_gpu0` (GPU 0): seed42 Stage 2 已跑到 Epoch 14/20 (val_loss=0.0734, acc=0.98)，进展正常
- `exp17_mlm_gpu1` (GPU 1): seed456 Stage 1 MLM 训练中 (Epoch 1)，进展正常

---
