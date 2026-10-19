# research scienceworld sft data check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld-sft-data-check_20260519T114835_result.json`
- **Structured JSON:** [`37fcaa03377c1c2e5d4d.json`](../../sessions/37/37fcaa03377c1c2e5d4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充分了。汇报结果：

## ScienceWorld SFT 数据生成状态

### 1. 进程状态
**仍在运行** (PID 755747)，当前处理第 25/30 个任务 `mendelian-genetics-unknown-plant`（dev var 314）。

### 2. 任务完成度
25/30 task types 已启动，剩余 5 个未开始：
- `power-component`
- `power-component-renewable-vs-nonrenewable-energy`
- `test-conductivity`
- `test-conductivity-of-unknown-substances`
- `use-thermometer`

### 3. 总体统计
- 总 trajectories: **3783**（还在增长）
- score=100: **2989** (79.0%)
- **已超过 500 条 SFT 阈值**

### 4. 各 task type 的 score=100 分布

| Task | score=100 / total | Rate |
|---|---|---|
| find-animal | 225/225 | 100% |
| find-living-thing | 225/225 | 100% |
| find-non-living-thing | 225/225 | 100% |
| find-plant | 225/225 | 100% |
| chemistry-mix | 24/24 | 100% |
| chemistry-mix-paint-secondary-color | 27/27 | 100% |
| chemistry-mix-paint-tertiary-color | 27/27 | 100% |
| grow-plant | 93/93 | 100% |
| identify-life-stages-1 | 9/9 | 100% |
| identify-life-stages-2 | 6/6 | 100% |
| lifespan-longest-lived | 93/93 | 100% |
| lifespan-longest-lived-then-shortest-lived | 93/93 | 100% |
| lifespan-shortest-lived | 93/93 | 100% |
| measure-melting-point-known-substance | 325/327 | 99.4% |
| measure-melting-point-unknown-substance | 223/225 | 99.1% |
| change-the-state-of-matter-of | 20/21 | 95.2% |
| melt | 20/21 | 95.2% |
| boil | 19/21 | 90.5% |
| grow-fruit | 77/93 | 82.8% |
| inclined-plane-friction-named-surfaces | 799/1038 | 77.0% |
| freeze | 16/21 | 76.2% |
| inclined-plane-determine-angle | 83/126 | 65.9% |
| inclined-plane-friction-unnamed-surfaces | 42/120 | 35.0% |
| **mendelian-genetics-known-plant** | **0/90** | **0%** |
| **mendelian-genetics-unknown-plant** | **0/315** | **0%** |

### 5. 数据路径和格式
- 输出路径：`/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl` + `scienceworld_sft_val.jsonl`
- **文件尚未写入**——脚本在所有 30 个任务完成后才一次性写出
- 格式：每行一个 JSON，包含 `messages`（multi-turn conversation）和 `metadata`（task, variation, final_score, num_steps, success）

### 6. 关键发现
- **mendelian-genetics 两类任务 gold path 全部失败**（0% score=100），315+90=405 条 trajectory 全为无效数据。这些似乎是 ScienceWorld 环境本身的 gold path 质量问题，不是脚本 bug。
- `inclined-plane-friction-unnamed-surfaces` 成功率也偏低（35%）。
- 剩余 5 个任务预计还需数小时。最终 score=100 数量预计 3000+，充足启动 SFT。

---
