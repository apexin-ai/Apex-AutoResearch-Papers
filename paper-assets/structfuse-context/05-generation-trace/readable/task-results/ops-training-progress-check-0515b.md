# ops training progress check 0515b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check-0515b_20260515T101843_result.json`
- **Structured JSON:** [`97a69a4cee56a7de3f74.json`](../../sessions/97/97a69a4cee56a7de3f74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## Qwen chain (cuda:0)
- **PID 337267: ALIVE** (运行 22h54m)
- **当前 subrun: embedding_distance_s44**, step 950/2816 (33.7%)
- 最新 eval (step 500): val_loss=0.4403, **R@1=0.5942**
- 下次 eval 在 step 1000
- 已完成 5/9 个目录存在（含正在跑的），4 个已完成

**新增完成 subrun:**
| subrun | best R@1 | 备注 |
|--------|----------|------|
| embedding_distance_s43 | 0.5606 (best_ckpt) / 0.5655 (final) | early stop@1500, val_loss best@500 |

**embedding_distance_s44 重点:**
- 目前 best R@1 = **0.5942**，vs random_s44 best = 0.6009 → **delta = -0.0067**
- 仅过了 1 次 eval（step 500），loss 仍在下降（step 900 loss=0.1194），后续 eval 有望超过
- embed_s43 在 step 1500 才达到 best R@1，s44 趋势更好

**Qwen 完成的 subrun 汇总:**
| subrun | best R@1 |
|--------|----------|
| random_s42 | 0.5527 |
| random_s43 | 0.5554 |
| random_s44 | 0.6009 |
| embedding_distance_s43 | 0.5606 |
| embedding_distance_s44 | 0.5942 (进行中) |

剩余: dataflow_aware_s43, dataflow_aware_s44 (+ 可能还有 s42 系列)

---

## StarCoder chain (cuda:1)
- **PID 519791: ALIVE** (运行 16h15m)
- **当前 subrun: random_s44**, step 400/2816 (14.2%)
- 尚无 eval（首次 eval 在 step 500）
- 已完成 subruns: 2/9

**新增完成 subrun:**
| subrun | best R@1 | 备注 |
|--------|----------|------|
| random_s43 | **0.4912** (step 1500) | early stop@2500, val_loss best=0.5239@1500 |

注：s43plus 脚本的 random_s43 曾被 kill（PID 442120），random_s43.log 显示是另一个进程跑完的。

**StarCoder 完成汇总:**
| subrun | best R@1 |
|--------|----------|
| random_s42 | 0.4604 |
| random_s43 | 0.4912 |

---

## M1 reextract v2
- **all.jsonl: 44,173 lines**（上次 25,582）
- 仍在运行，当前处理:
  - Project-MONAI/MONAI: 350/524 (66.8%)
  - getmoto/moto: 100/536 (18.7%)
- 这是最后两个大 repo，之前的 sqlfluff(1272)、pydicom(1315)、conan(972) 均已处理完或接近完成
- 注：原路径 `/root/structfuse/outputs/m1_reextract_v2/all.jsonl` 不存在，实际输出在 `/root/autodl-tmp/structfuse/full_m1_data/all.jsonl`，日志在 `/root/runs/structfuse-context/m1_reextract_v2.log`

---
