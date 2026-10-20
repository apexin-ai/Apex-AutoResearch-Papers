# diagnose plan019 1 7b rsft s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan019_1_7b_rsft_s44_20260519T033955_result.json`
- **Structured JSON:** [`54e2672a6f3e0086458f.json`](../../sessions/54/54e2672a6f3e0086458f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

**不是 GPU 故障、不是 OOM、不是服务器重启。** 三个实验各有不同情况：

---

### 1. plan019_1_7b_rsft_s43 & plan019_1_7b_rsft_s44 — 训练实际已完成

两个训练都跑完了全部 567/567 步，权重已正常保存：

| 实验 | 输出目录 | global_step | max_steps | final loss | token acc |
|------|----------|-------------|-----------|------------|-----------|
| s43 | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/` | 567 | 567 | 0.5526 | 86.9% |
| s44 | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44/` | 567 | 567 | 0.5539 | 87.1% |

两者都有完整的 `adapter_model.safetensors` (279MB)、`adapter_config.json`（inference_mode=true）和 checkpoint-567。

**为什么被报 failed**：监控系统依赖 sentinel file (`/tmp/agent-ml-exit/`) 或 W&B 心跳判断进程状态。这两个训练进程正常退出后，没有对应的 exit file（`/tmp/agent-ml-exit/` 里没有 `plan019_1_7b_rsft_s43.exit` 或 `plan019_1_7b_rsft_s44.exit`），`~/runs/faith-evidence-ie/` 里也没有对应 log。说明这两个任务**不是通过 agent-ml registry 提交的**（没有 tmux sentinel trap），监控检测到 "进程消失 + 无 sentinel + 无 W&B" 就 auto-resolve 为 failed。

**结论：假阳性。训练成功完成，可以直接用这些权重跑 eval。**

---

### 2. d112_rsft_s44_ced_score — 网络不可达导致真正失败

日志 (`~/runs/faith-evidence-ie/d112_rsft_s44_ced_score.log`) 显示：
- 11:12 成功加载 24216 条记录（3027 unique docs）
- 加载 NLI 模型时尝试访问 `huggingface.co` → `Network is unreachable` (Errno 101)
- 重试 5 次均失败（11:12 → 11:13:58，共 ~90 秒）
- 最终被 `Terminated`（SIGTERM）

尽管训练脚本设了 `HF_HUB_OFFLINE=1`，但 `rsft_score_filter` 脚本加载 `cross-encoder/nli-deberta-v3-base` 时仍尝试联网。

**注意**：当前 tmux 里有一个新的 `d112_ced_score` session（11:20 创建，PID 604576），正在 GPU 0 上跑 `rsft_score_filter`（输入是 `4b_sft_s44`，非原来的任务），说明已被手动重启/替换。

---

### 3. plan019_8b_rsft_s44_eval — 正常运行中

- PID 598911，GPU 3，18882MiB
- 进度：131/247 batches（~53%）
- 每 batch 约 43-46 秒，预计还需 ~1.5 小时完成

---

### 当前 GPU 状态

| GPU | 显存 | 进程 | 状态 |
|-----|------|------|------|
| 0 | 1501MiB/32607MiB | PID 604576 (rsft_score_filter) | 运行中 |
| 1 | 0MiB | — | 空闲 |
| 2 | 0MiB | — | 空闲 |
| 3 | 18891MiB/32607MiB | PID 598911 (8B eval) | 运行中 |

---

### 可否安全重试

- **s43 / s44 训练**：无需重试，已成功完成。直接用权重跑 eval 即可。GPU 1 和 GPU 2 空闲可用。
- **d112_rsft_s44_ced_score**：需要确认 NLI 模型本地缓存是否存在，或确保网络可达后重试。当前 GPU 0 被 score_filter 占用，等其完成后可重试。

---
