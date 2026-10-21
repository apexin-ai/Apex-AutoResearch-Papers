# check ft latency provenance

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ft_latency_provenance_20260518T173414_result.json`
- **Structured JSON:** [`5a4834df1ccb68930537.json`](../../sessions/5a/5a4834df1ccb68930537.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. "+2.3% (61 ms/doc)" 的确切来源

**数据来源不明。** 在两台服务器上均未找到产生这个数字的实验数据文件。

唯一相关的 FT latency 数据是 westd-16980 上的 Qwen LoRA SciERC 实验（`outputs/w5_lora_scierc_*.jsonl`，551 docs），实际测量结果为 **overhead = -1.04%**（constrained 反而略快 26.7 ms/doc），与 +2.3% 不符。

两台服务器上均不存在 `*ft_timing*`、`*lora_timing*`、`*ft_latency*`、`*lora_latency*` 等文件。

注：2.3% 和 61 ms 在数学上自洽（61ms / 2.56s baseline ≈ 2.4%），但没有实验文件产出这组数字。

### 2. 已验证的零射 latency 数据（对比参考）

| 实验 | 服务器 | 文件 | 文档数 | Overhead |
|------|--------|------|--------|----------|
| P8 SciERC (zero-shot) | westd-21461 | `p8_timing_*.jsonl` | 551 | **+13.13%** (546.7 ms/doc) |
| P8b DocRED (zero-shot) | westd-21461 | `p8b_timing_docred_*.jsonl` | 200 | **+2.43%** (470.0 ms/doc) |

两者均在 **RTX PRO 6000 Blackwell** 上运行，与 tex 中声称的 GPU 一致，数值也吻合（tex 写 13.1% 和 2.43%）。

注意：westd-16980 的 `runtime_benchmark.json`（也标注为 Blackwell）给出 Qwen SciERC full_s1 overhead = -22.2%，与 P8 的 +13.13% 矛盾。两份数据来自不同实验 run。

### 3. FT latency 实验的 GPU

无法确定，因为不存在对应的实验数据。tex 中声明 GPU 为"RTX PRO 6000 Blackwell"，但仅零射实验可验证这一点。w5 LoRA 数据在 westd-16980（也是 Blackwell）上运行但结果不匹配。

### 4. westd-21461 cuda:0 状态

**空闲。** 0MiB 显存占用，0% 利用率。cuda:1 被 python3 占用（18914MiB，83% util）。

---
