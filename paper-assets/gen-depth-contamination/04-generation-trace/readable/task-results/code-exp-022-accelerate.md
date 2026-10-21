# code exp 022 accelerate

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_022_accelerate_20260516T163539_result.json`
- **Structured JSON:** [`17df7f7c069fcb6fdb77.json`](../../sessions/17/17df7f7c069fcb6fdb77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both sessions running successfully:

- **cuda:0** (GPU 0, 4772 MiB): Running `qwen_base×qwen_instruct`, feature extraction depth 0
- **cuda:1** (GPU 1, 4280 MiB): Running `pythia_greedy×pythia`, feature extraction depth 0  
- **cuda:3** (GPU 3, 5672 MiB): Continuing `pythia_greedy×qwen_base` (will finish soon, then skip combos already done by cuda:0/1)

分配总结：
| GPU | Session | 组合数 | 内容 |
|-----|---------|--------|------|
| cuda:0 | exp022_cuda0 | 5 | qwen_base×qwen_instruct, qwen_cont256×{4 scorers} |
| cuda:1 | exp022_cuda1 | 2 | pythia_greedy×{pythia, olmo} |
| cuda:3 | exp022 (原) | ~1剩余 | pythia_greedy×qwen_base (即将完成)，之后跳过已完成的 |

cuda:3 的原始脚本会在到达后续组合时发现 `summary.txt` 已存在自动跳过，不会冲突。

---
