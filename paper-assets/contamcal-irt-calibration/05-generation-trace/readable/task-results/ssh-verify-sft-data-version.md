# ssh verify sft data version

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-sft-data-version_20260513T205822_result.json`
- **Structured JSON:** [`96c885c212986b5a21d0.json`](../../sessions/96/96c885c212986b5a21d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

---

## 结果

### 1. `sft_dosage_000.jsonl` **不含任何 paraphrase 数据** ✓

| 检查项 | 结果 |
|--------|------|
| `data_meta_0pct.json` | `"base_dataset": "Open-Orca/SlimOrca"`, `"contamination": "none"` |
| `_source` 字段（脚本注入标记） | **0** 匹配 |
| `paraphrase_parsed` 字段 | **0** 匹配 |
| `paraphrased_prompt` 字段 | **0** 匹配 |
| "paraphrase" 文本 grep | 237 匹配——全是 SlimOrca 原始 NLI 任务内容（"Are these sentences paraphrases of each other?"），**非注入数据** |

**脚本逻辑确认**：`prepare_sft_data.py` 以 `sft_dosage_000.jsonl` 为 `--base-data` 输入，仅对 dosage > 0% 混入 paraphrases。0% 文件是独立从 SlimOrca 采样的纯净数据。

### 2. 时间线

| 文件 | 修改时间 (May 14) |
|------|----------|
| sft_dosage_000.jsonl | 03:33 |
| humaneval_paraphrases.json | 03:10 |
| arc_challenge_paraphrases.json | 03:52 |
| gsm8k_paraphrases.json | 04:11 |
| sft_dosage_005~100.jsonl | 04:17 |

0% 文件独立生成，不依赖任何 paraphrase 文件。

### 3. 结论：当前 0% SFT 训练有效，不受 paraphrase 版本影响

### 4. MMLU 进度

- 总量: 14,042 items
- Attempt 1 完成 4,112 items → Attempt 2 剩余 9,930 items
- Attempt 2 进度: **139/621 batches (22%)**，~10s/batch
- 日志最后更新: 05:00 (服务器时间)
- 剩余 482 batches × ~10s ≈ **80 min**
- **ETA: ~06:20 服务器时间 (+0800)**

### 5. 需注意

dosage > 0% 文件（04:17 生成）目前仅含 arc_challenge + gsm8k paraphrases，**不含 humaneval 和 MMLU**。MMLU paraphrasing 完成后需重新运行 `prepare_sft_data.py` 更新这些文件。

---
