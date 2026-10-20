# debug kill duplicate and behavioral pilot v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_kill_duplicate_and_behavioral_pilot_v2_20260518T114002_result.json`
- **Structured JSON:** [`51edf58270eac78ec56e.json`](../../sessions/51/51edf58270eac78ec56e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Phase 1 结果：FAIL，SR = 0/3

**不进入 Phase 2。**

### 完整数据

| Episode | Success | Reward | Steps |
|---------|---------|--------|-------|
| 0 | fail | 0.000 | 300 (max) |
| 1 | fail | 0.000 | 300 (max) |
| 2 | fail | 0.000 | 300 (max) |

### 诊断

**Action 范围**：min=-0.360, max=0.996 — 量级看起来合理（不像 unnorm_key 用错时全 0 或全极端值）

**可疑现象 — action[0] 锁定**：第一个 action 维度在前 5 步全部固定为 `0.236`，其余 6 维正常变化：
```
step 0: [0.236, -0.014,  0.360,  0.033,  0.082,  0.328, 0.996]
step 1: [0.236,  0.411, -0.044, -0.000,  0.098,  0.175, 0.275]
step 2: [0.236, -0.360, -0.132,  0.005, -0.009,  0.103, 0.243]
step 3: [0.236,  0.176, -0.140, -0.014,  0.043,  0.191, 0.094]
step 4: [0.236,  0.130, -0.074, -0.000,  0.135,  0.352, 0.996]
```

**Reward = 0.0（所有 episode）**：机器人在 300 步内没有任何任务进展。

### 可能原因

1. **action[0] 锁定**：第一个 token 的 argmax 总映射到同一个 bin，可能导致 x 方向运动受限
2. **Transformers 版本兼容性**：checkpoint 期望 `transformers==4.40.1`，环境实际可能存在 inference regression（使用 `device_map` 绕过 `.to()` segfault 也可能引入差异）
3. **`device_map` vs `.to()`**：原始 behavioral_pilot.py 用 `.to("cuda:0")`，但在 Blackwell GPU + PyTorch 2.10 上 segfault；改用 `device_map` 后模型加载方式不同，可能影响 inference 行为
4. **任务本身难度**：task 0 (open_the_middle_drawer) 可能对这个 checkpoint 本身就难

### 环境问题记录

调试过程中发现两个 Blackwell GPU 特有问题：
- `.to("cuda:0")` 导致 segfault（`device_map="cuda:0"` 修复）
- MuJoCo EGL 必须在 `device_map` 模型加载前初始化，否则 segfault

---
