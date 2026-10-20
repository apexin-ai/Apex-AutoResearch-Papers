# code behavioral smoketest

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_behavioral_smoketest_20260519T044416_result.json`
- **Structured JSON:** [`6751fd0bef064041b21b.json`](../../sessions/67/6751fd0bef064041b21b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行中。ep 0 完成：fail，R=0.000，300 steps，52s。还有 ep 1 和 ep 2。

**当前状态汇总：**

- **环境修复**：修复了 3 个问题：
  1. MuJoCo `LD_LIBRARY_PATH` 缺失 → 添加 mujoco 包目录
  2. `MUJOCO_EGL_DEVICE_ID` 与 `CUDA_VISIBLE_DEVICES` 不匹配 → 设为 1
  3. numpy/scipy/accelerate 版本冲突 → 升级 scipy 1.11.4→1.15.3，numpy 恢复 2.2.6

- **Smoke test 正在跑**：PID=111373，cuda:1，1 task × 3 episodes × baseline
  - ep 0: fail (R=0, 300 steps, 52s)
  - ep 1-2 进行中
  - 预计 ~3min 后完成

- **注意**：之前的 smoketest 也是 SR=0%。如果本轮也全 fail，说明问题不在环境而在 checkpoint/task 匹配度，需要进一步排查。

- **Registry**: `behavioral_smoketest` → RUNNING

---
