# ops check exp progress 0524

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-progress-0524_20260523T220651_result.json`
- **Structured JSON:** [`8d1340f1ee76507b5fe3.json`](../../sessions/8d/8d1340f1ee76507b5fe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇报

### exp_019 (Pythia-410M, r=0.2, seed44) — cuda:1
- **当前：Gen 9/10（最后一代），生成阶段 5760/40000 (14.4%)**
- 结果文件已保存到 Gen 8，Gen 9 刚进入生成阶段
- 生成完还需 fine-tune + eval，预计 **再跑 ~1.5-2 小时完成全部 10 代**
- GPU 1 利用率 93%，显存 25.0/95.6 GB

### exp_020 (GPT-2-medium, r=0, seed42) — cuda:0
- **当前：Gen 5/10，生成阶段 44800/50000 (89.6%)**
- 结果文件已保存到 Gen 4，Gen 5 生成即将完成
- 还剩 5 代（Gen 5 生成尾声 + train/eval，再跑 Gen 6-10）
- 启动约 12 小时跑了 5 代，预计 **再跑 ~10-12 小时**
- GPU 0 利用率 58%（当前在生成阶段，训练时会更高），显存 25.8/95.6 GB

### GPU 状态
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 58% | 26.4/95.6 GB |
| 1 | RTX PRO 6000 Blackwell | 93% | 25.0/95.6 GB |

exp_019 即将完成；exp_020 大约明天早上跑完。

---
