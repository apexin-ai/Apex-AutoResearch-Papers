# analysis csmp gradual eval

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_csmp_gradual_eval_20260518T173728_result.json`
- **Structured JSON:** [`38de17da141d71840aa1.json`](../../sessions/38/38de17da141d71840aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。核心结果：

**α=0.50 (3 seeds)**
| k | Alarm Gen | EDD | 备注 |
|---|-----------|-----|------|
| 0.05 | 3 | 2.0 | h=1.53 延迟检测 |
| 0.10 | 2 | 1.0 | h=1.00 延迟检测 |
| 0.25 | **1** | **0.0** | 即时检测，3 seed 一致 |
| 0.50 | **1** | **0.0** | 即时检测 |
| 1.0 | **None** | N/A | 完全失败，k 过大吃掉信号 |

**α=0.75 (3 seeds)**
| k | Alarm Gen | EDD |
|---|-----------|-----|
| 0.05 | 2 | 1.0 |
| 0.10 | 2 | 1.0 |
| 0.25 | **1** | **0.0** |
| 0.50 | **1** | **0.0** |
| 1.0 | **1** | **0.0** |

**vs 简单阈值 (mean-2σ)**：CUSUM k=0.25 与 threshold n=1 在 alarm gen 上完全一致（都是 gen 1）。原因是 gen 0→1 的 drop 太大（α=0.50: 0.72, α=0.75: 1.04），任何合理检测器都会立刻报警。

**关键发现**：
1. k=0.25 在所有 α (0.50/0.75/1.0) 上 EDD=0，推荐值不变
2. k=1.0 在 α=0.50 彻底失败（S_t 永远为 0），sensitivity 丧失
3. CUSUM 与简单阈值 alarm gen 相同，但 CUSUM 有 FAR 保证（h 从 null data 校准）、S_max 提供 shift 严重度信息（α=0.75 S_max=7.7 >> α=0.50 S_max=4.0 >> α=1.0 intervention S_max=1.1）
4. 渐变型不需要不同的 k 参数——gen-0-to-gen-1 的 drop 已经足够大

---
