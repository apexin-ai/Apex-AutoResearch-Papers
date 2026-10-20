# analysis transfer v1 500step

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer-v1-500step_20260519T234128_result.json`
- **Structured JSON:** [`d7191a332d420ce78108.json`](../../sessions/d7/d7191a332d420ce78108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已足够。当前训练已到 step 5330（27%），远超 500-step 检查点。以下是完整分析：

---

## phase1_transfer_v1 — 500-Step 检查点分析

### D010 三项判定标准

| 标准 | 阈值 | Step 500 实测 | 判定 |
|------|------|---------------|------|
| dec_gnorm | > 0.01 | **0.0322** | **PASS**（勉强，快速衰减中） |
| hm_max | > 0.05 | **0.001130** | **FAIL**（差 44 倍） |
| hm_ent | 下降趋势 | **8.69→8.87 ↑** | **FAIL**（在上升） |

**综合判定：FAIL（1/3 pass，2/3 fail）**

---

### 指标详细趋势

#### L_transfer loss
| Step | L_transfer | transfer_grad_norm | grad_ratio |
|------|-----------|-------------------|------------|
| 0 | 0.000 | 0.000 | 0.00% |
| 100 | 4.713 | 0.396 | 2.35% |
| 200 | 4.310 | 0.241 | 1.23% |
| 300 | 4.385 | 0.125 | 0.55% |
| 400 | 4.147 | 0.069 | 0.42% |
| **500** | **4.183** | **0.032** | **0.17%** |
| 800 | 4.173 | 0.009 | 0.06% |
| 900 | 4.174 | 0.002 | 0.01% |
| 1000+ | **4.1744** | **~0.0003** | **0.00%** |
| 5000 | 4.1744 | 0.0001 | 0.00% |

**L_transfer 在 step ~800 后完全收敛到 4.1744，梯度归零。** 这个值接近 ln(65)≈4.17，decoder 没有学到任何有意义的表征。

#### L_action loss
| Step | L_act |
|------|-------|
| 0 | 0.707 |
| 100 | 0.402 |
| 200 | 0.781 |
| 300 | 0.527 |
| 400 | 0.523 |
| 500 | 0.492 |
| 5300 | ~0.25 |

L_action 正常下降，LoRA + action head 在学习，但与 afford decoder 无关。

#### Heatmap 指标
| Step | dec_gnorm | hm_max | hm_ent | hm_mean |
|------|-----------|--------|--------|---------|
| 0 | 0.0000 | 0.00540 | 8.69 | 6.1e-5 |
| 10 | 0.4560 | 0.00533 | 8.33 | 6.1e-5 |
| 100 | 0.3955 | 0.00182 | 8.71 | 6.1e-5 |
| 200 | 0.2412 | 0.00130 | 8.78 | 6.1e-5 |
| 300 | 0.1250 | 0.00102 | 8.85 | 6.1e-5 |
| 400 | 0.0690 | 0.00132 | 8.85 | 6.1e-5 |
| **500** | **0.0322** | **0.00113** | **8.87** | **6.1e-5** |
| 5000+ | **0.0003** | **0.00054** | **8.88** | **6.1e-5** |

hm_ent 从 8.69 单调上升至 8.88（接近 16×16=256 patch 的理论最大熵 ln(256)≈5.55... 不对，8.88 对应 e^8.88≈7205，这说明 spatial 分辨率可能更高）。关键是 **熵在持续上升，heatmap 越来越均匀**。

#### transfer_pos_count
日志中 `pos=` 字段显示大部分 batch 有 1-2 个正样本对，偶尔 pos=0（跳过 L_transfer）。Queue 稳定在 256。

---

### 与 phase1_lconsist_v1 对比

| 指标 | transfer_v1 @ 500 | lconsist_v1 参考值 | 对比 |
|------|-------------------|-------------------|------|
| grad_ratio | 0.17% | 0.01% | transfer 稍高但两者都极低 |
| hm_max | 0.00113 | 0.003 | lconsist 高 2.7× |
| hm_ent | 8.87 | **7.3** | **lconsist 显著更低**（有聚焦） |
| hm_mean | 6.1e-5 | 6.1e-5 | 相同（初始化值） |

**lconsist 的 hm_ent=7.3 说明 L_consist 至少让 decoder 产生了一定程度的空间聚焦，而 transfer_v1 的 hm_ent=8.87 完全是均匀分布——纯 L_transfer 对 afford decoder 没有任何训练效果。**

---

### 核心诊断

**Afford decoder 已死。** 原因链条：
1. L_transfer 是 contrastive loss（InfoNCE），作用于 pooled feature，不直接反向传播空间梯度到 decoder
2. 没有 L_consist 提供逐像素监督，decoder 没有任何信号来学习空间聚焦
3. dec_gnorm 从 step 500 的 0.032 衰减到 step 5000 的 0.0003，decoder 参数基本冻结
4. heatmap 退化为均匀分布（hm_ent→8.88, hm_max→0.0005）

### Checkpoint-500 状态

已保存：`/root/afford_invar/runs/libero_goal_no_noops+transfer+b2+lr0.0005+beta0.1/checkpoint-500/` ✓

---

### 判定

**FAIL — 建议 Path C kill。**

纯 L_transfer 无法驱动 afford decoder 学习。step 500 时 dec_gnorm 勉强过线但已在快速衰减，hm_max 差阈值 44 倍，hm_ent 反向上升。当前 step 5330 的数据确认 decoder 完全停滞，继续训练无意义。

---
