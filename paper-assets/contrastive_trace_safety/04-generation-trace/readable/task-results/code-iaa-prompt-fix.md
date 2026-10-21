# code iaa prompt fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_iaa_prompt_fix_20260519T190040_result.json`
- **Structured JSON:** [`f33ced24dc70ee23ab31.json`](../../sessions/f3/f33ced24dc70ee23ab31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改总结：

| 文件 | 改动 |
|------|------|
| `prompt_template.py` | **CP 定义**：从"first step where model commits to harmful output"改为"step after which safety-aware reasoning permanently ceases"；**Oscillating traces 指引**：明确 CP 是安全推理永久停止处而非首次不安全处；**Tie-breaking**：从选较早改为选较晚（确认安全推理已真正停止）；**2 个 few-shot 样例**：格式匹配 `[Step N]\ntext`，分别展示 oscillating trace (CP=5) 和 clear transition (CP=3) |
| `compute_kappa.py` | **新增 quadratic weighted Cohen's kappa** 作为主指标（`weights='quadratic'`），报告中标注 `(PRIMARY)`；**保留**所有原有指标（exact kappa、binned kappa、correlation、MAE）；**Window agreement 注释**：docstring 和报告底部均标注 `* Window agreement is raw proportion agreement, not chance-adjusted.` |
| `annotate.py` | 未改动（`format_prompt` 末尾措辞随 prompt_template 自动更新） |
| `sample_traces.py` | 未改动 |

---
