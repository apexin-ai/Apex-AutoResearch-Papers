# code repo level eval script prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-level-eval-script-prep_20260512T235002_result.json`
- **Structured JSON:** [`b45b1b02cbb26d7a1f2c.json`](../../sessions/b4/b45b1b02cbb26d7a1f2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**创建的脚本：**

| 脚本 | 功能 |
|---|---|
| `eval_repo_cls.py` | CLS verifier 推理，输出 predictions JSONL + summary JSON |
| `eval_repo_cwm.py` | CWM execution simulator 推理，输出同格式 JSONL + summary JSON |
| `paired_bootstrap_repo.py` | 读两个 predictions JSONL，做 clustered paired bootstrap + TOST 等价检验 (±2pp) |

**输出格式统一**：每条 prediction JSONL 包含 `{index, problem_id, label, pred, correct, truncated, gen_text}`，两个 eval 脚本格式一致，可直接喂给 `paired_bootstrap_repo.py`。

**关键参数**：
- `eval_repo_cls.py`: `max_seq_length=4096`, `max_new_tokens=8`, `batch_size=16`
- `eval_repo_cwm.py`: `max_seq_length=4096`, `max_new_tokens=64`, `batch_size=8`（CWM 生成更长）
- `paired_bootstrap_repo.py`: clustered bootstrap by `problem_id`，10000 resamples，TOST margin ±2pp，D008 Go/No-Go 决策

**数据**：9784 test instances (pass=7138, fail=2646)

**待训练完后的运行流程**：
```bash
# 1. CLS eval (用非训练 GPU)
python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_home/checkpoint-600 --device cuda:1

# 2. CWM eval (CWM checkpoint 就绪后)
python eval_repo_cwm.py --checkpoint_dir &lt;cwm_checkpoint> --device cuda:1

# 3. Paired bootstrap + TOST
python paired_bootstrap_repo.py \
  --cls_preds eval_repo_cls_predictions.jsonl \
  --cwm_preds eval_repo_cwm_predictions.jsonl
```

---
