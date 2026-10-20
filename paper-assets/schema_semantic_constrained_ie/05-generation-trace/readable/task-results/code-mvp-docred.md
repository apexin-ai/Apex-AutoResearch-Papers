# code mvp docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_docred_20260513T173912_result.json`
- **Structured JSON:** [`4ddc3b828000e04f3ded.json`](../../sessions/4d/4ddc3b828000e04f3ded.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

---

## DocRED 数据集 + 本体约束 + 适配代码 — 完成

### 1. DocRED Dev Set 统计
- **样本数**: 998 个文档
- **平均文档长度**: 200.5 词 (median=181, min=129, max=510)
- **平均实体数/文档**: 19.6
- **平均关系数/文档**: 12.3
- **总关系数**: 12,275

### 2. Entity Type 分布 (Dev Set)
| Type | Count | % |
|------|-------|---|
| LOC | 8,168 | 31.2% |
| PER | 4,797 | 18.4% |
| TIME | 4,044 | 15.5% |
| MISC | 3,913 | 15.0% |
| ORG | 3,900 | 14.9% |
| NUM | 1,319 | 5.0% |

### 3. Ontology Constraints 统计
- **训练集 triples**: 38,180
- **Relation types with data**: 96/96 (全覆盖)
- **每 relation 的合法 (head_type, tail_type) pair 数**: avg=5.68, min=1, max=15
- 分布: 1 pair (4 types), 2-5 pairs (46), 6-10 pairs (43), 11-15 pairs (3)
- 最受约束: P190(sister city), P205(basin country), P3373(sibling) 都只有 1 个合法 pair
- 最宽松: P527(has part) 15 pairs, P361(part of) 14 pairs, P17(country) 13 pairs

### 4. 代码文件
服务器 `/root/schema_semantic_constrained_ie/`:
- `analyze_ontology_docred.py` — 从训练数据提取本体约束
- `run_extraction_docred.py` — Qwen3-8B zero-shot extraction (cuda:1)
- `violation_checker_docred.py` — 三类违规检查

数据:
- `data/docred/{train_annotated.json, dev.json, rel_info.json}`
- `data/docred/ontology_constraints_docred.json`

本地 artifacts 同步在 `artifacts/` 目录。

### 5. Dry-Run 结果 (2 samples)
- 模型加载: 4 秒 (bfloat16, cuda:1)
- 推理速度: ~15 秒/文档 (~700 input tokens)
- JSON 解析成功率: 2/2 (100%)
- **Per-triple violation rate: 66.67%** (30 triples, 20 violated)
- 主要违规来源: 模型输出 DocRED schema 中不存在的 relation types (如 "available on", "uses", "built by")
- 少量 entity type violations (2 个)

### 6. 问题
- DocRED 原始 GitHub raw URLs 全部 404，改用 HuggingFace Hub 的 .gz 文件下载
- Qwen3-8B 模型权重未预装完成，通过 ModelScope 重新下载 (~15min)
- 模型实际路径嵌套在 `Qwen3-8B-ms/Qwen/Qwen3-8B/`（ModelScope 目录结构）
- `torch_dtype` 参数 deprecation warning（不影响运行）

---
