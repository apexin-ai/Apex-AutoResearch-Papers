# debug exp006 lmeval config

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp006-lmeval-config_20260514T050059_result.json`
- **Structured JSON:** [`ebc1cf443623cdeed5e0.json`](../../sessions/eb/ebc1cf443623cdeed5e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成，以下是全部结果。

---

## 1. lm-eval 完整调用配置

来源：`scripts/exp006_evaluate.py`，shell 脚本 `run_exp006.sh` 未覆盖任何默认参数。

实际调用等效于：
```python
lm_eval.simple_evaluate(
    model="hf",
    model_args="pretrained=&lt;model>,dtype=bfloat16,trust_remote_code=True,cache_dir=&lt;cache>,peft=&lt;adapter>",
    tasks=["mmlu", "hellaswag"],
    batch_size="auto",
    device="cuda:0",
)
```

| 参数 | 实际值 | 说明 |
|------|--------|------|
| `tasks` | `["mmlu", "hellaswag"]` | MMLU 展开为 57 个子任务 |
| `batch_size` | `"auto"` | lm-eval 自动探测 GPU 显存上限 |
| `num_fewshot` | **未设置** → 使用 task YAML 默认值（MMLU: 5-shot, HellaSwag: 10-shot） | 代码中未传 `num_fewshot` 参数 |
| `device` | `"cuda:0"` | 显式指定 GPU |

## 2. Eval 在 GPU 上运行

`device="cuda:0"` 在 `simple_evaluate()` 中显式设置，确认 eval 在 GPU 上执行。

## 3. Eval 耗时样本（6 个已完成 runs）

通过 `final_adapter` 目录 mtime（training 结束）和 `eval_results.json` mtime（eval 结束）计算：

| Run | adapter 完成 | eval 完成 | Eval 耗时 |
|-----|-------------|-----------|-----------|
| no-filter_s42 | 05:39:16 | 05:46:54 | **7m 38s** |
| no-filter_s123 | 06:23:34 | 06:31:08 | **7m 33s** |
| no-filter_s456 | 07:07:37 | 07:15:19 | **7m 42s** |
| no-filter_s789 | 07:51:47 | 07:59:24 | **7m 37s** |
| no-filter_s1024 | 08:35:52 | 08:43:29 | **7m 37s** |
| binary-ours_s42 | 09:21:08 | 09:28:49 | **7m 41s** |

**Eval 平均耗时：7m 38s**，方差极小（±5s），非常稳定。

每个 run 总耗时 ≈ 37min（training）+ 7.6min（eval）+ 3s（sleep）≈ **44.6min/run**。

binary-drayson_s42 正在训练中（有 checkpoint，无 final_adapter）。

## 4. 优化空间

- **`batch_size="auto"` 已经是最优设置**，lm-eval 自动探测显存上限，无需手动调大。
- **0-shot 替代 5-shot MMLU** 可以减少 eval 时间（减少 prompt 长度和推理量），但会改变评估协议。
- **减少 MMLU 子任务数** 可以缩短时间，但失去完整 MMLU 分数。
- 7.6min 对 1.5B 模型跑完整 MMLU（57 子任务, ~14k 题, 5-shot）+ HellaSwag（~10k 题）已经很快，没有明显瓶颈。

## 5. 热修改可行性

技术上可以——`run_exp006.sh` 每个 run 都重新调用 `python3 exp006_evaluate.py`，修改该文件会对后续 runs 生效。

**但不建议**：修改 eval 配置（如 fewshot 数、tasks 列表）会导致已完成 runs 和后续 runs 的评估协议不一致，结果不可比。当前 eval 仅占总耗时 17%（7.6min/44.6min），优化 eval 的收益有限。

---
