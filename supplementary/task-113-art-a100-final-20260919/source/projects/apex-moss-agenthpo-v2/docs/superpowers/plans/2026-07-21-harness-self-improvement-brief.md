# Harness Self-Improvement Research Brief Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a mentor-ready Chinese Markdown briefing that compares Meta-Harness, WECO AIDE², and RHI, extracts reusable mechanisms, and proposes a fused MOSS architecture.

**Architecture:** Produce one self-contained research document organized horizontally by architecture, evolution loop, feedback, evaluation, benchmark, generalization, results, and evidence boundaries. Follow the comparison with a mechanism inventory and a three-layer MOSS proposal that separates global evolution, task adaptation, and evaluation.

**Tech Stack:** Markdown, Mermaid, official papers, official project pages, official benchmark repositories.

## Global Constraints

- Write for a technical manager and support both research reporting and technical decision-making.
- Do not organize the body as three independent paper summaries.
- Do not add a standalone terminology tutorial.
- Separate published facts, authors' claims, and MOSS design inferences.
- Do not modify code, `CLAUDE.md`, or `AGENTS.md`.

---

### Task 1: Write and verify the comparative research brief

**Files:**
- Create: `docs/research/harness-self-improvement-comparison.md`
- Reference: `docs/research/meta-harness.md`
- Reference: `docs/research/harnessx.md`
- Reference: `docs/superpowers/specs/2026-07-21-harness-self-improvement-brief-design.md`

**Interfaces:**
- Consumes: Published architecture, benchmark, result, and limitation claims from official primary sources.
- Produces: A standalone Markdown briefing for mentor review and MOSS architecture discussion.

- [x] **Step 1: Draft the execution summary and unified comparison**

Write the title, scope note, executive summary, positioning table, architecture table, Mermaid data-flow diagrams, evolution-mechanism table, benchmark/generalization table, and evidence-boundary table. Clearly state that Meta-Harness searches task-specific executable harnesses, AIDE² evolves one general autoresearch harness and tests selected checkpoints externally, and RHI adapts a prompt harness separately for each concrete task.

- [x] **Step 2: Extract reusable mechanisms and incompatibilities**

Add a mechanism inventory grouped by storage/history, proposer/search, task adaptation, evaluation isolation, context routing, reward-hacking defense, and cost control. Explain that full raw-history retention and per-call context compression are complementary, while global evolution and task-local adaptation require separate datasets and promotion gates.

- [x] **Step 3: Define the fused MOSS architecture**

Add a three-layer Mermaid architecture covering global harness evolution, task-level prompt adaptation, and execution/evaluation. Specify the harness registry, lineage store, filesystem trace database, global coding-agent proposer, local RHI optimizer, evaluators, verifiers, judge calibration, budget controller, rollback, and frozen external benchmark gate.

- [x] **Step 4: Add an incremental delivery roadmap and mentor decisions**

Define Phase 1 as trace/version/evaluation foundations, Phase 2 as task-level Contract/Hop optimization, and Phase 3 as global code-level evolution and external-generalization promotion. End with concrete decision questions covering optimization scope, private metrics, frozen benchmarks, judge/verifier weighting, cost accounting, and release thresholds.

- [x] **Step 5: Verify structure and content**

Run:

```bash
rg -n '^#|^##|^###' docs/research/harness-self-improvement-comparison.md
rg -n 'Meta-Harness|AIDE²|RHI|MOSS|private|held-out|reward hacking|Contract|Hop' docs/research/harness-self-improvement-comparison.md
git diff --check
```

Expected:

- The heading output contains the three required parts: comparison, reusable mechanisms, and fused MOSS proposal.
- Every required research term appears in context.
- `git diff --check` produces no output.

- [x] **Step 6: Check Mermaid and source links**

Run a local structural check that verifies paired Mermaid fences and extracts all HTTP links:

```bash
python - <<'PY'
from pathlib import Path
import re

path = Path('docs/research/harness-self-improvement-comparison.md')
text = path.read_text()
assert text.count('```mermaid') >= 2
assert text.count('```') % 2 == 0
links = re.findall(r'https://[^)\s]+', text)
assert len(links) >= 8
print(f'mermaid_blocks={text.count("```mermaid")}, links={len(links)}')
PY
```

Expected: at least two Mermaid blocks and at least eight primary-source links.

- [x] **Step 7: Commit the final document**

```bash
git add docs/research/harness-self-improvement-comparison.md docs/superpowers/plans/2026-07-21-harness-self-improvement-brief.md
git commit -m "docs: compare harness self-improvement systems"
```
