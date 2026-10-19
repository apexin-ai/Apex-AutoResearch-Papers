# ssh urgent alpha sweep fix

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-alpha-sweep-fix_20260517T025643_result.json`
- **Structured JSON:** [`9282a21af21fc65ea8d5.json`](../../sessions/92/9282a21af21fc65ea8d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GPU 占用
| GPU | 显存 | 进程 |
|-----|------|------|
| 0 | 2734 MiB | alpha=0.0 eval (PID 837180) |
| 1 | 2894 MiB | alpha=0.1 eval (PID 751592) |

### 2. alpha=0.0
- **原因失败**：脚本含未识别参数 `--conditioning_mode concat`
- **修复**：已从 3 个脚本中删除该参数
- **重启**：tmux session `alpha_sweep_00`，PID 837180，正在跑 libero_spatial（4 suites: spatial/object/goal/libero_10）

### 3. alpha=0.1 (PID 751592)
- 运行 1h13m，libero_spatial 全部 10 个 task 目录已创建（`libero_spatial_0` ~ `_9`）
- 正在跑最后几个 episode 的 rollout，接近完成
- 当前 running_success_rate 显示 0.0%（单个 episode 的实时指标）
- **无 eval_info.json**——尚未完成汇总

### 4. alpha=0.3
- 未启动。等 alpha=0.1 完成释放 GPU 1 后启动
- 脚本已修复，可直接用

### 5. tmux sessions
```
alpha_sweep_00    — GPU 0, alpha=0.0 (刚启动)
alpha_sweep_0_1   — GPU 1, alpha=0.1 (接近完成)
```

### 下一步
alpha=0.1 预计很快完成 spatial。完成后需要在 GPU 1 上启动 alpha=0.3。是否需要我设置定时检查，在 alpha=0.1 结束后自动启动 0.3？

---
