# paper writing method

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260526T124004_result.json`
- **Structured JSON:** [`3e1f5381adc900c41d0d.json`](../../sessions/3e/3e1f5381adc900c41d0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。与旧版相比的主要修改：

1. **去除结果预判语言**：Full OCC+LN、Detach OCC、Cutoff、Reverse Cutoff 的描述改为中性的 "paired with X to isolate Y" 句式，删除了 "BN interference without gradient compensation" 和 "rescue" 等隐含结论方向的措辞
2. **方程符号定义**：补充了 $h$、$\phi_v$、$s_t^*$ 的含义
3. **BEV head 细节**：补充了 GT grid 的生成方式（projecting object bounding boxes onto table-plane BEV）
4. **Cutoff 描述精确化**：明确写出 post-cutoff = Detach mode 的具体含义（encoder gradients blocked, BatchNorm2d statistics continue to update）
5. **种子数明细**：Evaluation 中补充了 Cutoff@{15K, 25K}: 2 seeds 和 Cutoff@45K: 1 seed
6. **Bootstrap 层级结构**：补充了 hierarchical resampling 的两层结构（seeds → episodes）
7. **表格紧凑化**：添加 `\small`、`\setlength{\tabcolsep}{4pt}`、`@{}` 列间距
8. **无禁用术语**：无 crossover interaction、BN-mediated gradient calibration、gradient collapse

---
