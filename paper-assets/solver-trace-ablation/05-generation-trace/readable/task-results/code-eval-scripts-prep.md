# code eval scripts prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-scripts-prep_20260514T013607_result.json`
- **Structured JSON:** [`5fafcfef5ea36cebfe8a.json`](../../sessions/5f/5fafcfef5ea36cebfe8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都就绪。

---

### 任务 1：plan005 held-out eval

`eval_sta.py` 无需修改，已支持所有需要的参数和输出格式。可直接执行的命令：

```bash
export CUDA_VISIBLE_DEVICES=0  # 根据空闲GPU调整
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python3 scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/plan005_eval_sta_held_out.json
```

### 任务 2：plan014 downstream validation

`eval_downstream.py` 已创建并验证。逻辑：
- 生成 FOL → Prover9 证明 conclusion → "true"；证明 ¬conclusion → "false"；都不行 → "unknown"
- 与 gold label 对比计算 accuracy，按 answer type 分组，输出 confusion matrix

可直接执行的命令（对多个 checkpoint 跑）：

```bash
# plan005 (exec+STA)
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python3 scripts/eval_downstream.py \
  --checkpoint_path /root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/plan014_downstream_plan005.json

# plan001 exec-only s42 (baseline对比)
python3 scripts/eval_downstream.py \
  --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/plan014_downstream_plan001_s42.json
```

---
