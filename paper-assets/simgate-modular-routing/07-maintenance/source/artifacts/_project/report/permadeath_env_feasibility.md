# Permadeath Environment Feasibility Report: Crafter vs NetHack

**Date**: 2026-05-18  
**Purpose**: Evaluate Crafter and NetHack as second permadeath environment for replicating the episode-level counterfactual diagnostic framework (C3 gap)

---

## 1. Environment Comparison Table

| Dimension | ScienceWorld (current) | Crafter | NetHack (NLE) |
|---|---|---|---|
| **Installation** | pip install | `pip install crafter` (3 deps) | `pip install nle` (pre-built wheel) |
| **Observation** | Text (natural language) | Image (64x64 RGB) + semantic map (64x64) + inventory dict | ASCII (24x80 tty) + message + blstats (27 stats) + glyphs (21x79) |
| **Text interface** | Native | Not native; BALROG wrapper exists (Wu et al.) | Near-native (ASCII); nle-language-wrapper available |
| **Action space** | Text commands | 17 discrete (move, do, sleep, place, craft) | 23 discrete (movement, items, combat) |
| **Death mechanism** | Task-specific failure | Health depletion (9 HP, monsters/starvation/dehydration) | HP depletion (monsters, traps, food, poison) |
| **Episode length** | ~20-50 steps | ~150-1000 steps | 10^3-10^5 steps |
| **LLM agent performance** | Moderate | ~33% milestones (BALROG, GPT-4o) | ~1.5% progression (BALROG); GPT-5.2 best at 12.56% |
| **Deterministic/oracle** | Built-in simulator oracle | None exists; must build | AutoAscend (NeurIPS 2021 winner, rule-based, open source) |
| **Human expert** | High | 50.5% score | Ascension possible but rare |
| **Death rate (random)** | ~42% | 100% (avg 153 steps) | ~20% in 1000 steps (mostly timeouts) |

## 2. Technical Assessment

### 2.1 Crafter

**Installation**: Trivial. `pip install crafter` adds 3 packages (imageio, opensimplex, crafter). Tested on westb-14838, Python 3.12. No C compilation, no GPU needed for env itself.

**Observation space** (verified on server):
- RGB image: (64, 64, 3) uint8
- Semantic map: (64, 64) uint8 with object type IDs (1-16)
- Inventory dict: health, food, drink, energy, sapling, wood, stone, coal, iron, diamond, all tools
- Achievements dict: 22 binary achievements
- Player position: (2,) int64

**Action space**: 17 discrete actions:
- Movement: noop, move_left, move_right, move_up, move_down
- Interaction: do (context-sensitive), sleep
- Placement: place_stone, place_table, place_furnace, place_plant
- Crafting: make_wood/stone/iron_pickaxe, make_wood/stone/iron_sword

**Death mechanism**: Health depletes from monster attacks (zombies, skeletons), starvation (food=0), dehydration (drink=0). Health starts at 9, death at 0. Random agent dies 100% of the time, average 153 steps. Health is continuously trackable via `info['inventory']['health']`.

**Text interface options**:
- BALROG framework (ICLR 2025): provides language wrapper converting semantic map to spatial descriptions ("tree 3 steps to your north-west, health: 9/9")
- Mcrafter_LLM_Agent: multi-agent system with LLM integration (limited docs, 4 GitHub stars)
- Custom wrapper: straightforward given semantic map + inventory dict (1-2 days)

### 2.2 NetHack (NLE)

**Installation**: Trivial. `pip install nle` installs pre-built manylinux wheel (3.3 MB). Tested on westb-14838, Python 3.12. Depends on gymnasium, pybind11.

**Observation space** (verified on server):
- tty_chars: (24, 80) ASCII screen
- message: (256,) byte string
- blstats: (27,) int with HP, max_HP, str, dex, con, int, wis, cha, score, depth, gold, energy, AC, XP, time, hunger, etc.
- glyphs: (21, 79) glyph IDs
- screen_descriptions: (21, 79, 80) per-tile text descriptions
- Inventory: inv_strs (55, 80), inv_letters, inv_glyphs

