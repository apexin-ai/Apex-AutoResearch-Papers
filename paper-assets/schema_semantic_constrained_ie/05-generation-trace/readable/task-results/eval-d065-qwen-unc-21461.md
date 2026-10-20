# eval d065 qwen unc 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d065_qwen_unc_21461_20260520T101504_result.json`
- **Structured JSON:** [`be8a8d0d5c8c91c44963.json`](../../sessions/be/be8a8d0d5c8c91c44963.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总如下：

---

## Part A: d065 Qwen unc eval

**已有结果**（`d065_eval_qwen_unc.json`），无需重跑：

| 指标 | 值 |
|------|-----|
| **E-F1** | 82.35 (P=85.5, R=79.43) |
| **R-F1** | 40.89 (P=36.27, R=46.87) |
| ET | 0.00% (0) |
| RV | 0.23% (37) |
| DR | 0.56% (89) |
| CF | 0.08% (14) |
| Parse failures | 68 / 998 (6.81%) |
| Pred entities | 18,152 |
| Pred relations | 16,001 |

---

## Part B: d066 模型/数据/脚本可用性

| 资源 | 状态 |
|------|------|
| Qwen LoRA DocRED merged | ✓ `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` |
| Llama LoRA DocRED merged | ✓ `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` |
| DocRED data | ✓ `dev.json`, `ontology_constraints_docred.json`, SFT files |
| d066 scripts | ✓ `d066_docred_beam_sweep.sh`, `d066_beam_sweep_scierc.sh`, `d066_analyze_beam_sweep.py` |

**d066 DocRED beam sweep 已有输出：**

| 配置 | 状态 | 备注 |
|------|------|------|
| beam4 s1 (200) | ✓ 完成 | E-F1=83.59, R-F1=49.11, DR=0.0% |
| beam4 unc (200) | ✓ 完成 | E-F1=83.61, R-F1=49.12, DR=0.67% |
| beam8 s1 (200) | 🔄 运行中 | GPU1 PID 196653，2/200 行，刚启动 |
| beam1 unc | ⚠️ 38/200 行 | 中断/未完成 |
| beam1 s1 / beam2 s1 / beam2 unc / beam8 unc | ✗ 缺失 | |

d066 SciERC beam sweep 全部完成（beam 1/2/4/8 × con/unc，已有 eval）。

---

## Part C: GPU 状态

| GPU | PID | 利用率 | 显存 | 任务 |
|-----|-----|--------|------|------|
| GPU0 | 194615 | 85% | 18,919 / 97,887 MiB | d065 con rerun |
| **GPU1** | **196653** | **80%** | **18,923 / 97,887 MiB** | **d066 docred beam8 s1（刚启动）** |

**GPU1 不是空闲的**——正在跑 d066 docred beam8 s1（`--num_beams 8 --mode full_s1 --max_samples 200`）。

另外发现 d067 seed variance 也在此机器上跑过（qwen_scierc seed=123 和 llama_scierc seed=456 完成，qwen_docred seed=123 被 Terminated）。

---
