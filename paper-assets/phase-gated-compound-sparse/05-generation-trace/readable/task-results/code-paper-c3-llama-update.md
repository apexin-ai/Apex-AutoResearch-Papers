# code paper c3 llama update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper_c3_llama_update_20260514T185051_result.json`
- **Structured JSON:** [`cbaaf4b7898d141b5d82.json`](../../sessions/cb/cbaaf4b7898d141b5d82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。更新文件清单：

| 文件 | 修改内容 |
|------|---------|
| **paper_framing.md** | C8 status→confirmed (详细 evidence: d_z 0.19→0.34, s030 p=0.029, phase gradient d_z≈1.0); RC1 应对升级为跨架构泛化; Narrative Arc/Core Insight/Paper Positioning 加入 LLaMA 三架构表述 |
| **abstract.tex** | 模型列表改为"三模型、两架构 (Qwen2ForCausalLM, LlamaForCausalLM)"; 新增 LLaMA replication 句 (d_z 0.19→0.34, p_Bonf=0.029, ~1/40 magnitude) |
| **introduction.tex** | 新增 LLaMA 跨架构扩展句; contributions 改为"three models spanning two architectures" |
| **results.tex** | 新增 §5.5 Cross-Architecture Validation + Table 4 (tab:llama-cross-arch): 4 sparsity levels × d_z/median_diff/CI/Wilcoxon p; 文本描述 phase gradient d_z∈[1.00,1.12] vs random d_z∈[0.35,0.45], ~40× magnitude difference |
| **discussion.tex** | 新增 "Architecture-dependent magnitude" 段: 趋势一致但量级取决于架构特异的 attention distribution |
| **conclusion.tex** | Replication 句扩展加入 LLaMA cross-architecture |
| **limitations.tex** | "同架构"限制改为"已验证两架构族，更广泛架构 (Mistral, MLA) 仍需" |

---