**Action space**: 23 discrete. Varies by task; NetHackScore uses full action set.

**Death mechanism**: HP depletion from monsters, traps, starvation, poison, rotten food. Very deep death mechanics. Random agent: 20% death in 1000 steps (most timeout). LLM agents die much faster due to strategic errors (eating rotten corpses, exiting dungeon).

**Text interface options**:
- Native ASCII: already text-like, but spatial reasoning is hard for LLMs
- nle-language-wrapper: converts glyphs/stats/inventory to structured text ("tame kitten adjacent northeast, vertical closed door far westnorthwest")
- NetPlay (arxiv 2403.00690): full LLM agent framework with skill-based interface, open source
- BALROG: unified wrapper, tested with multiple LLMs

**Available NLE tasks**: NetHackScore, NetHackChallenge, NetHackEat, NetHackGold, NetHackOracle, NetHackScout, NetHackStaircase, NetHackStaircasePet

## 3. Deterministic Modality Assessment

### 3.1 ScienceWorld baseline (reference)
ScienceWorld has a built-in oracle simulator that executes ground-truth actions deterministically. This provides a clean "deterministic" modality that contrasts with the LLM agent's stochastic behavior.

### 3.2 Crafter: No existing oracle

**Option A: Rule-based heuristic using semantic map**
- Feasibility: HIGH. The semantic map (64x64 with object IDs) + full inventory state gives complete information for building a survival heuristic.
- Strategy: (1) move toward water when drink < threshold, (2) move toward food sources when food < threshold, (3) craft sword when materials available, (4) avoid/fight monsters based on health and weapon, (5) sleep when energy low.
- Expected death rate: 20-40% (significantly lower than random's 100%, but not zero due to environment stochasticity).
- Implementation: 2-3 days. The semantic map makes pathfinding straightforward.
- Analogy to ScienceWorld: This functions like a "near-optimal" policy rather than a true oracle, but the death rate asymmetry should be clear.

**Option B: Strong LLM as "oracle"** (e.g., o1/Claude Opus with CoT)
- Not truly deterministic; defeats the purpose of the framework.

**Option C: Trained RL agent (DreamerV2)**
- DreamerV2 achieves 10% score (best published RL). Could serve as "strong agent" vs LLM as "weak agent".
- Problem: training takes 1M env steps, and 10% score may not provide enough death rate contrast.

**Recommendation**: Option A. Building a heuristic using the semantic map is the cleanest approach and most analogous to ScienceWorld's oracle.

### 3.3 NetHack: AutoAscend (ideal oracle)

**AutoAscend** (NeurIPS 2021 NetHack Challenge winner):
- Pure rule-based system with handcrafted strategies for combat, food management, exploration, item identification
- Open source: github.com/maciej-sypetkowski/autoascend (254 commits, substantial codebase)
- Performance: median score ~5,000 (3x better than best neural agent), reaches 20+ dungeon levels
- Death rate: substantially lower than LLM agents (which die almost immediately)

**Integration complexity**:
- Requires modified NLE for game seeding (Docker setup provided)
- Not a simple `pip install`; needs Docker or manual NLE patching
- Running alongside LLM agent on same episodes requires careful seeding

**Death asymmetry**: Extremely strong. LLM agents (GPT-5.2 best, avg depth 3.5) vs AutoAscend (20+ levels). This provides the clearest DAF signal.

**Problem**: LLM agent performance is so low (~1.5% BALROG) that most episodes are trivially short, limiting the informativeness of routing labels.

## 4. Literature: LLM Agents on These Environments

### 4.1 Crafter + LLM

| Work | Year | Approach | Performance |
|---|---|---|---|
| BALROG (ICLR 2025) | 2024 | Zero-shot LLM/VLM agents | GPT-4o: 33.1%, Claude 3.5: 32.7% (language), 37.3% (vision) |
| EnvGen (COLM 2024) | 2024 | LLM generates training environments for RL | Faster achievement unlocking |
| Mcrafter_LLM_Agent | 2024 | Multi-agent LLM system | No published metrics |
| DAMCS (MA-Crafter) | 2025 | Multi-agent cooperative LLM | Focused on cooperation, not solo |

**Key finding**: LLM agents achieve ~33% milestone completion on Crafter. This is meaningful progress (random ~0%, human 50.5%), suggesting LLM agents survive long enough to produce informative episodes.

### 4.2 NetHack + LLM

| Work | Year | Approach | Performance |
|---|---|---|---|
| NetPlay (arxiv 2403.00690) | 2024 | Skill-based LLM agent | Avg 1,292 turns (unguided), 2,627 turns (guided) |
| BALROG (ICLR 2025) | 2024 | Zero-shot LLM agents | o1-preview: 1.57%, Claude 3.5: 1.5% |
| nethack-llm | 2023 | LLM actors for NetHack | Minimal docs, no benchmarks |
| "Can LLMs Play Nethack Yet?" | 2026 | GPT-5.2, Gemini 3, Claude Opus 4.5 | GPT-5.2 best: 12.56% BALROG, avg depth 3.5 |

**Key finding**: LLM agents remain terrible at NetHack even in 2026. GPT-5.2 reaches dungeon level 10 max but averages 3.5. The environment is too complex for current LLMs to generate meaningful task completion data.

## 5. Death Rate Assessment

### 5.1 Crafter
- **Random agent**: 100% death, avg 153 steps (tested, N=10)
- **LLM agent (estimated)**: ~60-80% death rate. BALROG agents achieve 33% milestones, implying some survival. Surviving episodes likely reach 500-1000 steps.
- **Heuristic agent (projected)**: ~20-40% death rate. With semantic map access, basic survival (water/food/monsters) is solvable.
- **Death asymmetry**: LLM ~70% death vs Heuristic ~30% death = strong asymmetry (similar to ScienceWorld's pattern)

### 5.2 NetHack
- **Random agent**: 20% death in 1000 steps; most timeout (tested, N=20). With longer episodes, death rate increases.
- **LLM agent**: >90% death rate. Die quickly from strategic errors (rotten food, exiting dungeon, poor combat).
- **AutoAscend**: <10% death rate in early game. Much longer survival.
- **Death asymmetry**: Very strong (LLM >90% vs AutoAscend <10%), but LLM episodes are trivially short.

### 5.3 Ideal range for framework
- ScienceWorld: ~42% internal death rate
- Target: 30-60% LLM death rate, with meaningful episode content before death
- **Crafter fits best**: LLM death rate likely in 60-80% range, episodes are substantive (~500 steps)
- **NetHack too extreme**: LLM death rate >90% and episodes are too short/uninformative

## 6. Recommendation

### 6.1 Primary recommendation: Crafter

**Rationale**:
1. **LLM agents work**: 33% milestone completion means episodes contain meaningful decision data
2. **Death rate is in range**: Estimated 60-80% for LLM, much lower for heuristic = clear DAF signal
3. **Full state access**: Semantic map + inventory enables building a clean heuristic "oracle"
4. **Short episodes**: ~500-1000 steps = affordable pilot (vs NetHack's 10K+ steps)
5. **Simple installation**: pip install, pure Python, no GPU for env
6. **Existing infrastructure**: BALROG text wrapper, multiple LLM agent codebases

**Why not NetHack**:
- LLM agents are too bad (~1.5% BALROG); episodes are uninformative
- Extremely long episodes (10^4-10^5 steps) = very expensive per-episode LLM cost
- AutoAscend integration requires Docker + modified NLE
- Death asymmetry is "too perfect" (>90% vs <10%) which makes routing trivially death-dominated

### 6.2 Pilot experiment: minimum viable plan

**Configuration**:
- Episodes: 50 pilot (25 per modality)
- LLM modality: GPT-4o-mini via BALROG text wrapper (cheapest option with ~30% milestone rate)
- Deterministic modality: Custom heuristic agent using semantic map
- Metrics: death rate per modality, DAF, routing label distribution

**Steps**:
1. Adapt BALROG Crafter text wrapper (or write custom from semantic map): 1-2 days
2. Build heuristic agent using semantic map + inventory: 2-3 days
3. Run 25 LLM episodes + 25 heuristic episodes: 1 day (mostly LLM API cost)
4. Compute counterfactual routing labels and DAF: 0.5 day
5. Analyze and document: 0.5 day

**Total**: 5-7 working days

**Estimated cost**: ~$5-15 for GPT-4o-mini API (500 steps x 25 episodes x ~$0.001/step)

### 6.3 Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| Heuristic agent death rate too similar to LLM | HIGH | Build progressively stronger heuristic; tune difficulty via starting inventory |
| BALROG text wrapper not directly reusable | MEDIUM | Crafter semantic map makes custom wrapper straightforward (1 day) |
| LLM death rate outside 30-60% range | MEDIUM | Adjust episode length cap; use stronger/weaker LLM |
| Crafter achievements don't map to ScienceWorld tasks | LOW | Focus on death/non-death binary, not task completion |
| Reviewer questions "is Crafter really permadeath?" | LOW | Crafter is explicitly a survival game; death is permanent and terminal |

### 6.4 Backup plan: MiniHack

If Crafter pilot fails (e.g., can't achieve meaningful death rate contrast):
- MiniHack offers shorter, focused tasks within the NetHack framework
- Episodes are ~10^2 steps (manageable)
- NLE infrastructure reusable
- BUT: no existing strong deterministic agent for MiniHack tasks specifically
- Estimated additional time: +3-5 days

---

## Appendix: Server Test Results

**Server**: westb-14838, Python 3.12.3

### Crafter installation
```
pip install crafter  # 3 new packages: crafter-1.8.3, imageio-2.37.3, opensimplex-0.4.5.1
```

### Crafter test
```
Obs shape: (64, 64, 3) uint8
Action space: DiscreteSpace(n=17)
Actions: ['noop', 'move_left', 'move_right', 'move_up', 'move_down', 'do', 'sleep', 
          'place_stone', 'place_table', 'place_furnace', 'place_plant', 
          'make_wood_pickaxe', 'make_stone_pickaxe', 'make_iron_pickaxe', 
          'make_wood_sword', 'make_stone_sword', 'make_iron_sword']
Info keys: inventory (dict), achievements (dict), semantic (64x64), player_pos (2,), reward, discount
Inventory: health=9, food=9, drink=9, energy=9, + resources + tools
Achievements: 22 binary (collect_*, defeat_*, eat_*, make_*, place_*, wake_up)

Random agent (10 eps, max 2000 steps):
  Deaths: 10/10 = 100%
  Avg steps: 153 +/- 61
  Min/Max: 34/258
```

### NLE installation
```
pip install nle  # 4 new packages: nle-1.3.0, gymnasium-1.2.0, pybind11-3.0.4, farama-notifications-0.0.6
```

### NLE test
```
Obs keys: glyphs, chars, colors, specials, blstats, message, inv_glyphs, inv_strs, 
          inv_letters, inv_oclasses, screen_descriptions, tty_chars, tty_colors, tty_cursor
Action space: Discrete(23)
tty_chars: (24, 80), message: (256,), blstats: (27,), glyphs: (21, 79)
screen_descriptions: (21, 79, 80)  # per-tile text descriptions built into NLE

Random agent (20 eps, max 1000 steps):
  Deaths: 4/20 = 20%
  Timeouts: 16/20
  Avg steps: 945 +/- 150
  Avg score: 20.2

Available tasks: NetHackScore, NetHackChallenge, NetHackEat, NetHackGold, 
                 NetHackOracle, NetHackScout, NetHackStaircase, NetHackStaircasePet
```
