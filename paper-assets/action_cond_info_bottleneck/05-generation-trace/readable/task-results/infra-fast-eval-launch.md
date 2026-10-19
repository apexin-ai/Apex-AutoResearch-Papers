# infra fast eval launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fast-eval-launch_20260515T164645_result.json`
- **Structured JSON:** [`dc86a7757a2d09230933.json`](../../sessions/dc/dc86a7757a2d09230933.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 已完成
- **环境就绪**: lerobot 0.5.1, torch 2.10.0+cu128, mujoco 3.8.1, libero/robomimic/bddl 已装
- **EGL 渲染验证通过**: `MUJOCO_GL=egl PYOPENGL_PLATFORM=egl`
- **lerobot-eval pipeline 验证通过**: 用 smolvla_base 做了 dry run，命令语法正确
- **实验已注册**: `mvp1_baseline_std` (RUNNING), `mvp1_baseline_plus` (RUNNING)
- **eval 脚本已创建**: `/root/acib/scripts/run_eval_std.sh`, `run_eval_plus.sh`
- **自动启动 watcher 运行中**: 各自独立监控模型下载，完成后立即启动 eval

### 当前阻塞：模型下载
HuggingFace 代理下载速度 ~15MB/min：

| 模型 | 进度 | 预计完成 |
|------|------|----------|
| `lerobot/smolvla_libero` (865MB) | 650M (75%) | ~15 min |
| `lerobot/smolvla_libero_plus` (865MB) | 310M (36%) | ~37 min |

### 自动流程
- **PID 28824**: 下载进程（两个模型并行下载）
- **PID 33094**: watcher → libero 下载完成后自动启动 `run_eval_std.sh`（GPU 0）
- **PID 33095**: watcher → libero_plus 下载完成后自动启动 `run_eval_plus.sh`（GPU 1）
- **Cron 61e0cba1**: 每 10 分钟自动检查 eval 进度

### eval 命令（每个模型跑 4 个 suite × 50 episodes）
```
lerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero \
  --env.task={libero_spatial,libero_object,libero_goal,libero_10} \
  --eval.n_episodes=50 --eval.batch_size=1
```

GPU 0 的 eval 预计 ~15 分钟后开始运行，GPU 1 约 37 分钟后开始。

---
