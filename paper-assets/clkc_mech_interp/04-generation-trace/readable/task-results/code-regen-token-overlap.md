# code regen token overlap

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_regen-token-overlap_20260525T201358_result.json`
- **Structured JSON:** [`d4a1beecc365984f6da3.json`](../../sessions/d4/d4a1beecc365984f6da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据缺失情况已经清晰了。让我整理分析结果：

**数据可用性汇总：**

| 目录 | EN data | ZH data | DE data | activations | probe results |
|------|---------|---------|---------|-------------|---------------|
| llama31/ | ✅ en_conflict_{train,test}_verified | ❌ | ❌ | en only | multiseed only |
| qwen3/ | ✅ en_conflict_{train,test}_verified | ❌ | ❌ | en only | multiseed + base |
| gemma2_v2/ | ✅ en + zh (verified/validated) | ✅ | ❌ | en + zh | multiseed |

**脚本可运行性：**

| 脚本 | 目标模型 | 缺失数据 | 能否运行 |
|------|---------|---------|---------|
| `token_overlap.py` | Qwen3 + Llama31 | `zh_conflict_*.jsonl` (llama31, qwen3) | ❌ |
| `token_overlap_en_de.py` | Llama31 | `de_conflict_*.jsonl` | ❌ |
| `token_overlap_enhanced.py` | Qwen3 + Llama31 | `zh_conflict_*.jsonl`, `zh_activations.pt`, `probe_results_bootstrap.json` | ❌ |

**三个脚本全部无法运行**，原因是核心输入数据缺失：

1. **ZH 数据仅存在于 gemma2_v2/**，llama31/ 和 qwen3/ 目录下没有 `zh_conflict_*.jsonl`
2. **DE 数据完全不存在**，没有任何 `de_conflict_*.jsonl` 文件
3. **ZH activations** 仅 gemma2_v2 有，llama31/qwen3 均缺失
4. 脚本引用的 `probe_results_bootstrap.json` 不存在（只有 `probe_results_multiseed.json`）

gemma2_v2 有完整的 EN-ZH 数据对，但三个脚本都没有配置 gemma2_v2 作为分析目标。

**结论：** 需要先补齐数据（为 llama31/qwen3 生成 ZH conflict 数据集，以及为 llama31 生成 DE conflict 数据集），或者修改脚本使其支持已有完整数据的 gemma2_v2，才能产出 token overlap 分析结果。

---
