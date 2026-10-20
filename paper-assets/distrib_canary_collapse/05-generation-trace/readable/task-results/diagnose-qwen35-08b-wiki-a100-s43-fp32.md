# diagnose qwen35 08b wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen35_08b_wiki_a100_s43_fp32_20260520T061050_result.json`
- **Structured JSON:** [`fbe4c90fc83cd29fc7c0.json`](../../sessions/fb/fbe4c90fc83cd29fc7c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了。`submit_training_job` 调用时 `timeout_hours=12`，但日志显示实验从 02:07 到 14:07 正好 12 小时被杀。

关键数据整理：

**时间线：**
- 提交时间：2026-05-19T18:07 (UTC) = 2026-05-20 02:07 (+0800)
- 超时时间：2026-05-20 14:07 (+0800)，正好 12h
- s42 (parent) 用了 12h 43m 完成

**产出状态：**
- gen_0 → gen_9：全部有 metrics.json（10 代完整）
- gen_10：仅有 synthetic_data + trainer 目录，训练到 step 3309/5000 (66%) 被杀，无 checkpoint、无 metrics
- gen_8、gen_9 checkpoint 存在
- 无 all_metrics.json

**速度对比：**
- s43 每步 ~1.78 it/s，gen_10 剩余 1691 steps ≈ 16 分钟
- 加上 metrics 计算 ~5-10 分钟，总共还需 ~25 分钟
- s43 预计总时长 ~12h 25m，与 s42 的 12h 43m 接近

```json
{"root_cause":"timeout_hours=12 设置过紧，实际需要 ~12.5h（parent s42 用了 12h43m）。gen_10 训练到 step 3309/5000 (66%) 时被 SIGTERM 杀掉，距完成仅剩 ~25 分钟","error_type":"timeout","generations_completed":"10/10 metrics complete, gen_10 training interrupted at 66%","has_partial_results":true,"partial_metrics":"gen_0-gen_9 metrics.json 完整；gen_9: ppl=945.24, entropy=1.309, eff_rank=109.6, mauve=0.033; 缺 gen_10 metrics 和 all_metrics.json","fix_steps":["用 --start_gen 10 从 gen_9 checkpoint 恢复，仅需跑 gen_10 训练+评估 (~1.5h)","命令: python -u iterative_train.py --model_name /root/autodl-tmp/models/Qwen3.5-0.8B-Base/ --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --output_dir results/generalize/qwen35_08b_wiki_a100_s43_fp32 --start_gen 10","submit_training_job timeout_hours=3","清理 gen_10 现有的 synthetic_data 和 trainer 目录再恢复，或确认 --start_gen 会自动覆盖"],"recommended_timeout_hours":15}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "timeout_hours=12 设置过紧，实际需要 ~12.5h（parent s42 用了 12h43m）。gen_10 训练到 step 3309/5000 (66%) 时被 SIGTERM 杀掉，距完成仅剩 ~25 分钟",
    "error_type": "timeout",
    "generations_completed": "10/10 metrics complete, gen_10 training interrupted at 66%",
    "has_partial_results": true,
    "partial_metrics": "gen_0-gen_9 metrics.json 完整；gen_9: ppl=945.24, entropy=1.309, eff_rank=109.6, mauve=0.033; 缺 gen_10 metrics 和 all_metrics.json",
    "fix_steps": [
      "用 --start_gen 10 从 gen_9 checkpoint 恢复，仅需跑 gen_10 训练+评估 (~1.5h)",
      "命令: python -u iterative_train.py --model_name /root/autodl-tmp/models/Qwen3.5-0.8B-Base/ --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --output_dir results/generalize/qwen35_08b_wiki_a100_s43_fp32 --start_gen 10",
      "submit_training_job timeout_hours=3",
      "清理 gen_10 现有的 synthetic_data 和 trainer 目录再恢复，或确认 --start_gen 会自动覆盖"
    ],
    "recommended_timeout_hours": 15
  }
}
```

</details>

---
