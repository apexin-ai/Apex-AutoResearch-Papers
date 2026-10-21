# code w10 llama docred beam 50

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_llama_docred_beam_50_20260517T071157_result.json`
- **Structured JSON:** [`7f94f550e1217828af70.json`](../../sessions/7f/7f94f550e1217828af70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并正在运行。

**报告：**

1. **模型路径**: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct` (ZS 版本，与之前 Llama SciERC beam 一致)

2. **完整命令**:
```bash
python run_constrained_extraction.py \
  --mode full_s1 --dataset docred \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/docred_llama_beam_50.jsonl \
  --decoding_strategy beam --num_beams 4 \
  --device cuda:0 --max_samples 50
```

3. **PID**: 424211 (cuda:0, 17.5GB 显存, 84% 利用率)

4. **预估耗时**: ~30-50 分钟。参考 Qwen DocRED beam 50 每样本 ~20-30s，Llama 因 grammar-first fallback 更频繁会稍慢，预估每样本 ~40-60s。

**注意事项**：
- tmux session: `llama_docred_beam`
- 日志: `/root/runs/schema_semantic_constrained_ie/w10_llama_docred_beam_50.log`
- 输出: `outputs/docred_llama_beam_50.jsonl`
- 任务参数中 `--data_path` 用了 `data/docred/dev.json`（非 `data/processed_data/docred_test.json`，后者不存在）
- `--decoding_strategy beam`（非 `--beam_search`，已从代码 argparse 确认）

---
