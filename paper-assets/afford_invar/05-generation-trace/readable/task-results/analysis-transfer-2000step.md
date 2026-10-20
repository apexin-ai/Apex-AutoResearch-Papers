# analysis transfer 2000step

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer-2000step_20260519T234235_result.json`
- **Structured JSON:** [`b80018dc229a0ad2f2cc.json`](../../sessions/b8/b80018dc229a0ad2f2cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

```
[L_transfer 2000-step] L_xfr=4.1744 | pos_count_avg=1.3 | hm_ent=8.88 | hm_max=0.000543 | dec_gnorm=0.0004
L_xfr 趋势: step 100→4.713, 200→4.310, 500→4.183, 800→4.173, 1000→0.000(pos=0), 1500→4.174, 2000→4.174, 5000→4.174
L_act 趋势: step 1000→0.228, 1500→0.289, 2000→0.379, 3000→0.279, 4000→0.346, 5000→0.305
verdict: PATH_C
```

**理由:**

1. **L_xfr 完全收敛到 ln(65)≈4.174（uniform baseline）**，从 step 800 开始就再无下降。5500步仍然 4.1744，transfer loss 提供零学习信号。

2. **Heatmap 完全均匀且在恶化：**
   - hm_mean 恒定 0.000061 ≈ 1/16384（128×128 均匀分布）
   - hm_max 从早期 0.0054 → 现在 0.0005，峰值在消失
   - hm_ent 从 8.69 → 8.88，趋近最大熵
   - hm_std 从 0.000151 → 0.000098，方差在缩小

3. **Decoder 梯度坍塌：** dec_gnorm 从早期 0.45 → 现在 0.0003，decoder 事实上已死。transfer_grad_norm 同步坍塌：0.396 → 0.000137，grad_ratio=0.0000。

4. **L_act 正常**（0.23-0.38），主任务未受影响，但 transfer 分支完全无效。

5. **pos_count 极低**（0-2/batch），正样本稀缺加速了崩溃。

**结论：** Heatmap 均匀 + L_xfr 无改善 + decoder 梯度死亡 = 经典 PATH_C。当前 transfer loss 设计在这个配置下无法产生有意义的 affordance 信号。

---
