# code deepseek repo eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek-repo-eval-prep_20260516T101013_result.json`
- **Structured JSON:** [`6d4eb99574f821b3aa12.json`](../../sessions/6d/6d4eb99574f821b3aa12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the report:

---

## DeepSeek Repo-Level Eval 就绪性报告

### 1. Tokenizer 兼容性: ✅ OK

| 属性 | 值 |
|------|-----|
| model_max_length | 16384 |
| pad_token | `<｜end▁of▁sentence｜>` (id=32014) |
| eos_token | `<\|EOT\|>` (id=32021) |
| config.eos_token_id | 32021 (匹配) |
| chat_template | 支持 system+user messages |

pad ≠ eos，config eos 与 tokenizer 一致，无问题。

### 2. eval 脚本兼容性

| 脚本 | 状态 | 说明 |
|------|------|------|
| **eval_repo_cwm.py** | ✅ Ready | `--model_name` 传 DeepSeek 路径即可。tokenizer 从 model_name 加载。`detect_thinking_support` 对非 Qwen 返回 `{}`（正确）。 |
| **eval_repo_verifier.py** (CLS) | ⚠️ 有限制 | `--model_name` 传 DeepSeek 路径。但 **tokenizer 从 checkpoint_dir 加载**（非 model_name），必须用 `best/` 子目录（train_unified.py 只在 best/ 下保存了 tokenizer）。中间 checkpoint 没有 tokenizer 文件。 |
| eval_repo_cls.py | ⬜ 仅工具模块 | 95行，无 main()，无 argparse。实际 CLS eval 是 eval_repo_verifier.py。 |

**无需代码改动**——只要 checkpoint_dir 指向 `best/` 即可。

### 3. 测试数据: ✅

`swebench_test.jsonl` = 9784 行

### 4. 训练状态

两个 checkpoint 目录当前为空（训练进行中，ETA May 17 09:30-12:00 UTC）。训练完成后产出结构预期为：
```
/root/autodl-tmp/checkpoints_deepseek_cls_repo/
  checkpoint-200/  (adapter only, no tokenizer)
  checkpoint-400/
  ...
  best/  (adapter + tokenizer) ← 用这个
```

### 5. 预估 Eval 命令（训练完成后直接跑）

**CLS:**
```bash
cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 eval_repo_verifier.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo/best \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test --save_predictions --device cuda:0 \
  --output results/deepseek_cls_repo_test.json
```

**CWM:**
```bash
cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/best \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test --device cuda:1 \
  --output_dir results/deepseek_cwm_repo_test/
```

> 两个 eval 可以并行跑在不同 GPU 上 (cuda:0 / cuda:1)。

---
