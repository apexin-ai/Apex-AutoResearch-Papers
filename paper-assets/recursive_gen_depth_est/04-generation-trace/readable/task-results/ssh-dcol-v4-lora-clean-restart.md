# ssh dcol v4 lora clean restart

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dcol_v4_lora_clean_restart_20260515T022544_result.json`
- **Structured JSON:** [`ab5bc7a37d24b5882b88.json`](../../sessions/ab/ab5bc7a37d24b5882b88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。汇报：

---

## 执行结果

### 1. cuda:1 清理
- 初始清理确认：0MiB，无进程 ✅
- 训练启动后另一个 worker 的 `extract_features.py` (PID 278173) 也在 cuda:1，占 9GB。97GB 显卡不受影响

### 2. LoRA 模块名
- `query_proj`, `key_proj`, `value_proj`（DeBERTa-v3-large 24层 × 3 = 72 个 LoRA adapter）

### 3. Trainable params
- **LoRA**: 2,359,296 (0.54% of backbone 436M)
- **总 trainable**: 2,676,979 (含 head + classifier + margins)

### 4. 显存
- dry-run 峰值: **3.83 GB**
- 实际运行: **4,694 MiB ≈ 4.6 GB** （远低于 15GB 限制）

### 5. PID
- **277577**，tmux session: `dcol_deberta_004`

### 6. 前 100 steps loss

| Step | Loss | CE | CL | Acc | LR |
|------|------|-----|-----|------|-----|
| 20 | 1.9045 | 1.3881 | 0.5164 | 25.6% | 3.05e-06 |
| 40 | 1.9047 | 1.3884 | 0.5163 | 25.6% | 6.10e-06 |
| 60 | 1.9041 | 1.3876 | 0.5165 | 25.7% | 9.15e-06 |
| 80 | 1.9033 | 1.3871 | 0.5162 | 26.2% | 1.22e-05 |
| 100 | 1.9026 | 1.3867 | 0.5159 | 26.5% | 1.52e-05 |

Loss 缓慢下降，无 NaN。当前仍在 warmup 阶段（5% ≈ 197 steps），lr 到达 3e-4 后下降应加速。

### 偏离指定参数的改动
1. **`lora_alpha`: 32 → 16** — alpha=32 (scaling=2.0) 导致 DeBERTa disentangled attention 在 ~5 步后产生 NaN。alpha=16 (scaling=1.0) 稳定
2. **移除 autocast** — DeBERTa-v2 的 `masked_fill(torch.finfo().min)` 与 bf16/fp16 不兼容（overflow），改用 float32。显存仍仅 4.6GB

---
