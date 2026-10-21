# ops check extended status v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-extended-status-v2_20260519T142226_result.json`
- **Structured JSON:** [`5b632d02398139c8d321.json`](../../sessions/5b/5b632d02398139c8d321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 31% | 4.8/97.9 GB |
| 1 | RTX PRO 6000 Blackwell | 79% | 9.5/97.9 GB |

## 实验状态

| 实验 | tmux | 当前步数/目标 | 进度 | 最新 eval_return | 最新 train_return |
|------|------|--------------|------|-----------------|------------------|
| **s2_ext** | 存活 | **424K/505K** | **84%** | 933.3 (422K) | 949.7 (424K) |
| **s3_ext** | 存活 | **308K/505K** | **61%** | 853.3 (300K) | 951.4 (308K) |
| **s4_ext** | 存活 | **268K/505K** | **53%** | 942.4 (262K) | 893.0 (268K) |

## s2_ext 详细数据

**s2 尚未完成**，当前 424K 步，预计还需 ~81K 步。

**Eval return 趋势（延长阶段，从 112K 恢复）：**
- 112K: 659.5 → 202K: 932.1 → 292K: **957.0** → 302K: **960.8** (peak) → 422K: 933.3
- **Peak eval return: 960.8**（302K 步）
- 300K 以后 eval 在 887~948 区间波动，最新 422K 为 933.3

**ve_ratio profile（value_mean / eval_return 近似）：**
- 整个延长阶段 ve_ratio 稳定在 **0.6 → 0.7 → 0.8**，缓慢上升
- 122K: 0.6 → 162K: 0.7 → 402K: 0.8 → 412K: 0.7 → 422K: 0.7
- value_mean 在后期稳定在 ~664，eval_return ~930 附近，ve_ratio ≈ 0.71

**s2_ext 按当前 fps (~8.3)，剩余 81K 步约需 ~2.7 小时完成。**

---
