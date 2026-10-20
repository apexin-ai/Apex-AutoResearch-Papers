# code exp3 icl oracle

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp3-icl-oracle_20260518T180847_result.json`
- **Structured JSON:** [`ac4c7cc280c22ed68ef0.json`](../../sessions/ac/ac4c7cc280c22ed68ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Dry-run 验证报告：

**产出文件**
- `/root/symb_invariant_consensus/run_icl_oracle.py` — 主脚本
- `/root/symb_invariant_consensus/scripts/run_icl_oracle.sh` — 启动脚本

**ICL Examples (5题，从评测中排除)**

| idx | id | answer | 推理类型 |
|-----|---------|---------|----------|
| 15 | folio_15 | True | 全称量化链 (2 premises) |
| 6 | folio_6 | True | 存在量词 + 条件推理 (6 premises) |
| 79 | folio_79 | False | 否定链推理 (5 premises) |
| 52 | folio_52 | False | 关系否定 (6 premises) |
| 3 | folio_3 | Unknown | XOR / 信息不足 (7 premises) |

**C001 Dry-run 验证结果**
- python3 可用
- 所有 import 通过
- 5 个 ICL example 的 `premises_fol` / `conclusion_fol` 均非空
- ICL block: 9034 chars, 增强 prompt: 10461 chars
- 模板替换无残留占位符
- 评测集: 199 题 (70 True + 61 False + 68 Unknown)
- 模型路径存在: `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`
- Mock 模式全流程跑通 199 题，extraction 796/796 成功，`ICL_ORACLE_DONE` 正常输出

**启动命令**: `bash scripts/run_icl_oracle.sh 0 8000`

---
