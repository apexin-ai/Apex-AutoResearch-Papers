# MiniHack/Permadeath Environment Feasibility Report

**Date**: 2026-05-19
**Purpose**: Evaluate MiniHack and alternatives as second permadeath environment for episode-level counterfactual diagnostic framework
**DDL**: EMNLP 2026-05-25 (~6 days)

---

## 1. MiniHack Evaluation

### API Availability

- **Installation**: `pip install minihack` (PyPI, requires cmake + NLE as dependency)
- **NLE dependency**: `pip install nle` installs pre-built manylinux wheel
- **Gymnasium interface**: Standard `gym.make("MiniHack-Room-5x5-v0")`, `reset()`, `step()`
- **Maturity**: Facebook AI Research project, NeurIPS 2021 Datasets & Benchmarks, actively maintained (last release 2025-03)

### Text Observation Support

**Native options** (via `observation_keys` parameter):
- `tty_chars`: (24, 80) ASCII screen representation (full terminal view)
- `message`: (256,) UTF-8 encoded on-screen message
- `screen_descriptions`: (21, 79, 80) per-tile textual descriptions
- `inv_strs`: (55, 80) textual inventory descriptions

**External wrappers**:
- **nle-language-wrapper** (`pip install nle-language-wrapper`): Converts all observations to structured text. Output format:
  - `text_glyphs`: "dark area far west, vertical wall near east"
  - `text_message`: Current game messages
  - `text_blstats`: HP, strength, gold, hunger, etc. in text
  - `text_inventory`: Item list with descriptions
  - `text_cursor`: Description of tile under cursor
  - **Text actions**: Can use "north", "wait", "apply" instead of discrete integers
- **BALROG framework** (ICLR 2025): Unified wrapper, tested with GPT-4o/Claude/Llama, supports vLLM for local inference

### Death Signal

- **Clear and reliable**: Episode terminates with `done=True` when HP reaches 0
- **Death causes**: Monsters, traps, starvation, poison, rotten food, falling
- **Trackable**: `blstats` contains current HP and max HP at every step
- **Info dict**: Contains death-related flags

### Deterministic Mode

- **Seed support**: `env.reset(seed=123)` controls procedural generation
- **Reproducibility**: Same seed + same actions = same state transitions
- **Caveat**: NetHack has some internal stochasticity (monster AI, item generation); same seed guarantees same map layout and initial conditions, but combat outcomes may vary slightly
- **Evaluation protocol**: NLE explicitly supports held-out seed evaluation for generalization testing

### Action Space

- **Navigation tasks** (Room, Corridor, River): ~8-12 discrete actions (8 compass directions + open/kick/search/eat)
- **Skill tasks** (Quest, Boxoban): Up to 75 discrete actions (inventory, spells, wands, combat)
- **Full NLE**: 98 pre-defined actions (16 compass + 82 commands)
- **Configurable**: Can restrict action space per task via `actions=` parameter

### LLM Agent Performance (from BALROG, ICLR 2025)

| Model | MiniHack Avg | NetHack Avg |
|---|---|---|
| Claude 3.5 Sonnet | 32.64% (overall) | ~1.5% |
| GPT-4o | ~30% (overall) | ~1% |
| o1-preview | Best on NetHack | 1.57% |
| Llama 3.1 70B | ~25% (overall) | <1% |

**Critical finding**: MiniHack Quest and Boxoban tasks were **never solved by any model**. Navigation tasks (Room, Corridor) are tractable. NetHack is essentially unsolvable for current LLMs.

**Known failure mode**: LLMs frequently exit the dungeon immediately (instant death) despite correctly identifying that exit = death when asked separately. This is the "knowing-doing gap."

### LLM Agent Implementation Complexity: **3/5**

**Existing codebases**:
1. **BALROG** (github.com/balrog-ai/BALROG): Full framework, supports vLLM, MiniHack included, conda install. Most complete option.
2. **NetPlay** (github.com/CommanderCero/NetPlay): GPT-4 only, skill-based, works on full NetHack. Code is small (~60% Python, 40% notebooks).
3. **nethack-llm** (github.com/kolbytn/nethack-llm): Supports HuggingFace models + OpenAI. Simpler but less documented.

**Recommended path**: Use BALROG framework (already wraps MiniHack, supports vLLM for local models).

### Estimated Implementation Time

| Component | Time |
|---|---|
| Install BALROG + MiniHack + nle-language-wrapper | 0.5 day |
| Configure text wrapper for target MiniHack tasks | 0.5 day |
| Adapt for Qwen2.5-7B via vLLM | 1 day |
| Build deterministic baseline agent | 1-2 days |
| Run 100 episodes (50 LLM + 50 deterministic) | 1 day |
| Compute counterfactual metrics + analysis | 0.5 day |
| **Total** | **4-5.5 days** |

