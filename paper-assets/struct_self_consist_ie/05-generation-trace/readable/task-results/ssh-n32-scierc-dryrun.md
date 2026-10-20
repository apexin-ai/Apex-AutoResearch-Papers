# ssh n32 scierc dryrun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n32_scierc_dryrun_20260522T032918_result.json`
- **Structured JSON:** [`c379d7b108a7cd08fbfc.json`](../../sessions/c3/c379d7b108a7cd08fbfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全成功。以下是验证报告：

---

## SciERC N=32 Dry-run 环境验证报告

### 1. 环境状态
| 项目 | 状态 |
|------|------|
| Python | 3.12.3 |
| vLLM | 0.18.1 |
| GPU | 4x RTX 5090 (32GB each), 全部空闲 |
| 磁盘 | 250GB 用了 91%，**剩余 24GB** |

### 2. SciERC Finetuned Model Checkpoint
- **路径**: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2`
- **大小**: 16GB (merged, bf16)
- 模型加载耗时 ~5s，总引擎初始化 ~11s

### 3. SciERC 数据
- **路径**: `/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/`
- 100 篇文档 → **551 个 sentence-level instances**（与之前 N=16 实验一致）

### 4. Dry-run 结果: 成功
- 5 instances × 32 samples = 160 prompts，**12 秒**完成采样（~13 it/s）
- Greedy F1: 0.8947, Oracle F1: 0.9474
- Verdict: **PASS**

### 5. 预估全量运行
- 551 instances × 32 samples = 17,632 prompts
- 按 12.36 it/s 推算，采样阶段 ~24 分钟
- 加模型加载 + greedy + 评估，**总计约 30-40 分钟**
- 之前 N=16 的 `samples.jsonl` 约 20MB，N=32 预估 **~37-40MB**（与 `scierc_n16_s456` 的 37MB 相当或略大）
- 磁盘 24GB 剩余足够

### 6. 正式提交命令

```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --data_dir data/scierc/processed_data \
  --dataset scierc \
  --subtask ner \
  --n_samples 32 \
  --temperature 1.0 \
  --seed 456 \
  --collect_logprobs \
  --output_dir output/scierc_n32_s456/' > output/scierc_n32_s456.log 2>&1 &
echo "PID=$!"
```

如需多 seed 运行，替换 `--seed 456` 为 `123` / `42`，对应修改输出目录。

---
