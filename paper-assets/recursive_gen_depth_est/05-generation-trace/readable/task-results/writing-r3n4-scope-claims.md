# writing r3n4 scope claims

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r3n4-scope-claims_20260516T011030_result.json`
- **Structured JSON:** [`40a4343b59a9c4f19c63.json`](../../sessions/40/40a4343b59a9c4f19c63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits confirmed. Here's the summary:

**Checklist results:**

| Check | Status |
|---|---|
| Every "consistent"/"universal" followed by scope | ✅ — abstract, introduction, method already scoped; fixed 1 unscoped instance in discussion.tex |
| Introduction "key insight" scoped | ✅ — L14 already says "the three model families and three decoding strategies studied" |
| Method scope disclaimer | ✅ — L26 already present |
| Limitations: LoRA vs wild contamination gap | ✅ — **added** sentence in "Controlled vs ecological setting" paragraph |
| No implied universal generalization | ✅ — fixed discussion.tex "generalizes across model families" and conclusion.tex "across all settings" |

**Edits made (3 files, 3 changes):**

1. **discussion.tex L5**: "generalizes across model families" → "across the three studied model families"; "a measurable early warning" → "a candidate early-warning signal...within this experimental scope"
2. **conclusion.tex L9**: "across all settings" → "across all nine model--strategy settings"
3. **conclusion.tex L13-14**: Added LoRA-vs-wild divergence sentence: *"This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure."*

R3-N4 scope-界定 action item updated to `done` in review_issues.yaml. The overall R3-N4 status remains `in_progress` because the pilot experiment (plan_015) is still running separately.

---
