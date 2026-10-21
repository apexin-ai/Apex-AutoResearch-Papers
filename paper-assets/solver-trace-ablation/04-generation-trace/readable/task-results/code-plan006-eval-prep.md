# code plan006 eval prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-eval-prep_20260514T111651_result.json`
- **Structured JSON:** [`b24c45e776351f62df6d.json`](../../sessions/b2/b24c45e776351f62df6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析结果：

## eval_sta.py 是否需要修改：**不需要**

eval_sta.py 从数据中只读取 `context`、`question`、`answer` 三个自然语言字段（第230-232行），完全不引用 `prolog_premises`/`prolog_query`/`fol_premises`/`fol_conclusion`。Prolog eval 流程：

1. `--logic_type prolog` → 选择 PROLOG_SYSTEM_PROMPT + PROLOG_USER_TEMPLATE + `prolog_sta_reward` 作为 reward_fn + `prolog` solver
2. 把自然语言 context/question 喂给模型，模型生成 Prolog formalization
3. `prolog_sta_reward()` 解析 formalization 文本提取 clauses 和 query，用 swipl 验证

**空的 `prolog_premises`/`prolog_query` 字段完全不影响 eval。**

## 训练状态

当前 step 444/500，约 5-6 分钟后完成。完成后最终模型权重会保存到 `/root/autodl-tmp/outputs/plan006_prolog_exec_s42/` 根目录（参照 plan006-prolog-sta-s42 的模式）。

## 完整 eval 命令

```bash
# 遵循 C002/C005：必须显式设 CUDA_VISIBLE_DEVICES
export CUDA_VISIBLE_DEVICES=<空闲GPU编号>

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation

python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/plan006_prolog_exec_s42 \
  --data_path data/test_held_out.jsonl \
  --output_path /root/autodl-tmp/outputs/plan006_prolog_exec_s42/eval_results.json \
  --logic_type prolog \
  --max_samples 100
```

## 注意事项

1. **GPU 分配**：运行前需确认哪张 GPU 空闲（`nvidia-smi`），显式设置 `CUDA_VISIBLE_DEVICES`
2. **数据选择**：plan006-prolog-sta-s42 的 eval 用的是 `train_500_seed42.jsonl --max_samples 100`（不是 test set）。如果需要跨实验可比，应与之保持一致。如用 `test_held_out.jsonl` 则是 100 条测试集
3. **等训练完成**：当前只有 checkpoint-400，须等最终模型权重保存到根目录后才能 eval。如果着急，也可先 eval checkpoint-400：`--model_path /root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-400`
4. **预期结果**：根据训练日志，exec-only 模式下 prove_rate≈1.0 但 ISR 极低（~0.05-0.1），与 sta 模式（ISR=0.5, 100% H7）形成对比。exec-only 不优化 ISR，所以 eval ISR 可能更低

---
