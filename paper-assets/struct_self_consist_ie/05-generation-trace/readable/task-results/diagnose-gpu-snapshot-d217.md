# diagnose gpu snapshot d217

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_snapshot_d217_20260521T044513_result.json`
- **Structured JSON:** [`6eb4ffa60303c791da3b.json`](../../sessions/6e/6eb4ffa60303c791da3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090
| GPU | Status | Memory |
|-----|--------|--------|
| 0 | **空闲** | 2MiB / 32607MiB |
| 1 | **空闲** | 2MiB / 32607MiB |
| 2 | **空闲** | 2MiB / 32607MiB |
| 3 | **空闲** | 2MiB / 32607MiB |

- 无 GPU 进程运行
- 32B 残留：**无**（已完成，verdict=MARGINAL）
- Checkpoints: `qwen25-32b-fewnerd-merged`, `qwen3-8b-conll2003-merged`, `qwen3-8b-fewnerd-exp021-merged`

## autodl-5090-b
| GPU | Util | PID | 实验 | 进度 |
|-----|------|-----|------|------|
| 0 | 86% | 305832 | fewnerd_t05_s456 (T=0.5 s456 n=8) | **87%** (260928/301184), ~12min剩余 |
| 1 | 91% | 305834 | fewnerd_t12_s456 (T=1.2 s456 n=8) | **90%** (270496/301184), ~10min剩余 |
| 2 | 2% | 315356 | **fewnerd_n16_seed42** (n=16 s42) | 刚启动 4min, rendering prompts |
| 3 | 33% | 315803 | **fewnerd_n16_seed123** (n=16 s123) | 刚启动 4min, rendering prompts |

## autodl-5090-c
| GPU | Util | PID | 实验 | 进度 |
|-----|------|-----|------|------|
| 0 | 99% | 252310 | 14b_inference_fewnerd (14B n=8) | **81%** (488368/602368), ~21min剩余 |
| 1 | 97% | 278145 | 14b_base_inference/conll2003_n1 (14B base n=1) | **6%** (202/3453), ~10min剩余 |
| 2 | 85% | 264875→265144 | fewnerd_7b_n16_s42 (7B n=16) | **81%** (488368/602368), ~21min剩余 |
| 3 | 92% | 277410 | fewnerd_n16_seed456 (8B n=16 s456) | **4%** (27296/602368), ~3h ETA |

## 实验状态汇总

| Exp ID | Registry Status | Registry 位置 | PID Alive? | 实际位置 | GPU Util | 进度 | 备注 |
|--------|----------------|---------------|------------|----------|----------|------|------|
| exp_14b_inference_fewnerd | RUNNING | 5090-c:0 | **252310 ✅** (4h15m) | 5090-c:0 | 99% | 81%, ~21min | 正常 |
| exp_fewnerd_7b_n16_s42 | RUNNING | 5090-c:2 | **264869 ✅** (2h15m) | 5090-c:2 | 85% | 81%, ~21min | 正常 |
| exp_fewnerd_t05_s456 | RUNNING | 5090-b:0 | **305832 ✅** (1h33m) | 5090-b:0 | 86% | 87%, ~12min | 正常，verdict.json 尚未生成 |
| exp_fewnerd_t12_s456 | RUNNING | 5090-b:1 | **305834 ✅** (1h33m) | 5090-b:1 | 91% | 90%, ~10min | 正常，verdict.json 尚未生成 |
| exp_14b_inference_conll | RUNNING | 5090:0 | **⚠️ 5090 无进程** | 5090-c:1 | 97% | 6% (n=1, ~10min) | **位置不符**：实际在 5090-c:1，且是 base model (非 finetuned)，n_samples=1 |
| exp_scierc_n16_s123 | RUNNING | 5090-b | — | 5090-b | — | **✅ 已完成** 12:40:05 | verdict=PASS, greedy_f1=0.660, oracle_f1=0.814, ρ_SJ=0.423 |
| exp_scierc_n16_s456 | RUNNING | 5090-b | — | 5090-b | — | **✅ 已完成** 12:40:36 | verdict=MARGINAL, greedy_f1=0.665, oracle_f1=0.811, ρ_SJ=0.378 |
| exp_fewnerd_n16_s456 | RUNNING | 5090 | **⚠️ 5090 无进程** | 5090-c:3 | 92% | 4%, ~3h ETA | **位置不符**：实际在 5090-c:3 |

## 关键发现

1. **5090 完全空闲** — 4 块 GPU 全部闲置，registry 中标记在 5090 上的两个实验实际都在 5090-c 上运行
2. **SciERC n16 两组已完成** — s123 PASS, s456 MARGINAL。GPU 已释放并启动了 fewnerd_n16_seed42 / seed123（未在 registry 中）
3. **5090-b GPU 2/3 上运行的是 fewnerd_n16 (seed42/seed123)**，不是 registry 中的 scierc 实验（已完成）
4. **14B ConLL 实验**在 5090-c:1 上运行的是 **base model**（非 finetuned），n_samples=1，output 目录为 `14b_base_inference/conll2003_n1`

---
