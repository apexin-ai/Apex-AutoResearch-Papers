# paper page count surgery

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_page_count_surgery_20260528T182642_result.json`
- **Structured JSON:** [`be2634615d332d0a2d92.json`](../../sessions/be/be2634615d332d0a2d92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:
- **Body pages: 8** (Limitations section ends on page 8, References begin at bottom of page 8)
- **Undefined references: 0**
- **"??" occurrences: 0**
- **Total PDF pages: 31**

Changes made:
1. **method.tex**: Compressed models/connectors description (4 paragraphs → 1), scoring functions (3 long paragraphs → 2 compact ones + moved attention alternatives to appendix), retention ratio paragraph (1 long → 3 sentences), CV spectrum equation (split `\begin{split}` → inline math), CV predictor paragraph (2 paragraphs → 1 + moved attention entropy to appendix), VTR section (2 paragraphs → 1)
2. **experiments.tex**: Compressed benchmark/models/protocol descriptions, removed cliff-vs-graded paragraph, shortened inverted-U margin paragraph, shortened figure captions
3. **appendix.tex**: Added "Attention-Based Scoring Methods" (moved from method), "Attention Entropy as Diagnostic" (moved from method), renamed existing subsection to "Attention-Based Scoring Results"
4. **main.tex**: Tightened float spacing (`textfloatsep` 8→6pt, `abovecaptionskip` 4→3pt) and added display math spacing controls

---
