# analysis eval llama lora only s42

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_lora_only_s42_20260522T074726_result.json`
- **Structured JSON:** [`c94013a48d2e9c321c2c.json`](../../sessions/c9/c94013a48d2e9c321c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

---

## Metrics: eval_llama_lora_only_s42

### TF (IID heldout, N=50, T=4)
| Metric | GAR-ours | GAR-dongre |
|--------|----------|------------|
| Turn1 avg GAR | 0.5645 | 0.0241 |
| **Mid-turns avg GAR** | **0.4807** | **0.0188** |
| Mid-turns avg nGAR | 11.8031 | 0.8261 |
| GAR recovery | +46.86pp | +0.66pp |
| Avg PPL | 2.60 | 2.60 |
| Avg NTP Loss | 0.9366 | 0.9366 |

### AR (Model-gen, N=5, T=10)
| Metric | GAR-ours | GAR-dongre |
|--------|----------|------------|
| Turn1 avg GAR | 0.0322 | 0.0455 |
| **Mid-turns avg GAR** | **0.0617** | **0.0226** |
| Mid-turns avg nGAR | 0.6065 | 0.2537 |
| GAR recovery | +4.96pp | +1.04pp |
| Avg PPL | 1.32 | 1.32 |
| Avg NTP Loss | 0.2787 | 0.2787 |

### Gap ratio
| Variant | TF GAR | AR GAR | TF/AR ratio |
|---------|--------|--------|-------------|
| GAR-ours | 0.4807 | 0.0617* | 7.79x |
| GAR-dongre | 0.0188 | 0.0226 | 0.83x |

*AR GAR-ours 被几个 spike 拉高 (Conv1-turn5: 0.471, Conv2-turn2: 0.228, Conv4-turns2,4: 0.467/0.495)，真实 non-spike mid-turn GAR 约 0.01-0.03。

---

## 与 Llama TG eval (llama_eval_s42) 对比

### TF 模式
| Metric | LoRA-only | TG | Δ | Δ% |
|--------|-----------|-----|---|----|
| GAR-ours | **0.4807** | 0.4836 | -0.0029 | **-0.6%** |
| GAR-dongre | **0.0188** | 0.018 | +0.0008 | +4.4% |
| PPL | **2.60** | 2.57 | +0.03 | +1.2% |

TF 指标几乎完全一致，gating 零增量。

### AR 模式
| Metric | LoRA-only | TG | 注意 |
|--------|-----------|-----|------|
| GAR-ours | 0.0617 | 0.0388 | 不可直接比 — LO=N5/T10, TG=N50/T4; LO 有 spike |
| PPL | 1.32 | 1.413 | LO 略低 |

AR 的 setup 不同（N/T 不匹配），且 GAR-ours 有 outlier spikes，不做硬比较。

---

## 与 Qwen LoRA-only (phase2_lora_only_s42) 对比

| Metric | Llama LO | Qwen LO | 模式一致? |
|--------|----------|---------|-----------|
| TF GAR-ours | 0.4807 | 0.4978 | ✓ 同量级 (~0.48-0.50) |
| TF PPL | 2.60 | 2.78 | ✓ 同量级 |
| AR GAR-dongre | 0.0226 | 0.0185 | ✓ 同量级 (~0.02) |
| AR PPL | 1.32 | 1.371 | ✓ 同量级 |

两个模型的 LoRA-only 表现模式完全一致。

---

## Conclusion: **SUCCESS**

```python
metrics = {
    "experiment": "eval_llama_lora_only_s42",
    "parent": "llama_lora_only_s42",
    "model": "Llama-3.1-8B-Instruct",
    "gate_type": "none",
    "tf": {
        "gar_ours": 0.4807, "gar_dongre": 0.0188,
        "ngar_ours": 11.8031, "ngar_dongre": 0.8261,
        "ppl": 2.60, "ntp_loss": 0.9366,
        "n_conversations": 50, "n_turns": 4,
    },
    "ar": {
        "gar_ours": 0.0617, "gar_dongre": 0.0226,
        "ngar_ours": 0.6065, "ngar_dongre": 0.2537,
        "ppl": 1.32, "ntp_loss": 0.2787,
        "n_conversations": 5, "n_turns": 10,
    },
    "gap_ratio_gar_ours": 7.79,
    "conclusion": "success",
    "notes": [
        "TF GAR-ours: LO=0.4807 vs TG=0.4836, Δ=-0.6% → gating零增量confirmed on Llama",
        "TF PPL: LO=2.60 vs TG=2.57, Δ=+1.2% → 几乎无差",
        "AR GAR-ours有outlier spikes(3-4个turn>0.2), 拉高均值至0.0617; dongre更干净=0.0226",
        "Llama与Qwen LoRA-only模式完全一致: TF GAR~0.48-0.50, AR GAR-dongre~0.02, TF PPL~2.6-2.8",
        "跨模型确认: gating机制对GAR无增量贡献, TF-AR gap完全由training-inference mismatch驱动",
    ],
}
```

核心结论：Llama LoRA-only TF GAR-ours=0.4807 与 TG TF GAR-ours=0.4836 仅差 0.6%，PPL 差 1.2%。跨模型（Llama + Qwen）确认 gating 机制是零增量，TF-AR gap 完全来自 exposure bias。

---
