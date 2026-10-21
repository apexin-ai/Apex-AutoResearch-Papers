# ops cwm eval status check v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-eval-status-check-v2_20260524T020231_result.json`
- **Structured JSON:** [`5ef091b8728d130ba3c6.json`](../../sessions/5e/5ef091b8728d130ba3c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态（4 张 5090 全部在跑，87-92% 利用率）

| GPU | PID | 任务 | VRAM | 进度 | Running Acc |
|-----|-----|------|------|------|-------------|
| 0 | 309505 | s456 ckpt300 reeval | 21.1/32.6 GB | 4280/9784 (43.7%) | **~66.2%** |
| 1 | 312223 | s42 ckpt300 reeval | 21.1/32.6 GB | 2776/9784 (28.4%) | **68.95%** |
| 2 | 309866 | s123 ckpt300 reeval | 21.6/32.6 GB | 4120/9784 (42.1%) | **~64.3%** |
| 3 | 272025 | s42 ckpt6100 test | 27.9/32.6 GB | 9640/9784 (**98.5%**) | **69.52%** |

### ckpt6100 eval（GPU 3）— 即将完成

- 剩余 144 样本，预计 ~15 分钟内完成（~10:20 CST / 02:20 UTC）
- 使用 `--max_seq_length 4096`（注意：比 ckpt300 reeval 的 2048 长）
- Running accuracy: 6702/9640 = **69.52%**

### ckpt300 × 3 seeds 预计完成时间

- s456 (GPU 0): ~7-8h → ~17:40 CST
- s42 (GPU 1): ~13h → ~23:00 CST（最慢，起步晚）
- s123 (GPU 2): ~8h → ~18:10 CST

### Table 2 核对

已完成的 Qwen3-8B CWM ckpt6100 per-test accuracy：

| Seed | Accuracy | 来源 |
|------|----------|------|
| s123 | 67.33% (6588/9784) | `qwen3_8b_cwm_repo_s123_eval` ✅ |
| s456 | 66.93% (6548/9784) | `qwen3_8b_cwm_repo_s456_eval` ✅ |
| s42 | **69.52%** (6702/9640) | `cwm_8b_ckpt6100_test` 🔄 98.5% |

- **Table 2 当前值**: 66.48 ± 1.15
- **新 3-seed 均值** (s42 完成后): (67.33 + 66.93 + 69.52) / 3 ≈ **67.93 ± 1.37**
- **偏差**: 均值上升 +1.45pp

⚠️ **注意**: 当前跑的 ckpt6100 eval 用了 `--max_seq_length 4096`，而已完成的 s123/s456 eval 的 seq_length 未知。如果它们用的是 2048，则 s42 的 69.52% 不可直接与 s123/s456 比较——seq_length 不同会引入系统性偏差。需要确认之前 s123/s456 eval 的 seq_length 参数。

---
