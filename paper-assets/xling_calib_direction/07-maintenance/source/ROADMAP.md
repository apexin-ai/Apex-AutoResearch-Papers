# xling_calib_direction — Research Dashboard

> 最后更新: 2026-05-21 13:49 UTC | 更新原因: plan_001 (Qwen3-235B) RUNNING on 4 GPU. PID 299313. Verification pending.

## 核心方向
Cross-lingual correctness probe transfer: LLM 内部 correctness direction 的跨语言可迁移性。**Novelty 锚点**：CKA Simpson's Paradox（partial ρ=-0.29, p=0.078, 符号反转确认）+ control task（selectivity depth-dependent）。详见 paper_framing.md。

## 当前进展
- **阶段**: Research + 审稿进行中 + 论文写作并行
- **MVP**: 3/3 完成 ✓
- **Research**: plan_013 ✓; CKA pilot ✓; CKA 数据修正 ✓
- **plan_001 (Qwen3-235B)**: **🟢 RUNNING** — PID 299313, 4 GPU, 24 层 × 20 语言, ~20-40h
- **plan_002 (Llama4)**: 6 次失败 → killed, 推后至 plan_001 完成后（D019）
- **plan_013_v2**: RUNNING（CPU-bound, PID 47972, 4/8 层）
- **Dream 趋势**: #3 best=4/6 WA; #4 best=3.5/5 Findings → **目标: 4/5 正会**
- **论文写作**: Intro ✅ | Method ✅ | Related Work ✅ | Experiments Setup ✅ | Figures pilot ✅ | 剩余: Abstract, Results, Conclusion

## 模型状态
| 模型 | 量化 | 状态 |
|------|------|------|
| Qwen3-235B-A22B | GPTQ-Int4 | **🟢 RUNNING** plan_001 (PID 299313, 4 GPU) |
| Llama 4 Scout 17B-16E | W4A16 | ⏸️ 推后（脚本需 CPU 调试） |
| Gemma 4 32.7B Dense | BF16 | ⏳ 等新服务器 SSH |

## GPU 执行计划 (westd-13176, 4× RTX PRO 6000 96GB)

**Phase 1 (NOW)**: plan_001 Qwen3 on 4 GPU (~20-40h) ✅ RUNNING
**Phase 2 (plan_001 完成后)**: plan_002 Llama4 on 4 GPU (~6-10h)
**Phase 3**: plan_008 Gemma4（新服务器）
**CPU 并行**: plan_013_v2; Llama4 脚本调试; CKA 分析准备

## 近期任务
- [x] plan_001 启动 ✅ (PID 299313)
- [ ] plan_001 验证（Reviewer 独立核实 GPU 占用 + log 正常）
- [ ] plan_001 运行期间：CPU 调试 Llama4 extract_activations.py
- [ ] 新服务器 SSH → plan_008 (Gemma 4)
- [ ] plan_001 完成 → 立即启动 plan_002 (Llama4)
- [ ] plan_011 CKA full-scale — 依赖 plan_001/002 activations
- [ ] plan_003 CaCLR + high-dim MMD — 依赖 plan_001/002 activations

## 阻塞项
- **Agent 反复卡死** (本 session 7 次) — 系统级 bug，Issue open
- **新服务器 SSH 未提供** — 阻塞 plan_008 (Gemma 4)

## 关键发现
- **CKA Simpson's Paradox** (confirmed + strengthened): pooled ρ=+0.08 vs partial ρ=-0.29 (p=0.078), 符号反转。根因: compute_cka.py positional split bias → 已修正用 full data
- **plan_013 controls**: selectivity 在深层集中，correctness direction 非伪信号

## GPU 预算
- **westd-13176**: 4× RTX PRO 6000 96GB — 当前全部用于 plan_001
- **新服务器(待开)**: 4× RTX 6000 96G
- P0 总计: 190 GPU-h; 实际墙钟 ~38h + plan_008 新服务器并行

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D019 | 2026-05-21 | Swap execution order: plan_001 (Qwen3) first, plan | plan_001, plan_002 |
| D018 | 2026-05-21 | Llama4 and Qwen3 extraction must serialize on 4-GP | plan_002, plan_001 |
| D017 | 2026-05-21 | Float16 activation storage + parallel extraction o | plan_001, plan_002 |
| D016 | 2026-05-21 | Dream #4 processed (3.5/3/2 on ACL 1-5 scale). Add | plan_003, plan_008 |
| D015 | 2026-05-21 | Re-dream processed (4/FAIL/3). P0 structurally app | plan_003, plan_013, plan_001, plan_002 |
| D014 | 2026-05-21 | Dream median Action Matrix: 3.5/5 Borderline Accep | plan_010, plan_002, plan_008 |
| D013 | 2026-05-21 | Depth-transfer narrative correction: overall posit | plan_013, mvp_001 |
| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |
| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |
| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |



