# code seed robustness prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed_robustness_prep_20260515T122922_result.json`
- **Structured JSON:** [`77e98616737428d31a7a.json`](../../sessions/77/77e98616737428d31a7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个脚本已部署到 `westd-11235:/root/trace-verdict-study/scripts/`：

**`run_seed_robustness.sh`** (108 行)
- `--gpu` 参数，默认 0
- 串行跑 seeds 42/123/456
- seed=42：检测 `vota/final/` 已有 checkpoint → 跳过训练直接评估
- seed=123/456：训练输出到 `vota_seed{123,456}/`，wandb run name 对应
- 每个 seed 完成后打印 accuracy + CI + per-class metrics
- 全部完成后调 `aggregate_seeds.py` 汇总

**`aggregate_seeds.py`** (212 行)
- 读取 3 个 eval_results.json，计算 accuracy/pass_f1/fail_f1 的 mean ± std
- Pairwise two-proportion z-test（检验任意两个 seed 的 accuracy 差异是否显著）
- 支持 `--prediction_paths` 传入 per-sample 预测做 McNemar test（continuity-corrected）
- 输出 STABLE / ACCEPTABLE / UNSTABLE verdict
- 无 scipy 依赖（纯 numpy + math.erfc）

启动命令（GPU 空闲后）：
```bash
bash /root/trace-verdict-study/scripts/run_seed_robustness.sh --gpu 0
```

---
