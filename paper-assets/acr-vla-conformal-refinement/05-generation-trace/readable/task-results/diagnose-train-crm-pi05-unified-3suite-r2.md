# diagnose train crm pi05 unified 3suite r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train-crm-pi05-unified-3suite-r2_20260524T195302_result.json`
- **Structured JSON:** [`0f579a310cb380bd4101.json`](../../sessions/0f/0f579a310cb380bd4101.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已收集完毕。以下是诊断报告：

---

## 诊断报告：train-crm-pi05-unified-3suite-r2

### 失败原因：**平台级进程终止（非 OOM）**

### 证据

| 项目 | 结果 |
|------|------|
| 日志终止位置 | Epoch 26 batch 50/684 处收到 SIGKILL (PID 326314) |
| 日志最后时间 | 2026-05-25 03:55:53（运行约 9h17m，未触发 12h timeout） |
| 系统 RAM | 1.0TB 总量，仅用 41GB，**非系统内存 OOM** |
| GPU 显存 | GPU0 当前 580/24564 MiB（训练用 GPU 已释放），**非 GPU OOM** |
| 模型大小 | 仅 615,966 参数，batch_size=256 显存开销极小 |
| OOM 内核日志 | AutoDL 容器无 `/var/log/kern.log`、`/var/log/syslog`，无法访问 `dmesg`，但从资源余量判断不是 OOM |

日志中 `Killed` 后仍有 epoch 26 batch 100-250 的输出，这是因为 `timeout` 包装进程被杀后，Python 训练进程作为孤儿进程短暂继续运行了几个 batch 后也被终止。

**最可能原因**：AutoDL 平台层面终止（实例计费到期 / 控制台手动关机 / 平台维护）。

### 最后成功的 Checkpoint

| 文件 | 时间 |
|------|------|
| `checkpoint_epoch0025.pt` (7.4MB) | 2026-05-25 03:47 |
| `crm_best.pt` (2.5MB) | 2026-05-25 03:47 |

最佳 val_loss = **0.004790**（epoch 25），训练趋势仍在稳步下降。

### 修复方案

1. **恢复训练**：从 `checkpoint_epoch0025.pt` resume，只需跑剩余 25 个 epoch
2. 确认 AutoDL 实例有足够的计费时长（预估剩余训练需 ~9 小时）
3. 无需降 batch_size——资源充足，不存在 OOM 风险

---
