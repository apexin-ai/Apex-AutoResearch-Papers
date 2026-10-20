# diag urgent gpu recovery 20260521T1610

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754_result.json`
- **Structured JSON:** [`84fbe071ec5c93df0a28.json`](../../sessions/84/84fbe071ec5c93df0a28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 任务 1: openvla_long_pipeline_v1 诊断

**状态：部分完成，非完全失败**

- `/tmp/exp_openvla_long_pipeline_v1.log` 不存在，无日志可查
- `results/libero_long/` 下有 **4 个 JSON**（无 trained/untrained 子目录）：
  - `action_r2_probing.json` ✓
  - `l1_attention_profile.json` ✓
  - `cross_instruction_classification.json` ✓
  - `rsa_analysis.json` ✓
- **缺失**：`counterfactual_combined.json` — 第 6 阶段（counterfactual）未完成
- **关键问题**：脚本定义了 trained/untrained 两个 condition，但结果直接写入 `RESULTS_BASE/` 而非子目录。目前只有一组数据，推测**第一个 condition 的前 4/5 阶段完成后崩溃**，第二个 condition 未开始
- R2 probing 数值特征（image_mean ~0.87-0.88，very flat across layers）符合 **trained OpenVLA** 的模式

---

## 任务 2: tracvla_spatial_untrained_v1 结果

**状态：3/4 阶段完成，缺 counterfactual**

### R2 Probing (untrained)

| Layer | image_mean | last_preaction |
|-------|-----------|---------------|
| L0 | 0.7761 | 0.5911 |
| L4 | 0.7812 | 0.7132 |
| L8 | 0.7892 | 0.6942 |
| L12 | 0.7806 | 0.7195 |
| L16 | 0.7961 | 0.7207 |
| L20 | 0.7814 | 0.7139 |
| L24 | 0.7694 | 0.7116 |
| L28 | 0.7714 | 0.7036 |
| L31 | 0.7589 | 0.7065 |

Pattern: image R2 高且平（~0.76-0.80），last_preaction 从 L0 的 0.59 快速升至 L4 的 0.71 后也趋于平坦。

### L1 Attention (untrained)
- **32/32 heads instruction-dominant**（0 mixed, 0 image-dominant）
- Top 5: head_8 (0.996), head_26 (0.984), head_19 (0.983), head_1 (0.959), head_28 (0.955)
- 最低: head_2 (0.569), head_24 (0.602)

### Cross-instruction Classification (untrained)
- 所有层 image_mean = 1.0, last_preaction = 1.0（仅 L0_last_preaction = 0.977）
- 近乎完美的 10-way 分类 → 每层表征都能完美区分不同指令

### Counterfactual: **未完成**（文件不存在）

---

## 任务 3: tracvla_spatial_full_v2 (trained)

**PID 521837 已结束。结果完整 — 4/4 JSON 齐全。**

### R2 Probing (trained)

| Layer | image_mean | last_preaction |
|-------|-----------|---------------|
| L0 | 0.8059 | 0.6656 |
| L4 | 0.8091 | 0.7954 |
| L8 | 0.8134 | 0.7908 |
| L12 | 0.8231 | 0.7980 |
| L16 | 0.8311 | 0.8035 |
| L20 | 0.8310 | 0.7981 |
| L24 | 0.8169 | 0.7463 |
| L28 | 0.8223 | **0.6150** |
| L29 | 0.8136 | **0.5040** |
| L30 | 0.7970 | **0.4472** |
| L31 | 0.7907 | 0.6712 |

**关键发现**：trained 模型 last_preaction R2 在 L28-L30 急剧下降（0.80→0.45），L31 部分回升至 0.67。Image R2 保持高位。这个 "action token R2 collapse" 在 untrained 中不存在。

### L1 Attention (trained)
- 30/32 instruction-dominant, **2 mixed** (head_13: 0.450, head_22: 0.474), 0 image-dominant
- Training 使部分 heads 从 instruction-dominant 转向 mixed

### Cross-instruction Classification (trained)
- 所有层 ≥ L1: image_mean=1.0, last_preaction=1.0
- L0: image=1.0, last_preaction=0.923

### Counterfactual (trained) — **完整**

| Condition | Cohen's d | MSE |
|-----------|----------|-----|
| empty | 1.327 | 0.107 |
| shuffled | 1.295 | 0.094 |
| paraphrased | 1.183 | 0.072 |
| wrong | 1.172 | 0.080 |

所有条件 d>1（大效应量），wrong condition token_divergence_rate=1.0。

---

## 任务 4: 下一批脚本就绪状态

| 脚本 | 存在 | 大小 |
|------|------|------|
| tracvla_long_full_pipeline.py | ✓ | 24.7KB |
| tracvla_goal_full_pipeline.py | ✓ | 23.3KB |

tracvla_long 配置确认正确：TracVLA-Phi3V + Phi-3-Vision base，输出到 `{trained,untrained}/` 子目录，包含完整 5 阶段。

---

## 任务 5: GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 0% | 0 / 97887 MiB |
| 1 | 0% | 0 / 97887 MiB |

**两卡完全空闲，可立即启动下一批实验。**

---

## 行动建议摘要

1. **openvla_long**：部分完成（4/5 阶段 × 1 condition），且没有 trained/untrained 分目录。需检查脚本是否有 bug 导致两个 condition 写到同一目录互相覆盖，以及 counterfactual 阶段崩溃原因
2. **tracvla_spatial untrained**：缺 counterfactual。可单独补跑 counterfactual 阶段
3. **tracvla_spatial trained**：**完整可用**，数据质量好
4. GPU 空闲，可启动 tracvla_long 或 tracvla_goal

---
