# ops prep s43 eval pipeline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-s43-eval-pipeline_20260515T033726_result.json`
- **Structured JSON:** [`93c897f86dbd27997682.json`](../../sessions/93/93c897f86dbd27997682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇报如下：

---

## Eval Pipeline 预检结果

### 1. 就绪状态：**是（就绪）**

| 检查项 | 状态 | 说明 |
|--------|------|------|
| `eval_sta.py` | ✓ | 位于 `scripts/eval_sta.py`（非根目录） |
| 测试集 | ✓ | `data/proofwriter_fol_100.jsonl`，100 条。**注意：任务描述的 `proofwriter_test_normal.jsonl` 不存在**，按 C008 约束必须用 `proofwriter_fol_100.jsonl` |
| Solvers | ✓ | Prover9/SWI-Prolog/Z3 已确认可用 |
| 磁盘 | ✓ | 82G/250G (33%)，剩余 169G，eval 空间充足 |

### 2. 训练进程状态

- PID 117566 正在运行，已运行 **~55 分钟**
- 输出目录 `/root/autodl-tmp/outputs/exp1_random_b03_s43_r4`，当前 **16GB**
- GPU: cuda:0

### 3. 推荐 Eval 命令

训练完成后，checkpoint 路径为 `/root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500`。

```bash
export CUDA_VISIBLE_DEVICES=0 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/solver-trace-ablation && \
python3 scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/exp1_random_b03_s43_r4/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43_r4.json \
  --logic_type fol \
  --max_new_tokens 512 \
  --timeout 5
```

### 4. 关键修正

任务描述中 `proofwriter_test_normal.jsonl`（258 条）在服务器上不存在。所有历史 eval（含 s42/s44）均使用 `proofwriter_fol_100.jsonl`（100 条），C008/C009 约束也明确要求此文件。eval 应沿用。

---
