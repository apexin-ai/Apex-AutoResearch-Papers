# analysis exp hopper trained s0 ext

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_trained_s0_ext_20260527T080108_result.json`
- **Structured JSON:** [`0d48ae31c3e5b1de3a8e.json`](../../sessions/0d/0d48ae31c3e5b1de3a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## exp_hopper_trained_s0_ext — 结论：**NEGATIVE**

**训练状态**：正常完成，跑到 168K steps（超过目标 150K），无报错。

**NVE 轨迹（105K→158K）**：

| Step | ve_ratio | eval_return |
|------|----------|-------------|
| 105K | **0.897** (alert=1) | 3.26 |
| 118K | 0.376 ↓ | 15.08 |
| **128K** | **5.519** ↑ | 2.06 |
| 138K | 0.370 ↓ | 47.40 |
| 148K | 0.550 | 46.90 |
| 158K | 0.439 | **81.58** |

**假设被证伪的三个原因**：
1. 105K 的"指数上升"趋势在续训后**断裂**（0.897→0.376）
2. 128K 的 5.52 峰值是**单点瞬态**（eval_return 同时暴跌至 2.06），仅持续 1 个 eval 点，不满足 D155 要求的 ≥2 点
3. Gate 全程锁定 dt=2（entropy=0），事件门控机制完全未激活，不满足时序因果标准

**性能方面**：eval_return 从 3.26 增长至 81.58（25×），模型在持续学习，但 CIVO 现象不存在。

Registry 已更新为 DONE/negative，报告已注册为 artifact。

---
