# infra acib v3 dryrun

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_acib-v3-dryrun_20260515T204134_result.json`
- **Structured JSON:** [`ef83ea985807248f2cc0.json`](../../sessions/ef/ef83ea985807248f2cc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过。

## 结果汇总

### 代码检查（全部 PASSED）
| 检查项 | 状态 |
|--------|------|
| beta_warmup_steps arg | OK |
| beta_current warmup | OK |
| REQUESTS_CA_BUNDLE | OK |
| SSL_CERT_FILE | OK |
| HF_HUB_DISABLE_XET | OK |
| cosine schedule | OK |
| grad_clip | OK |

### 模型加载 + ACIB 初始化（OK）
- **模型**: 450,169,185 total, 100,004,001 trainable (22.2%)
- **ACIBLoss**: beta 可动态设置（warmup 逻辑可用）
- **ACIBScorer**: 正常初始化

### 全量 1-step dry-run（未完成）
- 数据集 `lerobot/libero` 的视频文件（457 个 mp4）未缓存，下载到 85% 时超时
- 原因：AutoDL 代理下载 HuggingFace 大文件慢，且 eval 任务占带宽

### run_acib_v3_train.sh
- 已创建并部署到 `/root/acib/scripts/run_acib_v3_train.sh`

### 需要在正式训练前完成的事项
1. **LIBERO 数据集下载**：训练开始前需要确保数据集完整缓存。建议在 eval 结束后、训练开始前，用后台命令预下载：
   ```
   CUDA_VISIBLE_DEVICES="" python3 -c "from lerobot.datasets.lerobot_dataset import LeRobotDataset; LeRobotDataset('lerobot/libero')"
   ```
2. **HF_TOKEN**：当前无认证，可能限速。设置 token 可加速下载

---
