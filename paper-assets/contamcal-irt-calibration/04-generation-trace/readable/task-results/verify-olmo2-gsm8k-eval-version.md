# verify olmo2 gsm8k eval version

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_olmo2-gsm8k-eval-version_20260521T102233_result.json`
- **Structured JSON:** [`898f68ee88eec3e83a5c.json`](../../sessions/89/898f68ee88eec3e83a5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cqa1 d005_s123 eval 输出目录为空（已运行 5+ 小时），进程可能极慢或卡住。

---

## 调查结论

### Part 1: evaluate.py 版本调查 — **确认版本差异**

**根因**：s0 使用了修改后的 evaluate.py（37775 bytes），s42/s123 使用了旧版（37591 bytes, C009 reference）。关键差异：

| 变更 | 影响 |
|------|------|
| `max_new_tokens` 512→**256** | **致命**：GSM8K CoT 推理常需 300+ tokens，256 截断导致系统性降分 |
| 添加 `system_prompt="You are a helpful assistant."` | 改变 prompt 格式，影响模型行为 |
| 逐条→batch + left-padding | 可能引入 attention mask 差异 |
| 添加 `normalize_numeric_answer()` | 答案匹配逻辑不同 |

**证据**：
- s0 vs s42 disagreement = 286/1319 (21.7%)，s42 vs s123 = 193/1319 (14.6%)。s0 与其他两个 seed 的差异系统性偏大。
- 时间戳：s42/s123 = 5月20日，s0 = 5月21日（evaluate.py 在此期间被修改）
- 37591 bytes 版本**不在 git 中**（只有一个初始 commit 33904 bytes），需要手动恢复

**结论：s0=60.58% 不可靠，需要用旧版 evaluate.py 重跑。**

### Part 2: GPU 2

GPU 2 正在跑 OLMo-2 d025_s0 GSM8K eval（PID 511187），**也在用新版 evaluate.py（37775 bytes）**。产出也将不可靠。

四个 GPU 全满，无法填充新任务：
- GPU 0: 50981 MiB（96%）
- GPU 1: 44479 MiB（96%）
- GPU 2: 16707 MiB（91%）— d025_s0 eval（错误版本）
- GPU 3: 37911 MiB（89%）

### Part 3: cqa1 PID 460555

**不是僵尸进程**。PID 460555 状态 `Rl`（正在运行），是 Qwen2.5-7B d005_s123 GSM8K eval。但输出目录空了 5+ 小时，可能极慢（24GB GPU 跑 7B 模型 batch_size=2 很吃力）。

也在用 37775 bytes 版本 evaluate.py（两台服务器已同步到新版）。

### 建议行动

1. **恢复 evaluate.py 到 37591 bytes 版本**（需要手动从 diff 反向构建，或找其他备份）
2. **Kill westd GPU 2 d025_s0 eval**（结果不可靠）
3. **cqa1 PID 460555**：你确认要 kill 吗？它是活跃 eval 但也用了错误版本，且进度可疑
4. **等版本统一后**：重跑 s0 d000 + d025_s0（全部用同一版本）

需要我执行哪些操作？

---
