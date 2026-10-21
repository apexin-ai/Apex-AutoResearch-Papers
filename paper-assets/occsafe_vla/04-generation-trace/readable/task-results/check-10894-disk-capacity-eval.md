# check 10894 disk capacity eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_10894-disk-capacity-eval_20260527T081626_result.json`
- **Structured JSON:** [`698c9d3db4e31a45abc9.json`](../../sessions/69/698c9d3db4e31a45abc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全了，汇报结论。

## 评估结果

### 磁盘现状
| 指标 | 值 |
|------|-----|
| 总容量 | 250G |
| 已用 | 201G |
| **可用** | **50G** |

### Checkpoint 保存策略（finetune.py:1280-1288）
- `save_freq = 10,000` 步保存一次
- **内置 rotation：保留最新 3 个 checkpoint，超过 3 个自动删除最旧的**
- 单个 checkpoint ≈ **15G**

### 空间推演

**当前两个在跑实验的增长预测**（各自从 2 ckpts → 最终 3 ckpts）：

| 实验 | 当前 | 稳态峰值(3ckpt) | 瞬时峰值(save时4ckpt) | 净增长(稳态) |
|------|------|-----------------|---------------------|-------------|
| full_occ_ln_v2_s1c | 30G | 45G | 60G | +15G |
| full_occ_ln_v2_s2 | 30G | 45G | 60G | +15G |

两个在跑实验还需 +30G（稳态），50G 剩余 → **剩余约 20G**。

**新实验 detach_ln_v2_s0c_r2 的需求**：
- 稳态峰值 = 3 × 15G = **45G**
- 瞬时峰值（4ckpt 未 rotate 时）= **60G**

### 结论：**不安全**

20G 余量跑不了需要 45G 的新实验。即使不考虑新实验，三者同时保存 checkpoint 时瞬时峰值可能触发磁盘满。

**要跑新实验，必须先清理已完成的 checkpoint**。当前可清理的已完成实验共约 **120G**：

| 目录 | 大小 |
|------|------|
| ablation_occ_detach_s3_v2 | 15G |
| cutoff_45k_s2_v2 | 15G |
| detach_ln_s3 | 15G |
| full_occ_ln_s0 | 15G |
| full_occ_ln_s3_v2 | 15G |
| mvp_occ_s3_v2 | 15G |
| reverse_cutoff_s2_v2 | 15G |
| vanilla_v2_s1 | 15G |

清理其中任意 **3 个**（释放 45G）即可安全启动新实验。

---
