# code folio data prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_folio-data-prep_20260515T194855_result.json`
- **Structured JSON:** [`41df646755a37153d533.json`](../../sessions/41/41df646755a37153d533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 产出汇报

### 1. FOLIO 数据
- **来源**: `/root/autodl-tmp/crdd/data/folio-validation.jsonl` (CRD 项目，204 条)
- **子集**: 30 题，保存到 `data/folio_subset.json`
- **标签分布**: True=10, False=10, Unknown=10（均衡）
- 原始 label "Uncertain" 已映射为 "Unknown"

### 2. ProofWriter 扩展
- **来源**: D5 validation set (600 条)
- **扩展后**: 30 题 (原 10 → 30)，True/False/Unknown 各 10
- 默认 `--n-problems` 已从 10 更新为 30

### 3. Prompt 适配决策
- **新建 `FOLIO_PROMPT` template**（不复用 `LOGIC_PROMPT`）
  - ProofWriter 的 LOGIC_PROMPT: "given facts and rules" + "statement true/false/unknown"
  - FOLIO 的 FOLIO_PROMPT: "given premises" + "conclusion logically follows/contradicted/undetermined"
  - 措辞更贴合 FOLIO 的自然语言前提→结论判断范式
- **Constraint extraction**: 复用 `LOGIC_EXTRACTION_PROMPT`，FOLIO 和 ProofWriter 同属逻辑域，约束结构一致
- Pipeline domain dispatch: `dataset="folio"` → `task_type="folio"`（trace生成用 FOLIO_PROMPT），constraint extraction 仍走 `domain="logic"`

### 4. Dry-run 结果
- `eval_folio.py --dry-run`: 30/30 prompt assembly OK，6/6 answer extraction OK
- `eval_proofwriter.py --dry-run`: 30/30 OK，answer extraction OK
- FOLIO loader 验证: 30 problems loaded, 分布正确
- `normalize_logic_answer` 正确处理 Uncertain→Unknown 映射

### 5. 新增/修改文件
| 文件 | 操作 |
|------|------|
| `data/folio_subset.json` | 新增，30 题 |
| `data/folio_loader.py` | 新增 |
| `data/prepare_folio.py` | 新增 |
| `data/proofwriter_subset.json` | 重建为 30 题 |
| `data/proofwriter_loader.py` | default n=30 |
| `eval_folio.py` | 新增 |
| `eval_proofwriter.py` | default n=30 |
| `sica/trace_generator.py` | 新增 FOLIO_PROMPT，folio task_type 支持 |
| `sica/pipeline.py` | folio domain dispatch |

### 6. 后续步骤
- v3 实验完成后，运行 `python eval_folio.py --k 12 --temperature 0.7 --max-tokens 16384 --save-intermediates`
- 运行 `python eval_proofwriter.py --k 12 --temperature 0.7 --save-intermediates`（30 题版本）
- 可选：将 FOLIO 整合到 `run_full_mvp.py` 的 `load_all_problems` 中

---
