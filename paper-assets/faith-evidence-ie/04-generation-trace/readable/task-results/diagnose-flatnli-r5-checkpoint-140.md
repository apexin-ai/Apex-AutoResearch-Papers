# diagnose flatnli r5 checkpoint 140

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_flatnli-r5-checkpoint-140_20260514T172119_result.json`
- **Structured JSON:** [`92d9fec3272e5d790588.json`](../../sessions/92/92d9fec3272e5d790588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果报告

### 状态总览
- **检查的 checkpoint**: step 120（最新可用，checkpoint-140 尚未生成）
- **训练进度**: step 134/200，约 48s/step，checkpoint-140 约 5 分钟后生成
- **进程**: PID 73407 存活，GPU PID 73412（子进程），占用 11608 MiB on cuda:3
- **save_steps**: 实际为 20（下一个 checkpoint 在 step 140）

### frac_zero_std 趋势（恢复训练后）

| Step | frac_zero_std | KL | reward | nli_reward |
|------|--------------|------|--------|------------|
| 100 | 0.0 | — | 1.236 | 0.911 | ← r3 结束点
| **105** | **0.9** | 0.485 | 0.363 | 0.043 | ← 恢复后立即崩溃
| 110 | 0.7 | 0.435 | 1.082 | 0.249 |
| 115 | 0.5 | 0.458 | 0.913 | 0.427 |
| **120** | **0.8** | 0.456 | 0.560 | 0.171 | ← 最新

### 关键判断

**frac_zero_std = 0.8 @ step 120 → WAIT FOR CHECKPOINT-140**

趋势不乐观：
- frac_zero_std 在 0.5–0.9 之间震荡，无收敛迹象（105→110 好转，115 继续好转到 0.5，但 120 反弹到 0.8）
- KL 稳定在 0.44–0.49，显著高于正常范围
- NLI reward 从恢复前的 0.91 崩至 0.04–0.43，step 120 仅 0.17
- reward 同步下滑：1.24 → 0.56

### 异常指标
- **恢复后立即退化**：step 100→105 的 frac_zero_std 从 0.0 跳到 0.9，说明从 r3 恢复的衔接有严重问题
- **KL 全程高位**：~0.46 持续不降，模型偏离参考策略过远
- **grad_norm 骤降**：step 105 的 grad_norm 仅 0.059（恢复前 ~0.4–0.9），信号接近消失

### 建议
等 checkpoint-140（约 5 分钟后）再决定。如果 frac_zero_std ≥ 0.9，立即 kill。按当前震荡模式，大概率维持 0.7–0.9 范围，不太可能自行恢复。

---
