# code validate cwm analysis scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_validate-cwm-analysis-scripts_20260514T172329_result.json`
- **Structured JSON:** [`e592998933bab3de404e.json`](../../sessions/e5/e592998933bab3de404e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `memory.md`。核心结论：

**已就绪：**
- `eval_repo_cwm.py` / `eval_repo_cls.py` / `eval_repo_verifier.py` 均支持 `--split val`、`--max_seq_length`、`--checkpoint_dir`
- `analyze_cwm_errors.py` 完整可用，支持 error mode 分类、unparseable 分析、CWM vs CLS 对比，输出 JSON summary
- 8B eval 无需专用脚本，通过 `--model_name Qwen/Qwen3-8B` 即可

**已有 Checkpoints：**
- CLS 8B: seed42 已完成 (200/400/600)，seed123 训练中 (最新 3000)
- CWM 8B: 训练中 (最新 1600)
- CWM 4B: v12 (300-700)，seed123 (200-600)

**需注意：**
1. `eval_repo_cls.py` 的 `max_seq_length` 硬编码为 2048，val 时需手动传 `--max_seq_length 8192`（其他两个脚本已自动切换）
2. 8B eval 时 batch_size 需下调（建议 1-2）
3. CWM 8B 和 CLS 8B seed123 训练仍在进行

---
