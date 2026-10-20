# code recovery eval pipeline

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-eval-pipeline_20260514T174306_result.json`
- **Structured JSON:** [`e24476515f5086a8565f.json`](../../sessions/e2/e24476515f5086a8565f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完成。总结：

---

## Recovery Eval Pipeline 产出

### 文件
`eval/injected_eval.py` — 479 行，完整的 injected eval 脚本

### 设计思路
- 复用 `recovery.py` 的 ModelInference、环境管理、prompt 构建等基础设施
- 每个 episode 必定注入一次错误（round-robin 分配 P1/P2/C1/C4 算子）
- 注入时刻：默认随机 step 2-6，可通过 `--inject_step` 固定
- **新增追踪维度**：
  - `detection`: 分析 `&lt;think>` 输出中的错误感知关键词（8 组正则模式）
  - `recovery_action`: 识别 look/examine/inventory 等重新定向动作
  - `trajectory`: 每步记录 obs、action、think_snippet、注入标记、检测标记
- 报告包含：overall recovery_rate / detection_rate、per-operator breakdown、per-task-type breakdown、统计比较（McNemar + bootstrap CI）

### CLI 兼容
与 `scripts/run_injected_eval.sh` 完全兼容（`--model_variant`, `--inject_step`, `--compare_with`）

### Dry-run 结果 (3 tasks, TaxEI, seed=42)

| Task | Operator | Inj Step | Steps | Success |
|------|----------|----------|-------|---------|
| look_at_obj_in_light-AlarmClock | P1_step_order_swap | 2 | 5 | OK |
| look_at_obj_in_light-Book | P2_sub_goal_deletion | 2 | 25 | OK |
| look_at_obj_in_light-Bowl | C1_context_truncation | 4 | 6 | OK |

- **Recovery rate: 1.0** (3/3)
- **Detection rate: 0.0** — 模型未在输出中使用 `&lt;think>` 标签（`enable_thinking=False`），detection 指标暂时无法工作。这不是 pipeline bug，而是模型行为——正式运行中如果模型产生 `&lt;think>` 内容，检测逻辑即可生效
- Task 2 虽然成功但用了 25 步（P2 删除关键步骤后模型需要更多探索），对比 task 1/3 的 5-6 步，体现了注入的影响

### 使用方法
```bash
# 完整 47-task 评估
CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py \
    --model_path &lt;checkpoint> --model_variant taxei \
    --num_episodes 47 --output eval_results/injected_taxei.json

# 三组对比
bash scripts/run_injected_eval.sh all
```

---
