# research eval script analysis

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval-script-analysis_20260516T111146_result.json`
- **Structured JSON:** [`805026cd1894bf39adc1.json`](../../sessions/80/805026cd1894bf39adc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已充分。结论如下：

---

## 结论

### 1. 之前的 74.5% 是 **injected recovery rate**，不是 clean success rate

证据：`llama31_taxei_s42.json` 头部明确写着 `"inject": true`，输出字段为 `recovery_rate: 0.745`，并有 `detection_rate` 和 `by_operator` 分解（C1/C4/P1/P2）。

`injected_eval.py` **没有**任何 `--no_inject` 参数——它永远注入错误。`recovery_rate` 的含义是：**注入错误后，模型仍然完成任务的比例**（即 task success under injection）。

### 2. `--model_variant` 只是一个标签

它仅用于报告中的 `model_variant` 字段，不控制任何注入逻辑。注入行为由脚本本身硬编码（轮流使用 P1/P2/C1/C4 四种 operator）。

### 3. 如何执行 clean eval

项目里有另一个脚本 `eval/recovery.py`，它有 `--inject` / `--no_inject` 开关（`store_true`/`store_false`，默认 `False`）。

Clean eval 命令：

```bash
CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py \
    --model_path /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387 \
    --base_model /root/autodl-tmp/models/meta-llama/Llama-3.1-8B \
    --num_episodes 47 \
    --task_list eval/eval_tasks_47.json \
    --output eval_results/llama31_taxei_s42_clean.json
```

不加 `--inject` 即为 clean eval（默认 `inject=False`）。

### 4. 输出格式区别

| | Clean eval (`recovery.py`, no `--inject`) | Injected eval (`injected_eval.py`) |
|---|---|---|
| `inject` 字段 | `false` | `true` |
| 核心指标 | `success_rate` | `recovery_rate` + `detection_rate` |
| 分解维度 | `by_task_type` | `by_operator` (P1/P2/C1/C4) |
| 有无 detection 分析 | 无 | 有 |

已有的 `mini_vanilla_clean.json` 就是用 `recovery.py` 不加 `--inject` 生成的（`"inject": false, "success_rate": 0.149`）。

---
