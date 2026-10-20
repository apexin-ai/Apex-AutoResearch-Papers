# ops d050 verify and relay

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d050-verify-and-relay_20260518T163003_result.json`
- **Structured JSON:** [`aa546ec43dc98566b6ad.json`](../../sessions/aa/aa546ec43dc98566b6ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 任务 1：exp_001_sft_7b_d050_s42 — **成功完成**

| 项目 | 值 |
|---|---|
| 状态 | 3642/3642 steps，"Training complete." |
| 完成时间 | 2026-05-19 00:24:19 |
| 训练时长 | 1h39m (5941s) |
| 最终 train_loss | 0.9599 |
| 最终 mean_token_accuracy | 0.7641 |
| 最后一个 log batch | loss=0.9376, token_acc=0.7748 |
| adapter_model.safetensors | 154MB ✓ |
| lora_alpha | 32 ✓ |
| tokenizer | 存在 ✓ |
| checkpoint 路径 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s42/lora_adapter/` |

### 任务 2：exp_001_sft_7b_d025_s123 — **已启动**

| 项目 | 值 |
|---|---|
| 主进程 PID | 42743 |
| GPU | cuda:1, 40589MiB 占用, 98% util |
| 数据 | sft_dosage_025.jsonl, 54133 samples |
| 日志 | `/root/autodl-tmp/logs/train_7b_d025_s123.log` |
| Registry | RUNNING，已注册 |

预计训练时长约 1.5h（参考 d050 的 3642 steps / 1h39m，d025 数据量略少）。

---
