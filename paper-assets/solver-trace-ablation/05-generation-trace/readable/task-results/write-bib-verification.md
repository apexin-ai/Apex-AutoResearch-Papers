# write bib verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_bib-verification_20260514T220538_result.json`
- **Structured JSON:** [`6f43432ad6c28e2a6fc0.json`](../../sessions/6f/6f43432ad6c28e2a6fc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three entries verify against the sources. No edits needed.

### Verification Results

**1. `rlsf` — VERIFIED OK**
- Authors confirmed: Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh ✓
- Title "RLSF: Fine-tuning LLMs via Symbolic Feedback" matches arXiv 2405.16661v1 ✓
- (Note: v2 was retitled to "RLSF: Reinforcement Learning via Symbolic Feedback" — current bib uses v1 title, which is consistent with the arXiv ID listed.)

**2. `spurious-rewards` — VERIFIED OK**
- All 14 authors confirmed in correct order: Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Yiping Wang, Sewoong Oh, Simon Shaolei Du, Nathan Lambert, Sewon Min, Ranjay Krishna, Yulia Tsvetkov, Hannaneh Hajishirzi, Pang Wei Koh, Luke Zettlemoyer ✓
- Title, arXiv ID, year all match ✓

**3. `kwa-catastrophic-goodhart` — VERIFIED OK**
- Authors confirmed: Thomas Kwa, Drake Thomas, Adrià Garriga-Alonso ✓
- Title matches (NeurIPS proceedings uses lowercase "regularizing" in the URL, but the paper title content matches) ✓
- Venue NeurIPS 2024 confirmed ✓

No edits made to `references.bib`.

Sources:
- [arXiv: RLSF Fine-tuning LLMs via Symbolic Feedback](https://arxiv.org/abs/2405.16661)
- [arXiv: Spurious Rewards: Rethinking Training Signals in RLVR](https://arxiv.org/abs/2506.10947)
- [NeurIPS 2024: Catastrophic Goodhart](https://proceedings.neurips.cc//paper_files/paper/2024/hash/1a8189929f3d7bd6183718f42c3f4309-Abstract-Conference.html)
- [arXiv: Catastrophic Goodhart](https://arxiv.org/abs/2407.14503)

---
