# monitor exp013d early steps

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013d-early-steps_20260514T083537_result.json`
- **Structured JSON:** [`ab80d2a897c04e0e9803.json`](../../sessions/ab/ab80d2a897c04e0e9803.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控结果

**两个实验均已崩溃，GPU 已释放（3 MiB each）。**

### exp013d（PID 272157）— 目标实验
| 项目 | 状态 |
|------|------|
| 崩溃时间 | 16:36（初始化阶段） |
| 崩溃点 | 模型加载后，Raylet 被 SIGKILL |
| 根因 | **`RAY_object_store_memory=30GB` 未生效**，object store 仍为默认 70.3GB |
| 到达 step 6？ | **否** — 从未开始任何训练步骤 |

### exp012_test（PID 277765）— 不明来源的测试实验
| 项目 | 状态 |
|------|------|
| 配置 | `_alfworld_exp012_reward_fix`（不是 dense reward） |
| env_groups | **8**（不是 4） |
| RAY_object_store_memory | **未设置** |
| 进展 | 完成 step 5 validation（success=0%, reward=0） |
| 崩溃点 | **step 6 training rollout** — Actor worker OOM killed |
| 崩溃原因 | 和 exp013b/c 完全一致：env_groups=8 + object_store 70GB → OOM |

### 诊断

1. **exp013d 的核心问题**：`RAY_object_store_memory` 环境变量在启动 Ray 之前未被 export，所以 Ray 用了默认值（~70% 可见内存 ≈ 70GB）。`env_groups=4` 已正确配置，但环境变量缺失导致初始化阶段就崩溃了（比 exp013b/c 更早）。

2. **exp012_test 是谁启动的？** 可能是另一个 Worker 在 exp013d 崩溃后启动的。它用的是 env_groups=8 + 无 object_store 限制，注定重蹈覆辙。

3. **内存关口未验证** — 两个实验都没活到 step 6 rollout。

### 下一步
重启 exp013d 时必须确保：
```bash
export RAY_object_store_memory=32212254720  # 30GB in bytes
```
在 `python train.py` **之前**执行。可以用 `grep RAY_object /proc/&lt;pid>/environ` 验证。

---
