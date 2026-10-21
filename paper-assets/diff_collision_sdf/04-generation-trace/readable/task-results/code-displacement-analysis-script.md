# code displacement analysis script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_displacement_analysis_script_20260525T152443_result.json`
- **Structured JSON:** [`06421675369c8971120d.json`](../../sessions/06/06421675369c8971120d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

1. 脚本无报错
2. 输出格式正确，task 名称提取正常（orange juice, chocolate pudding, milk, bbq sauce）
3. Batch Comparison 表格正常
4. Sensitivity Analysis 正常
5. Histogram PDF 生成成功

关键发现：**两个模型在 threshold=0.001m 时 Filtered CAR 均为 0%**——所有 "safe" episodes 都是 frozen（displacement < 0.001m）。只有在 threshold=0.0001m 时才有 1-1.5% 的 filtered CAR。这证实了几乎所有 "safety" 来自 action collapse 而非真实避碰。

脚本已部署到 `/root/colliforce-vla/scripts/analyze_displacement.py`，本地副本在 `artifacts/analyze_displacement.py`。

---
