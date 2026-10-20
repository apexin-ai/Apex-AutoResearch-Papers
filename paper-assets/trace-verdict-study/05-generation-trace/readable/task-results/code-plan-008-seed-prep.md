# code plan 008 seed prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_seed_prep_20260515T120629_result.json`
- **Structured JSON:** [`01bc002ba65f234fca4c.json`](../../sessions/01/01bc002ba65f234fca4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出**
| 文件 | 位置 |
|------|------|
| 批量训练脚本 | `/root/trace-verdict-study/scripts/run_seed_robustness.sh` |
| 聚合分析脚本 | `/root/trace-verdict-study/scripts/aggregate_seeds.py` |

**dry-run 结果**
- `run_seed_robustness.sh --help` ✅ 正常输出用法
- `aggregate_seeds.py --help` ✅ 正常输出用法

**参数确认**
- `train_sft.py` 支持 `--seed`（默认42）、`--gradient_checkpointing` ✅
- `evaluate.py` 支持 `--output`、`--checkpoint_dir` ✅
- 脚本内已设 `CUDA_VISIBLE_DEVICES` 和 `--gradient_checkpointing`

**运行方式**
```bash
# 默认跑 seed 123, 456
bash scripts/run_seed_robustness.sh --gpu 0

# 聚合所有3个seed（含已跑完的seed42）
python scripts/aggregate_seeds.py --paths \
  /root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/eval_results.json \
  /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123/final/eval_results.json \
  /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final/eval_results.json
```

**预计时间**: 每个 seed ~2.5h（训练2h + 评估15min + 模型加载等），两个 seed 串行共 ~5h。

**注意**: seed 42 结果目录是 `vota/`（无 seed 后缀），新的是 `vota_seed{123,456}/`，聚合时需要用 `--paths` 显式指定三个路径。McNemar 检验需要 per-sample predictions（当前 evaluate.py 不保存），aggregate 脚本中已注明。

---
