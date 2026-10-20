# analysis exp 018 full sgs walker s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018_full_sgs_walker_s1_20260516T124144_result.json`
- **Structured JSON:** [`89b2097735d298c6ee08.json`](../../sessions/89/89b2097735d298c6ee08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成

**结论：SUCCESS — Full-SGS 完全消除 CIVO**

| 指标 | 值 |
|------|-----|
| eval_return peak/final | 915.7 @ 105K |
| NVE peak | **0.72x** @ 75K (阈值 1.5x) |
| NVE sustained avg | 0.55x |
| 对比 baseline (009d) | +22%~+53% |

关键发现：
- NVE 全程 < 1.0x，value function 始终**低估**实际表现（CIVO 的反面）
- eval_return 单调递增至 915.7，无 collapse
- 性能远超 baseline（600-750），说明 obs decoder 梯度不仅导致 CIVO，还主动干扰 policy learning

**对 hypothesis 的判定**：CIVO 是 **gradient-level** 漏洞。Obs decoder 梯度（93% 的梯度贡献）流经 `dt_emb` 是 root cause。Reward-only SGS（016e）无效是因为 reward gradient ≈ 0，等于没 stop 任何东西。

Registry 已更新（metrics + conclusion=success + notes），报告已注册为 artifact。

---
