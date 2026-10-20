# research test set eval prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_test-set-eval-prep_20260521T053550_result.json`
- **Structured JSON:** [`dcf83462a992965681c6.json`](../../sessions/dc/dcf83462a992965681c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。汇报如下：

---

## Test Set Eval 前置准备调研结果

### 1. SFT/RSFT Adapter 可用性 — 全部 ✅

| Adapter | 路径 | 状态 |
|---------|------|------|
| Qwen3-1.7B SFT | `sft_output_qwen3_1_7b_bf16/` | ✅ May 16 |
| Qwen3-4B SFT | `sft_output/` | ✅ May 14 |
| Qwen3-8B SFT | `sft_output_qwen3_8b_bf16/` | ✅ May 16 |
| Qwen3-14B SFT | `sft_output_14b/checkpoint-144/` | ✅ May 19 |
| LLaMA-3.1-8B SFT | `sft_output_llama_3_1_8b/` | ✅ May 16 |
| LLaMA-3.1-8B RSFT | `rsft_output_llama_3_1_8b_k1/` | ✅ May 18 |
| Qwen3-14B RSFT | `rsft_output_14b/` | ✅ May 21 |

### 2. Test Set 数据文件 — ✅

- **DocRED** `test.json`: 存在，**无 labels**（keys: vertexSet, title, sents）→ 需 CodaLab 提交
- **Re-DocRED** `test_revised.json`: 存在（`/root/autodl-tmp/data/re-docred-repo/data/`），**有 labels** → 可本地评测

### 3. CodaLab 提交流程 — ⚠️ 有问题

**DocRED CodaLab** (`competitions.codalab.org/competitions/20717`):
- 平台返回 **502**，疑似已关闭。CodaLab 于 2025-12-31 停止接受新提交。
- GitHub Issue #65 也报告过 "Invalid file type (application/json)" 错误
- 提交格式（如果能用的话）：JSON array of `{title, h_idx, t_idx, r, evidence}`

**Re-DocRED**:
- **无需 CodaLab**，test_revised.json 自带 labels，可本地评测
- Leaderboard 在 [PapersWithCode](https://paperswithcode.com/sota/relation-extraction-on-redocred)

### 4. 代码准备 — ✅ 基本就绪

`freige/eval/test_inference.py` 已有完整流程：
- 加载模型 + adapter → 对 test.json 做推理（不需要 gold labels）
- 输出 `predictions.json` + `codalab_submission.json`
- 支持 `--no_evidence` 参数
- 自动做 entity name → vertexSet index 映射
- 有 `--sft_adapter` 参数支持 stacked adapter

**但有一个问题**：`prepare_test_data()` 硬编码读 `SPLIT_FILENAMES["test"]` = `test.json`，如果要跑 Re-DocRED 的 `test_revised.json`，需要传不同的 `--data_path` 指向 `re-docred-repo/data/` 目录，且 SPLIT_FILENAMES 中没有 `test_revised` 的映射，代码会 fallback 到 `test.json`。需要小改代码或加参数。

### 5. 需要用户确认的事项

1. **DocRED CodaLab 已死，怎么办？**
   - 选项 A：放弃 DocRED test eval，只报 Re-DocRED test 结果
   - 选项 B：尝试联系 thunlp 作者获取 test labels
   - 选项 C：论文中只报 dev set 结果（DocRED），test 结果只报 Re-DocRED
   
2. **哪些模型需要跑 test set？** 全部 7 个 adapter？还是只跑 best models（如 RSFT-14B、RSFT-LLaMA-8B）？

3. **Re-DocRED test_inference 代码适配**：需要改 `test_inference.py` 支持 `test_revised.json`，或者手动把文件 rename/symlink。是否现在改？

---
