# ssh n17 elo update and prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_elo_update_and_prep_20260523T140108_result.json`
- **Structured JSON:** [`98ad0d6019438453fa6a.json`](../../sessions/98/98ad0d6019438453fa6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 产出

**1. evaluation.py ARENA_ELO 更新** — 两台服务器均已更新
- rtx6000-4x: `/root/gated_mfrm_judge_bias/exp003/evaluation.py` ✓
- autodl-8gpu: `/root/gated_mfrm_judge_bias/exp003/evaluation.py` ✓
- 18 个 key（17 targets + gpt-4-0314 reference），snapshot 2026-05-19

**2. Model name 映射检查** — 无兼容性问题
- 数据文件中已有 9 个模型名与 ARENA_ELO key 完全一致
- N=17 config（`config_llama_arena_n17.yaml` 等）中的 18 个 target_models 与 ARENA_ELO 18 个 key 一一对应
- 不需要额外 name mapping

**3. 一键启动脚本** — `/root/gated_mfrm_judge_bias/exp001/run_n17_evaluation.sh`
- 9 个 judge 全部并行启动，带 API key 检查和日志输出
- 已 `chmod +x`

**4. Judge prompt template 分析** — 对新模型完全通用
- `PAIRWISE_JUDGE_PROMPT` 和 `POINTWISE_JUDGE_PROMPT` 只用 `{prompt}`/`{response_a}`/`{response_b}` 占位符，不引用 model name
- 无 model-specific 处理逻辑
- target_models 列表从 config YAML 读取，无 hardcoded model list
- `judge_interface.py` 的 `JUDGE_MAP` 已包含全部 9 个 judge（含 proxy 版本）

**5. 兼容性问题** — 未发现

---
