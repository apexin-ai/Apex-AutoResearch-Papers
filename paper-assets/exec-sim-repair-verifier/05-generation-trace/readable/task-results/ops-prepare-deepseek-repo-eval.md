# ops prepare deepseek repo eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-deepseek-repo-eval_20260516T101327_result.json`
- **Structured JSON:** [`5aa3aa8e31b647d92a01.json`](../../sessions/5a/5aa3aa8e31b647d92a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有准备工作完成。总结：

---

## 报告

### 1. eval 脚本 DeepSeek 支持

| 脚本 | 状态 |
|------|------|
| `eval_repo_cls.py` | 之前被截断（95行），已修复部署完整版（388行），支持 DeepSeek |
| `eval_repo_cwm.py` | 之前无 DeepSeek 支持，已重写部署（471行），完整适配 |

两个脚本均包含：
- `detect_model_family()` → 自动检测 deepseek/qwen/auto
- `get_stop_token_ids()` → DeepSeek 使用 `<|EOT|>` (32021) + `<｜end▁of▁sentence｜>` (32014)
- `get_chat_template_kwargs()` → DeepSeek 返回空 dict（无 enable_thinking）
- `_apply_chat_template_safe()` → 系统角色回退合并
- `model.generate()` 中传入 `eos_token_id=eos_ids`

### 2. 数据和路径确认

- 测试数据：`swebench_test.jsonl` = 9784 行 (pass=7138, fail=2646)
- 模型：`/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct` 加载正常
- Checkpoint 目录已创建但空（训练中，预计 cls ~03:00 UTC May 17, cwm ~22:00 UTC May 17）
- 输出目录已创建，磁盘剩余 73GB 充足

### 3. 部署清单

- `/home/sonny/exec-sim-repair-verifier/eval_repo_cls.py` (388行)
- `/home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py` (471行)
- `/home/sonny/exec-sim-repair-verifier/run_deepseek_repo_eval.sh`

### 4. 使用方式

```bash
# CLS eval (训练完成后)
bash run_deepseek_repo_eval.sh cls 3

# CWM eval (训练完成后)
bash run_deepseek_repo_eval.sh cwm 3
```

### 5. 注意事项

- Checkpoint 目录 `checkpoints_deepseek_cls_repo/best/` 和 `checkpoints_deepseek_cwm_repo/best/` 当前为空，训练脚本需要在完成时创建 `best/` 符号链接或目录。需确认训练脚本是否会自动创建 `best/`——如果不会，启动 eval 前需手动指定具体 checkpoint 路径。

---
