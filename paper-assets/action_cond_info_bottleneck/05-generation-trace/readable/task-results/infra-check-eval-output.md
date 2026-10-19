# infra check eval output

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-eval-output_20260515T180127_result.json`
- **Structured JSON:** [`3e611317c0a05d8e884d.json`](../../sessions/3e/3e611317c0a05d8e884d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断结果如下：

---

## 诊断报告

### 1. baseline_std (GPU 1) — 全部失败，零结果

**两次运行都失败了：**
- **第 1 次运行**（main.log 记录）：4 个 suite 全部 `ModuleNotFoundError: No module named 'robosuite'`
- **第 2 次运行**（per-suite .log 记录，tee 覆写了 1st run 日志）：4 个 suite 全部 `OSError: Can't load processor for 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'`，根因是 `[Errno 101] Network is unreachable`

**所有输出目录为空**（libero_spatial/, libero_object/, libero_goal/, libero_10/ 下均无文件）。GPU 1 完全空闲（1 MiB, 0%）。

### 2. baseline_plus (GPU 0) — 前 3 个 suite 失败，libero_10 刚启动

| Suite | 状态 | 说明 |
|-------|------|------|
| libero_spatial | FAILED | `OSError: Can't load processor` (网络不可达) |
| libero_object | FAILED | 同上 |
| libero_goal | FAILED | 同上，结束于 02:04:21 |
| libero_10 | **正在启动** | PID 85315，GPU 5.4GB，已建好 10 个 env + 加载完 weights，正在加载 processor |

**所有输出目录也为空**。libero_10 很可能也会因同样的 processor 下载错误而崩溃。

### 3. 数据集下载
- 正在下载 `lerobot/libero`，目前 570 MB（进度 ~84%/457 files），有间歇超时但在重试

### 4. GPU 利用率
- **GPU 0**: RTX PRO 6000 Blackwell, 5407 MiB / 97887 MiB, 0% util（刚加载完 weights）
- **GPU 1**: RTX PRO 6000 Blackwell, 1 MiB / 97887 MiB, 0% util（完全空闲）

### 5. 根因分析

**两个 eval 脚本都缺少 AutoDL 网络配置**：
```bash
# 缺少这些关键行：
source /etc/network_turbo
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1
```

eval 过程中 transformers 尝试从 HF Hub 下载 `SmolVLM2-500M-Video-Instruct` 的 `chat_template.jinja` 和 processor_config → 网络不可达 → 崩溃。模型权重能加载是因为已在本地缓存，但 processor 的额外文件缺失。

### 6. 建议修复

**方案 A（推荐）**：先用一个有网络的脚本把 processor 缓存到本地，然后离线跑 eval：
```bash
# 预缓存 processor
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
python3 -c "from transformers import AutoProcessor; AutoProcessor.from_pretrained('HuggingFaceTB/SmolVLM2-500M-Video-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"

# 然后在 eval 脚本中加：
export HF_HUB_OFFLINE=1
```

**方案 B**：直接在 eval 脚本开头加 `source /etc/network_turbo` + SSL 证书环境变量。

**需要重跑**：baseline_std 全部 4 个 suite + baseline_plus 的 spatial/object/goal（共 7 个 suite），libero_10 是否需要重跑取决于当前这次是否存活。

是否现在执行修复？

---
