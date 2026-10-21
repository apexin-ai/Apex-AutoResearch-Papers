# paper writing discussion plan013

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_discussion-plan013_20260514T143641_result.json`
- **Structured JSON:** [`0dac45e5a1a4977043ac.json`](../../sessions/0d/0dac45e5a1a4977043ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已添加。数字一致性检查：

| 数字 | Limitations 段落 | 论文其他处 | Registry | 一致? |
|------|-----------------|-----------|----------|-------|
| 245 episodes | ✓ | experiments.tex L6 | - | ✓ |
| 150 no_preference (61.2%) | 150/245=61.2% | experiments.tex L22 | 61.2% | ✓ |
| 86 det + 9 int = 95 | 75+20=95 | experiments.tex L22 | 95 genuine | ✓ |
| 70+5 death asymmetry | 75 | - | 70+5 | ✓ |
| 16+4 score comparison | 20 | - | 16+4 | ✓ |
| 97.4% step tie rate | ✓ | method.tex L6 | 97.39%→97.4% | ✓ |
| 57.3% strict-only | ✓ | - | 0.5729 | ✓ |
| 57.6±0.5% full-label | ✓ | - | 0.5761±0.005 | ✓ |

段落约 135 words，覆盖了全部要求：
1. **Oracle circularity 回应** — 0% tie-break labels, 100% genuine
2. **排除数据** — 61.2% tied episodes excluded, 分 both-alive/both-dead
3. **训练 label 审计** — 95 labels 全部 genuine，按 death asymmetry / score comparison 分解
4. **Strict-only retrain** — balanced_acc within 1σ，score-comparison labels 贡献可忽略
5. **Step-level tie rate** — 97.4% 引用 §2.1，motivate episode-level approach

---
