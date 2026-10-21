# code mistral unconstrained eval and constrained launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_unconstrained_eval_and_constrained_launch_20260517T203210_result.json`
- **Structured JSON:** [`759bf705be2d8315e001.json`](../../sessions/75/759bf705be2d8315e001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，已处理 1/246 样本（constrained decoding 比 unconstrained 慢得多是正常的）。

---

## Mistral Unconstrained 全量结果
- Parse Success: 194/246 (78.9%)
- Violation Rates: ET=0.0%, EV=37.3%, RoV=63.9%, AC=0.0%, CF=0.0%
- Trigger F1: 0.0241 (P=0.0219, R=0.0268)
- Argument F1: 0.0000
- Entity F1: 0.0000

## Mistral Constrained 启动状态
- tmux session: `mistral_constrained`
- GPU: cuda:1 (15291 MiB 已占用)
- 命令:
  ```
  cd /root/schema_semantic_constrained_ie && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/mistral_constrained_full.jsonl --resume 2>&1 | tee logs/mistral_constrained_full.log
  ```
- 初始进度: 1/246
- 确认运行中: yes

**备注:** `--skip_on_error` 参数不存在于 `run_constrained_extraction.py`，脚本内部已有 try/except 错误处理（unconstrained 运行时 52 条 parse failure 也正常完成了 246/246）。

---
