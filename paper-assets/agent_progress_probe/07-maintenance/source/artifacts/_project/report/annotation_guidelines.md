# Annotation Guidelines: Agent Progress vs. Stagnation

## 1. Task Overview

You will be shown a sequence of actions taken by an AI coding agent (SWE-agent) as it attempts to fix a software bug. Each sequence is a **window** of consecutive steps from the agent's trajectory.

**Your task**: For each window, judge whether the agent is **making progress** toward solving the bug, or whether it is **stagnating** (stuck, looping, or making no meaningful headway).

---

## 2. Key Concepts

### What is a "Window"?

A window is a consecutive segment of the agent's actions, typically covering 5-10 steps. Each step consists of:
- **[Thought]**: The agent's reasoning about what to do next
- **[Command]**: The shell/editor command the agent executes
- **[Output]**: The result returned by the environment

You see these steps in sequence, as they occurred during the agent's run.

### What is "Progress"?

The agent is making progress when it is **meaningfully advancing toward a solution**. This includes:

- **Locating relevant code**: Reading files, searching for functions, understanding the codebase structure
- **Diagnosing the bug**: Examining error messages, tracing execution flow, identifying root cause
- **Implementing a fix**: Editing source code to address the identified issue
- **Verifying the fix**: Running tests, checking output, confirming the fix works
- **Exploring productively**: Trying different approaches after one fails (not repeating the same approach)

### What is "Stagnation"?

The agent is stagnating when it is **not making meaningful headway**. This includes:

- **Repeating commands**: Executing the same or very similar commands multiple times with no new information gained
- **Looping on errors**: Getting the same error repeatedly without changing approach
- **Searching fruitlessly**: Searching for files/terms that don't exist, repeatedly, without adjusting search strategy
- **Going in circles**: Returning to a state it was already in, undoing and redoing changes
- **Stuck on wrong track**: Persistently pursuing an approach that is clearly not working

---

## 3. Decision Framework

Use this flowchart to guide your judgment:

```
1. Is the agent executing different, meaningful actions across the window?
   YES → likely Progress
   NO  → likely Stagnation

2. Is the agent gaining new information or making changes to the code?
   YES → likely Progress
   NO  → likely Stagnation

3. Are the agent's actions building on each other (each step informed by previous)?
   YES → Progress
   NO  → Stagnation
```

---

## 4. Boundary Cases

### 4.1 Failure followed by correction → **PROGRESS**
The agent tries something, it fails, and the agent immediately adjusts its approach based on the error. This is productive debugging.

### 4.2 Trying a new approach that fails → **Depends**
- If the agent tries a genuinely new approach and it fails, but the agent hasn't tried this before → **Progress** (exploration)
- If the agent tries variations of the same failed approach without fundamentally changing strategy → **Stagnation**

### 4.3 Reading documentation / exploring codebase → **Usually PROGRESS**
If the agent is reading files, searching for related code, or examining the codebase structure to understand the problem, this is progress — even if no code changes are made in this window.

### 4.4 Making edits that introduce errors → **Depends**
- If the edit is a meaningful attempt at fixing the bug and the error is a minor syntax issue → **Progress**
- If the agent keeps making similar broken edits without learning from the errors → **Stagnation**

### 4.5 Agent near the end of its trajectory → **Judge the window, not the outcome**
Even if the agent eventually fails to solve the bug, individual windows may still show progress. Similarly, even in a successful trajectory, some windows may show stagnation. Judge the window in isolation.

### 4.6 Agent issues `submit` command → **Usually PROGRESS**
If the agent submits its solution, the window containing the submission is typically progress (the agent believes it has a solution). However, if the agent is submitting out of desperation without having made meaningful changes, it could be stagnation.

### 4.7 Mixed window (some progress, some stagnation) → **Majority rule**
If a window contains both productive and unproductive steps, judge based on the overall character. If more than half the steps are productive, label Progress; otherwise, Stagnation.

---

## 5. Annotation Format

For each window, provide:

| Field | Values | Description |
|-------|--------|-------------|
| **label** | `1` (Progress) or `0` (Stagnation) | Your primary judgment |
| **confidence** | `1` (uncertain), `2` (fairly sure), `3` (very sure) | How confident you are in your label |
| **comment** | Free text (optional) | Brief reason if the case is ambiguous |

