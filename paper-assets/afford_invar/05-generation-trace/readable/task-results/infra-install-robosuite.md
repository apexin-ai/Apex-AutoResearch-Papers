# infra install robosuite

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_install-robosuite_20260519T225340_result.json`
- **Structured JSON:** [`f8410df04c73177a8e1f.json`](../../sessions/f8/f8410df04c73177a8e1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 安装结果

| 包 | 版本 | 状态 |
|---|---|---|
| mujoco | 3.8.1 | 新装 |
| robosuite | 1.5.2 | 新装 |
| bddl | 3.6.0 | 新装 |
| easydict | 1.13 | 新装 |
| cloudpickle | 3.1.2 | 新装 |
| imageio[ffmpeg] | 2.37.3 + ffmpeg | 已有+补装 ffmpeg |
| libero | 本地安装 | 已有 |
| libegl1-mesa-dev | 系统包 | 新装 |

### Rendering
- **EGL** 模式正常工作
- `export MUJOCO_GL=egl` 已写入 `/root/.bashrc`

### Sanity Check
- robosuite `Lift` 环境创建/reset/close：**通过**
- LIBERO benchmark 访问（6 个 suite: libero_spatial, libero_object, libero_goal, libero_90, libero_10, libero_100）：**通过**
- LIBERO config 写入 `/root/.libero/config.yaml`，datasets 目录指向 `/root/autodl-tmp/libero_datasets`

### 注意
- numpy 被降级到 1.26.4（robosuite 依赖），训练中的进程不受影响（已加载旧版本到内存）
- LIBERO benchmark API 用 `get_num_tasks()` / `get_task(i)` 而非 `n_tasks` / `task.language`

---
