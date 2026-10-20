# code svs formalization

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_svs_formalization_20260514T042906_result.json`
- **Structured JSON:** [`ca5f61f9ec37a97f1367.json`](../../sessions/ca/ca5f61f9ec37a97f1367.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部就绪，语法正确，接口完整：

| 文件 | 类 | 公开方法 |
|---|---|---|
| `claim_decomposer.py` | `ClaimDecomposer` | `decompose`, `decompose_batch` |
| `autoformalize.py` | `AutoFormalizer` | `formalize`, `formalize_batch`, `validate_z3_syntax` |
| `vocab_normalizer.py` | `VocabNormalizer` | `extract_vocab`, `normalize_vocab_llm`, `normalize_vocab_regex` |

关键设计点：
- **VocabNormalizer** 按 dataset 自动选路：ProofWriter 走 regex 快速提取，FOLIO 等走 LLM；regex 提取空时自动 fallback 到 LLM
- **AutoFormalizer.validate_z3_syntax** 实际构建 Z3 环境（从 vocab 动态创建 Function/Const）再 `eval` FOL 字符串，不是字符串匹配
- 所有 LLM 调用都带 retry + JSON 解析容错（claim_decomposer 有句号分割 fallback）
- `__init__.py` 已存在且正确 re-export 了三个类

---
