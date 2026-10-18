# diagnose smolvla seed43 failed

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smolvla_seed43_failed_20260521T182700_result.json`
- **Structured JSON:** [`56506f0aeb2fdea3a90a.json`](../../sessions/56/56506f0aeb2fdea3a90a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：**监控误报（False Positive）**

3 个实验全部正常完成，不存在 OOM / 磁盘满 / CUDA error 等问题。Cron 监控检测到进程退出 + 无 W&B 信号，自动判定为失败，但实际上进程是正常结束的。

### 实际结果

| 实验 | SR | 结果文件 |
|---|---|---|
| baseline seed43 | **59.6%** (298/500) | `smolvla_baseline_object_seed43.json` |
| random k=0.95 seed43 | **0.2%** (1/500) | `smolvla_random_prune_k095_object_seed43.json` |
| l2_norm k=0.95 seed43 | **0.0%** (0/500) | `official_libero_object_l2_norm_k0.95_true_removal.json` |

时间线验证：日志显示 01:08-01:25 CST 启动，01:52-02:15 CST 完成（对应 UTC 17:08-18:15），cron 约 18:24 UTC 检测到进程消失。

### 影响

- **不影响** westd-38929 上其他实验。服务器当前空闲（4x RTX PRO 6000 全部 idle）
- **不需要重跑** — 结果已完整保存
- 已将 3 个实验的 registry conclusion 从 `failed` 修正为 `success`

### 建议

Cron 监控对无 W&B 的 eval 实验存在误判风险。可考虑在 eval 脚本结束时写一个 completion marker 文件（如 `.done`），让 cron 检查该文件来区分正常退出 vs 异常死亡。

---
