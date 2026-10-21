# code unify eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unify-eval_20260514T133544_result.json`
- **Structured JSON:** [`e3e9a6d4bd9a0ba094f5.json`](../../sessions/e3/e3e9a6d4bd9a0ba094f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果汇总

### Fix 1: 删除 run_eval.py
- `/root/autodl-tmp/freige/eval/run_eval.py` 已删除
- 无其他文件引用它（仅自身 docstring 中提及）

### Fix 2: 统一 JSON parsing
**evaluator.py:**
- 新增 `_try_parse_json_list`、`_repair_truncated_json`、`_normalize_triples` 三个模块级函数
- `parse_model_output` 签名改为 `(output_text: str) -> tuple[list[dict], bool]`，整合截断修复逻辑
- `compute_format_compliance` 中调用更新为 `parsed, _ = parse_model_output(raw_text)`

**inference.py:**
- import 添加 `parse_model_output`
- 删除 Section D（本地的 `parse_model_output`、`_try_parse_json_list`、`_repair_truncated_json`、`_normalize_triples`）
- `run_inference` 中调用 `parse_model_output(generated_text)` 返回 `(parsed, format_ok)` — 签名兼容

### Fix 3: _triple_key relation 不做 lower
已确认：`_triple_key` 返回 `(doc_id, head.lower().strip(), tail.lower().strip(), relation)` — relation 保持原始大小写，无需修改。inference.py 中无独立 triple matching 逻辑。

### Sanity Check
- 脚本启动无 import error
- 模型加载成功（Qwen3-4B + SFT LoRA adapter）
- 数据准备成功（985 eval docs, 12275 gold triples）
- 完成 1 batch 推理（4 docs），无 crash（tqdm 进度: 1/247, 109.94s/it）
- 注意：服务器上已有一个先前启动的完整 eval 作业（`mvp2_sft_eval_r2`，已跑到 36/62 batch），使用旧代码，已 kill sanity check 释放 GPU

---
