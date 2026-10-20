# test plan004 dryrun

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_plan004-dryrun_20260517T225030_result.json`
- **Structured JSON:** [`ecd8be34f0cb4ffafaf8.json`](../../sessions/ec/ecd8be34f0cb4ffafaf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All modules verified. Here's the summary:

---

## Dry-Run Results

### 1. `--help` 验证 ✅
所有新参数存在：`--train_path`, `--quality_check`, `--bertscore_threshold`, `--skip_perturb`

### 2. Mini Perturbation (3条) ✅
- 27 user turns 全部成功 paraphrase，0 失败
- Qwen3-8B 从本地缓存加载正常

**示例对比：**
| | Original | Perturbed |
|---|---|---|
| jailbreak | "Hey there! I've been trying to figure out how to stay secure online..." | "Hey, what's up? I've been really focused on staying safe while browsing the web..." |
| benign | "Could you help me with replacing a leaky faucet in my bathroom?" | "Can you guide me through fixing a dripping tap in my master bathroom?" |

### 3. M001 `&lt;think>` 标签泄漏检查 ✅
**No leakage detected.** 双重保护生效：`enable_thinking=False` + `strip_thinking()` 后处理。

### 4. BERTScore 质量模块 ✅
安装了 `bert-score` 和 `sentence-transformers` 后正常运行：
- BERTScore F1: **0.920 ± 0.012**（高语义保持）
- Semantic Similarity: **0.766 ± 0.112**
- Lexical Overlap: **0.196 ± 0.044**（低词汇重叠 = aggressive paraphrase）
- Low-quality turns filtered: **0/27**（阈值 0.6）

### 5. TF-IDF Baseline 模块 ✅
- 训练集 350 samples，训练正常
- 原始/扰动数据上评估均可运行

### 需要修复的问题
- `torch_dtype` 参数 deprecation warning（应改为 `dtype`），不影响功能但会在 transformers 未来版本失效
- `bert-score` 和 `sentence-transformers` 需要预先安装（代码中是 lazy import，可在 requirements 中标注）

---