### Estimated 100-Episode Runtime

- Navigation tasks (Room/Corridor): ~50-200 steps/episode
- Qwen2.5-7B via vLLM on single GPU: ~0.5-1s per step (prompt + generation)
- 100 episodes x 100 steps avg = ~10,000 inference calls
- **Estimated wall time**: 3-6 hours on 1x GPU (parallelizable)

### Key Risks

1. **Navigation tasks may be too easy**: Room-5x5 might have low death rates even for LLMs, reducing DAF signal
2. **Skill tasks are unsolvable**: 0% success for all LLMs = no meaningful episode data
3. **Deterministic baseline unclear**: No AutoAscend equivalent for MiniHack-specific tasks; must build custom heuristic or use shortest-path solver
4. **Seed determinism partial**: Monster AI introduces stochasticity even with fixed seeds
5. **Episode length mismatch**: MiniHack navigation episodes are very short (~50 steps) vs ScienceWorld (~20-50 steps) = comparable, but less decision content per episode

---

## 2. Alternative Environments Comparison

| Dimension | MiniHack (nav) | MiniHack (skill) | Crafter | ALFWorld | BabyAI |
|---|---|---|---|---|---|
| **Text obs** | Via wrapper | Via wrapper | No (image 64x64) | Native text | Grid + text instructions |
| **Death signal** | Yes (HP=0, done) | Yes (HP=0, done) | Yes (HP=0, done) | **No** (task fail != death) | Partial (lava only) |
| **Det mode** | Seed support | Seed support | `Env(seed=0)` | Seed support | Seed support |
| **LLM adaptable** | Yes (BALROG) | Yes but 0% success | Needs VLM/wrapper | Yes (native text) | Partial (grid obs) |
| **Impl cost** | Medium (3/5) | Medium (3/5) | Medium (3/5) | Low (2/5) | Low (2/5) |
| **Death rate (LLM)** | ~30-60% (est.) | ~95%+ | ~60-80% (est.) | N/A (no death) | Low (<10% most tasks) |
| **Death rate (baseline)** | ~5-20% (heuristic) | ~50%+ | ~20-40% (heuristic) | N/A | ~0% (lava avoidable) |
| **Permadeath framing** | Strong (roguelike) | Strong (roguelike) | Strong (survival) | **Weak** | Weak |
| **Recommended** | **Yes** | No | **Yes (backup)** | No | No |

### ALFWorld Assessment

- **Text-based**: Yes, native. LLM agent literature is extensive (ReAct, Reflexion, etc.)
- **Death mechanism**: **None**. Episodes end on task completion or max steps (150). Task failure = truncation, not death. No HP, no permadeath.
- **Verdict**: **Not suitable**. Cannot be framed as permadeath environment. "Task failure" is categorically different from "agent death."

### Crafter Assessment (from prior report)

- **Already evaluated on server**: 100% random agent death rate, 17 discrete actions, image observations
- **Text interface**: Needs BALROG wrapper or custom semantic-map-to-text converter
- **Heuristic oracle**: Buildable from semantic map (64x64 object IDs) + full inventory state
- **LLM performance**: ~33% milestone completion (BALROG), meaning episodes contain meaningful decisions
- **Verdict**: **Strong backup**. Death mechanics are clear, LLM agents produce informative episodes, heuristic oracle is feasible.
- **Downside vs MiniHack**: No native text observation; image-to-text wrapper adds a layer of complexity and potential information loss.

### BabyAI Assessment

