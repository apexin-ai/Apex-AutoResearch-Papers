# ssh check progress all

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-progress-all_20260518T222249_result.json`
- **Structured JSON:** [`54968a8adc9b941da047.json`](../../sessions/54/54968a8adc9b941da047.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 占用

| GPU | 进程 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| cuda:0 | 14B d050 s42 (PID 56094) | 63G/98G | 70% | 60°C |
| cuda:1 | Gemma2 d005 s42 (PID 62861) | 54G/98G | 67% | 57°C |
| cuda:2 | lm_eval d025_s42 (PID 71368) | 18G/98G | 0% | 32°C |
| cuda:3 | 14B d100 s42 (PID 59313) | 64G/98G | 59% | 51°C |

### 训练进度

| 实验 | GPU | 进度 | Loss | Token Acc | ETA |
|------|-----|------|------|-----------|-----|
| **14B d050 s42** | 0 | 3362/3642 (**92.3%**) | 0.94 | 0.770 | ~14 min (~06:37) |
| **Gemma2 d005 s42** | 1 | 1844/3177 (**58.0%**) | 1.19 | 0.728 | ~61 min (~07:24) |
| **14B d100 s42** | 3 | 2151/4159 (**51.7%**) | 0.92 | 0.768 | ~110 min (~08:13) |

### Eval (cuda:2) — 全部失败

**根因：网络不通**。`[Errno 101] Network is unreachable`，无法从 HuggingFace Hub 下载 MMLU 数据集。

- d000_s42 — FAILED
- d005_s42 — FAILED
- d005_s123 — FAILED
- d025_s42 — 当前正在运行，**极大概率同样失败**

成功完成数: **0**。没有产出任何 results.json。

### 14B d025 s42 — 训练已完成

- `adapter_model.safetensors` 存在
- lora_alpha=32, lr=5e-5 ✓
- **无 `.done` sentinel 文件**
- `train_config.json` 不含 final_loss / final_eval_accuracy 字段（脚本可能未写入）

### 需要关注

1. **Eval 网络问题需要解决**：MMLU 数据集需要预先下载到本地，或配置离线模式（`HF_DATASETS_OFFLINE=1`），或修复网络连接
2. 14B d050 即将完成（~14min），完成后 cuda:0 可复用
3. d025 缺少 .done 标记和最终指标，需确认训练脚本是否有这个功能

---
