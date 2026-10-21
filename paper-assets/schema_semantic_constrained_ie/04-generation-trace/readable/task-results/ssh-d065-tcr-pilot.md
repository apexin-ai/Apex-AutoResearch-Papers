# ssh d065 tcr pilot

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d065_tcr_pilot_20260519T112723_result.json`
- **Structured JSON:** [`9e0239098cec701a7706.json`](../../sessions/9e/9e0239098cec701a7706.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**TCR Pilot 全部跑通，4 个 SciERC S1 配置结果：**

| Config | CF 修正前 | CF 修正后 | DR Δ | E-F1 Δ | Fundamental% |
|--------|---------|---------|------|--------|-------------|
| ZS Qwen | 9.75% (245) | **0%** | +0.28pp | -1.29pp | 2.04% |
| ZS Llama | 6.40% (162) | **0%** | +0.22pp | -1.78pp | 1.85% |
| LoRA Qwen | 1.19% (21) | **0%** | +0.00pp | -0.75pp | 0% |
| LoRA Llama | 0.46% (8) | **0%** | +0.00pp | -0.18pp | 0% |

核心发现：
- **CF 100% 消除**，所有配置修正后为 0
- **DR 几乎无副作用**：LoRA 模型 DR 不变，ZS 模型仅增加 +3~5 个 DR violation（~0.2pp）
- **E-F1 小幅下降**（-0.18pp 到 -1.78pp），R-F1 不变
- **Fundamental conflict 极少**（ZS ~2%，LoRA 0%），schema 对 SciERC 不过度约束

产出文件：
- 脚本：`/root/schema_semantic_constrained_ie/scripts/tcr_resolver.py`
- 修正后 JSONL：`outputs/tcr/` 下 4 个文件
- 报告：`d065_tcr_pilot_results.md`（已注册 artifact）

---
