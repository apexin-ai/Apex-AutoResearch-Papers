# code mvp dif power sim phase2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_dif_power_sim_phase2_20260520T185329_result.json`
- **Structured JSON:** [`d7062aedaf2fa2d4caac.json`](../../sessions/d7/d7062aedaf2fa2d4caac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 artifacts 全部注册成功。任务完成，总结如下：

---

## Phase 2 半合成验证结果：**PASS**

### 参数来源
PSN-IRT 4PL 模型的 MMLU 14,042 items（取 a, b 两参数用于 2PL）

### 真实 vs 合成参数差异
| 参数 | 真实 MMLU | 合成 (Phase 1) |
|------|-----------|----------------|
| a (discrimination) | mean=1.20, std=0.54 | mean≈1.13, std≈0.60 |
| b (difficulty) | mean=**-0.84**, std=0.79 | mean=0.00, std=1.00 |

关键差异：真实 MMLU items 平均难度低 0.84 logits（更容易），区分度略低。

### Core Region 结果（δ≥1.4, N≥80, ETS C 分类）

| N | δ | ETS-C TPR | ETS-C FPR | Verdict |
|---|---|-----------|-----------|---------|
| 80 | 1.4 | **0.682** | 0.036 | PASS |
| 80 | 1.6 | **0.722** | 0.039 | PASS |
| 100 | 1.4 | **0.758** | 0.040 | PASS |
| 100 | 1.6 | **0.797** | 0.042 | PASS |

- **4/4 core conditions PASS**（ETS-C TPR≥0.65, FPR≤0.10）
- **Pass+ MET**：δ≥1.4, N≥100 时 min ETS-C TPR = 0.758 ≥ 0.75
- **零 FPR>0.15 violations**

### 结论
Phase 1 用合成参数得到的 DIF 检测功效结论在真实 MMLU IRT 参数下**稳健成立**。尽管真实参数分布存在显著差异（difficulty 左移、discrimination 略低），ETS C 分类在 N≥80, δ≥1.4 条件下仍可靠检测污染（TPR 0.68-0.80, FPR 0.04）。

---
