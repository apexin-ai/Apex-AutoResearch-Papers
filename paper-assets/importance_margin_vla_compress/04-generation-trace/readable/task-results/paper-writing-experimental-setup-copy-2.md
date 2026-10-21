# paper writing experimental setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experimental_setup_20260521T120135_result.json`
- **Structured JSON:** [`066e03042fc9ed74df3d.json`](../../sessions/06/066e03042fc9ed74df3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1206 raw words (~1050 rendered). Final checks pass: no em-dash, no explanatory en-dash, no "Importantly/Notably/Interestingly", no paragraph-initial "This/These/It", no -ing participle endings after the fixes.

Changes from the previous version:
- **§3.1**: Added π0.5 (4B, 768 tokens, 3 cameras, ×√d scaling) and CogACT (literature corroboration, 74.2% SR under 78% pruning). Expanded LIBERO suite descriptions. Added π0.5 98.2% baseline.
- **§3.2**: Merged the old §3.2 (SmolVLA ablation) and §3.3 (cross-model protocol) into a unified pruning protocol section. Two methods (L2 norm-based vs. random) with model-specific k ranges. Added the OpenVLA-vs-X-VLA cross-method reasoning.
- **§3.3**: VTR setup retained, minor additions (scaled dot-product attention, M=16 compression ratio, 3-seed evaluation).
- **§3.4**: New standalone section for diagnostic metrics (CV + attention entropy), moved out of the old §3.3. Added CV ranges for each taxonomy class and the OFT/OpenVLA entropy comparison.

---
