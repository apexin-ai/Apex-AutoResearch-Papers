# ssh urgent dual check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-dual-check_20260519T194905_result.json`
- **Structured JSON:** [`fc97613c4baff0aaf0ff.json`](../../sessions/fc/fc97613c4baff0aaf0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结论

### 1. GPU 0 CWM s123 训练 — ✅ 正常启动中
Python 进程活着（PID 862545），正在加载模型到 GPU。几分钟后应该开始训练。

### 2. DeepSeek CWM s123 generation length — 不是 ~1.0 token，是编码问题

**gen_text 存储的是 BPE tokenizer 编码格式**（`Ġ` = 空格，`Ċ` = 换行），不是原始文本。用 `split()` 计 word 数时，因为没有 ASCII 空格，整段文本被当成 1 个 "word"。

实际统计（Ġ→空格后）：
| 指标 | DeepSeek CWM s123 | D146 (Qwen3-8B) |
|------|-------------------|-----------------|
| Mean | **104.9** tokens | 149.8 tokens |
| Median | **109** | 125.0 |
| Max | **512** | 946 |
| Min | 1 | 1 |

DeepSeek generation 平均比 Qwen3 短 ~30%，max 被截断在 512（可能是 max_new_tokens 设置）。9668/9784 (98.8%) 的 gen_text 包含 `Ġ` 字符 — 说明 eval 脚本保存的是未解码的 tokenizer 输出而非 decoded text。

**结论：generation length ~1.0 是统计 bug（字段编码问题），不是模型问题。** 实际 mean ~105 tokens，合理但偏短，可能受 `max_new_tokens=512` 限制。

---
