# ssh check generalize status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_generalize_status_20260517T081615_result.json`
- **Structured JSON:** [`819e323ac3999edf3de2.json`](../../sessions/81/819e323ac3999edf3de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态汇报：**

两个泛化实验均在运行中，均未完成。

| 实验 | GPU | 已完成 gen | 当前状态 | 预估剩余 |
|------|-----|-----------|---------|---------|
| Pythia-410M wiki | cuda:0 (PID 247554) | gen_0, gen_1, gen_2 (3/11) | gen_3 合成数据生成中 | ~2.5h |
| OPT-1.3B wiki | cuda:1 (PID 249384) | gen_0 (1/11) | gen_1 训练中 step 4000/5000 (80%) | ~3.5h |

- **5-method 分析**：无法运行，两个实验均未完成（需 11 个 gen 目录）
- **第三实验**：两个 GPU 均被占用，暂不启动

---
