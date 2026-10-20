# check cwm 8b seq config

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cwm-8b-seq-config_20260515T103846_result.json`
- **Structured JSON:** [`18500fb452b766d84c12.json`](../../sessions/18/18500fb452b766d84c12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## 训练配置

| 参数 | CWM 8B (`train_repo_cwm_8b.py`) | CLS 8B (`train_repo_verifier_8b.py`) |
|------|------|------|
| **max_seq_length** | **2048**（默认值，日志中未传覆盖参数） | **2048**（默认值，日志中未传覆盖参数） |

两个脚本的 argparse 默认值均为 `--max_seq_length 2048`，日志中无该参数出现 → 使用默认值。

## 推理配置（eval 脚本）

| 参数 | CWM (`eval_repo_cwm.py`) | CLS (`eval_repo_cls.py`) |
|------|------|------|
| **max_new_tokens** | **1024** | **8** |
| **eval max_seq_length** | val=8192, test=2048（自动） | 2048 |

## 有效输入上下文

- **CWM 8B**: 2048 - 1024 = **~1024 tokens**（训练时 prompt+target 共 2048，target 是 execution_output 可达上千 token）
- **CLS 8B**: 2048 - 8 = **~2040 tokens**（target 只是 "pass"/"fail" 一个词）

## 关键观察

1. CWM 训练截断率: train 4.5%, **val 20.2%** — val 集截断严重
2. CLS 训练截断率: train 3.8%, **val 20.2%** — 相同 val 集，也有 20% 截断
3. CWM 的 eval 脚本注释（第8行）明确说明：`Longer max_new_tokens (1024 vs 8) since CWM generates execution traces`
4. CWM 训练时 prompt 和 target 拼接后截断到 2048，execution_output 较长时会被截断，实际可用给 prompt（code diff + test）的空间大约只有 1024 tokens

---
