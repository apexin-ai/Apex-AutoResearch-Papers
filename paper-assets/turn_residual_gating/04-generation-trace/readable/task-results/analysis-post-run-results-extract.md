# analysis post run results extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_post_run_results_extract_20260520T092327_result.json`
- **Structured JSON:** [`4b92469fa5f66f699b1d.json`](../../sessions/4b/4b92469fa5f66f699b1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已提取。汇总如下：

---

## 1. attention_steering_v7_tg_gen — SUCCESS

JSON 输出已保存: `runs/attention_steering/phase2_tg_s42_v7_attention_steering.json`

| β | Mid-GAR | PPL |
|---:|--------:|----:|
| 0.0 | 0.0280 | 1.41 |
| 0.5 | 0.0287 | 1.39 |
| 1.0 | 0.0349 | 1.36 |
| 2.0 | 0.0620 | 1.41 |
| 5.0 | 0.6795 | 1.91 |
| 10.0 | 0.9590 | 4.22 |

**关键发现**: β=0→2 GAR 缓升但 PPL 几乎不变；β=5 出现急剧跳变（GAR 0.068→0.68，PPL 仅升到 1.91）；β=10 GAR 几乎饱和（0.96）但 PPL 代价明显（4.22）。存在一个 β∈[2,5] 的 phase transition。无错误。

---

## 2. phase2_tg_s42_v8b_ss_fixed — FAILED

- **失败位置**: Epoch 1, Step 4300（`train_phase2_v8b.py:477`, `loss.backward()`）
- **失败原因**: **CUDA OOM** — 尝试分配 448 MiB，GPU 总容量 94.97 GiB，但其他进程占用大量显存：
  - Process 157667: 26.76 GiB
  - Process 158713: 17.28 GiB
  - PyTorch 自身已分配 45.21 GiB + 4.81 GiB reserved
- **Checkpoint**: 有一个保存在 `checkpoints/tg_v8b_ss_fixed_s42/epoch_0`（训练初期保存）
- **训练状态**: SS ratio 已到 0.500（scheduled sampling 到了 50% 目标），Loss ~1.0，Gate ~0.94。训练本身在正常收敛
- **诊断**: 不是代码 bug，是 GPU 被其他进程抢占显存。需要独占 GPU 重跑

---

## 3. trc_baseline_v7_tg — 实际完成（EXIT_CODE=1 是 tee 路径问题）

EXIT_CODE=1 原因: 脚本开头 `tee: runs/trc_baseline/trc_baseline.log: No such file or directory`（目录不存在导致 tee 失败），但**三个 checkpoint 的 TRC 测量全部完成**。

JSON 输出:
- `runs/trc_baseline/phase2_tg_s42_v7_trc.json`
- `runs/trc_baseline/phase2_lora_only_s42_trc.json`
- `runs/trc_baseline/base_model_trc.json`

| Checkpoint | TF TRC | Gen TRC | Gap (TF-Gen) | Ratio |
|:-----------|-------:|--------:|-------------:|------:|
| **v7 TG** (LoRA+gates) | 0.3339±0.114 | 0.3323±0.093 | +0.0016 | 1.005 |
| **LoRA-only** | 0.3490±0.108 | 0.4106±0.070 | −0.0617 | 0.850 |
| **Base model** | 0.1494±0.056 | 0.1494±0.056 | 0.0000 | 1.000 |

**关键发现**:
- **v7 TG**: TF≈Gen（Gap≈0, Ratio≈1.0），说明 gating 消除了 teacher-forcing / free-generation 之间的 TRC 偏差
- **LoRA-only**: Gen TRC > TF TRC（Gap=−0.06, Ratio=0.85），生成时表征一致性反而更高——可能是 exposure bias 导致的 overcorrection
- **Base model**: TF=Gen（完全一致），符合预期——base model 没有经过 turn-level 训练，TRC 本身低（0.15），且生成模式没有引入偏差

---
