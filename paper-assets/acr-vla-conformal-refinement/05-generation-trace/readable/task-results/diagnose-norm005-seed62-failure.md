# diagnose norm005 seed62 failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_norm005-seed62-failure_20260521T011327_result.json`
- **Structured JSON:** [`4d09f0c7f1db08a78fae.json`](../../sessions/4d/4d09f0c7f1db08a78fae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**失败根因：进程被外部 SIGKILL 同时杀死，非代码错误。**

### 证据

- 3 个失败日志（seed61/62/63）全部停在 "rollout 5/10" 处，**无任何 Python traceback、CUDA error、segfault**，日志仅 13-14 行（~1.5KB）
- 同批次实际有 **5 个进程同时死亡**（还包括 norm003_seed64 和 norm01_seed60，这两个甚至没开始 rollout，停在 "10 tasks loaded"）
- 所有日志修改时间集中在 08:44-08:54，说明是同一时刻被杀
- 无 core dump，日志中无 "Killed" 字样
- 对比：同服务器上更早的成功实验（obs_only_object_*，4KB 完整日志）和当前正在运行的实验（seed71-75）均正常

### 根因判断

5 个 LIBERO eval 进程同时启动，每个都要加载 SmolVLA + 10 个 MuJoCo 仿真环境。并发环境初始化导致 **CPU RAM 峰值过高**，触发了 cgroup/容器 OOM killer 发送 SIGKILL。当前 1TB RAM 充足（已用 65GB），是因为失败批次已释放内存。

### 3 个实验同因？

是，同一批次同一原因。

### 是否影响当前运行实验？

**不影响。** nvidia-smi 显示 6 个 GPU 进程正常运行（PID 922504 等），GPU 温度 36-43°C，内存使用正常（~5.2GB/24GB）。

### 建议

1. **直接重跑**这 3 个（实际 5 个）失败实验，无需改配置
2. **控制并发数**：避免同时启动 5+ 个 eval 进程，建议每批最多 3-4 个，或错开启动时间（间隔 2-3 分钟让环境加载峰值错开）

---
