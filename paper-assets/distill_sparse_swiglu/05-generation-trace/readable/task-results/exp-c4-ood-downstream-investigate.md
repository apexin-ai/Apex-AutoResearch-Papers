# exp c4 ood downstream investigate

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c4_ood_downstream_investigate_20260520T115749_result.json`
- **Structured JSON:** [`7f09eb67e794ed25ba91.json`](../../sessions/7f/7f09eb67e794ed25ba91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process alive (PID 250944). Log output is buffered (nohup + Python full buffering) — actual progress won't appear until chunks flush. This is normal for 6-task downstream eval, expected runtime ~1-2 hours.

**调研结论：**

| 问题 | 结果 |
|------|------|
| `--calibration_data` 参数 | 原来不支持，已添加 (`choices=["wikitext2", "c4"]`) |
| Mask 预测方式 | `teal_global` = 静态 calibration-based；`per_token` = 动态每 token |
| C4 OOD downstream 是否可行 | **可行** — `teal_global` 模式下，改 calibration data 为 C4 即可测 predictor 对 calibration domain shift 的鲁棒性 |
| C4 数据 | 已有 `/root/autodl-tmp/data/c4_val/` (~800MB) |

**代码修改（benchmark_eval.py）：**
- L119: 新增 `--calibration_data` 参数
- L153: `get_calibration_ids()` 接受 `dataset` 参数
- L348, L374: 两个 call site 透传 `args.calibration_data`

**已提交实验：**
- `c4_ood_downstream_kl30` on westd-41718:cuda:1 (PID 250944)
- C4 calibration + teal_global + uniform 30% + 6 tasks (arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa)
- 对比基准：`bench_kl30_uniform`（WikiText-2 calibration 下的同 checkpoint 同 tasks）

日志：`/root/distill_sparse_swiglu/logs/c4_ood_downstream_kl30.log`

---
