# diag exp002 100step sanity

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp002-100step-sanity_20260518T170849_result.json`
- **Structured JSON:** [`f90a09e00fe1d9c402f6.json`](../../sessions/f9/f90a09e00fe1d9c402f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**exp-002** (step 54/8000, cuda:0):
- **R1**: mean≈-0.43 (step 50), 持续为负，远低于预期 0.3-0.8 范围。std=0.85，min=-1, max=1，方差极大
- **R3**: mean≈0.33-0.62，稳定 >0.3，修复有效
- **combined**: 0.14-0.35，偏低（R1 拖累）
- 无 NaN，步进正常，~29s/step

**exp-003** (step 36/8000, cuda:1):
- R3 logging 正常，mean≈0.25-0.78，波动合理
- `d_syc not loaded` WARNING 每步出现（符合预期，R3-only 配置）
- ~30s/step

**GPU**: 双卡均在运行，PID 69020 占 63.6GB (cuda:0)，PID 70649 占 38.2GB (cuda:1)，温度正常 56-58°C。

**判断：告警** — exp-002 的 R1 持续大幅为负是主要隐患。50 步时 R1 mean=-0.43，模型在 R1（权重 0.25）上表现恶化而非学习。可能原因：R3（权重 0.75）主导梯度，R1 被牺牲。建议观察到 100 步，若 R1 仍无改善趋势需评估是否调整权重配比。exp-003 健康。

---
