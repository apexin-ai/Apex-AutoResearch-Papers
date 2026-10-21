# ssh cqa1 cross family eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cqa1-cross-family-eval_20260519T055013_result.json`
- **Structured JSON:** [`b768228538f1f3a628e1.json`](../../sessions/b7/b768228538f1f3a628e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整状况评估如下，需要你确认后再动手：

## 现状

| 项 | 状态 |
|---|---|
| **GPU** | PID 161500 占用 6GB 显存（孤儿进程，Qwen 7B batch 已全部完成，此进程是被 pkill 遗漏的 d000_s123 both-mode 残留） |
| **磁盘** | 35GB 可用。OLMo-2-7B 模型 28GB，Gemma-2-9B 35GB，都在 westd-29999 上 |
| **网络** | cqa1 无法访问 HuggingFace，需从 westd scp |
| **Adapter** | westd 上有：OLMo-2-7B_d000_s42 (625MB), Gemma-2-9b_d000/d005/d025/d050_s42 (各891MB) |

## 需要确认的操作

1. **Kill PID 161500** — 释放 6GB GPU。这是孤儿进程，10 个 Qwen 7B aligned eval 已由 original-mode 全部完成，此进程的增量 gsm8k/humaneval 已跑 8h 疑似卡住。
2. **删除 `/root/autodl-tmp/models/Qwen2.5-7B/`（15GB）** — Qwen 7B eval 已全部完成，释放空间用于下载 OLMo/Gemma。
3. **顺序执行**：
   - scp OLMo-2-7B 模型 (28GB) + adapter → 评估 → 删除 OLMo 模型
   - scp Gemma-2-9B 模型 (35GB) + 4个 adapter → 评估 4 个 checkpoint → 完成

确认后立即开始？

---
