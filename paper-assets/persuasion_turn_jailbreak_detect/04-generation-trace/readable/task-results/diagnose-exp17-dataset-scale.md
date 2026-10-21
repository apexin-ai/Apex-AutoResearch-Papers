# diagnose exp17 dataset scale

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp17_dataset_scale_20260519T234801_result.json`
- **Structured JSON:** [`f6b695e1c14b3c403e31.json`](../../sessions/f6/f6b695e1c14b3c403e31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/exp17_diagnosis.md`。

**核心结论**：

- **根本原因**：`train_deberta_mlm.py` 保存 HF safetensors 格式，但 `train_classifier.py --mode treatment` 用 `torch.load()` 加载 `model.pt`，格式不匹配导致 MLM Stage2 全部 FileNotFoundError crash。
- **Vanilla 3 seeds**：全部正常完成（val_acc 0.97-0.99）
- **9-class 3 seeds**：通过 resume 完成，但 seed=42 Stage2 结果退化（val_loss=0.0, val_acc=1.0），需审查
- **MLM 3 seeds**：修复脚本已在 GPU 0/1 上运行（改用 `--mode baseline --model_name` 绕过），预计 ~30min 完成
- **W&B**：所有脚本 `WANDB_MODE=disabled`，这是 cron 判定 failed 的直接原因
- **需关注**：fix 脚本用 `--mode baseline` 代替 `--mode treatment`，需确认两种 mode 下 embedding 提取的语义等价性

---
