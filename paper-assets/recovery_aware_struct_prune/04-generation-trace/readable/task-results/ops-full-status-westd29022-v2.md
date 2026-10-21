# ops full status westd29022 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_westd29022_v2_20260518T175007_result.json`
- **Structured JSON:** [`3dc88311d4eb73a3e28c.json`](../../sessions/3d/3dc88311d4eb73a3e28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 状态汇总

### GPU 概览
| GPU | Temp | Power | VRAM | Util |
|-----|------|-------|------|------|
| cuda:0 | 84°C | 599W/600W | 90.6/97.9 GB | 99% |
| cuda:1 | 84°C | 610W/600W | 31.5/97.9 GB | 99% |
| cuda:2 | 74°C | 533W/600W | 16.8/97.9 GB | 97% |
| cuda:3 | 58°C | 344W/600W | 17.7/97.9 GB | 90% |

4 tmux sessions active, all 4 GPUs busy.

---

### 各实验进度

**cuda:0 — grpo_cka_only_20_extended_300 (GRPO训练)**
- 进度: **181/300 steps (60%)**
- 速度: ~114.78s/step
- ETA: ~3h48m (约 05:40 UTC 完成)
- 状态: 正常训练中，reward=1.00 on latest sample

**cuda:1 — eval_math500_grpo_standard_20_fair**
- 进度: **126/500 (25%)**
- Interim acc @ 100: **0.3600 (36.0%)**
- 速度: ~87-135s/problem (极慢，无 max_new_tokens 限制)
- ETA: ~14-17h 剩余（非常慢）

**cuda:2 — eval_math500_sft_cka_only_20_v4**
- 进度: **80/500 (16%)**
- Interim acc @ 50: **0.3000 (30.0%)**
- 速度: ~5-37s/problem（变化大）
- 启动时间: 01:07 UTC, 运行 ~43min
- ETA: ~4-6h

**cuda:3 — eval_math500_dense_unpruned**
- 进度: **469/500 (94%)**
- Interim acc @ 450: **0.7378 (73.8%)**
- 速度: ~26-42s/problem
- ETA: **~15-20min 即将完成**

---

### 已完成结果文件
| File | Accuracy | Total |
|------|----------|-------|
| math500_grpo_unpruned.json | **69.0%** | 500 |

（这是之前的结果，不是本轮新产出）

---

### 关键观察
1. **cuda:3 dense_unpruned 即将完成**（469/500），预计 ~02:10 UTC 出结果。interim 73.8% 与之前 westd 的 73.6% 一致，验证通过。
2. **cuda:1 standard_fair 极慢** — 没有 `--max_new_tokens` 限制，部分问题生成超长序列（单题 5-6min）。126/500 跑了 4h44m，剩余可能需要 14h+。
3. **cuda:0 GRPO 训练稳定**，60% 进度，约 4h 后完成。
4. **cuda:2 sft_cka v4** 刚启动不久（43min），16% 进度，预计 4-6h。

暂不更新 registry，等 dense_unpruned 完成后再收割。

---
