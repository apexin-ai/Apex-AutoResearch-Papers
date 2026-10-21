# ops gpu audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit_20260514T003001_result.json`
- **Structured JSON:** [`41fbc3d9a37613996ba7.json`](../../sessions/41/41fbc3d9a37613996ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 巡检结果

### GPU 全景

| GPU | 进程 | 显存 | 利用率 | 状态 | ETA |
|-----|------|------|--------|------|-----|
| 0 | PID 235243 — sft_d100_05B | 22.0/24.6 GB | 94% | SFT 训练 73% (3031/4159) | ~19 min |
| 1 | PID 229370 — eval_05B_d000_s42 | 3.7/24.6 GB | 33% | GSM8K 76% (1006/1319) | ~28 min |
| 2 | PID 229516 — eval_05B_d000_s123 | 3.7/24.6 GB | 33% | GSM8K 73% (965/1319) | ~33 min |
| 3 | PID 242581 — eval_3B_d000_s123 | 9.0/24.6 GB | 65% | GSM8K 3% (44/1319) | ~2h44m |
| 4 | PID 243290 — eval_15B_d000_s42_v2 | 5.8/24.6 GB | 50% | GSM8K 2% (31/1319) | ~2h11m |
| 5 | PID 239729 — sft_d005_05B_v3 | 22.0/24.6 GB | 49% | SFT 训练 59% (1860/3177) | ~23 min |

所有 6 个 PID 存活，无异常。

---

### 已完成 SFT 最终指标

| 任务 | train_loss | token_accuracy | 耗时 | 退出码 |
|------|-----------|----------------|------|--------|
| sft_0pct_3B_s123 | **1.131** | 0.751 | 3.6h | 0 |
| sft_0pct_15B_s123 | **1.260** | 0.731 | 1.7h | 0 |
| sft_0pct_05B_s123 | **1.539** | 0.676 | 55min | 0 |

---

### 正在运行的 Eval 已出结果

| 任务 | MMLU Acc | GSM8K 进度 |
|------|----------|------------|
| eval_3B_d000_s123 | **0.6362** (8933/14042) | 3% — 刚开始 |
| eval_15B_d000_s42_v2 | **0.5753** (8079/14042) | 2% — 刚开始 |
| eval_05B_d000_s42 | (已完成,日志截断) | 76% |
| eval_05B_d000_s123 | (已完成,日志截断) | 73% |

---

### 进行中 SFT 当前 loss

| 任务 | 当前 loss | epoch | 进度 |
|------|----------|-------|------|
| sft_d100_05B | ~1.53 | 0.67 | 73% |
| sft_d005_05B_v3 | ~1.53 | 0.50 | 59% |

---

### MMLU Paraphrase

**无进程运行，无输出文件。** 两个路径 (`/root/autodl-tmp/exp001/paraphrase_data/` 和 `/root/contamcal-irt-calibration/exp001/paraphrase_data/`) 均未找到 `mmlu_paraphrases*.json`。

---

### 异常/注意事项

1. **HuggingFace 连接超时**: GPU 1/2 的 eval 进程启动时遇到大量 HF 超时（gsm8k 数据集下载），最终通过重试恢复。GPU 3/4 启动时加了 `network_turbo` 避免了此问题。
2. **bitsandbytes 警告**: GPU 3/4 的 eval 进程报 `libnvJitLink.so.13` 缺失，属非致命错误，不影响评估。
3. **Paraphrase 未启动**: GPU 0 当前被 sft_d100_05B 占满（94%），无 paraphrase 进程。

---