### When to use each confidence level:
- **3 (very sure)**: The window clearly shows one pattern. E.g., agent is obviously looping, or agent is clearly editing code and running tests.
- **2 (fairly sure)**: The window leans one way but has some ambiguity. E.g., agent is exploring but you're not sure if it's productive.
- **1 (uncertain)**: The window is genuinely ambiguous. E.g., mixed signals, borderline cases from Section 4.

---

## 6. Annotated Examples

### Example P1: PROGRESS (confidence=3)

**Context**: Agent is working on a specutils bug about uncertainty propagation in spectrum resampling.

```
[Thought] Now, let's add the test code to `test_fix.py`. This will include the
necessary imports and a script to replicate the issue...
[Command] edit 1:1
import numpy as np
from astropy.nddata import StdDevUncertainty
from astropy.units import Quantity
from specutils import Spectrum1D
from specutils.manipulation import FluxConservingResampler
[Output] [File: /specutils/test_fix.py (30 lines total)] ...

[Thought] The test script has been created. Now, let's run the test script to
verify that the uncertainty is correctly propagated with the fix.
[Command] python test_fix.py
[Output] RuntimeWarning: invalid value encountered in divide ...

[Thought] The test script has successfully verified that the uncertainty is
correctly propagated with the fix. The RuntimeWarning indicates NaN values
which are expected at boundary regions...
[Command] rm test_fix.py
[Output] Your command ran successfully ...

[Thought] The test script has been successfully removed. Now, let's submit
our changes.
[Command] submit
```

**Why Progress**: The agent writes a test, runs it, interprets the result correctly, cleans up, and submits. Each step builds logically on the previous one. Clear forward motion.

---

### Example P2: PROGRESS (confidence=2)

**Context**: Agent is searching for relevant code in a DVC project.

```
[Thought] It seems that the DvcException is not being raised directly in the
run.py file. This might mean the exception is being raised in a different module...
[Command] search_dir "raise DvcException" dvc
[Output] Found 34 matches for "raise DvcException" in /dvc/dvc: ...

[Thought] The search returned many locations. Let's narrow down to the specific
file handling the reproduce command...
[Command] open dvc/command/reproduce.py
[Output] [File: /dvc/command/reproduce.py (85 lines total)] ...

[Thought] Now let's check where the stage execution happens...
[Command] search_file "def reproduce" dvc/repo/reproduce.py
[Output] Found 2 matches ...
```

**Why Progress**: The agent is systematically narrowing its search — from a broad directory search to specific files. Each search result informs the next action. This is productive exploration even though no code changes are made.

---

### Example P3: PROGRESS (confidence=2)

**Context**: Agent is fixing a bug in a Textual framework test, encountering errors along the way.

```
[Thought] The test script failed because there is no active app context.
To fix this, we need to create an app instance...
[Command] edit 1:1
from textual.app import App
from textual.widget import Widget
app = App()
parent = Widget()
child = Widget()
...
[Output] [File: /textual/test_move_child.py (41 lines total)] ...

[Thought] It looks like there was a duplication error in the test script.
Let's fix the script by removing the duplicated lines...
[Command] edit 1:41
from textual.app import App
from textual.widget import Widget
app = App()
...
[Output] [File: /textual/test_move_child.py (23 lines total)] ...

[Thought] The test script has been updated. Let's run it again.
[Command] python test_move_child.py
[Output] Test completed successfully, no errors.
```

**Why Progress**: Even though the agent made an error (duplication), it immediately recognized and fixed it. The trajectory shows error → correction → success, which is productive debugging.

---

### Example S1: STAGNATION (confidence=3)

**Context**: Agent is searching for code in a B2 Command Line Tool project.

```
[Thought] It seems that our search for "synchronize" didn't find any matches.
Let's try searching for "sync action queue"...
[Command] search_file "sync action queue"
[Output] No matches found for "sync action queue" ...

[Thought] It seems that our search for "sync action queue" didn't find any
matches either. The code might handle the sync action queue in a specific file...
[Command] find_file "synchronization actions queue"
[Output] No matches found for "synchronization actions queue" ...

[Thought] Since our search for "synchronization actions queue" didn't find
any matches, it's possible that the code doesn't reference it directly...
[Command] find_file "sync actions"
[Output] No matches found for "sync actions" ...
```

