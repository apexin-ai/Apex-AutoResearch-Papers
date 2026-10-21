# code p8c ft latency v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p8c_ft_latency_v2_20260518T175037_result.json`
- **Structured JSON:** [`93028b862a50b25110f5.json`](../../sessions/93/93028b862a50b25110f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验状态总结：

**P8c FT SciERC Latency** 已在运行中：
- **服务器**: westd-21461, GPU 0 (NVIDIA RTX PRO 6000 Blackwell)
- **模型**: `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`（已在本机，无需 rsync）
- **tmux session**: `p8c_ft_latency`
- **进度**: Phase 1/2 unconstrained — 151/551 docs（约 27%）
- **预估时间**: unconstrained ~27min + constrained ~27min，约 45 分钟后完成

**已完成的操作**：
1. 定位 merged 模型 — 已在 westd-21461
2. 确认 P8c 脚本 `run_p8c_ft_scierc_latency.sh` 已存在且在运行
3. 修复 `analyze_latency.py` 支持自定义输出路径（避免覆盖 P8 report）
4. 修复 P8c 脚本的 analyze 调用输出到 `p8c_latency_report.json`
5. Registry 注册 `p8c_ft_scierc_latency` → RUNNING

**待办**: 运行完成后手动运行 `python3 analyze_latency.py &lt;unc> &lt;con> &lt;p8c_report>` 确认结果（因为修改运行中脚本可能导致末尾分析步骤异常），然后更新 registry 为 DONE。

---
