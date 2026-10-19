# diag eval object v5 full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-object-v5-full_20260513T234515_result.json`
- **Structured JSON:** [`f55577165b395653c902.json`](../../sessions/f5/f55577165b395653c902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 失败根因

**MuJoCo/EGL 非确定性 segfault + 缺少心跳输出导致监控系统误判。**

具体证据链：

1. **日志最后执行到**：`[eval] 10 tasks loaded.`——SmolVLA 加载成功（0.93GB GPU），10 个 LIBERO object 环境创建完毕，进入 rollout 循环后进程静默死亡。

2. **不是 OOM**：容器 cgroup 内存限制 60GB（`memory.max=64424509440`），实际 RSS ≈ 10GB，`oom_kill=0`。

3. **不是磁盘满**：根分区 58%（13GB 可用）。

4. **崩溃是 C 层 segfault**：无 Python traceback，SIGSEGV handler 未触发，无 sentinel 文件写出——典型的 MuJoCo/OpenGL 原生代码崩溃，绕过了所有 Python 级错误处理和 shell EXIT trap。

5. **非确定性**：我用相同参数手动跑了完整复现测试（SmolVLA + 10 envs + rollout K=10），有时通过有时崩溃。evaluate.py 直接跑（n_rollouts=2）也复现了崩溃（PID 124446 在 rollout 阶段死亡）。

6. **触发条件**：同一 GPU 上 PyTorch CUDA 推理（SmolVLA K=10 × 50 denoising steps）与 MuJoCo EGL 渲染（10 个 OffScreenRenderEnv 共存）并发使用。容器仅暴露 `/dev/nvidia3` + `/dev/dri/renderD131`（8 卡主机的第 3 块卡），EGL/CUDA 资源竞争。

7. **监控系统侧**：每 120 秒轮询检测进程存活，但 K=10 的 rollout 每步约 3-4 秒、每 5 rollouts 才打印一次。n_rollouts=10 时首次输出需 **~80 分钟**，进程在这段沉默期内崩溃后被标记为 "process dead 5×"。

### 建议修复方案

**方案 1（推荐）：懒加载环境 + 更频繁心跳**

修改 `evaluate.py`，不要预创建 10 个 env，每个 task 单独创建/销毁：

```python
# 改 load_libero_env 为 load_task_info（只返回元信息，不创建 env）
# 在 rollout 循环内：
for task_info in task_infos:
    env = OffScreenRenderEnv(**task_info["env_args"])  # 按需创建
    ...rollout...
    env.close()  # 用完即关
```

同时在 rollout_single 中每步/每 N 步打印心跳：
```python
if step % 50 == 0:
    print(f"[heartbeat] task={task_name} rollout={r} step={step}", flush=True)
```

**方案 2（快速验证）：用 osmesa 替代 EGL**

```bash
MUJOCO_GL=osmesa  # 替代 egl，软件渲染更稳定，速度慢 ~2x 但不会 segfault
```

**方案 3：减小并发压力**

- 先用 K=1 跑通验证流程
- 确认稳定后再提升到 K=10

---
