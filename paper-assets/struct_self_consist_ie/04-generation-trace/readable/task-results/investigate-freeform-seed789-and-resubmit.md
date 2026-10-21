# investigate freeform seed789 and resubmit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_freeform_seed789_and_resubmit_20260515T191050_result.json`
- **Structured JSON:** [`dfbbbde3fb13843392b3.json`](../../sessions/df/dfbbbde3fb13843392b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已掌握。

## 调查结论

**seed789 没有可用结果。** 目录 `exp_freeform_ablation_seed789/` 存在但完全为空。

- **v1**：vLLM EngineDeadError 崩溃，未产出任何数据
- **v2**：处理到 550/551 prompts（99.8%）时收到 SIGTERM，engine 被中止，结果未写入磁盘

### 就绪状态

| 项目 | 状态 |
|------|------|
| 模型 `checkpoints/qwen3-8b-scierc-merged-v2/` | OK |
| 脚本 `run_freeform_inference.py` | OK |
| 数据 `data/scierc/processed_data` | OK (551 instances) |
| cuda:2 | 空闲 (4 MiB, 0%) |

### 参考参数（seed123/456 一致）

```
n_instances=551, n_samples=8, temperature=1.0, max_tokens=1024, use_grammar=false
```

### 推荐提交命令

先清空旧的空目录，然后在 tmux 中运行：

```bash
cd /root/autodl-tmp/struct_self_consist_ie/
rm -rf results/exp_freeform_ablation_seed789/

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=2 nohup python run_freeform_inference.py \
  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --output_dir results/exp_freeform_ablation_seed789 \
  --seed 789 \
  --num_samples 8 \
  --temperature 1.0 \
  --max_tokens 1024 \
  > ~/runs/struct_self_consist_ie/exp_freeform_seed789_v3.log 2>&1 &
```

预计耗时 ~230s，与 seed123/456 一致。是否现在提交？

---
