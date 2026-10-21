# audit anonymization check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_anonymization-check_20260523T162845_result.json`
- **Structured JSON:** [`e7b4b700739005cc333a.json`](../../sessions/e7/e7b4b700739005cc333a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存至 `artifacts/anonymization_audit.md`（`save_project_file` 不允许写自定义文件名，改用本地 `Write` 写入 artifacts 目录）。

## 核心结论

**无需修复**。代码库不包含作者姓名、邮箱、机构信息、个人 GitHub/W&B/HuggingFace URL。

| 检查项 | 命中数 | 状态 |
|---|---|---|
| 邮箱 | 0 | ✅ |
| `WANDB_ENTITY` | 0 | ✅ |
| `WANDB_PROJECT` | 10（默认 `"schema_semantic_constrained_ie"`，5 个训练脚本各 2 处） | ⚠️ 边缘但安全 |
| `github.com/` | 0 | ✅ |
| `huggingface.co/` `wandb.ai/` URL | 0 | ✅ |
| `author=` / `setup.py` / `pyproject.toml` | 0 / 不存在 | ✅ |
| Copyright / Affiliation / University 字符串 | 1（`ontology_scalability_benchmark.py:41` 中 `'University'` 是本体实体类型标签） | ✅ |
| `.env` / `.ini` / `.gitconfig` | 不存在 | ✅ |

唯一边缘项：`WANDB_PROJECT` 默认值 `"schema_semantic_constrained_ie"` 是仓库/课题名，不暴露作者。由于未硬编码 entity，账户取决于运行时 `wandb login` 身份，符合 ARR 匿名要求。

---
