# prep swebench dryrun random s42

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_swebench_dryrun_random_s42_20260514T080904_result.json`
- **Structured JSON:** [`22482b69563c77673c05.json`](../../sessions/22/22482b69563c77673c05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。

---

## SWE-bench Eval Pipeline Dry-Run 报告

### 1. Dry-run 结果：通过（附 1 个前置条件）

| 测试项 | 结果 | 说明 |
|--------|------|------|
| Pipeline 逻辑 (mock) | ✅ | 5 instances, 正确输出 jsonl + summary.json |
| 数据加载 (HF dataset) | ✅ | SWE-bench Lite 缓存可用, 需 `HF_DATASETS_OFFLINE=1` |
| 模型加载 (CPU) | ✅ | 12.1s, Qwen2.5-Coder-3B + LoRA, 6.2GB model.pt |
| 模型推理 (CPU) | ✅ | 3 candidates in 5.8s, 排名语义正确（frobnicator 文件排第一） |
| 输出格式 | ✅ | `per_instance_results.jsonl` + `summary.json` 格式正确 |
| Resume 支持 | ✅ | 正确跳过已完成 instances |
| 错误处理 | ✅ | clone 失败优雅处理, 不中断 pipeline |
| **Repo clone** | ❌ | **SWE-bench 12 个 repo 均未缓存, 与 M1 训练数据无重叠** |

### 2. 需修复的问题

**唯一 blocker**：SWE-bench Lite 的 12 个 repo（astropy, django, matplotlib, seaborn, flask, requests, xarray, pylint, pytest, scikit-learn, sphinx, sympy）全部不在 `/root/autodl-tmp/structfuse/full_m1_data/repos/` 中。正式 eval 前必须启用网络 `source /etc/network_turbo`，eval 脚本会按需 clone（首次约 10 分钟）。

**非关键**：
- `kernels` 包未装 → warning only，不影响 float32/float16 推理
- HF Hub 不可达 → 已缓存, 设 `HF_DATASETS_OFFLINE=1` 即可

### 3. 正式 Eval 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
cd /root/structfuse

export HF_DATASETS_OFFLINE=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/qwen_random_s42_recall \
    --device cuda \
    --batch-size 16 \
    --repo-cache-dir /root/autodl-tmp/structfuse/full_m1_data/repos
```

### 4. 耗时预估

- CPU baseline: 3 texts → 5.8s（~2s/text）
- GPU (RTX PRO 6000) 预估 10-20x faster → ~0.1-0.2s/text
- 平均每 instance ~200-500 .py files → GPU ~10-30s/instance
- 300 instances + 12 repos 首次 clone
- **总计约 1-3 小时**（单 GPU）

### 5. 潜在问题

- 大 repo（django ~4000 .py files, sympy ~1500）可能单 instance 耗时 2-5 分钟
- `--pool-size` 参数可限制每 instance 最大候选文件数，加速但牺牲 recall
- 支持 resume，如果中途中断可直接重跑，不会重复已完成的 instances

---
