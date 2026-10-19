# ops westd 41718 diagnose fix c4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-41718-diagnose-fix-c4_20260518T064715_result.json`
- **Structured JSON:** [`5037768643a0ac4ade92.json`](../../sessions/50/5037768643a0ac4ade92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 诊断结果：无需重新提交

v2 实验**已在之前成功运行完毕**，只是 registry 状态卡在 RUNNING 未更新。

### C4 OOD 结果汇总

| 实验 | C4 PPL | 状态 |
|------|--------|------|
| dense baseline (v2) | **9.2075** | DONE |
| KL30 s123 (v2) | **16.0259** | DONE |
| KL30 s42 (已有) | **16.0458** | DONE |

PPL 退化：30% sparsity → C4 PPL 从 9.21 升至 ~16.03（+74%）。两个 seed 高度一致（16.03 vs 16.05）。

### 已完成修复
1. **Registry 更新**: `c4_ood_kl30_s123_v2` 和 `c4_ood_dense_baseline_v2` 状态从 RUNNING → DONE(success)，metrics 已录入
2. **HF_HUB_OFFLINE 永久写入**: `/root/.bashrc` 已追加 `HF_HUB_OFFLINE=1` 和 `HF_DATASETS_OFFLINE=1`，防止未来再因网络下载失败

---
