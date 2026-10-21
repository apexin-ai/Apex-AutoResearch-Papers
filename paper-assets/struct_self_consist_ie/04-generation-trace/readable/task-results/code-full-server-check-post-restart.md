# code full server check post restart

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full_server_check_post_restart_20260519T125009_result.json`
- **Structured JSON:** [`95260b1a676fd2b16915.json`](../../sessions/95/95260b1a676fd2b16915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Server A (autodl-5090) — 32B QLoRA Training
- **进程**：存活（PIDs 804665-804668，4 GPU 进程）
- **GPU**: 70% / 78% / 100% / 91%，显存 ~29-30 GB / 32 GB
- **Step**: 3659/41180 (8.9%)
- **Loss**: 0.0624 (step 3650), grad_norm: 0.288
- **Checkpoint**: checkpoint-3000 (20:22 保存), checkpoint-2000, checkpoint-1000
- **Speed**: ~2.5s/it, 预计剩余 ~26h

## Server B (autodl-5090-b) — 72B Zero-shot Inference
- **进程**：存活（VLLM Workers PIDs 59314-59317，4 GPU 100%，~31.9 GB / 32 GB）
- **SciERC**: 551 行 ✓ (完成)
- **CoNLL**: 3453 行 ✓ (完成)
- **FewNERD**: 推理中 — 295704/301184 prompts (**98.2%**)
  - 301184 = 37648 instances × 8 samples
  - 剩余 ~5480 prompts，预计几分钟内完成
  - 速度: ~7110 toks/s input, ~1792 toks/s output
- **Signal report**: `full_signal_report.json` 已存在，但仅含 scierc + conll2003 结果（FewNERD 完成前生成的）
- **注意**: FewNERD 输出目录尚未创建，推理完成后会写入。脚本应会自动更新 signal report 包含 FewNERD 结果

## Server C (autodl-5090-c)

### 14B (cuda:0,1)
- **进程**：存活（PIDs 56978-56979，~25.5-25.9 GB）
- **GPU**: 97% / 97%
- **Step**: 6617/41180 (16.1%)
- **Loss**: 0.0604 (step 6600), grad_norm: 0.574
- **Checkpoint**: checkpoint-6000 (20:28), checkpoint-4000, checkpoint-2000
- **Speed**: ~2.2s/it

### 7B (cuda:2,3)
- **进程**：存活（PIDs 72042-72043，~16.7-17.7 GB）
- **GPU**: 93% / 93%
- **Step**: 2000/20590 (9.7%)
- **Loss**: 0.072 (step 2000), grad_norm: 0.528
- **Checkpoint**: 暂无（尚未到第一个保存点）
- **Speed**: ~2.3s/it
- Pipeline 日志显示 1523/2353（pipeline 内部子进度，非训练 step）

---

**总结**: 4 个实验全部存活，状态正常。72B FewNERD 推理 98.2%，几分钟内即将完成。3 个训练任务稳步推进，loss 均在合理下降。

---
