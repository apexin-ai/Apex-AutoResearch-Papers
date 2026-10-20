# debug ablation 50demos main check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_ablation_50demos_main_check_20260517T214805_result.json`
- **Structured JSON:** [`e797616803cccbd9bd3e.json`](../../sessions/e7/e797616803cccbd9bd3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Experiment Status ===
Status: SUCCESS
Output file: exists (15209 bytes, created May 18 05:46)

=== Analysis Results ===

Layer  | baseline   | control8   | all24      | all32     
------------------------------------------------------------
L1     | 0.5567     | 0.5732     | 0.6153     | 0.5823    
L8     | 0.6199     | 0.6311     | 0.6377     | 0.6311    
L13    | 0.6763     | 0.6787     | 0.6762     | 0.6636    

=== Bootstrap Δ vs baseline (95% CI) ===
all24 L1:  Δ=+0.0585 [0.0420, 0.0752] p=0.0000
all24 L8:  Δ=+0.0177 [0.0085, 0.0277] p=0.0000
all24 L13: Δ=-0.0002 [-0.0087, 0.0088] p=0.9556
all32 L1:  Δ=+0.0256 [0.0153, 0.0370] p=0.0000
all32 L8:  Δ=+0.0112 [-0.0075, 0.0289] p=0.2394
all32 L13: Δ=-0.0127 [-0.0261, -0.0020] p=0.0138
control8 L1:  Δ=+0.0165 [0.0046, 0.0269] p=0.0084
control8 L8:  Δ=+0.0111 [0.0018, 0.0224] p=0.0166
control8 L13: Δ=+0.0023 [-0.0078, 0.0113] p=0.6308

=== Specificity Check (all24 vs control8) ===
L1:  Δ=+0.0421 [0.0286, 0.0563] p=0.0000
L8:  Δ=+0.0066 [-0.0043, 0.0187] p=0.2516
L13: Δ=-0.0025 [-0.0169, 0.0130] p=0.7354

Saved figures:
- fig_ablation_4condition_bar.pdf
- fig_ablation_3layer_grouped.pdf
Saved combined JSON: ablation_50demos_combined.json
```

关键发现：ablate_all24 在 L1 层的 action probe R² 提升最大（+0.0585, p<0.001），且显著超过 control8 随机头（+0.0421, p<0.001），证明效果具有 specificity。效果集中在早期层（L1），中间层（L8）效果减弱，最后层（L13）无显著差异。

---
