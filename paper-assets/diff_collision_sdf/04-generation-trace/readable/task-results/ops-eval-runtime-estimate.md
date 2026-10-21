# ops eval runtime estimate

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-runtime-estimate_20260529T001144_result.json`
- **Structured JSON:** [`e57c6eab928b2381285e.json`](../../sessions/e5/e57c6eab928b2381285e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## 评估结果

### 运行时基准

根据历史 eval 日志（200 episodes = 4 tasks × 50 ep），单次 eval 耗时：

| 日志 | 服务器 | 耗时 |
|------|--------|------|
| eval_spatial_lora_ctrl_s0_30k | 35807 | ~41 min |
| eval_spatial_sdf_s0_l005_30k | 35807 | ~41 min |
| eval_phase2_18k_s2_l0 | 35807 | ~34 min |
| eval_multiseed_sdf_l01_s0_eseed0 | 35807 | ~39 min |
| eval_multiseed_lora_s0_eseed0 | 35807 | ~40 min |
| eval_multiseed_sdf_l01_s0_eseed123 | 45947 | ~79 min |

**典型 ~40 min/次**（45947 上一次 79 min 可能是并行干扰）。两台 GPU 当前均空闲（0% 利用率）。

---

### 实验 1: eval_phase2_18k_s2

- **Checkpoint 状态**: ❌ **18K checkpoint 不存在**
  - `phase2_stage1_seed0_l005/` 只有 step `10000` 和 `best`（best 也是 10K）
  - 训练似乎在 10K 就停了
- **已有结果**: `eval_phase2_18k_s2_l0_object.json` 存在，但用的是 `seed2_l0/18000` checkpoint（不同 run），非 phase2_stage1
- **结论**: 如果需要 phase2_stage1 的 18K，需要先继续训练；如果接受 10K checkpoint，可以跑，~40 min

### 实验 2: eval_spatial_bowl_lora_ctrl_s0_v2

- **Checkpoint 状态**: ✅ 完好
  - 路径: `westd-35807:/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/pi05_lora_baseline_spatial_bowl_seed0/30000/`
  - `model.safetensors` = 7.5GB ✓
- **已有结果**: `eval_spatial_lora_ctrl_s0_30k.json` 已存在（seed=7, 200 episodes）
  - 结果: Avg TSR=49.0%, Avg CAR=12.0%
- **结论**: 如果 v2 是相同配置的重跑，结果已有；如果要换 seed/参数，~40 min 可完成
- **注意**: Checkpoint 在 westd-35807 上，不在 45947

### 实验 3: Robustness seed evals

已完成的 multiseed 结果：

| 方法 | 已有 eval seeds |
|------|----------------|
| LoRA baseline s0 | eseed 0, 42, 99, 123 (4 seeds) |
| SDF l01 s0 | eseed 0, 42, 99, 123, 256 (5 seeds) |

- 如需额外 seed，每个 ~40 min
- 两台 GPU 并行可同时跑 2 个 eval

---

### DDL 可行性

两台 GPU 空闲，每次 eval ~40 min。今天内（假设还剩 12+ 小时）每台 GPU 可跑 **15+ 次 eval**，时间非常充裕。

**主要瓶颈是 Phase2 18K checkpoint 缺失**——不是时间问题，是数据问题。其余实验都能在 DDL 前完成。

---