**Why Stagnation**: The agent is searching for variations of the same term, getting "No matches found" each time, without meaningfully changing its strategy. It's not trying different keywords, examining the directory structure, or reading likely files. This is fruitless repetitive searching.

---

### Example S2: STAGNATION (confidence=3)

**Context**: Agent is lost in a DVC project, searching for files that don't exist.

```
[Thought] It seems there are no files named `filter.py`. Let's try searching
for the `find.py` file within the `dvc` directory...
[Command] find_file "find.py" dvc
[Output] No matches found for "find.py" in /dvc/dvc

[Thought] It seems there are no files named `find.py`. Let's try searching
for the `kmeans.py` file within the `dvc` directory...
[Command] find_file "kmeans.py" dvc
[Output] No matches found for "kmeans.py" in /dvc/dvc

[Thought] It seems there are no files named `kmeans.py`. Let's try searching
for the `visualize.py` file within the `dvc` directory...
[Command] find_file "visualize.py" dvc
[Output] No matches found for "visualize.py" in /dvc/dvc

[Thought] It seems there are no files named `visualize.py`. Let's try searching
for the `transform.py` file within the `dvc` directory...
[Command] find_file "transform.py" dvc
```

**Why Stagnation**: The agent is guessing random filenames (filter.py, find.py, kmeans.py, visualize.py, transform.py) that have nothing to do with the DVC project. Every search fails. The agent shows no learning from failures and no strategic adjustment. This is classic "flailing."

---

### Example S3: STAGNATION (confidence=3)

**Context**: Agent repeatedly tries to `cd` into a directory that doesn't exist.

```
[Thought] It seems that the stix2-pattern-validator-v2 repository is not
accessible in the current environment...
[Command] cd stix2-pattern-validator-v2
[Output] /bin/bash: line 650: cd: stix2-pattern-validator-v2: No such file or directory

[Thought] It seems that the stix2-pattern-validator-v2 repository is not
accessible in the current environment...
[Command] cd stix2-pattern-validator-v2
[Output] /bin/bash: line 663: cd: stix2-pattern-validator-v2: No such file or directory

[Thought] It seems that the stix2-pattern-validator-v2 repository is not
accessible in the current environment...
[Command] cd stix2-pattern-validator-v2
[Output] /bin/bash: line 676: cd: stix2-pattern-validator-v2: No such file or directory

[Thought] It seems that the stix2-pattern-validator-v2 repository is not
accessible in the current environment...
[Command] cd stix2-pattern-validator-v2
[Output] /bin/bash: line 689: cd: stix2-pattern-validator-v2: No such file or directory
```

**Why Stagnation**: The agent executes the exact same command 4 times, getting the exact same error. The thought text is nearly identical each time. This is the clearest possible stagnation — a pure repetition loop with zero adaptation.

---

## 7. Important Reminders

1. **Judge the window, not the trajectory outcome.** A window from a successful trajectory can still show stagnation. A window from a failed trajectory can still show progress.

2. **Don't read too much into individual steps.** Focus on the overall pattern across the window. One wasted step in an otherwise productive window is still Progress.

3. **When in doubt, use confidence=1.** Ambiguous cases are expected and valuable. Don't force a high-confidence label when you're genuinely unsure.

4. **The `[Thought]` text is the agent's reasoning, not ground truth.** The agent may claim to be making progress when it's clearly stuck. Judge by actions and results, not just the agent's self-assessment.

5. **Speed matters less than consistency.** Take your time to be consistent across windows. If a similar pattern appears later, it should get the same label.

---

## 8. Workflow

1. **Calibration round** (before starting): All 3 annotators label the same 15 windows independently. Then meet to discuss disagreements and align on edge cases.
2. **Main annotation**: Label your assigned batch. Flag any windows you find genuinely impossible to label.
3. **Adjudication**: After main annotation, cases with 3-way disagreement are discussed and resolved.
