# code eval sta prolog

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-sta-prolog_20260514T061756_result.json`
- **Structured JSON:** [`2edf040e3e4ef8121ddc.json`](../../sessions/2e/2edf040e3e4ef8121ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Prolog 评估管道完全正常工作：

- **PrologSolver** 可用（swipl 在 PATH 中）
- **parse_prolog_formalization** 正确解析两种格式（inline `?-` 和 labeled `Query:`）
- **prolog_sta_reward** 返回正确结构：`execution_reward`, `sta_reward`, `combined_reward`, `details`（含 components 列表）
- 3 个 clause 全部 necessary → ISR=1.0 ✓
- proof 失败 → execution_reward=0, sta_reward=0 ✓
- 有冗余 clause 时 ISR=0.333（3 个中只有 1 个 necessary）✓

**结论**：eval_sta.py 的 Prolog 支持已经完整实现，无需修改。具体包括：
- `--logic_type prolog` CLI 参数 ✓
- PROLOG_SYSTEM_PROMPT / PROLOG_USER_TEMPLATE ✓
- LOGIC_CONFIG 调度到 `prolog_sta_reward` ✓
- `src/sta/prolog_reward.py` 完整实现（解析、ablation、ISR 计算）✓
- `src/solvers/prolog.py` + factory `get_solver("prolog")` ✓
- 输出指标格式与 FOL 一致（prove_rate, mean_isr, isr_std, proved_only_isr, component stats）✓

**无遗留问题**。plan006 Prolog GRPO 实验的 post-training ISR 评估可以直接用：
```bash
python scripts/eval_sta.py --model_path &lt;checkpoint> --data_path &lt;data> --output_path &lt;out.json> --logic_type prolog
```

---
