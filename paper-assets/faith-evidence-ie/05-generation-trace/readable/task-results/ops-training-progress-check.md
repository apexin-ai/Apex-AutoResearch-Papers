# ops training progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260514T221133_result.json`
- **Structured JSON:** [`136367ebc08cd4340ca0.json`](../../sessions/13/136367ebc08cd4340ca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. mvp2_grpo_ced_lr5e6_r1（GRPO 训练）
| 项目 | 值 |
|------|-----|
| 状态 | **运行中** (cuda:0, PID 90085) |
| 进度 | **81/200 步 (40.5%)** |
| 速度 | ~98-111 s/step |
| 预估完成 | **~09:40**（约 3.3h 后） |
| Checkpoints | ckpt-20, 40, 60, **80**（刚保存） |

**最近指标 (step 80)**:
- loss: 0.046, reward: **0.283**
- format_reward: 0.249, f1_reward: **0.016**, ced_reward: **0.018**
- KL: 0.009（step 5 时曾飙到 2.4B，已恢复）

**趋势**: reward 在 0.23-0.30 间波动，f1/ced reward 始终极低。format reward 稳定 ~0.22-0.25。

---

### 2. mvp2_eval_lr5e6_r1_ckpt20（ckpt-20 eval）— **已完成**
没有活跃 session/进程，结果已写入。

| 指标 | 值 | 门控 |
|------|-----|------|
| **rel_f1** | **0.0077** | **FAIL** (需 > 0.30) |
| precision | 0.0071 | — |
| recall | 0.0084 | — |
| evi_f1 | 0.628 | — |
| format_ok | 99.1% | — |
| TP / pred / gold | 102 / 14440 / 12151 | — |
| truncated | 587/985 docs | — |

**关键门控未通过。** 模型产生了大量预测（14440）但几乎没有命中（102 TP）。格式合规率很高，但 relation extraction 质量极差。

---

### 3. mvp2_eval_lr5e6_r1_ckpt40（ckpt-40 eval）
| 项目 | 值 |
|------|-----|
| 状态 | **运行中** (cuda:2, PID 101842) |
| 进度 | **27/62 batches (44%)** |
| 速度 | ~95-96 s/batch |
| 预估完成 | **~07:08**（约 56 min 后） |

---

### 4. mvp2_eval_sft_baseline（新增 — SFT baseline eval）
| 项目 | 值 |
|------|-----|
| 状态 | **运行中** (cuda:3, PID 104979) |
| 进度 | **9/62 batches (15%)** |
| 速度 | ~109 s/batch |
| 预估完成 | **~07:28**（约 96 min 后） |

---

### 异常与风险

1. **ckpt-20 关键门控 FAIL** — rel_f1 = 0.0077，离 0.30 差距巨大。ckpt-40 eval 正在跑，但鉴于训练 reward 趋势（f1_reward 始终 < 0.02），ckpt-40 通过门控的可能性不大。
2. **训练 KL 异常** — step 5 出现 2.4B 级 KL 飙升（后恢复），可能导致早期训练方向偏离。
3. **大量截断** — 587/985 文档被截断（max_new_tokens=1024 不够），模型倾向生成冗长输出。
4. 所有进程运行正常，无卡死或 OOM 迹象。

---
