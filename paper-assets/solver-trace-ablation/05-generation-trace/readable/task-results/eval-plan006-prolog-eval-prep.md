# eval plan006 prolog eval prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan006-prolog-eval-prep_20260514T111715_result.json`
- **Structured JSON:** [`1bde5ac4f135befadc42.json`](../../sessions/1b/1bde5ac4f135befadc42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结如下：

## 分析结果

### eval_sta.py 不需要修改

eval_sta.py 从数据集只读 3 个字段：`context`、`question`、`answer`（第 210-212 行）。**完全不读 `prolog_premises`/`prolog_query`/`fol_premises`/`fol_conclusion`**。

`prolog_sta_reward` 函数也不从 `problem` dict 读任何数据字段——它只解析模型生成的 `formalization` 文本来提取 clauses 和 query。

所以空字段问题不存在，eval 可以直接跑。

### eval 数据

使用 `data/proofwriter_fol_100.jsonl`（100 条，与 plan006-prolog-sta-s42 评估用的相同）。该文件包含 `context`/`question`/`answer` 字段，完全够用。

### Checkpoint 状态

当前 `/root/autodl-tmp/outputs/plan006_prolog_exec_s42/` 下有 `checkpoint-400`。训练完成后会出现 `checkpoint-500`（`save_total_limit=1` 会自动删除 checkpoint-400）。

### Eval 命令

```bash
cd /root/solver-trace-ablation && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export CUDA_VISIBLE_DEVICES=&lt;GPU_ID> && \
python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --logic_type prolog \
  --output_path /root/autodl-tmp/outputs/eval_sta_plan006_prolog_exec_s42.json
```

注意：
- `&lt;GPU_ID>` 需要在训练结束后确认哪张卡空闲（C002/C005 约束）
- 如果训练结束后最终模型在根目录而非 checkpoint-500，改 `--model_path` 为 `/root/autodl-tmp/outputs/plan006_prolog_exec_s42`
- 训练完成后先 `ls /root/autodl-tmp/outputs/plan006_prolog_exec_s42/` 确认 checkpoint 路径

### 预计 eval 时间

参照 plan006-prolog-sta-s42：107.5s（1.1s/sample × 100 samples），约 **2 分钟**。

---
