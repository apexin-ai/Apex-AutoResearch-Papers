# infra server setup deploy v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server-setup-deploy-v2_20260515T122853_result.json`
- **Structured JSON:** [`b64553daddaf6ee7e779.json`](../../sessions/b6/b64553daddaf6ee7e779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度极慢（HF 无认证限速）。汇总当前状态。

## 部署状态汇总

### 已完成

| 项目 | 状态 |
|------|------|
| **服务器环境** | Python 3.12.3, torch 2.8.0+cu128, 2x RTX PRO 6000 Blackwell (98GB each) |
| **依赖包** | lerobot 0.5.1, transformers 5.8.1, peft 0.19.1, wandb 0.24.2, accelerate 1.13.0 |
| **代码部署** | 16 个文件全部部署（train.py, evaluate.py, run_mvp.sh, 5 configs, 7 imm 模块, _lerobot_compat.py） |
| **API 兼容修复** | `_lerobot_compat.py` 绕过 lerobot 0.5.x groot bug + 新导入路径 |
| **语法检查** | train.py, evaluate.py, 所有 imm 模块通过 |
| **Mock test** | `python -m imm.smolvla_wrapper` 全通过（forward/backward/eval） |

### 下载进行中（HF 无认证限速严重）

| 资源 | 进度 | 说明 |
|------|------|------|
| SmolVLM2-500M 基座模型 | ~387MB / ~1GB | 8/15 blobs 完成，7 个 stalled |
| SmolVLA 配置 | 9/10 文件完成 | 1 个大 blob 卡住 |
| 数据集 | metadata 完成 | 12 个视频文件下载 stuck |

### 需要注意的问题

1. **需要 HF_TOKEN** — 服务器无 HuggingFace 认证 token，大文件下载被严重限速。**建议设置 `HF_TOKEN` 环境变量后重新下载。**

2. **LIBERO 数据集不可用** — `lerobot/libero_object_no_noops` 在 lerobot v2 (0.5.x) 中不存在。当前用 `lerobot/aloha_sim_insertion_scripted_image` 作为替代。如果需要使用 LIBERO，需要找到 v2 格式的数据集名或自行转换。

3. **SmolVLA 模型配置差异** — lerobot/smolvla_base 的 config.json 显示 `prefix_length: 0`, `action_dim: 6`, `state_dim: 6`。train.py configs 中设置了 `action_dim: 720` (ACIS), 可能需要根据实际模型结构调整。

### 下一步

设置 HF token 后，重新运行模型/数据集下载即可完成全部环境搭建：
```bash
export HF_TOKEN="hf_your_token_here"
huggingface-cli login --token $HF_TOKEN
```

---
