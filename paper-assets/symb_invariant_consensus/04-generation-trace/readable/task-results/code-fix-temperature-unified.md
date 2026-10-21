# code fix temperature unified

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-temperature-unified_20260518T113315_result.json`
- **Structured JSON:** [`cace3aeb9025b70d6f45.json`](../../sessions/ca/cace3aeb9025b70d6f45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，验证通过。

## 修改汇总

| 文件 | 行号 | 修改 |
|------|------|------|
| `sica/constraint_extractor.py` | L120 | `__init__` 新增 `temperature: float = 0.3` 参数 |
| `sica/constraint_extractor.py` | L125 | 新增 `self.temperature = temperature` |
| `sica/constraint_extractor.py` | L136 | `temperature=0.3` → `temperature=self.temperature` |
| `run_full_mvp.py` | L201 | `--temperature` default `0.7` → `0.3` |
| `scripts/run_case_study_extract.sh` | L64 | `--temperature 0.7` → `0.3` |
| `scripts/run_folio_trace_regen.sh` | L65 | `--temperature 0.7` → `0.3` |
| `scripts/run_cross_model_mistral.sh` | L72 | `--temperature 0.1` → `0.3` |
| `scripts/cross_model_extract.py` | L33 | `--temperature` default `0.1` → `0.3` |

## 验证结果

- `VLLMBackend.__init__` 现在接受 `temperature` 参数，默认 0.3
- `call()` 使用 `self.temperature` 而非硬编码值
- 所有脚本和 CLI 默认值统一为 T_ext=0.3

---
