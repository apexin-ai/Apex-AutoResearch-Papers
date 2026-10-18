# diagnose openvla eval westd38929 batch fail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_openvla_eval_westd38929_batch_fail_20260521T070443_result.json`
- **Structured JSON:** [`c0065bdb2f38ee5ac82b.json`](../../sessions/c0/c0065bdb2f38ee5ac82b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 根因：AutoDL 容器 GPU 缩配

westd-38929 主机有 **9 块 NVIDIA RTX PRO 6000 Blackwell (97GB)**，但容器当前只挂载了 **1 块 GPU** (`/dev/nvidia2`)。4 个实验分别绑定 cuda:0/1/2/3，运行 ~1h43m 后 GPU 设备被平台回收，进程被 SIGKILL。

### 关键证据
| 指标 | 值 |
|------|-----|
| `nvidia-smi -L` | 仅 1 GPU (Device Minor 2) |
| `/proc/driver/nvidia/gpus/` | 主机 9 块 GPU |
| 日志停止时间 | 14:45-14:49（3 分钟跨度依次停止） |
| 日志末尾 | 正常进度输出，无 error/traceback |
| 实验进度 | 各完成 Task 1-3，Task 4/10 中被杀（~30%） |
| 系统 RAM | 1TB 中仅用 46GB（排除 CPU OOM） |

### 修复建议（未执行，等指令）
1. **优先**：AutoDL 控制台恢复至 4 GPU 配置，重跑 4 个实验
2. **备选**：单 GPU 顺序执行（每个 ~5.5h，共 ~22h）
3. 建议用 tmux 运行防止 SSH 断连

诊断已追加到 `memory.md` 失败模式记录段落。

---
