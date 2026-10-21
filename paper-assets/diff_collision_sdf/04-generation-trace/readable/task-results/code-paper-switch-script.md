# code paper switch script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper_switch_script_20260527T190838_result.json`
- **Structured JSON:** [`80be14c032e1ab022084.json`](../../sessions/80/80be14c032e1ab022084.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本完成。`artifacts/paper_switch.py` — 12/12 替换在两种 scenario 下全部通过 dry-run 验证。

**使用方式**:
```bash
python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run  # 预览
python paper_switch.py --s2-car 57.5 --s2-tsr 48.0             # 实际替换 + 编译
```

**决策逻辑**: 3-seed permutation test (C(9,3)=84), 单尾 p < 0.05 → Scenario C (modest significant), 否则 Scenario B (full redundancy)。

**边界参考**: s2≥56 → Scenario C (p=0.048), s2≤55 → Scenario B (p=0.071)。

---
