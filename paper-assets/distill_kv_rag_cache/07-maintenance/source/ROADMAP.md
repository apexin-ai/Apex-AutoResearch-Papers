# distill_kv_rag_cache — Research Dashboard

> 最后更新: 2026-05-14 08:33 UTC | 更新原因: MVP Kill — 核心假设被否决 (D004)

## 核心方向
CompressLink: 联合优化 KV cache 压缩 bit 分配（RABA）与恢复 token 选择（CEGR）。

## 状态：**KILLED** (D004, 2026-05-14)

核心假设被 MVP 否决。Kill Criterion #1 完全触发：D（联合优化）在所有条件下从未优于 A（独立处理）。

## MVP 结果摘要

| 条件 | D (F1) | A (F1) | E (F1) |
|------|--------|--------|--------|
| per-sample 6x | 0.314 | 0.314 | 0.314 |
| offline 6x | 0.35 | 0.35 | 0.314 |
| per-sample 8x | 0.2 | 0.2 | 0.314 |
| offline 8x | **0.0** | 0.114 | 0.314 |

## 失败根因

1. **CEGR**: per-token compression error 与正确恢复目标反相关。PCA 下高误差 token 是统计异常 token，不是 QA 关键 token。CEGR 修复后 C F1 从 0.2 降至 0.0。
2. **RABA**: boundary tokens 仅 ~3%，bit 重分配效果可忽略。Offline PCA 下可能有害（D 是最差配置）。
3. **核心洞察**: NoPE+PCA+RoPE 场景下 compression error ≠ token importance，联合优化前提不成立。

## 有价值的发现（可复用）

- Boundary recomputation 是唯一有效的恢复机制（MEPIC 贡献）
- 6x PCA 压缩 + 5% boundary restoration 即可恢复 baseline EM
- Compression 无 restoration 在所有比率（4x-32x）完全崩塌 → RoPE 放大量化噪声
- Per-sample PCA 过于强大，掩盖所有方法差异；离线 PCA 才能暴露真实信号

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D004 | 2026-05-14 | Kill 决策：CompressLink 核心假设被 MVP 否决，终止当前方向 | — |
| D003 | 2026-05-14 | MVP 数据集从 NQ 切换为 HotpotQA，chunk_size 恢复 512 | — |
| D002 | 2026-05-14 | MVP 标准细化：加 kill criteria、D > max(B,C) 协同条件、6x 对照、退 | — |
| D001 | 2026-05-14 | MVP 方案确定：4 组对比验证 RABA+CEGR 联合优化价值 | — |


