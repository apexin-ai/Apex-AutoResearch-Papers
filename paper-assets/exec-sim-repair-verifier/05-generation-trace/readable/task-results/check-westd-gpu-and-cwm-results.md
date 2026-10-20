# check westd gpu and cwm results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-gpu-and-cwm-results_20260514T172510_result.json`
- **Structured JSON:** [`8e47586a10bb40411ad4.json`](../../sessions/8e/8e47586a10bb40411ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总报告：

---

## Part 1: GPU 状态

| GPU | PID | 进程 | VRAM | 利用率 | 已运行 | 进度 |
|-----|-----|------|------|--------|--------|------|
| **cuda:0** | 195531 | CWM eval seed123 (ckpt-500) | 13.0/32.6 GB | 88% | 16h22m | **9224/9784 (94.3%)** |
| **cuda:1** | 195668 | CWM eval v12 (ckpt-500) | 13.0/32.6 GB | 88% | 16h22m | **9336/9784 (95.4%)** |
| **cuda:2** | 245775 | CWM 8B training (from ckpt-1200) | 21.2/32.6 GB | 90% | 2h57m | **1668/6633 (25%)** |
| **cuda:3** | 248041 | CLS 8B seed123 training (from ckpt-2400) | 26.8/32.6 GB | 91% | 2h38m | **~3200/6633 (48%)** |

**所有 4 卡占满，无空闲。**

## Part 2: CWM Eval 进度（未完成）

仍在运行，尚无结果文件：

- **seed123** (cuda:0): 9224/9784, running_acc=**59.0%**, ~52s/8样本 → **预计 ~60 min 后完成**
- **v12** (cuda:1): 9336/9784, running_acc=**57.9%**, ~51s/8样本 → **预计 ~48 min 后完成**

v12 先完成，seed123 后 ~12 min 完成。

## Part 3: 8B 训练 Checkpoint 状态

**CWM 8B** (cuda:2):
- 最新 checkpoint: **ckpt-1600**
- eval_loss 趋势: 0.364 (1400) → 0.369 (1500) → 0.374 (1600) — 缓慢上升
- ETA 全量: ~16h

**CLS 8B seed123** (cuda:3):
- 最新 checkpoint: **ckpt-3000**
- eval_loss 趋势: **0.278 (2800) → 0.324 (3000) → 0.426 (3200)**
- **⚠️ 明显过拟合，eval_loss 从 2800 步后快速上升。最佳 checkpoint 可能是 ckpt-2800。**

## Part 4: CLS val@5120 Sweep

**无法立即启动** — cuda:1 正在跑 CWM eval v12，预计 ~48 min 后释放。

命令已准备好，cuda:1 空闲后可以在 tmux `eval_cls_val5120` 中串联执行：
- CLS v5 ckpt-400 val@5120
- CLS v5 ckpt-600 val@5120

现有 test@2048 参考结果：
- v5 ckpt-400: acc=78.43%, f1_macro=68.41
- v5 ckpt-600: acc=76.37%, f1_macro=71.17 (f1更高但acc更低)

## Part 5: CWM eval on cuda:0

仍在运行中，不需要干预。~60 min 后完成。

## 异常

**CLS 8B seed123 过拟合严重** — eval_loss 从 0.278 (step 2800) 暴涨到 0.426 (step 3200)。建议 Director 考虑是否提前终止，最佳 checkpoint 为 ckpt-2800 或更早。

---

是否要我在 ~50 分钟后回来检查 CWM eval 结果并启动 CLS val@5120 sweep？

---
