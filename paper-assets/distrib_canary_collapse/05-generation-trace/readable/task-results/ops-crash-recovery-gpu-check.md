# ops crash recovery gpu check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_crash-recovery-gpu-check_20260515T121353_result.json`
- **Structured JSON:** [`6e3e448e7705294512af.json`](../../sessions/6e/6e3e448e7705294512af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black (98GB) | 7,497 MiB | 72% | PID 117637 (gpt2m_v3) |
| 1 | RTX PRO 6000 Black (98GB) | 14,391 MiB | 47% | PID 89758 (a075) |

## 进程状态
| 实验 | 父PID | 子PID | 状态 | 运行时间 | CPU |
|------|-------|-------|------|---------|-----|
| gpt2m_v3 | 117632 (Ss+) | 117637 (Rl) | **运行中** | 6m51s | 106% |
| a075_s42 | 89753 (Ss+) | 89758 (Rl) | **运行中** | 6h29m | 167% |

## Generation 进度

**a075_s42** (synthetic_ratio=0.75):
- gen_0 ~ gen_7: metrics.json ✅ (共8个完成)
- gen_8: 目录已创建，训练中（刚完成 5000/5000 steps, train_loss=0.478）— 正在做 gen_8 的后处理/合成数据生成阶段
- gen_9, gen_10: 未开始
- all_metrics.json: 不存在
- 训练 loss 趋势: 2.016 → 1.190 → 0.842 → 0.690 → 0.573 → 0.516 → 0.478

**gpt2m_v3** (gpt2-medium, synthetic_ratio=1.0):
- 输出目录仅有 config.json，无 gen_0 子目录
- 日志显示 "Generation 0 (baseline)" 后全是 padding warning（122行）
- 运行仅 ~7 分钟，正在 gen_0 的合成数据生成阶段（GPU 72% 利用率）

## tmux Sessions
- `alpha_sweep_a075_s42` — 创建于 13:44
- `gen_wiki_gpt2m_a100_s42_v3` — 创建于 20:07

两个实验都在正常运行。a075 接近完成（8/11 generations done），gpt2m_v3 刚启动不久。

---
