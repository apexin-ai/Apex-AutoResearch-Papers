# code advbench data prep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_advbench_data_prep_20260519T193636_result.json`
- **Structured JSON:** [`49f430c69d961a7bf49f.json`](../../sessions/49/49f430c69d961a7bf49f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。产出汇总：

| 文件 | 状态 |
|------|------|
| `data/advbench/harmful_behaviors.csv` | 520 prompts (header + 520 rows) |
| `src/advbench/__init__.py` | 已创建 |
| `src/advbench/generate_traces.py` | `--help` 通过 |
| `src/advbench/annotate_cp.py` | `--help` 通过 |
| `src/iaa/__init__.py` | 已创建（之前缺失） |
| `from src.iaa.prompt_template import ...` | import 成功 |

关键设计：
- **generate_traces.py**: greedy decoding, `&lt;think>` 块内按双换行分步, 支持 `--start/--end` 分片 + `--dry-run`, 自动跳过已生成的 trace（resume）
- **annotate_cp.py**: 从 `src.iaa.prompt_template` import `format_prompt`/`get_system_prompt`, Groq Qwen3-32B, 指数退避重试, 跳过已标注 trace（resume）, JSON 响应解析兼容 markdown code block

---
