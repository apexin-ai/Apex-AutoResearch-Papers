# code plan 010 analysis scripts

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_analysis_scripts_20260516T045507_result.json`
- **Structured JSON:** [`043c759d1fff8eeac765.json`](../../sessions/04/043c759d1fff8eeac765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写入并通过语法检查。

| 脚本 | 路径 | 输出 |
|------|------|------|
| RSA | `/root/vla-ssd/scripts/rsa_libero_spatial.py` (278行) | `results/rsa/rsa_libero_spatial.json` |
| Action Probe | `/root/vla-ssd/scripts/action_probe_libero_spatial.py` (368行) | `results/functional_validation/action_probe_libero_spatial.json` |

关键设计：
- 两个脚本均从特征目录自动发现 task（`glob("*.h5")`），不硬编码 task 列表
- 启动时检查特征目录和 action 数据目录是否存在，不存在则 `sys.exit(1)` 并提示
- RSA：Method B 全参数对齐 `rsa_unified_vla.py`（cosine rep + euclidean act + N_SAMPLE=20 + Spearman + bootstrap CI 1000）
- Action Probe：全参数对齐 `fulllayer_action_probe.py`（50ep/patience5/lr1e-3/hidden256/seed42），trained/untrained 双进程并行跑两张 GPU
- Bootstrap pairwise 对比：best-vs-best + same-layer，两种 aggregation 都做

---
