# diagnose plan 007 redocred rsft r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_007_redocred_rsft_r2_20260516T174244_result.json`
- **Structured JSON:** [`274562b4eb63fb8bd56d.json`](../../sessions/27/274562b4eb63fb8bd56d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：Pipeline Bug — eval 命令参数传错。**

Re-DocRED eval 运行时传了 `--model_path Qwen3-4B --sft_adapter rsft_checkpoint`，而正确应为 `--model_path rsft_checkpoint --sft_adapter sft_output`。

这导致 RSFT LoRA 增量被直接 merge 到裸 Qwen3-4B（缺少 SFT 基底），模型退化为开放域 IE——输出自由文本关系（"born", "won medal"）和错误字段名（"sentence_ids" 替代 "evidence"），与 DocRED 标签集完全无法匹配。

修复：用与 DocRED eval 一致的参数顺序重跑即可，预期 F1 应接近 DocRED 上的 0.46（可能略低因为 Re-DocRED 更难）。

---
