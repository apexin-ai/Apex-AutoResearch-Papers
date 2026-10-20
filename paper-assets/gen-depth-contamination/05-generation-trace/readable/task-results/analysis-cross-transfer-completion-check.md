# analysis cross transfer completion check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-transfer-completion-check_20260520T003813_result.json`
- **Structured JSON:** [`829a2ba5b7773fe3f030.json`](../../sessions/82/829a2ba5b7773fe3f030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete status report:

---

## DeBERTa Cross-Transfer Status

### Processes
All 3 PIDs (208306/208307/208308) exited. All 4 GPUs idle (0%, 0 MiB). No tmux sessions.

### GPU Assignments (all completed successfully)
| GPU | Pairs Run |
|---|---|
| GPU1 | pythia↔olmo, pythia↔qwen7b |
| GPU2 | olmo↔qwen7b, pythia→llama8b, llama8b→pythia |
| GPU3 | olmo↔llama8b, **pythia↔mistral7b** (wrong pairs) |

### Coverage: 10/12 expected pairs complete

**Missing 2 pairs** (GPU3 ran mistral7b pairs instead):
- `wiki_qwen7b → wiki_llama8b`
- `wiki_llama8b → wiki_qwen7b`

**Extra 2 pairs** (bonus, not in expected 4-model set):
- `wiki_pythia → wiki_mistral7b` (K\*=2)
- `wiki_mistral7b → wiki_pythia` (K\*=2)

### K\* Indexing: 3 JSONs need +1 correction

None of the 12 JSONs have the `kstar_indexing` field. 3 are still 0-indexed:

| File | Current K\* | Corrected K\* (1-indexed) |
|---|---|---|
| `wiki_pythia__to__wiki_olmo` | 0 | **1** |
| `wiki_olmo__to__wiki_qwen7b` | 1 | **2** |
| `wiki_olmo__to__wiki_llama8b` | 1 | **2** |

Remaining 7 JSONs already have correct 1-indexed values.

### Cross-Transfer Matrix (corrected K\*, 1-indexed)

| Train ↓ \ Test → | pythia | olmo | qwen7b | llama8b |
|---|---|---|---|---|
| **pythia** | — | K\*=1 | K\*=3 | K\*=2 |
| **olmo** | K\*=1 | — | K\*=2 | K\*=2 |
| **qwen7b** | K\*=2 | K\*=1 | — | ❌ missing |
| **llama8b** | K\*=2 | K\*=1 | ❌ missing | — |

### Actions Needed
1. **Rerun 2 missing pairs** on an available GPU: qwen7b↔llama8b
2. **Fix 3 JSONs**: apply +1 to kstar and add `"kstar_indexing": "1-indexed"` to all JSONs
3. **Registry**: not updated (experiment incomplete at 10/12)

---
