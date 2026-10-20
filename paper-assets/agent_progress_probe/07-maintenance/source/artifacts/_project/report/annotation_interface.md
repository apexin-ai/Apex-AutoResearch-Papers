# Annotation Interface & Quality Control

## 1. Tool Recommendation

### Option A: Google Sheets (Recommended for speed)

**Why**: Fastest setup, zero infrastructure, all 3 annotators can work in parallel copies, easy to export for κ computation.

**Setup**:
- One master sheet with all 450 windows
- 3 copies (one per annotator), each with `annotator_label`, `confidence`, `comment` columns unlocked
- Columns visible to annotators: `id`, `agent_actions`, `trajectory_outcome`
- Columns hidden from annotators: `majority_label`, `confidence` (LF confidence — to avoid anchoring bias)

**Pros**: No setup time, familiar interface, easy sharing.
**Cons**: Long text rendering in cells is awkward; no built-in annotation UX.

### Option B: Label Studio (Recommended for quality)

**Why**: Purpose-built annotation tool with IAA tracking, task queue management, and structured labeling UI.

**Setup**:
```bash
pip install label-studio
label-studio start --port 8080
```

**Configuration**:
```xml
<View>
  <Header value="Agent Trajectory Window" />
  <Text name="context" value="$trajectory_outcome" />
  <Text name="actions" value="$agent_actions" />
  <Choices name="label" toName="actions" choice="single">
    <Choice value="Progress" />
    <Choice value="Stagnation" />
  </Choices>
  <Rating name="confidence" toName="actions" maxRating="3" />
  <TextArea name="comment" toName="actions"
            placeholder="Optional: explain your reasoning"
            rows="2" />
</View>
```

**Pros**: Better UX for reading long text, built-in agreement metrics, task assignment.
**Cons**: Requires server setup (can run locally or on a shared machine).

### Option C: Custom HTML Page (Middle ground)

A single-page HTML/JS app that loads the CSV, renders one window at a time with syntax-highlighted actions, and saves labels to localStorage + CSV export.

**Pros**: Good UX, no server needed, works offline.
**Cons**: Requires ~2 hours to build.

### Recommendation

**Use Google Sheets** for the calibration round (15 windows), then switch to **Label Studio** for the main annotation if the team has server access. If server setup is blocked, stay with Google Sheets for all 450.

---

## 2. Data Format

### What Each Window Shows to the Annotator

| Field | Source | Shown? | Purpose |
|-------|--------|--------|---------|
| `id` | Sequential | Yes | Reference number |
| `agent_actions` | Formatted text | Yes | The actual steps to judge |
| `trajectory_outcome` | Metadata | Yes | Context (submitted/exit_context/early_exit) |
| `trajectory_id` | Metadata | No (available for debugging) | Which trajectory this comes from |
| `window_idx` | Metadata | No | Position in trajectory |
| `majority_label` | LF vote | **No** | Hidden to avoid anchoring |
| `confidence` (LF) | LF agreement | **No** | Hidden to avoid anchoring |

### Agent Actions Format

The `agent_actions` field is pre-formatted with `[Thought]`, `[Command]`, `[Output]` markers:

```
[Thought] The error indicates that energy_bins should be specified as a
Quantity with a unit...
[Command] edit 15:15
energy_bins = [0.5, 1.5, 2.5] * u.TeV
end_of_edit
[Output] Your proposed edit has introduced new syntax errors...
---
[Thought] The edit command caused a syntax error. Let me fix the indentation...
[Command] edit 15:15
    energy_bins = [0.5, 1.5, 2.5] * u.TeV
end_of_edit
[Output] [File: /specutils/test_fix.py (30 lines total)] ...
```

Steps within a window are separated by `---` dividers.

### Truncation Policy

- `[Output]` fields are truncated to 500 characters with `...` suffix if longer (full file listings, long error traces)
- `[Thought]` fields are truncated to 300 characters
- `[Command]` fields are shown in full

This keeps each window readable in ~1-2 minutes while preserving the essential information for judgment.

---

## 3. Annotation Flow

### Phase 0: Annotator Training (30 min)

1. All annotators read the Annotation Guidelines document
2. Walk through the 6 examples together
3. Q&A on edge cases

### Phase 1: Calibration Round (1-2 hours)

**Goal**: Align annotators and identify guideline gaps.

| Step | Action | Detail |
|------|--------|--------|
| 1 | Independent labeling | 15 windows × 3 annotators (same windows) |
| 2 | Compute pilot κ | Expect κ = 0.4-0.7 on first pass |
| 3 | Disagreement discussion | Go through each disagreement, document resolution |
| 4 | Update guidelines | Add clarifications for discovered edge cases |
| 5 | Second pilot (if κ < 0.5) | 10 new windows, re-check agreement |

**Calibration window selection**: Choose 5 from each of:
- Clear progress (conf=3, label=1)
- Clear stagnation (conf=3, label=0)
- Ambiguous (conf=1, mixed LFs)

### Phase 2: Main Annotation (3-4 hours per annotator)

