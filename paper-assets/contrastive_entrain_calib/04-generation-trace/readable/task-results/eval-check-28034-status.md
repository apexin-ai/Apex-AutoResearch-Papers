# eval check 28034 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-28034-status_20260522T123155_result.json`
- **Structured JSON:** [`960966a4c9e60df0778e.json`](../../sessions/96/960966a4c9e60df0778e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | Util | VRAM | 任务 |
|-----|------|------|------|
| 0 | 47% | 16.5/32 GB | ckpt-7500 eval (运行中) |
| 1 | 48% | 16.3/32 GB | exp-002v3-ckpt2000 eval (运行中) |
| 2 | 0% | 空闲 | — |
| 3 | 0% | 空闲 | — |

### Eval 进度
- **ckpt-7500 (exp-003-s2, R3-only seed2)**: 20/362 pairs，刚开始不久（~20:28 打印第一个 progress）。输出目录为空，尚未产出结果。
- **exp-002v3-ckpt2000 (Cosine R1 pre-collapse)**: 140/362 pairs（~39% 完成），速度约 20 pairs/66s。预计还需 ~15 分钟完成。输出目录同样为空。

### Bootstrap AUROC CI (CPU)
正在运行，已有中间结果：
- **Qwen3 5-fold CV Mean AUROC = 0.8269**
- **OOF AUROC = 0.7588 [0.7251, 0.7958]** (95% CI)
- Per-strength: weak=0.6464, medium=0.8371, strong=0.8828
- Full CV bootstrap 进度: 1000/2000 (约 50%)，ETA ~13 min

### ckpt-8000
无 ckpt-8000 相关文件或 eval 结果，GPU 2/3 也未在运行任何任务。

### 磁盘
- 根分区: 8.0/30G (27%)
- 数据盘: 100/350G (29%)
- 均充足。

**结论**: 两个 eval 任务和 bootstrap 分析都在正常运行，exp-002v3-ckpt2000 最先完成（~15min），ckpt-7500 还需更久。GPU 2/3 空闲，可以安排 ckpt-8000 eval 或其他任务。

---
