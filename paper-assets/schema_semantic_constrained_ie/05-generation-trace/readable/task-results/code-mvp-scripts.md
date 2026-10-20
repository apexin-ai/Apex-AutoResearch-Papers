# code mvp scripts

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_scripts_20260513T173700_result.json`
- **Structured JSON:** [`25bd6c7bd79384183ace.json`](../../sessions/25/25bd6c7bd79384183ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 产出汇报

### 1. SciERC test set
- **100 docs, 551 sentences, 1685 entities, 974 relations**
- 数据来源：HuggingFace `zj88zj/SCIERC`（原始 nlp.cs.washington.edu 的 695MB tar.gz 含 ELMo 嵌入，下载极慢）

### 2. ontology_constraints.json 各关系合法 pair 数

| Relation Type | Valid Pairs | Instances |
|---|---|---|
| Used-for | 35 | 1690 |
| Feature-of | 26 | 173 |
| Hyponym-of | 21 | 298 |
| Part-of | 21 | 179 |
| Compare | 17 | 166 |
| Conjunction | 25 | 400 |
| Evaluate-for | 23 | 313 |

### 3. 代码文件

| 文件 | 路径 |
|---|---|
| `analyze_ontology.py` | `/root/schema_semantic_constrained_ie/analyze_ontology.py` |
| `run_extraction.py` | `/root/schema_semantic_constrained_ie/run_extraction.py` |
| `violation_checker.py` | `/root/schema_semantic_constrained_ie/violation_checker.py` |
| `ontology_constraints.json` | `/root/schema_semantic_constrained_ie/ontology_constraints.json` |

### 4. Dry-run 结果（3 samples, transformers backend）
- JSON 解析成功率：3/3 (100%)
- Entity type violations: 0/10 (0%)
- Relation D/R violations: 1/5 (20%)
- Cross-field consistency violations: 0
- Entity/Relation exact-match F1: 0（zero-shot 下 span 不完全匹配是预期的）

### 5. 问题与解决

| 问题 | 解决 |
|---|---|
| 原始 SciERC 下载 695MB（含 ELMo），从中国下载极慢 | 改用 HuggingFace `zj88zj/SCIERC` 只下载 JSON 文件 |
| 数据中关系类型为全大写（`USED-FOR`），代码预设为 Title-Case | 添加 `RAW_TO_CANONICAL` 映射做标准化 |
| vLLM 0.18.1 不支持 `Qwen3ForCausalLM` 架构 | 使用 `--backend transformers` 回退，正常运行 |
| 模型 ModelScope 首次下载中断 | 重新用 `snapshot_download` 下载到 `Qwen3-8B-ms` 目录 |

### 全量运行命令

```bash
cd /root/schema_semantic_constrained_ie
python3 run_extraction.py \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
  --data_path data/processed_data/test.json \
  --output_path outputs/raw_outputs.jsonl \
  --backend transformers

python3 violation_checker.py \
  --input_path outputs/raw_outputs.jsonl \
  --constraints_path ontology_constraints.json \
  --output_path outputs/violation_report.json
```

---
