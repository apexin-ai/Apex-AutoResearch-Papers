# ops m046 canonical sweep 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m046_canonical_sweep_17855_20260520T084753_result.json`
- **Structured JSON:** [`035a3a726d04c5d59547.json`](../../sessions/03/035a3a726d04c5d59547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

| exp_dir | PermG (old→new) | TY (old→new) | K≥3 (old→new) | K≥4 (new) | 变化? |
|---------|-----------------|--------------|----------------|-----------|-------|
| `scale_check/pythia69b_wiki_a100_s42` | 7→7 | 1→1 | 5→5 | 0 | **无** |
| `scale_check/pythia69b_wiki_a100_s43` | 6→6 | 0→0 | 6→6 | 0 | **无** |
| `generalize/qwen35_08b_wiki_a100_s42_fp32_v2` | 8→8 | 6→6 | 6→6 | 3 | **无** |
| `generalize/qwen35_08b_wiki_a100_s43_fp32` | 6→6 | 0→0 | 6→6 | 0 | **无** |
| `generalize/gpt2m_wiki_a100_s43_bf16` | N/A→0 | N/A→3 | N/A→0 | 0 | **新建**（之前无分析） |
| `padding_robustness/a100_s42_fp32` | 6→6 | 0→0 | 6→6 | 0 | **无** |
| `generalize/pythia410m_wiki_a100_s43` | 6→6 | 4→4 | 6→6 | 4 | **无** |

**smollm3_3b_wiki_a100_s43_17855**: 仅 5 gen，数据不足，Perm Granger 全 N/A，K≥3=0。不可用。

### 17855 上缺失的实验

以下任务中列出的目录在 17855 上**不存在**（可能在 19828 上）：
- `gen_gpt2m_a100_s42_fp32` (GPT-2m s42)
- `generalize_pythia410m_wiki_a100_s42` (Pythia-410m s42)
- `smollm3_3b_wiki_a100_s42_v3` (SmolLM3 s42)

### 结论
D123 TY-fixed 脚本重跑后，**所有 7 个完整实验的 PermG / TY / K≥3 均与旧值完全一致**，无任何数值变化。gpt2m_s43_bf16 为新生成的分析（PermG=0, K≥3=0，信号极弱）。

---
