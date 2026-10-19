# code plan009 pathological matrices v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-pathological-matrices-v2_20260520T181421_result.json`
- **Structured JSON:** [`b00e1a9fe49655f48c6b.json`](../../sessions/b0/b00e1a9fe49655f48c6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，所有组件正常：

- `--help` 输出正确的参数文档
- GPU (`cuda:0`) 正常使用
- 3 类病态 C 矩阵（near-permutation × 4 ε、rank-deficient × 2 ranks、block-diagonal × 1 block config）均生成成功
- plim 计算、bias 统计、feature 提取、OLS 回归全部无 bug
- `tau_true(C=I) = 1.997155`（接近理论值 `beta_T=2.0`，N=100k 下的有限样本误差）
- R² = 0.806（effective_rank 是最强预测因子，p < 1e-5）
- 输出 JSON 和回归结果 txt 已写入 `artifacts/plan009/`

脚本已就绪，等审批后可用全量参数（M=1000, K={3,5,7}, 7 topos）正式运行。

---
