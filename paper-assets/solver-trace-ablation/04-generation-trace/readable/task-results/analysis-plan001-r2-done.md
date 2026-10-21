# analysis plan001 r2 done

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan001-r2-done_20260513T234636_result.json`
- **Structured JSON:** [`200848b7aacd9feac977.json`](../../sessions/20/200848b7aacd9feac977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。以下是完整分析：

---

## plan001-exec-only-s42-r2 训练结果

### Metrics 总表

| 指标 | 值 |
|------|-----|
| 总步数 | 500 |
| 训练时长 | 62.2 min |
| overall prove_rate | **0.6743** |
| overall ISR | **0.6677** |
| last-50 prove_rate | **0.8525** |
| last-50 ISR | **0.8525** |
| last-100 prove_rate | **0.8650** |
| last-100 ISR | **0.8612** |
| first-20 prove_rate | 0.1625 |
| parse_rate | 1.0 (全程) |
| 首次 prove_rate=1.0 | step 109 |
| 持续 ≥0.8（rolling-10）| step 133 起 |
| 步数达到 1.0 的比例 | 166/500 (33.2%) |
| mean loss | 0.0067 |

### 训练曲线（分窗口 prove_rate）

| 窗口 | prove_rate | 趋势 |
|------|-----------|------|
| 1–50 | 0.185 | 冷启动 |
| 51–100 | 0.238 | 缓慢爬升 |
| 101–200 | **0.663** | 急剧跃升 |
| 201–300 | 0.784 | 持续上升 |
| 301–400 | 0.849 | 接近平台 |
| 401–500 | **0.865** | 平台期 |

**曲线形态**：经典 sigmoid。step 50-200 快速爬升，step 200+ 逐渐收敛到 ~0.86 平台。未完全饱和到 1.0。

### Baseline 对比

| 实验 | prove_rate | ISR | 备注 |
|------|-----------|-----|------|
| base model (phase0) | 0.120 | 0.064 | 未训练 |
| 100-step exec-only (r5) | 0.151 | 0.148 | 训练集 |
| 100-step held-out eval (plan003) | 0.320 | 0.206 | held-out |
| **500-step exec-only (本次, last-100)** | **0.865** | **0.861** | 训练集 |

相对提升（last-100 vs base model）：
- prove_rate: **+621%** (0.12 → 0.865)
- ISR: **+1245%** (0.064 → 0.861)

### 关键检查

1. **prove_rate 饱和？** 未完全饱和。平台期在 ~0.86，非 1.0。33.2% 的单步达到 1.0，但平均未饱和。

2. **ISR ≡ prove_rate？** 近似但不严格相等。500 步中有 13 步 (2.6%) ISR < prove_rate（差异 0.125–0.5），说明 exec-only 模式下仍有少量 "proved but low-ISR" 情况（可能是部分 proof 质量差异）。

3. **Reward hacking？** 无。最大 rolling-10 跳跃仅 0.1042，是渐进式学习而非突变。

4. **Loss 趋势：** 极低（mean=0.0067, last-50=0.0089），接近零但未完全归零，与 prove_rate 未完全饱和一致。

### 结论

训练成功。500 步 exec-only GRPO 在训练集上把 prove_rate 从 0.12 提升到 0.865（last-100），曲线在 step ~200 后收敛。

**关键注意**：以上所有指标都是训练集表现。真正的结论需要 held-out eval。考虑到 100-step 时 held-out prove_rate 是 0.32（训练集 0.151），500-step 的 held-out 表现可能明显低于训练集的 0.865。建议尽快跑 held-out eval 验证泛化能力。

---
