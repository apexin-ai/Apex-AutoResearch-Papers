# code mvp scripts

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-scripts_20260513T045148_result.json`
- **Structured JSON:** [`0ca11f6e0d1d633b0751.json`](../../sessions/0c/0ca11f6e0d1d633b0751.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 仍不可用（另一个 Worker 在配置中）。文件已全部写在本地项目目录，等 SSH 恢复后上传。

文件清单和说明：

| 文件 | 功能 |
|------|------|
| `src/scienceworld_utils.py` | ScienceWorld 环境工具：创建/重置/步进/关闭环境、`fork_and_lookahead()` action-replay forking、`run_episode_with_logging()` |
| `src/phase0_validate_forking.py` | Phase 0 验证：10 个 variation 跑 fork，测量成功率/延迟/内存，输出 gate 判定 |
| `src/llm_agent.py` | Qwen2.5-7B ReAct agent：`select_action_react()` 单步选 action、`generate_candidate_actions()` 生成 top-n 候选，支持 vLLM/HF 后端，自动探测模型路径 |
| `src/phase1_signal.py` | Phase 1 主实验：3-way comparison（always-internal / always-deterministic / oracle-routing），逐 episode 记录 JSONL + 汇总 summary.json |
| `src/analysis.py` | 结果分析：bootstrap 90% CI、per-task 判定、ROADMAP Pass/Conditional/Fail 标准 |
| `src/run_all.sh` | 全流程脚本：Phase 0 gate → Phase 1 双 GPU 并行 → Analysis |

全部 5 个 Python 文件语法验证通过。

待 SSH 恢复后需要：
1. 上传 6 个文件到 `/root/autodl-tmp/simgate-modular-routing/src/`
2. 确认 ScienceWorld API 的精确 task type 名称，更新 `scienceworld_utils.py` 顶部常量和 `phase0_validate_forking.py` 中 `PHASE0_TASKS`
3. 确认模型实际路径，更新 `llm_agent.py` 的 `MODEL_SEARCH_PATHS`

---
