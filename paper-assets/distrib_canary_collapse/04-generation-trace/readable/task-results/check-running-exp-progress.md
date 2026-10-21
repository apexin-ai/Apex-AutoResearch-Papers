# check running exp progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_exp_progress_20260519T173023_result.json`
- **Structured JSON:** [`6133fe6b89250dd3495f.json`](../../sessions/61/6133fe6b89250dd3495f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。整理结果：

## GPU 状态

**westd-17855** (6 GPU H100/A100):
| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 99% | 28.5/97.9 GB | a060_s43 + a030_s42 (共享) |
| 1 | 97% | 14.2/97.9 GB | **未列出，有未知实验运行** |
| 2 | 97% | 14.4/97.9 GB | c4_a075_s42 |
| 3 | 65% | 14.5/97.9 GB | a035_s42 |
| 4 | 94% | 14.2/97.9 GB | a040_s42_v2 |
| 5 | 94% | 14.4/97.9 GB | c4_a050_s42 |

**westd-19828** (2 GPU A100):
| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 92% | 29.8/97.9 GB | opt13b_s43 |
| 1 | 93% | 64.7/97.9 GB | smollm3_3b_v3 |

---

## 实验进度汇总

| exp_id | 服务器 | GPU | 当前进度 | 阶段 | 预估剩余 | 预估完成时间 |
|--------|--------|-----|----------|------|---------|-------------|
| alpha_sweep_a060_s43_fp32 | 17855 | 0 (共享) | gen 8/10, step 2403/5000 (48%) | 训练中 | ~1.4h | +1h24m |
| alpha_sweep_a030_s42_fp32 | 17855 | 0 (共享) | gen 4/10, step 4217/5000 (84%) | 训练中 | ~3.6h | +3h36m |
| c4_a075_s42_fp32 | 17855 | 2 | gen 8/10, step ~2243/5000 (45%) | 训练中 | ~47min | +47m |
| alpha_sweep_a035_s42_fp32 | 17855 | 3 | gen 7/10 | 合成数据生成 | ~1.2h | +1h12m |
| alpha_sweep_a040_s42_fp32_v2 | 17855 | 4 | gen 8/10, step ~4193/5000 (84%) | 训练中 | ~42min | +42m |
| c4_a050_s42_fp32 | 17855 | 5 | gen 8/10, step ~1943/5000 (39%) | 训练中 | ~47min | +47m |
| opt13b_wiki_a100_s43_fp32 | 19828 | 0 | gen 3/10 | 评估中(MAUVE) | ~6.8h | +6h48m |
| smollm3_3b_wiki_a100_s42_v3 | 19828 | 1 | gen 10/10 | 合成数据生成 | ~1.5h | +1h30m |

---

## 预估 GPU 释放时间线

**最先释放（~40-50 min）：**
- `a040_s42_fp32_v2` → cuda:4 @ 17855
- `c4_a075_s42_fp32` → cuda:2 @ 17855
- `c4_a050_s42_fp32` → cuda:5 @ 17855

**第二批（~1-1.5h）：**
- `a035_s42_fp32` → cuda:3 @ 17855
- `a060_s43_fp32` → cuda:0 @ 17855（但 a030 仍占用 GPU 0）
- `smollm3_3b_wiki_a100_s42_v3` → cuda:1 @ 19828

**较晚释放（~3.5h）：**
- `a030_s42_fp32` → cuda:0 @ 17855（最后释放 GPU 0）

**最晚释放（~7h）：**
- `opt13b_wiki_a100_s43_fp32` → cuda:0 @ 19828

---

## 备注

1. **cuda:0 共享确认**：a060_s43 和 a030_s42 确实在同一物理 GPU 0 上（28.5GB 显存 = 2× 单实验用量），各自通过 `CUDA_VISIBLE_DEVICES` 映射为 cuda:0，训练速度约为独占 GPU 的一半（3.59 vs 7.68 it/s）。a060 完成后，a030 速度应回升至 ~7.68 it/s，剩余时间可能缩短。

2. **GPU 1 @ 17855 有未知实验**（14.2GB / 97% 利用率），不在任务列表中。

3. **每代时间参考**（实测）：Pythia-410M 独占 ~18min/gen，共享 ~34min/gen；OPT-1.3B ~58min/gen；SmolLM3-3B ~75-90min/gen。

---
