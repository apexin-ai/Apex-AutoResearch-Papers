# verifier-tts-struct-ie — Research Dashboard

> 最后更新: 2026-05-11 19:51 UTC | 更新原因: 同步实验结果 + 补充 D006 硬退出条件

## 核心方向
表征 TTS 对结构化信息抽取的适用边界。核心发现：NER 上并行 TTS 候选多样性真实存在（oracle +6.49pt），但 5 种 training-free 聚合方法均无法有效利用。正在测试 sequential self-refinement 作为最后 MVP 判定。

## 当前进展
- **阶段**: MVP 验证（最后一轮测试）
- mvp-001 NER 并行: **PARTIAL** — oracle +6.49pt，最佳聚合 +0.66pt，所有统计聚合 <1.0pt
- mvp-002 RE: **INCOMPLETE** — baseline 6.2% 太低，N≥8 推理失败（vLLM 连接错误）
- mvp-003 Verifier: **NEGATIVE** — 同模型自验证 Pearson r=0.09，完全无效
- mvp-004 Sequential: **执行中** — 8 卡并行，K={1,2,3,4} 轮 self-refinement，预计 ~30min

## MVP 关键数据（NER）
| 方法 | 最佳配置 | F1 | vs greedy(42.05) |
|------|---------|-----|-----------|
| Binary freq merge | N=8,k=2 | 42.71±0.59 | +0.66 |
| IoU SC | N=8,τ=0.3 | 42.24±0.72 | +0.19 |
| Verify-selected | N=16 | 42.00±0.33 | -0.05 |
| **Oracle** | **N=16** | **48.54±0.36** | **+6.49** |
| Sequential (TBD) | K=? | ? | ? |

## 硬退出条件（D006）
- ✅ Pass: sequential@K≥3 > greedy ≥ 1.0pt → MVP 通过
- ❌ Kill: sequential@K≥3 也 <1.0pt → training-free TTS 不适用于 IE，kill 或 pivot

## 近期任务
- [ ] mvp-004 sequential 结果 → pass/kill 判定
- [ ] 修正 mvp-001 registry conclusion 为 "partial"（非 "success"）
- [ ] 修正 mvp-002 registry conclusion 为 "incomplete"（非 "negative"）
- [x] mvp-001 NER 5 种聚合方法测试
- [x] mvp-002 RE N=4 测试（N≥8 失败）
- [x] mvp-003 LLM verifier 测试

## GPU 预算
- seetacloud-bjb2-structtts 8x RTX 5090 (cuda:0-7, 项目专用)
- 当前: mvp-004 使用全部 8 卡

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D007 | 2026-05-11 | MVP FAIL — D006 kill 条件触发，escalate 给用户决定项目去向 | mvp-004 |
| D006 | 2026-05-11 | D005 补充硬退出条件：mvp-004 sequential@K≥3 < 1.0pt → kill | — |
| D005 | 2026-05-11 | 不 kill 项目，MVP 扩展测试 sequential self-refinement 作为最后 | mvp-001, mvp-002, mvp-003 |
| D004 | 2026-05-11 | Freq merging 也未达标（+0.66pt），并行测试 verifier-based sel | mvp-001 |
| D003 | 2026-05-11 | Per-entity SC（exact 和 IoU）均失败，pivot 到 entity-level | mvp-001 |
| D002 | 2026-05-11 | MVP 实验采用 3 random seeds 控制噪声，pass 阈值保持 ≥1.0 F1（均值） | — |
| D001 | 2026-05-11 | MVP 选用 SciERC NER + Qwen3-8B，验证并行 TTS 核心机制 | — |

