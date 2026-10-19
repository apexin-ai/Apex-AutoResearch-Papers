# diagnose eval obs only object norm003 seed62

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed62_20260521T004858_result.json`
- **Structured JSON:** [`c2c78c12f3a7e30cb882.json`](../../sessions/c2/c2c78c12f3a7e30cb882.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 1. 日志关键内容

**原始实验 (seed62)**:
```
nohup: failed to run command 'python': No such file or directory
```
纯 PATH 问题，`python` 未找到。

**重试实验 (seed62_r2)**:
```
[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)
[eval] Override max_correction_norm = 0.03
[eval] 10 tasks loaded.
  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5
```
- 创建时间 08:39:47，最后修改 08:48:01，运行约 8 分钟后**静默退出**
- 日志中**无任何 error/traceback/OOM/killed 信息**
- **未生成 JSON 输出文件**

### 2. 关键发现：批量静默死亡

同批次所有 norm003 实验都在相同时间窗口（08:44-08:48）异常退出：

| 实验 | 日志大小 | 最后状态 | 停止时间 |
|------|---------|----------|---------|
| seed62_r2 | 1622B | task 1, rollout 5/10 | 08:48 |
| seed63_r2 | 1609B | task 1, rollout 5/10 | 08:48 |
| seed64 | 1711B | task 1, rollout 10/10 | 08:48 |
| seed65 | 1538B | task 1, rollout 5/10 | 08:44 |

**均无错误输出，均未完成。**

### 3. 失败根因：GPU 显存 OOM 被系统 kill

当前服务器状态（08:50:42）：6× RTX 4090（24GB each），有 **10 个 python 进程**分布在 6 块 GPU 上，多块 GPU 双进程占用 ~11.4GB。

判断逻辑：
- 4 个进程在**同一时间窗口静默死亡** → 系统级 kill（非 Python 异常）
- 每个进程需 ~5.7GB 显存（SmolVLA + CRM + LIBERO 仿真），LIBERO rollout 过程中显存会动态增长
- 多进程共享 GPU 时，累积显存超过 24GB 限制 → CUDA OOM 或 OS OOM killer
- AutoDL 容器无 kern.log/syslog，无法直接确认，但行为模式完全吻合 OOM kill

### 4. 需要重试，建议修复方式

- **用 `CUDA_VISIBLE_DEVICES` 隔离 GPU**：每个评估进程独占一块 GPU
- **控制并发数**：最多 6 个并行（每 GPU 一个），不要在同一 GPU 上跑两个评估
- **或串行执行**：如果 GPU 资源紧张，排队逐个跑

---