- **Environment**: Part of Minigrid (Farama Foundation). Grid-world with text instructions ("go to the red ball").
- **Death mechanism**: Only via lava tiles. Most tasks have no lava. Stepping on lava = `done=True, reward=0`.
- **Action space**: 6-7 discrete (turn left/right, forward, pickup, drop, toggle)
- **Text observation**: Instructions are text, but grid state is symbolic (not text). Would need wrapper.
- **LLM performance**: BALROG includes BabyAI; LLMs perform relatively well on simple tasks.
- **Verdict**: **Not suitable**. Death mechanism too narrow (only lava, most tasks don't have it). Cannot meaningfully diagnose "death dominance."

---

## 3. Recommended Plan

### Primary: MiniHack Navigation Tasks via BALROG

**Why MiniHack over Crafter**:
1. **Native text via nle-language-wrapper**: No image-to-text conversion needed; structured text observations are production-ready
2. **Roguelike permadeath**: NetHack is the canonical permadeath game in RL literature; reviewers immediately understand it
3. **BALROG framework**: Tested with multiple LLMs, supports vLLM, ready-to-use
4. **Action space via text**: nle-language-wrapper accepts text commands ("north", "eat", "kick"), natural for LLM agents
5. **Established benchmark**: BALROG (ICLR 2025) provides published baselines for comparison

**Target tasks** (in order of priority):
1. `MiniHack-Room-5x5-v0` / `MiniHack-Room-15x15-v0`: Simple navigation, clear death from monsters
2. `MiniHack-Corridor-R3-v0` / `MiniHack-Corridor-R5-v0`: Multi-room navigation with monsters
3. `MiniHack-River-v0`: Requires crossing river (can drown = death)

**Deterministic baseline options**:
- **Shortest-path BFS on observed map**: Use `screen_descriptions` or `glyphs` to build occupancy grid, BFS to goal
- **Heuristic**: Move toward staircase, avoid monsters, eat when hungry
- Both are implementable in 1-2 days for navigation tasks

### Implementation Schedule (5 days to DDL)

| Day | Task |
|---|---|
| Day 1 (May 19) | Install BALROG + MiniHack on server; verify text wrapper works; test 5 manual episodes |
| Day 2 (May 20) | Adapt BALROG for Qwen2.5-7B-Instruct via vLLM; run 10 pilot LLM episodes; measure death rate |
| Day 3 (May 21) | Build deterministic heuristic agent (BFS + survival rules); run 10 pilot episodes; measure death rate |
| Day 4 (May 22) | Full run: 50 LLM + 50 deterministic episodes; compute DAF and routing labels |
| Day 5 (May 23) | Analyze results; write environment description section for paper; buffer for issues |
| Buffer (May 24) | Final integration into paper |

### Resources Needed

- **GPU**: 1x GPU on westb-13313 for vLLM inference (Qwen2.5-7B-Instruct)
- **Model**: Qwen2.5-7B-Instruct (already available)
- **Dependencies**: minihack, nle, nle-language-wrapper, BALROG (all pip-installable)
- **No additional cost**: Local inference via vLLM, no API calls

---

## 4. Key Risks and Mitigation

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| MiniHack navigation too easy for LLM (low death rate, no DAF signal) | HIGH | MEDIUM | Use harder tasks (Room-15x15, Corridor-R5); if still too easy, fall back to Crafter |
| BALROG + vLLM integration issues | MEDIUM | MEDIUM | BALROG docs show vLLM support; nethack-llm is simpler fallback; worst case, write custom wrapper (~1 day) |
| NLE/MiniHack build fails on server (cmake/C++ issues) | MEDIUM | LOW | Pre-built wheels available; Docker fallback |
| Deterministic heuristic too strong or too weak | MEDIUM | MEDIUM | Tune heuristic aggressiveness; use multiple heuristic variants (random-walk, BFS, full-heuristic) |
| 100 episodes insufficient for statistical significance | LOW | LOW | Focus on effect size and qualitative patterns; 50 episodes per modality should show clear trends if death asymmetry exists |
| Crafter fallback needed (adds 2-3 days) | HIGH | LOW | Prior report already covers Crafter setup; heuristic agent design is documented; can reuse BALROG Crafter wrapper |

### Fallback Decision Point

**End of Day 2**: If MiniHack LLM pilot shows <20% or >90% death rate on navigation tasks, switch to Crafter immediately. Crafter's estimated 60-80% LLM death rate and pre-validated server setup make it the safest fallback.

---

## 5. Comparison with Existing ScienceWorld Setup

| Dimension | ScienceWorld (current) | MiniHack (proposed) |
|---|---|---|
| Observation | Natural language | Structured text via wrapper |
| Action | Free-form text | Text commands via wrapper |
| Death mechanism | Task-specific failure | HP depletion (monsters, traps, starvation) |
| Deterministic modality | Built-in oracle | BFS/heuristic agent |
| LLM death rate | ~42% | ~30-60% (estimated) |
| Episode length | ~20-50 steps | ~50-200 steps (navigation) |
| Permadeath framing | Moderate (task failure) | Strong (roguelike, canonical permadeath) |
| Reviewer perception | "Text adventure" | "Roguelike game" (different genre = good for generalization claim) |

**Key advantage for reviewers**: MiniHack/NetHack is from a completely different domain (roguelike games vs science education), uses different observation/action modalities, and has a fundamentally different death mechanism (HP-based combat vs task failure). This strengthens the "framework generalizes" claim significantly.
