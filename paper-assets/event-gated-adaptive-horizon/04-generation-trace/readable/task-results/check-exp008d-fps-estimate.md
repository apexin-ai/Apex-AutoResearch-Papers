# check exp008d fps estimate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp008d-fps-estimate_20260524T205825_result.json`
- **Structured JSON:** [`745168ccd71b904a2dc3.json`](../../sessions/74/745168ccd71b904a2dc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总结果：

---

## FPS 与时间估算

### 直接数据来源

**exp_008d Walker config FPS（training-only, from metrics.jsonl）：**

| 实验 | 服务器/GPU | FPS (steps/sec) | 备注 |
|------|-----------|-----------------|------|
| exp_009b_008d_walker_s2 | bjb1-45299 / RTX PRO 6000 Blackwell | 6.8-7.2 | trained dt_emb + subsample ON + H=8 |
| exp_009e_008d_walker_s1 | bjb1-45299 / RTX PRO 6000 Blackwell | 6.5-7.0 | 同配置 |
| exp_042 frozen_dt_emb_walker | bjb1-40020 / RTX 4090 | 7.9-8.0 | frozen（非 trained），作参考 |
| exp_047 frozen_dt_emb_walker_s1 | bjb1-40020 / RTX 4090 | 7.8-8.2 | 同上 |

### 估算逻辑

1. **bjb1-45299 RTX PRO 6000 Blackwell 上 exp_008d Walker**：logged FPS ~6.9 steps/sec
2. **RTX 4090 vs RTX PRO 6000 缩放比**：frozen_dt_emb Walker 在两台机器上分别是 ~8.0 vs ~10.0 fps → 比例 0.80x
3. **估算 exp_008d Walker 在 RTX 4090**：6.9 × 0.80 ≈ **5.5 steps/sec**（training-only）
4. **Wall-clock 开销**：exp_009b 实际跑了 112K steps in 11.57 hours（registry 时间），含 eval/logging/checkpoint → wall-clock rate ~9,700 steps/hr

```
exp_008d Walker FPS:
  - bjb1-45299 (RTX PRO 6000): ~6.9 steps/sec = ~24,800 steps/hr (training-only)
  - bjb1-40020 (RTX 4090) 估算: ~5.5 steps/sec = ~19,800 steps/hr (training-only)
  来源: exp_009b/009e metrics.jsonl fps 字段 + exp_042/047 跨GPU缩放

60K steps 预估时间 (bjb1-40020 RTX 4090 cuda:1):
  - 基于 exp_009b wall-clock 缩放: (60/112) × 11.57h × 1.25 ≈ 7.7 hours
  - 考虑 cuda:1 潜在 CPU 争用: ~8-10 hours
  - 最佳估计: ~8 hours

exp_063 RSSM fidelity 分析:
  - 总运行时间: 28 minutes (18:53:48 → 19:21:37, 实际脚本执行时间)
  - 分析了 2 个 checkpoint (exp_001 baseline + exp_008d collapsed)
  - 单个 checkpoint 分析: ~14 minutes
  来源: exp_063 registry started_at/completed_at

12 个 checkpoint 分析总时间: 12 × 14 min ≈ 168 min ≈ 2.8 hours

总时间（训练 + 分析）: 8 + 2.8 ≈ 11 hours (range: 10-13 hours)
```

### 注意事项
- **GPU 差异大**：bjb1-45299 是 RTX PRO 6000 Blackwell (98GB)，bjb1-40020 是 RTX 4090 (24GB)，没有 exp_008d 在 RTX 4090 上的直接数据，上述是间接估算
- **cuda:1 争用**：如果 cuda:0 同时跑其他实验，MuJoCo（CPU-bound）会有 CPU 争用，可能额外慢 10-20%
- **RSSM 分析脚本**需要改写来支持 Walker 的 obs_keys（当前硬编码为 Cheetah 的 height/orientations/velocity），但 Walker Walk 也是 proprioceptive，改动小

---
