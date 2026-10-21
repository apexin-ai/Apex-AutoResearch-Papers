# prep exp 017 018 scripts

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp-017-018-scripts_20260517T020717_result.json`
- **Structured JSON:** [`c29b30c3404d2c471793.json`](../../sessions/c2/c29b30c3404d2c471793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**产出总结**:

| 项目 | 状态 |
|------|------|
| **脚本位置** | `/root/symb_invariant_consensus/scripts/run_exp017_strategyqa.sh`&lt;br>`/root/symb_invariant_consensus/scripts/run_exp018_arc.sh` |
| **数据集** | `data/strategyqa_200.json` (200条, Yes/No常识推理)&lt;br>`data/arc_challenge_200.json` (200条, ABCD科学多选) |
| **eval脚本解析** | 两个 `--help` 均通过 |
| **数据格式** | 字段: `id, problem, choices, answer, dataset, level` |

**脚本配置**:
- 模型: Qwen2.5-14B-Instruct (`/root/autodl-tmp/models/Qwen2.5-14B-Instruct`)
- 参数: K=12, T=0.7, `--n-problems 60`, seed=42
- vLLM: port 8000, max-model-len 4096, gpu-util 0.9
- 输出: `results/exp017_strategyqa/` / `results/exp018_arc/`

两个脚本 self-contained，可直接 `bash scripts/run_exp017_strategyqa.sh` 执行。注意两个实验共用 port 8000，需串行运行（或改其中一个端口）。

---
