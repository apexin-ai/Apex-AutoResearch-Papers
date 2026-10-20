# 72B Backbone Scaling — Episode Collection Progress

**Check time:** 2026-05-17 19:05 CST (11:05 UTC)

## Process Status

| Item | Status |
|------|--------|
| PID 617494 | **alive** (uptime: 1h13m) |
| tmux `backbone-scaling-70b` | **alive** |
| Command | `python src/episode_level_collection.py --model_path Qwen2.5-72B-Instruct-AWQ --episodes 20 --max_steps 30 --tp 2` |

## Episode Completion by Task Type

| Task Type | Completed | Target | Status |
|-----------|-----------|--------|--------|
| chemistry-mix | 17 | 20 | **in progress** |
| find-animal | 0 | 20 | pending |
| find-non-living-thing | 0 | 20 | pending |
| freeze | 0 | 20 | pending |
| grow-fruit | 0 | 20 | pending |
| identify-life-stages-1 | 0 | 20 | pending |
| identify-life-stages-2 | 0 | 20 | pending |
| inclined-plane-determine-angle | 0 | 20 | pending |
| lifespan-longest-lived | 0 | 20 | pending |
| lifespan-longest-lived-then-shortest-lived | 0 | 20 | pending |
| measure-melting-point-unknown-substance | 0 | 20 | pending |
| **Total** | **17** | **220** | **7.7%** |

## Timing Estimate

- First episode output: 17:59:30 CST
- Last episode written: 19:04:09 CST
- 17 episodes in 64.65 min → **3.80 min/episode**
- Remaining: 203 episodes × 3.80 min = **12h 51min**
- **Estimated completion: May 18, ~08:00 CST (May 18, 00:00 UTC)**
