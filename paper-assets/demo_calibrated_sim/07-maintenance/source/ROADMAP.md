# demo_calibrated_sim — Research Dashboard

> 最后更新: 2026-05-13 15:30 UTC | 更新原因: Post-MVP: research phase entered, paper_framing updated (D014), experiment_plan created, dream launched

## 核心方向
Calibration failure taxonomy for LLM user simulators in dialect-aware agentic evaluation. Core finding: BCP and DPO calibration both fail, with **scale-dependent failure severity** — destructive at 7B (FM1/FM3), selective ignoring at 14B. 详见 paper_framing.md。

## 当前阶段
**Research phase**（MVP 通过 D013/D014，2026-05-13）

## 当前进展
- MVP PASS via Plan C (cross-scale empirical analysis)
- C1 (FM1-3 at 7B): ✅ moderate evidence (mvp-004, single run + hgate-dpo003-merged 4 runs for FM3)
- C2 (FM4 DPO reversal): ✅ strong evidence (hgate-dpo003-merged, 4 runs, 10/12 gap expansion)
- C3 (scale-dependent severity): ✅ strong evidence (qwen14b-bcp-001, 4 runs; FM1/FM3 not replicated at 14B)
- C4 (implications): analytical, grounded in C1-C3
- paper_framing.md: ✅ fully updated with 14B data + scale-dependent framing (D014)
- experiment_plan.yaml: ✅ created (4 P0 done, 1 P1 planned, 1 P2 optional)
- Dream simulate: 🔄 running (full mode, post-MVP)

## 近期任务
- [ ] Dream 结果出来后审查 framing/plan 结构性问题
- [ ] 启动 Paper Agent 论文写作（Dream 通过后）
- [ ] Bootstrap CI 统计检验（plan_005, P1, CPU only）
- [ ] 联系 Manager 确认服务器迁移时间线 + 新服务器 GPU 可用性
- [ ] 14B DPO (plan_006, P2) — 取决于新服务器 GPU 和时间

## 时间线
- EMNLP 2026 ARR deadline: **2026-05-25**（12 天）
- 论文写作启动: Dream 完成后（预计今天内）
- 14B DPO（如做）: 需新服务器，~11-13h

## GPU 预算
- 当前分配: cqa1-21977 cuda:2,3 (2× RTX 4090)
- 状态: MVP 完成，GPU 空闲。Manager 通知 MVP 后迁移到新独享服务器
- 新服务器: 待 Manager 确认

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D015 | 2026-05-13 | 接受 Reviewer 评估：当前 claims 多处 overclaim，必须补 GPT-4o-m | mvp-004, qwen14b-bcp-001 |
| D014 | 2026-05-13 | C3 framing 修正：从"cross-scale replication of FM1-3"改 | qwen14b-bcp-001, mvp-004, hgate-dpo003-merged |
| D013 | 2026-05-13 | MVP PASS (Plan C): BCP 失败是结构性的，非容量限制。进入 research 阶 | qwen14b-bcp-001, mvp-004, hgate-dpo003-merged, mistral-bcp-001 |
| D012 | 2026-05-13 | Mistral completion=0%（tool-calling 能力不足），Plan B mu | mistral-bcp-001, llama-bcp-001, hgate-dpo003-merged |
| D011 | 2026-05-13 | Plan A FAIL：hgate-dpo003-merged 2/4 runs H2+H3 双 F | hgate-dpo003-merged, mvp-004, diag-lora-merge |
| D010 | 2026-05-13 | vLLM LoRA serving bug 确认：merged DPO-003 completion | hgate-dpo003, dpo-003 |
| D009 | 2026-05-12 | Reviewer critical 修正：llama-bcp-001 overclaim 降级；Pl | llama-bcp-001, dpo-003 |
| D008 | 2026-05-12 | Llama BCP generalizability 不足，hedge 下载 Mistral-7B， | llama-bcp-001, mvp-004, dpo-003 |
| D007 | 2026-05-12 | Llama BCP 无效（floor effect），cuda:3 释放后试 Mistral-7B； | llama-bcp-001 |
| D006 | 2026-05-12 | TRL+Qwen2.5 mismatch 根因确认，dpo-002 继续跑 + 并行调查修复方案准备 | dpo-001, hgate-dpo001, dpo-002 |

