# diagnose qwen25 14b scale 002 failure

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen25_14b_scale_002_failure_20260518T181615_result.json`
- **Structured JSON:** [`831fe206ecacc1e7face.json`](../../sessions/83/831fe206ecacc1e7face.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败原因
**注册实验 `qwen25_14b_scale_002` 的 EXIT_CODE=1 来自模型下载阶段**，不是实验本身。

具体错误：下载 `model-00005-of-00008.safetensors` 时，aria2c 遇到 SSL/TLS handshake failure（`The TLS connection was non-properly terminated`），hf-mirror.com CDN 连接断开。脚本有 `set -e`，download 子脚本返回非零码后整个 pipeline 立即退出。

### 失败阶段
**模型下载阶段**（第一步），Python 实验脚本从未执行。

### 实验实际已完成
好消息：实验**后来被成功重跑了**（可能是手动或另一个 job）。内部日志 `logs/qwen25_14b_scale_validation.log` 显示：
- 模型全部 8 个 shards 下载完成（时间戳 May 17 19:37 ~ May 18 01:25）
- Python pipeline 跑了 **24.8 小时**，于 May 19 02:12 完成
- 结果已保存到 `results/qwen25_14b_scale/summary.json`

### 实验结果摘要
| 指标 | 值 |
|------|-----|
| RF 4-class acc | 0.5405 [0.5337, 0.5474] |
| LR 4-class acc | 0.4881 [0.4815, 0.4949] |
| RF 3-class (no d0) acc | 0.5739 [0.5659, 0.5811] |
| d0v1 AUC | 0.6432 |
| d1v2 AUC | 0.7133 |
| d2v3 AUC | 0.7283 |
| Top features | kurt_ppl, skew_ppl, var_surprisal, p90_ppl, p90_surprisal |

### 修复建议
**无需修复**。实验已成功完成，结果完整。只需将 registry 中 `qwen25_14b_scale_002` 的状态更新为反映实际完成情况即可。

如果未来要防止同类下载失败，可以在 `download_qwen25_14b.sh` 中加 retry 逻辑（当前 aria2c 虽设了 `--max-tries=10`，但 SSL/TLS 断开不在其重试范围内），或将下载和实验分成两个独立 step，下载失败不影响后续重跑。

---
