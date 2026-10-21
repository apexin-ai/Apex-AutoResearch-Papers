# code plan 003 e2e eval prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-003-e2e-eval-prep_20260514T062439_result.json`
- **Structured JSON:** [`c36b5e21b4c93b5c7ba4.json`](../../sessions/c3/c36b5e21b4c93b5c7ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是报告。

---

## Plan-003 端到端评估：调研报告

### 一、现有代码组件清单

| 文件 | 作用 | 对 plan-003 的价值 |
|------|------|-------------------|
| `src/ablation_eval_common.py` | 核心 eval 框架：`run_routed_episode()` + `run_ablation_eval()` + `EvalConfig` + `RouterFn` 类型签名 | **直接复用** — plan-003 的骨架已在此 |
| `src/llm_agent.py` | Qwen2.5-7B ReAct agent + vLLM serving | 直接复用 — action generation |
| `src/scienceworld_utils.py` | ScienceWorld env utilities, `fork_and_lookahead` | 直接复用 |
| `src/router_sft_eval.py` | Router offline classification eval（加载 LoRA adapter 做 batch 推理） | **参考** — adapter 加载 + prompt 构造方式 |
| `src/ablation_implicit_7b.py` | Plan-004(c) 7B 隐式 router | **参考模板** — 展示如何实现 `RouterFn` 包装类 |
| `src/ablation_implicit_1_7b.py` | Plan-004(b) 1.7B 隐式 router | 参考模板 |
| `src/router_sft_train.py` | Router SFT 训练 | 参考 — prompt format, label mapping |

### 二、Checkpoint 现状

| 目录 | 状态 |
|------|------|
| `checkpoints/plan-002-formal/final_adapter/` | 训练完成，但 **accuracy=0.0**（全预测 internal，confusion matrix 显示 390 个 det 样本全部误分类） |
| `checkpoints/plan-002-formal-v4/` | **空目录**，尚未开始训练 |

### 三、训练数据

- `results/sft_data_death_aware/sft_triples.jsonl`: 150 samples
- 90 条 det-preferred, 0 条 internal-preferred, 60 条其他（被跳过）
- 极端不平衡：有效训练数据中 100% det-preferred

### 四、Plan-003 需要新增/修改的内容

**1. 新增 `src/plan003_e2e_eval.py`** （~250 行，主要工作量）

需实现：
- `ExplicitRouterFn` class — 加载 Qwen3-1.7B + LoRA classification adapter，每步推理 internal/deterministic，同时用 LLM agent 生成 action
- 5 个 baseline RouterFn：`always_det`, `always_internal`, `oracle_routing`（查 sft_triples 标签）, `random_routing`, `confidence_threshold`（基于 router softmax 概率）
- Bootstrap 90% CI 计算（plan-003 notes 要求）
- Catastrophic failure rate 统计（score == -100 的比例）
- 主入口：遍历全部 6 个条件 → `ablation_eval_common.run_ablation_eval()`

**2. 新增 `scripts/launch_plan003.sh`** （~30 行）

**3. 可能小幅扩展 `ablation_eval_common.py`**
- 增加 bootstrap CI 和 catastrophic failure rate 到 `compute_episode_metrics()`
- 或在 plan003 脚本中后处理（更低侵入性）

### 五、预估工作量

| 项目 | 时间 |
|------|------|
| `plan003_e2e_eval.py` 编写 | 2-3h |
| `launch_plan003.sh` | 0.5h |
| 测试 + 调试 | 1-2h |
| **开发总计** | **~4-6h** |
| GPU 运行时间 | ~15h（6 conditions × 11 tasks × 5 variations × 30 steps） |

### 六、关键风险

1. **无可用 checkpoint**: plan-002-formal accuracy=0.0，plan-002-formal-v4 为空。plan-003 完全依赖有效的 router checkpoint，当前无法启动。
2. **数据极端不平衡**: 训练集 0 条 internal-preferred → 如果 v4 训练仍用此数据，router 可能退化为 always-det，plan-003 结果将无法区分 router 条件和 always-det baseline。
3. **双模型内存**: router (1.7B) + backbone (7B vLLM) 需同时加载，单 GPU (24GB A6000) 可能紧张，可能需要 router 用 CPU 推理或两卡分配。

---
