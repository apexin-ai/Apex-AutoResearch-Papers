# ssh 5090 n16 s42 postmortem and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_n16_s42_postmortem_and_fill_20260521T151645_result.json`
- **Structured JSON:** [`dea2b8f5c6b20a3af349.json`](../../sessions/de/dea2b8f5c6b20a3af349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### exp_fewnerd_n16_s42_v2
- **结果**: 完成（verdict=FAIL，但数据采集和 report 生成成功）
- **samples.jsonl**: 存在，37648 行（完整）
- **关键指标**:
  - greedy_f1=0.7885, oracle_f1=0.9059, oracle_headroom=0.1173
  - rho_FK_cond=**-0.019**（基本为零）, rho_SJ_cond=0.213, logprob_rho_cond=0.176
  - structural_beats_surface=true, sample_f1_pct_zero=25.15%
- **注意**: FK_cond 在 N=16 时降到接近零，与 N=8 的模式可能不同，值得对比分析
- **registry**: 已更新 → DONE/success

### cuda:0 状态
- **GPU 0: 空闲**（0% util, 2 MiB）
- GPU 1-3: 忙（86%/74%/57% util, 各 ~30GB）

### 建议下一个实验
PREPARING 队列中优先级最高的 N=16 实验：
1. **exp_fewnerd_n16_s456_v2** — 完成 FewNERD N=16 三种子集（s42 已完成，s123 在 ANALYZING，差 s456）
2. **exp_scierc_n16_s42** — SciERC N=16 扩展

建议在 cuda:0 启动 **exp_fewnerd_n16_s456_v2**，补齐 FewNERD N=16 的第三颗种子。

---