| Detail | Value |
|--------|-------|
| Total windows | 450 |
| All windows labeled by | All 3 annotators |
| Estimated time per window | 1-2 minutes |
| Estimated total time | 8-15 hours per annotator |
| Batch size | 50 windows per session |
| Break recommendation | Every 50 windows (avoid fatigue-induced drift) |

**Assignment**: All 3 annotators label all 450 windows (full overlap for Fleiss κ computation).

### Phase 3: Adjudication (1-2 hours)

1. Compute Fleiss κ on full 450-window set
2. Identify 3-way disagreements (all annotators give different labels — unlikely with binary labels but possible if treating "refuse to label" as a third option)
3. Identify 2-vs-1 splits where the minority annotator has confidence ≥ 2
4. Discuss and resolve these cases → produce final gold label via majority vote or consensus

---

## 4. Quality Control

### 4.1 Inter-Annotator Agreement

**Primary metric**: Fleiss' κ (for 3 raters, binary labels)

```python
from sklearn.metrics import cohen_kappa_score
import numpy as np

def fleiss_kappa(ratings_matrix):
    """
    ratings_matrix: (n_items, n_categories) — count of raters per category
    """
    n_items, n_cat = ratings_matrix.shape
    n_raters = ratings_matrix.sum(axis=1)[0]
    
    p_j = ratings_matrix.sum(axis=0) / (n_items * n_raters)
    P_i = (ratings_matrix ** 2).sum(axis=1) - n_raters
    P_i = P_i / (n_raters * (n_raters - 1))
    
    P_bar = P_i.mean()
    P_e = (p_j ** 2).sum()
    
    kappa = (P_bar - P_e) / (1 - P_e)
    return kappa

# Usage:
# ratings[i] = [count_stagnation, count_progress] for window i
# e.g., if 2 annotators say progress and 1 says stagnation: [1, 2]
```

**Interpretation**:

| κ Range | Interpretation | Action |
|---------|---------------|--------|
| κ ≥ 0.8 | Almost perfect | Proceed with gold set |
| 0.6 ≤ κ < 0.8 | Substantial | Acceptable; adjudicate disagreements |
| 0.4 ≤ κ < 0.6 | Moderate | Review guidelines, add more examples, possibly re-annotate |
| κ < 0.4 | Poor | Major guideline revision needed before proceeding |

**Target**: κ ≥ 0.6 (substantial agreement).

### 4.2 Annotator Drift Detection

Monitor per-annotator statistics across batches:

| Metric | Check | Flag if |
|--------|-------|---------|
| Progress rate | Per annotator across batches | Differs by > 15pp from other annotators |
| Confidence distribution | Per annotator | One annotator uses confidence=3 for > 50% of labels |
| Labeling speed | Time per window | < 20 seconds average (too fast = not reading carefully) |
| Agreement with majority | Pairwise κ | One pair has κ < 0.5 while others are > 0.7 |

### 4.3 Gold Label Construction

For each window, the final gold label is determined by:

1. **Unanimous agreement** (3/3): Use that label. Confidence = max(annotator confidences).
2. **Majority agreement** (2/3): Use majority label. Confidence = average of majority annotator confidences.
3. **All disagree** (N/A for binary, but if allowing "skip"): Send to adjudication round.

### 4.4 Problematic Window Handling

If an annotator flags a window as "impossible to label":
- If 2+ annotators flag it → exclude from gold set, document as ambiguous
- If 1 annotator flags it → use the other 2 annotators' majority label

---

## 5. Post-Annotation Analysis Plan

### 5.1 IAA Report
- Overall Fleiss κ
- κ by stratum (confidence level, label, outcome)
- Confusion matrix between annotator pairs

### 5.2 LF Accuracy vs. Human Gold
- Per-LF accuracy, precision, recall against gold labels
- Majority vote accuracy against gold labels
- Identify systematic LF biases (e.g., outcome_backpropagation may over-predict stagnation for failed trajectories)

### 5.3 Label Model Evaluation
- Train label model on LF outputs → predict labels for gold-set windows → compare against gold
- This directly tests Claim 1: "temporal label model outperforms naive majority vote"

### 5.4 Probe Evaluation
- Compare probe predictions against gold labels
- Identify probe failure modes (high-confidence errors that humans get right)

---

## 6. Timeline

| Date | Milestone |
|------|-----------|
| 5/14 (today) | Materials ready (this document + guidelines + sampling strategy) |
| 5/15 | Generate final 450-window sample CSV, set up annotation tool |
| 5/16 | Annotator training + calibration round (15 windows) |
| 5/17-5/19 | Main annotation (3 annotators × 450 windows) |
| 5/20 | Compute κ, adjudication if needed |
| 5/21 | Gold set finalized, begin label model evaluation |
| 5/25 | EMNLP deadline |

---

## 7. File Deliverables

| File | Format | Content |
|------|--------|---------|
| `annotation_sample_450_blind.csv` | CSV | Windows for annotators (no gold labels) |
| `annotations_annotator_{1,2,3}.csv` | CSV | Each annotator's labels |
| `gold_labels_450.csv` | CSV | Adjudicated gold labels |
| `iaa_report.md` | Markdown | Agreement statistics |
| `lf_vs_gold_analysis.json` | JSON | LF accuracy breakdown |
