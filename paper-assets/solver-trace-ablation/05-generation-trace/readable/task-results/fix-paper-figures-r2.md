# fix paper figures r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper-figures-r2_20260514T232946_result.json`
- **Structured JSON:** [`4bf0c5923828e731e1d5.json`](../../sessions/4b/4bf0c5923828e731e1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**修复结果：**

| 图表 | 修改 | 验证 |
|------|------|------|
| **fig1** | panel (b) 标题改为 `Formalization\nLeave-One-Out Ablation`（fontsize 9→8, pad 6→8） | 39744 bytes |
| **fig2** | 新增底部堆叠柱状图：Non-hacking/H1/H7 三色（Step 100: H7=28%, NH=69%；Step 500: H1=87%；Step 1000: H1=100%） | 16776→25052 bytes（增加了底部 panel） |
| **fig3/fig4** | 图例已确认全部为 "Non-hacking"（无 "Genuine"），重新生成 | 大小不变 |

fig2 的 `tight_layout` warning 是因为 twinx 双轴，不影响输出质量。

---
