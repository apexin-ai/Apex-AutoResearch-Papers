# analyze exp 048 cheetah civo extension completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_048_cheetah_civo_extension_completion_20260522T211521_result.json`
- **Structured JSON:** [`15826cdee4f4d44f5fa9.json`](../../sessions/15/15826cdee4f4d44f5fa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果。

---

## exp_048 Cheetah CIVO Extension — 完整结果

**状态**: 正常完成，312K steps（最后 eval 在 302K），无报错。

### ve_ratio 轨迹（baseline=0.656）

| Step | ve_ratio | NVE | eval_return |
|------:|--------:|-----:|----------:|
| (105K) | ~46.3 | 70.64 | — (继承自 exp_010b) |
| 112K | — | — | 9.2 |
| 122K | 6.135 | 9.35 | 9.5 |
| 132K | 2.955 | 4.50 | 20.1 |
| 142K | 2.919 | 4.45 | 20.4 |
| **152K** | **23.925** | **36.47** | **2.4** |
| **162K** | **24.112** | **36.76** | **2.3** |
| 172K | 9.268 | 14.13 | 6.2 |
| 182K | 12.795 | 19.50 | 4.1 |
| 192K | 8.002 | 12.20 | 5.8 |
| 202K | 4.110 | 6.26 | 12.5 |
| 212K | 7.441 | 11.34 | 7.2 |
| 222K | 3.816 | 5.82 | 13.7 |
| 232K | 4.016 | 6.12 | 12.7 |
| 242K | 6.477 | 9.87 | 7.7 |
| **252K** | **1.432** | **2.18** | **32.8** |
| 262K | 4.570 | 6.97 | 10.1 |
| 272K | 3.366 | 5.13 | 13.1 |
| 282K | 1.790 | 2.73 | 23.5 |
| 292K | 3.056 | 4.66 | 13.9 |
| 302K | 1.803 | 2.75 | 23.4 |

### 核心判断：Cheetah CIVO **部分自修复，但未完全恢复**

**ve_ratio 三阶段**：
1. **快速初始下降**（105K→142K，~37K steps）：ve_ratio 从 ~46.3 骤降到 2.9（NVE 70.6→4.5），减少 94%
2. **二次 CIVO 爆发**（152K-162K）：ve_ratio 回弹到 24.1（NVE 36.8），eval_return 崩溃到 2.3-2.4
3. **振荡式缓慢下降**（162K→302K，140K steps）：ve_ratio 在 1.4-12.8 之间大幅振荡，最终收敛到 1.8（NVE 2.75）

**最终状态**：
- ve_ratio: 1.803（NVE=2.75）— 仍是 baseline 的 2.75 倍
- eval_return: 23.4 — 远低于 vanilla Cheetah 正常水平
- Gate 完全坍塌：dt=2 占比 100%，零时间灵活性

### 与 Walker (exp_045) 对比

| 指标 | Walker (exp_045) | Cheetah (exp_048) |
|------|-----------------|-------------------|
| 起始 ve_ratio | 4.91 | ~46.3 (NVE 70.6) |
| 最终 ve_ratio | 0.05 | 1.80 |
| 修复比例 | 99% | 96% |
| 最终 NVE | ~0.08 | 2.75 |
| 修复用时 | 170K steps | 197K steps（仍未完全修复）|
| 二次爆发 | 无 | 有（152K-162K，NVE 回到 37）|
| 完全恢复？ | **是** | **否** |

### Paper Narrative

这是**最强的结果**：CIVO 严重程度决定可恢复性。
- Walker（NVE~5）：完全自修复，CIVO 是可逆的暂态现象
- Cheetah（NVE~70）：部分自修复但留有永久损伤——ve_ratio 振荡剧烈且无法归零，gate 永久坍塌，eval_return 恢复缓慢且低位震荡
- 存在 **severity threshold**：轻度 CIVO 可逆，极端 CIVO 造成不可逆的 value function 损伤和 gate 功能丧失

---
