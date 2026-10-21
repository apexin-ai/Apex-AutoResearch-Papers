# code d009 llama prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d009_llama_prep_20260514T094600_result.json`
- **Structured JSON:** [`0f406591e28f01cfeef7.json`](../../sessions/0f/0f406591e28f01cfeef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

**兼容性：零代码修改，完全通过。**

| 检查项 | 结果 |
|--------|------|
| Tokenizer 加载 | OK — vocab_size=128000, pad=None→eos_token（代码已处理） |
| `enable_thinking=False` | OK — Llama template 静默忽略该参数 |
| Chat template 格式 | OK — system/user/assistant 正确分隔 |
| XGrammar TokenizerInfo | OK |
| XGrammar GrammarCompiler | OK |
| JSON schema 编译 | OK |
| First-token uniqueness | 6/6 唯一: Task(6396) Method(3607) Material(13721) Metric(55410) OtherScientificTerm(11663) Generic(20560) |
| Dry-run unconstrained 2 samples | 2/2 OK，E=5/3, R=1/0, ~5s/sample |
| Dry-run full_s1 2 samples | 2/2 OK，E=5/3, R=1/0, ~5.6s/sample |

## 实验启动命令

两组实验可直接执行，DocRED 完成后在任一 GPU 上启动：

**Exp 1 — unconstrained baseline:**
```bash
nohup python run_constrained_extraction.py --mode unconstrained --dataset scierc \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/processed_data/test.json --constraints_path ontology_constraints.json \
  --output_path outputs/phase2_scierc_llama_unconstrained.jsonl \
  --device cuda:0 --max_new_tokens 2048 > /tmp/llama_unconstrained.log 2>&1 &
```

**Exp 2 — full_s1 (grammar+semantic):**
```bash
nohup python run_constrained_extraction.py --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/processed_data/test.json --constraints_path ontology_constraints.json \
  --output_path outputs/phase2_scierc_llama_full_s1.jsonl \
  --device cuda:0 --max_new_tokens 2048 > /tmp/llama_full_s1.log 2>&1 &
```

预计每组 ~46 min（551 samples × ~5s）。两组可并行跑在 cuda:0/cuda:1 上（各占 ~16GB，当前各有 ~80GB 空闲）。命令已注册为 artifact `art_20260514_49e74a`。

---
