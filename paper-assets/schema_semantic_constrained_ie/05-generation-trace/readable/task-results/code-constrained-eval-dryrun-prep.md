# code constrained eval dryrun prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_constrained_eval_dryrun_prep_20260515T230350_result.json`
- **Structured JSON:** [`1e1e907bed56136eaee9.json`](../../sessions/1e/1e1e907bed56136eaee9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，报告已注册。总结：

**所有 7 项检查全部通过：**
- 两个 merged model 完整（config.json + 4× safetensors + tokenizer）
- DocRED dev.json + ontology_constraints_docred.json 存在
- `run_constrained_extraction.py` 支持 `--model_path` 自定义模型、`--max_samples` 控制样本数
- Qwen 2-sample dry-run：✅ 加载模型 → 读取约束（6 entity types, 96 relations）→ 输出合法 JSON
- Llama 2-sample dry-run：✅ 同上

**零阻塞项。** unconstrained eval 完成后可直接用报告中的命令提交 constrained eval，两个模型分别跑在 cuda:0 / cuda:1 上并行执行。

---
