# diagnose gen wiki gpt2m a100 s42 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gen_wiki_gpt2m_a100_s42_v2_20260515T120343_result.json`
- **Structured JSON:** [`07f24a57f299825803af.json`](../../sessions/07/07f24a57f299825803af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：`/root/autodl-tmp/models/gpt2-medium/` 下的符号链接指向了错误的 HF cache 路径——缺少 `hub/` 层级（指向 `.hf_cache/models--gpt2-medium/...` 而非 `.hf_cache/hub/models--gpt2-medium/...`），导致所有链接悬空，tokenizer 找不到 `vocab.json`，`vocab_file=None` 触发 TypeError。

**已修复**：重建全部 7 个符号链接到正确路径，验证 tokenizer 加载成功（vocab_size=50257）。

**可以直接重跑实验。**

报告已写入 `artifacts/report_gen_wiki_gpt2m_failure.md`。

---
