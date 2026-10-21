# code plan 004b prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004b-prep_20260514T010212_result.json`
- **Structured JSON:** [`702a3188543ad2f25c4d.json`](../../sessions/70/702a3188543ad2f25c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕，汇总如下：

---

## 1. plan-002 代码验证：**PASS**

| 文件 | 状态 |
|------|------|
| `src/death_aware_labeling.py` | `expand_input_dirs()` 在 L138，`--dry_run` 支持正常 |
| `src/router_sft_eval.py` | 存在，imports 完整（torch, sklearn, peft, transformers） |
| `scripts/launch_plan002.sh` | Step 1/2/3 完整（labeling → SFT training → standalone eval） |

**dry-run 结果**：扫描 26 个 task 目录，145 episodes → 4386 SFT steps。分布：
- det-preferred: 68 episodes / 2160 steps
- internal-preferred: 1 episode / 30 steps
- no-preference: 76 episodes / 2196 steps
- 严重类别不均衡（internal 仅 1 episode），launch 脚本已配置 `--class_weights auto --upsample_minority`

## 2. plan-004b launch 脚本：**已存在**

路径：`scripts/launch_plan004b.sh`，包含：
- Step 1: `ablation_data_converter.py` 将 plan-002 labels 转 implicit 格式（依赖 `results/plan_001b_labels/`）
- Step 2: `ablation_implicit_1_7b.py train`（Qwen3-1.7B，gpu_id=1）
- 前置依赖 `ablation_data_converter.py` 和 `ablation_implicit_1_7b.py` 两个源文件尚需确认是否已编写

## 3. plan-001b 数据收集快照

两个 tmux session 运行中：`plan-001b-gpu0-v2`、`plan-001b-gpu1`

| task | episodes |
|------|----------|
| find-animal | 20 |
| find-non-living-thing | 20 |
| grow-fruit | 20 |
| identify-life-stages-1 | 20 |
| identify-life-stages-2 | **9** |
| inclined-plane-determine-angle | 20 |
| lifespan-longest-lived-then-shortest-lived | **17** |
| **total** | **126** |

5/7 tasks 已达 20 episodes；`identify-life-stages-2`（9）和 `lifespan-longest-lived-then-shortest-lived`（17）仍在收集中。

---
