# analysis transfer 1000step

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer-1000step_20260519T234221_result.json`
- **Structured JSON:** [`e1e48c6e57b87966f92b.json`](../../sessions/e1/e1e48c6e57b87966f92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。

```
[phase1_transfer_v1 @ step 5389] 已远超 1000 步检查点

L_xfr=4.1744 | pos_count_avg=1.55 | L_act≈0.30 | dec_gnorm=0.0003
趋势: L_xfr 从 1.74 (step 3-4) → 4.174 (step 1000) → 4.174 (step 5389)，完全无下降
判断: WARNING — 严重问题

详细分析:
1. L_xfr 卡死在 ~4.1744 (≈ -log(1/N) 随机基线)，从 step 1000 到 5389 零改善
2. dec_gnorm 从早期 0.45→0.15 迅速衰减到 0.0002-0.0008，decoder 几乎没有梯度
3. pos_count 平均 1.55，偶有 0（此时 L_xfr=0，不参与优化）
4. hm_mean/hm_std 也完全固定 (0.000061/0.000098)，heatmap 没学到任何东西
5. L_act 在 0.20-0.45 波动，未见明显下降趋势

结论: transfer head 完全没学——loss 锁在随机基线，decoder 梯度消失。
这个 run 已经跑了 5000+ 步仍无进展，继续跑不会改善，建议停掉排查。
```

可能原因：
- transfer loss 的梯度无法有效回传到 encoder/LoRA（dec_gnorm→0 说明 decoder 参数已停止更新）
- 正对数量太少（avg 1.55），信号极弱
- loss 权重或学习率设置可能有问题

---
