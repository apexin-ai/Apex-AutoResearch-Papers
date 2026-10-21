# fix c4 s43 mauve tokenizer

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c4_s43_mauve_tokenizer_20260517T200623_result.json`
- **Structured JSON:** [`c19dad985c03d2d9ffe1.json`](../../sessions/c1/c19dad985c03d2d9ffe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复完全成功。**

- Gen 0 metrics 已计算完成：`ppl=20.60, entropy=2.9559, eff_rank=72.5`
- `metrics.json` 已写入 gen_0 目录
- 实验已自动进入 Generation 1/10 的合成数据生成阶段

## 总结

- **修复方式**：方式 A（`TRANSFORMERS_OFFLINE=1`）
- GPT-2 tokenizer 已通过 hf-mirror.com 预下载到 `/root/autodl-tmp/.hf_cache`
- MAUVE 评估在离线模式下成功加载 GPT-2 tokenizer 并完成特征提取
- C4 seed-43 实验已正常运行，Gen 0 完成，正在进行 Gen 1

---
