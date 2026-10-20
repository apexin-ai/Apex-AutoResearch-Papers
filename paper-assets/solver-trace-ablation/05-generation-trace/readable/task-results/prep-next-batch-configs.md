# prep next batch configs

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_next-batch-configs_20260516T034925_result.json`
- **Structured JSON:** [`ce1ad48804f9f8e65be0.json`](../../sessions/ce/ce1ad48804f9f8e65be0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 服务器状态汇总

### GPU
| GPU | 型号 | VRAM 占用 | 利用率 | 状态 |
|-----|------|----------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 79.5/97.9 GB | 15% | 训练中 (PID 604569) |
| 1 | RTX PRO 6000 Blackwell (98GB) | 80.4/97.9 GB | 98% | 训练中 (PID 604647) |

两块 GPU 均被 β=0.2 ISR sweep 占用，无空闲 GPU。

### 磁盘
| 挂载点 | 容量 | 已用 | 可用 |
|--------|------|------|------|
| / (根) | 30G | 9.1G (31%) | 21G |
| /root/autodl-tmp (数据盘) | 250G | 141G (57%) | 110G |

数据盘明细：outputs=110G, models=31G, hf_cache=105M。

### Git
`/root/solver-trace-ablation` 不是 git 仓库（代码直接部署，非 clone）。

---

## 配置文件清单

### 已有配置
| 文件 | reward_mode | β | seed |
|------|------------|---|------|
| grpo_additive_bonus.yaml | additive_bonus | 0.3 | 42 |
| grpo_additive_bonus_b01.yaml | additive_bonus | 0.1 | 42 |
| grpo_additive_bonus_b02.yaml | additive_bonus | 0.2 | 42 |
| grpo_additive_random.yaml | additive_random | 0.3 | 42 |
| grpo_additive_random_b01.yaml | additive_random | 0.1 | 42 |
| plan018_random_b01_s43.yaml | additive_random | 0.1 | 43 |
| plan018_random_b01_s44.yaml | additive_random | 0.1 | 44 |

### 本次新建配置
| 文件 | reward_mode | β | seed | 用途 |
|------|------------|---|------|------|
| grpo_additive_bonus_b005.yaml | additive_bonus | 0.05 | 42 | P1: β=0.05 ISR base |
| sweep_isr_b005_s43.yaml | additive_bonus | 0.05 | 43 | P1: β=0.05 ISR s43 |
| sweep_isr_b005_s44.yaml | additive_bonus | 0.05 | 44 | P1: β=0.05 ISR s44 |
| sweep_random_b01_s45.yaml | additive_random | 0.1 | 45 | P2: random β=0.1 s45 |

---

## 需注意的问题

**sweep_isr_b005_s42 可能不需要重跑**：该目录（31GB）包含完整的 checkpoint-500，trainer_state 显示 `should_training_stop=true`，reward_log 中 `beta_t=0.05` 正确。训练看起来已正常完成 500 步。上下文说"D098 bug 被 killed 需重跑"，但实际数据显示训练已完成且 β 值正确。建议先用 eval_sta.py 评估该 checkpoint，确认结果是否可用再决定是否重训。

**磁盘压力**：数据盘 57% 已用，每个训练输出约 16-31GB。同时跑两个新实验前需确认空间充足（当前 110G 可用，足够 3-4 个并行实验）。

---

## 下一批就绪度

| 实验 | 配置 | 输出目录 | 就绪 |
|------|------|---------|------|
| P1: β=0.05 ISR s42 | ✅ grpo_additive_bonus_b005.yaml | ⚠️ 已有完整输出，需确认是否可复用 |  |
| P1: β=0.05 ISR s43 | ✅ sweep_isr_b005_s43.yaml | 空 | ✅ |
| P1: β=0.05 ISR s44 | ✅ sweep_isr_b005_s44.yaml | 空 | ✅ |
| P2: random β=0.1 s45 | ✅ sweep_random_b01_s45.yaml | 空 | ✅ |

等 β=0.2 训练完成释放 GPU 后即可提交。

---
