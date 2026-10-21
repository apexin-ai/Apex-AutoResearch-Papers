# ops urgent status check westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check-westd_20260518T203200_result.json`
- **Structured JSON:** [`10623b7ea69d8d084551.json`](../../sessions/10/10623b7ea69d8d084551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告 — westd-29999 (2026-05-19 04:32 UTC)

### 1. GPU 状态
4x NVIDIA RTX PRO 6000 (98GB) — **全部满载，0 空闲**

| GPU | PID | VRAM | Util | 任务 |
|-----|-------|------|------|------|
| 0 | 56094 | 63GB | 91% | Qwen2.5-14B_d050_s42 |
| 1 | 49198 | 55GB | 81% | gemma-2-9b_d000_s42 |
| 2 | 53527 | 65GB | 93% | Qwen2.5-14B_d025_s42 |
| 3 | 59313 | 64GB | 99% | Qwen2.5-14B_d100_s42 |

### 2. 14B 训练 — 全部进行中

| 实验 | GPU | 进度 | ETA |
|------|-----|------|-----|
| d025_s42 | 2 | 1483/3384 (44%), epoch=0.43, loss=0.87 | ~1h40m |
| d050_s42 | 0 | 1149/3642 (31%), epoch=0.31, loss=0.85 | ~2h05m |
| d100_s42 | 3 | 91/4159 (2%), epoch=0.02, loss=0.95 | ~3h57m |

三个均无 .done / trainer_state.json / adapter（正常，训练未结束）。alpha=32, lr=5e-5 参数正确。

### 3. Gemma-2-9B pilot — 进行中，即将完成

- **2747/3125 (88%)**, epoch=0.88, loss=1.24, GPU 1
- **ETA ~18分钟**

### 4. Qwen2.5-7B_d050_s123 — 完成 ✓

- exit_code=0, 训练完成于 03:02:58 UTC
- adapter 已保存，**.done 文件缺失**（需要补建）
- tmux session 已退出，PID 46060 残留（无害）

### 5. Phi-4 / OLMo-2 下载 — 失败

| 模型 | shards | 状态 |
|------|--------|------|
| Phi-4 | 5/6 | 不完整，无下载进程 |
| OLMo-2-7B | 5/6 | 不完整，无下载进程 |

**网络不通** — curl huggingface.co 超时。需等网络恢复后重下最后 1 shard。

### 6. S1 信号 — 完成 ✓

- d050_s123: arc_challenge, gsm8k, mmlu ✓
- d100_s123: arc_challenge, gsm8k, mmlu ✓

### 7. tmux sessions — 4 active

`exp_001_sft_14b_d025_s42`, `exp_001_sft_14b_d050_s42`, `exp_001_sft_14b_d100_s42`, `exp_001_sft_gemma2_9b_d000_s42`

---

**需要关注**:
1. **Gemma-2-9B ~18min 后完成** → GPU 1 将释放，可用于下一任务
2. **网络 DOWN** → Phi-4 / OLMo-2 各缺 1 shard，无法继续下载
3. **7B_d050_s123 缺 .done** → 训练正常完成但 .done 标记未写入

---
