# d062: Beam Search (k=4) Latency Benchmark Results

## Setup
- **Model**: Qwen3-8B LoRA SciERC merged
- **Dataset**: SciERC test set (551 samples)
- **Server**: westd-21461 (CUDA:0 via CUDA_VISIBLE_DEVICES=1)
- **Decoding**: beam search, num_beams=4, max_new_tokens=2048
- **Modes**: unconstrained vs full_s1 (constrained)

## Timing Results

### Per-document latency (s/doc)

| Condition | Mean | Median | P5 | P95 | Std | Min | Max | Total (s) |
|-----------|------|--------|-----|------|------|------|------|-----------|
| Greedy unconstrained (P8c) | 2.612 | - | - | - | - | - | - | - |
| Greedy constrained (P8c) | 2.873 | - | - | - | - | - | - | - |
| **Beam-4 unconstrained** | **3.446** | 3.030 | 1.354 | 7.227 | 1.975 | 0.538 | 14.985 | 1898.7 |
| **Beam-4 constrained** | **4.013** | 3.581 | 1.762 | 8.040 | 2.126 | 0.907 | 17.163 | 2211.0 |

### Overhead Analysis

| Comparison | Ratio |
|-----------|-------|
| Beam-4 unc / Greedy unc | 1.319x |
| Beam-4 con / Greedy con | 1.397x |
| Constraint overhead (beam): con/unc | 1.165x |
| Constraint overhead (greedy): con/unc | 1.100x |

## Key Findings

1. **Beam search adds ~32-40% latency** over greedy decoding, depending on whether constraints are applied.
2. **Constraint overhead increases slightly under beam search** (16.5% vs 10.0% for greedy), because the constraint checker runs on all 4 beams at each token step.
3. **Total constraint + beam overhead**: beam-4 constrained is 1.54x slower than greedy unconstrained (4.013 / 2.612).
4. **Practical implication**: For 551 SciERC test sentences, beam-4 constrained takes ~37 min vs ~24 min for greedy unconstrained. The overhead is moderate and acceptable for offline/batch IE.

## Output Files
- `/root/autodl-tmp/schema_outputs/d062_beam4_unconstrained.jsonl` (551 lines)
- `/root/autodl-tmp/schema_outputs/d062_beam4_constrained.jsonl` (551 lines)
- Log: `/root/autodl-tmp/schema_outputs/d062_beam_latency.log`
