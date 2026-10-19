# ops unzip assets tail logs

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unzip-assets-tail-logs_20260516T042424_result.json`
- **Structured JSON:** [`3a93d8e56520e4eca7d4.json`](../../sessions/3a/3a93d8e56520e4eca7d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

解压进程仍在运行。

## 结果报告

### (a) LIBERO-Plus 解压
- `assets.zip` 位于 `/root/autodl-tmp/libero_plus_assets/assets.zip`（非用户给的路径）
- 文件数量多，30s 内未完成，已用 nohup 后台执行，PID=395986，进程确认在跑
- 日志：`/tmp/unzip_libero.log`，可稍后用 `tail /tmp/unzip_libero.log` 确认完成

### (b) 4 路训练状态

所有训练总 steps = **10,000**，每 50 步 ≈ 51s（~1.02s/step）

| 训练 | PID | 当前 Step | Loss | LR | Grad Norm |
|------|--------|-----------|-------|----|-----------|
| lora_visual (r16) | 391439 | **1750** | 0.0139 | 1.87e-4 | 0.04 |
| lora_physical (r16) | 391516 | **1750** | 0.0136 | 1.87e-4 | 0.04 |
| lora_universal_r16 | 391658 | **1750** | 0.0144 | 1.87e-4 | 0.03 |
| lora_universal_r48 | 391805 | **1750** | 0.0139 | 1.87e-4 | 0.02 |

**进度**：1750/10000 = **17.5%**

**预计完成时间**：剩余 8250 步，50 步/51s → 还需 ~8415s ≈ **2h20min** → **约 14:45（北京时间）**

4 路 loss 都已从 ~0.095 降到 ~0.014 并趋于平稳，训练正常。

---
