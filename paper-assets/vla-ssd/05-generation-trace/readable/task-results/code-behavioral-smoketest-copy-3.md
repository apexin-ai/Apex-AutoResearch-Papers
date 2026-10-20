# code behavioral smoketest

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_behavioral_smoketest_20260519T042351_result.json`
- **Structured JSON:** [`40fb3fa66e06856af024.json`](../../sessions/40/40fb3fa66e06856af024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境验证完成，smoke test 正在运行。汇报如下：

---

## 环境验证结果

| 项目 | 状态 | 详情 |
|------|------|------|
| conda env `libero` | ✅ | `/root/miniconda3/envs/libero/` |
| MuJoCo | ✅ 3.8.1 | 需在 shell 层面设 `LD_LIBRARY_PATH` (Python 内 `os.environ` 对当前进程 `dlopen` 无效) |
| EGL rendering | ✅ | `MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1` |
| LIBERO | ✅ | 需 `NUMBA_DISABLE_JIT=1` 绕过 NumPy 2.0 vs numba 不兼容 |
| Checkpoint | ✅ | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/` (4 shards, 加载成功) |
| 已有脚本 | ✅ | `behavioral_smoketest.py` 已存在 |

## 之前失败的原因（已修复）

之前 `behavioral_pilot_w4` SR=0/3 的根因是 **MuJoCo 加载失败**（`libmujoco.so.3.1.6 not found`），导致 env 根本无法正常创建。这次修复了两个关键问题：

1. **`LD_LIBRARY_PATH`**：必须在 shell 层面设置，不能在 Python 内用 `os.environ`（Linux `dlopen` 在进程启动时缓存 `LD_LIBRARY_PATH`）
2. **`MUJOCO_EGL_DEVICE_ID=1`**：robosuite 断言 EGL device ID 必须在 `CUDA_VISIBLE_DEVICES` 字符串中

## 当前状态

- **PID**: 107414，westd-19183 cuda:1
- **日志**: `/root/autodl-tmp/vla-ssd/results/behavioral_smoketest_v2.log`
- 模型已成功加载，Phase 1 (Baseline) 正在跑 3 episodes
- 预计 15-20 分钟完成
- Registry 已更新 notes（无法重置 DONE→RUNNING，notes 记录了 v2 重跑信息）

---
