# code bcp prompts

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bcp-prompts_20260512T100012_result.json`
- **Structured JSON:** [`bee134571bc96b1fedce.json`](../../sessions/be/bee134571bc96b1fedce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。四个文件已创建在 `artifacts/prompts/` 下：

| 文件 | 说明 |
|------|------|
| `base_user_simulator.txt` | 基础 τ-Bench retail user simulator prompt，无行为约束 |
| `bcp_user_simulator.txt` | BCP 变体，含 `{question_rate}%` / `{politeness_rate}%` 占位符 |
| `bcp_variants.yaml` | 6 组参数变体（aave_target / uncalibrated_baseline / overcorrected / 两个单维消融） |
| `prompt_loader.py` | `PromptLoader` 类，支持 `load_base` / `load_bcp` / `load_variant`，单维消融时自动生成只含对应约束的模板 |

---
