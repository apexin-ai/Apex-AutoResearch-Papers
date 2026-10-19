# code d010 phase c router compat

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d010_phase_c_router_compat_20260516T104453_result.json`
- **Structured JSON:** [`3e2c2236b686bbce439b.json`](../../sessions/3e/3e2c2236b686bbce439b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase C 验证完成。报告已写入 `artifacts/phase_c_router_compatibility_report.md`。

## 结论: **NEED_RETRAIN**

关键发现：

1. **PaliGemma 在 pi0_libero fine-tuning 时未被冻结** — 777/777 参数全部改变，0 个保持不变
2. **Vision tower layer 6（Router 所用层）变化显著** — 平均 diff 0.2856，LayerNorm 和 bias 变化达 0.7~1.7，足以根本性改变激活分布
3. **Router 必须重训** — 原始 F1=0.9963 在新激活分布上预计将严重退化

## 重训路径

- **阻塞项**: Phase B 完成 pi0_libero 加载修复
- **工作量**: ~2-3 小时（激活收集 1-2h + Router 训练 <10min）
- **现有管线可复用**: `phase1/train_par_router.py` + 激活收集流程，只需换模型为 pi0_libero
- **长期建议**: 后续 fine-tuning 应冻结 vision tower 前 10 层，避免每次迭代都重训 Router

---
