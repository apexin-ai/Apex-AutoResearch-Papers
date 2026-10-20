# ops check humaneval sandbox path

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_humaneval_sandbox_path_20260519T073410_result.json`
- **Structured JSON:** [`42845783d7164805b135.json`](../../sessions/42/42845783d7164805b135.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结论如下：

## 结果

| Eval | 状态 | PATH 问题 | pass@1 |
|------|------|-----------|--------|
| **SFT CKA-only** (已完成) | 164/164 `No such file or directory: 'python'` | **是** | 0.0% (假的) |
| **GRPO CKA-only** (已完成) | 正常 | 否 | 20.12% (33/164) |
| **RASP fair** (cuda:3, 运行中) | ~53/164, 正常执行中 | 否 | ~15.0% |
| **Standard fair v3** (cuda:2, 运行中) | ~20/164, 正常执行中 | 否 | ~5.0% |

## 根因分析

- `eval_humaneval.py` 第 51 行用 `subprocess.run(["python", tmp_path])` 调用裸 `python`
- westd-29022 系统 PATH 没有 `/root/miniconda3/bin`，`python` 和 `python3` 都不在默认 PATH 中
- **GRPO CKA-only、RASP fair、Standard fair v3** 都从 conda 激活的 shell 启动，进程环境继承了 `/root/miniconda3/bin` 在 PATH 中（已通过 `/proc/74303/environ` 确认），所以 `python` 能正常找到
- **SFT CKA-only** 很可能从未激活 conda 的 shell 启动，导致 `python` 不在 PATH 中，164 题全报 `No such file or directory: 'python'`

## 结论

- **RASP fair 和 Standard fair v3 没有 PATH 问题**，正在正常运行
- **SFT CKA-only 的 0% 是 PATH 问题导致的假结果，需要重跑**
- 建议修复 `eval_humaneval.py` 第 51 行：`["python", tmp_path]` → `[sys.executable, tmp_path]`，彻底避免 PATH 依赖

---
