# code grounding prompt ablation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grounding-prompt-ablation_20260518T214627_result.json`
- **Structured JSON:** [`a4690e613d822798bbe4.json`](../../sessions/a4/a4690e613d822798bbe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### Dry-run 结果

| 项目 | 结果 |
|------|------|
| Task | chemistry-mix, 1 episode |
| Score | 0.0 (未完成任务，但未死亡) |
| Death | **No** (baseline 同 task/variation 下 internal 得分 -100.0) |
| Steps | 30 (max) |
| 时间 | 44.8s |
| `focus on` 使用 | **0 次**（完全避免） |
| 输出格式 | 与 baseline episodes.jsonl 兼容 |

### vLLM 状态

代码使用 **in-process vLLM**（`from vllm import LLM`），不需要外部 API server。每次脚本运行自动加载模型到 GPU 0（14.25 GiB，RTX 5090 32GB），加载时间 ~4秒。

### 完整实验运行命令

```bash
cd /root/autodl-tmp/simgate-modular-routing && \
nohup /root/miniconda3/bin/python src/run_grounding_prompt_ablation.py \
  --task_types "chemistry-mix,find-animal,freeze,grow-fruit,identify-life-stages-1,identify-life-stages-2,inclined-plane-determine-angle,lifespan-longest-lived,lifespan-longest-lived-then-shortest-lived,measure-melting-point-unknown-substance" \
  --episodes 20 \
  --gpu_id 0 \
  --max_steps 30 \
  --seed 42 \
  --output_dir results/grounding_prompt_ablation/ \
  > results/grounding_prompt_ablation.log 2>&1 &
```

### 预计运行时间

- 每 episode ~45秒（30 步 × ~1.5s/步）
- 200 episodes（10 tasks × 20 eps）
- **预计总时间：~2.5 小时**
- 模型加载一次性开销 ~10s

### 脚本路径

`/root/autodl-tmp/simgate-modular-routing/src/run_grounding_prompt_ablation.py`

### 设计说明

- 采用方式 B（复制运行逻辑 + 修改 system prompt），因为现有代码不支持 system prompt 参数化
- 通过 `llm_agent.SYSTEM_PROMPT = patched` monkey-patch 实现，`select_action_react()` 引用模块级全局变量，patch 生效
- 所有参数与 baseline 一致：temperature=0.3, seed=42, max_steps=30, vLLM in-process
- 两张 GPU 均空闲，full run 使用 GPU 0

---
