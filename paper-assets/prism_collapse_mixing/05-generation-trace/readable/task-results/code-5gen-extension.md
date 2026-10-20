# code 5gen extension

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_5gen_extension_20260516T002113_result.json`
- **Structured JSON:** [`b4271ca6eadb084ce093.json`](../../sessions/b4/b4271ca6eadb084ce093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码已审查完毕。结论：

## 审查结果

### 已经是动态的（无需修改）

| 文件 | 机制 |
|------|------|
| `analyze_correlation.py` | `glob.glob("signals_gen*_seed*.json")` 自动发现，`gens = sorted(data[s].keys())` |
| `plot_results.py` | `glob.glob("signals_gen*_seed*.json")` 自动发现 |
| `plot_collapse_trajectory.py` | `glob.glob("signals_gen*_seed*.json")` 自动发现 |
| `train.py` | 接收 `--gen` 参数，无上限 |
| `compute_signals.py` | 接收 `--gen` 参数，无上限 |
| `generate_synthetic.py` | 接收 `--gen` 参数，无上限 |
| `prepare_data.py` / `prepare_train.py` / `build_train.py` | 数据准备脚本，无代数逻辑 |

### 唯一需关注的文件

**`run_pipeline.py`** — 已有 `--num_generations` 参数，**但默认值是 3**（第 154 行）。所有循环都用 `args.num_generations`，没有硬编码。运行 5 代只需：

```bash
python run_pipeline.py --num_generations 5
```

### 潜在问题

`real_pool.jsonl` 有 ~400M tokens。`split_real_pool()` 会均分给 `num_generations` 代：
- 3 代 → 每代 ~133M tokens（> 100M，够用）
- **5 代 → 每代 ~80M tokens（< `SYNTH_TOKENS_PER_GEN=100M`）**

合成数据每代生成 100M tokens，但真实数据只有 80M tokens，混合比例会从 1:1 变为 0.8:1。如果需要严格 1:1 混合，要么增大 `real_pool`（准备 500M+ tokens），要么把 `SYNTH_TOKENS_PER_GEN` 也改成可配置的。

**结论：代码已经支持 5 代训练，无需改代码。** 唯一要注意的是数据量够不够——如果需要保持 1:1 混合比例，需要准备更多真实数据。

---
