# ratekv — Research Dashboard

> 最后更新: 2026-05-16 03:23 UTC | 更新原因: Dream 完成 → 补实验冲刺计划（multi-seed + CodeLlama E2E + 扩展 ablation）

## 核心方向
Per-head KV cache quantization 的 **2-bit compounding 是跨架构通用失败模式**，cardinality constraint 是通用修复，non-uniform allocation 极少有效（8/9 模型无收益）。详见 `paper_framing.md`。

## 当前阶段: Dream 后补实验冲刺 (ARR May 25, 距今 ~9 天)

**投稿目标**: EMNLP 2026 Main (ARR May 25, 2026)
**Dream 评分 (compounding-forward framing)**: best 3.5/6 | median 3/6 | worst 3/6
**对比 Round 2 实际**: 2.75/5 → 有提升，best case 35-45% 接受率
**核心差距**: multi-seed null results + CodeLlama E2E + Qwen-centric ablations + 无理论模型

## Dream 三档一致的结构性问题 → 行动计划

### 确认行动项（立即执行）
1. ✅ **CodeLlama constrained MCKP** — 9/9 fully experimental（已派 cuda:0）
2. ⏳ **4 模型 × 3-seed PPL** — Llama/Mistral/Yi/Gemma-2 multi-seed 确认 null results
3. ⏳ **Mistral 8K eval** — long-context 扩展（已派 cuda:1）
4. ⏳ **Llama budget sweep** — 2×/4×/8× 非 Qwen ablation
5. ⏳ **Compounding sweeps** — Yi/Gemma-2/CodeLlama/Phi-3/InternLM2（5 架构）
6. ⏳ **C4 cross-dataset** — 3 models
7. [ ] **论文修复**: 理论 toy model (§3.X), compounding figure 移入正文, symmetric-only deployment 举例
8. [ ] **Solver equivalence** 扩展到 Yi/Gemma-2（从已有数据派生）

### 观察项（等真实实验）
- [Dream 观察] KIVI asymmetric compounding test — best case 审稿人认为最重要缺失实验
- [Dream 观察] Qwen-32B profiling — 是否为第二个 Spread model
- [Dream 观察] Diagnostic holdout — DeepSeek-V2/Mixtral 如有资源可尝试

## GPU 调度
westd-37397: 2× RTX PRO 6000 98GB
- cuda:0 → CodeLlama constrained MCKP (~30min) → multi-seed Llama (3×30min) → compounding sweeps
- cuda:1 → Mistral 8K eval (~45min) → multi-seed Mistral (3×30min) → compounding sweeps

## 48h Pipeline 估算
| 阶段 | GPU-hours | 内容 |
|------|-----------|------|
| Phase 1 | ~1.5h | CodeLlama constrained + Mistral 8K |
| Phase 2 | ~6h | 4 models × 3-seed PPL (两卡并行 ~3h) |
| Phase 3 | ~8h | 5 compounding sweeps + 3 C4 + Llama budget |
| Phase 4 | ~4h | downstream multi-seed CIs |
| **Total** | **~20h** | **两卡并行 ~12h wall time** |

## 模型覆盖 (当前 9/9 diagnostic accuracy)
| Model | Shape | Constrained | Compounding | Long-ctx | Multi-seed |
|-------|-------|-------------|-------------|----------|------------|
| Qwen-7B | Spread | ✅ | ✅ | ✅ 8K | ✅ 3-seed |
| Qwen-14B | Flat | ✅ | — | — | — |
| Llama-8B | Spike | ✅ | ✅ | ✅ 8K | ⏳ |
| Mistral-7B | Flat | ✅ | ✅ | ⏳ 8K | ⏳ |
| Yi-1.5-9B | Spike | ✅ | — | ⏳ | ⏳ |
| Gemma-2-9B | Flat | ✅ | — | ⏳ | ⏳ |
| Pythia-1.4B | Flat | ✅ | — | — | — |
| Phi-3-medium | Flat | ✅ | ⏳ | — | — |
| InternLM2-7B | Flat | ✅ | ⏳ | — | — |
| CodeLlama-7B | Spike | ⏳ | ⏳ | — | — |

## GPU 预算
已分配: 2× RTX PRO 6000 (westd-37397)，pipeline ~12h wall time，预算充裕

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D069 | 2026-05-16 | CodeLlama constrained MCKP 确认 Spike，9/9 diagnostic | codellama_constrained_mckp |
| D068 | 2026-05-16 | Dream 确认 compounding-forward framing 优于旧 framing，但 | dream_20260516T021448 |
| D067 | 2026-05-15 | Kill invalid Qwen compounding sweep and regenerate | qwen_compounding_sweep |
| D066 | 2026-05-15 | Rerun Mistral compounding sweep with bf16_2bitonly | mistral_compounding_sweep, llama_compounding_sweep |
| D065 | 2026-05-15 | 重跑 Mistral compounding sweep 用 bf16_2bitonly profi | mistral_compounding_sweep, llama_compounding_sweep |
| D064 | 2026-05-15 | 重跑 Mistral compounding sweep（路径 A）：统一用 bf16_2biton | llama_compounding_sweep, mistral_compounding_sweep |
| D063 | 2026-05-15 | Table 4 统一为各模型 optimal k（与 Table 1 一致），否决统一 k=8 方案 | llama_downstream_eval, downstream_eval_qwen, w3_downstream_eval |
| D062 | 2026-05-15 | Round 2 审稿响应策略：全面 reframing（claim 降级）+ spread 模型搜索 | round2_review |
| D061 | 2026-05-15 | Mistral Table 1 更新为 hires k=2 数据；KIVI+MCKP 定位为 ort | mistral_hires_constrained_mckp_v2, kivi_mckp_combined_qwen7b |
| D060 | 2026-05-15 | Pythia-1.4B Flat 预测验证通过，诊断准确率 7/7；论文 t1/t5 统一使用 ca | pythia14b_constrained_pipeline |

