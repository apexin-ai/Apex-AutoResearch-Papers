# Gemma-2-9B-IT ScienceWorld 第三次修复报告

**日期**: 2026-05-20
**服务器**: westb-13313, GPU 1 (RTX 5090 32GB)
**模型**: /root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it

## Step 1: GPU 1 状态确认

- GPU 1 初始状态: 0MiB/32607MiB, 无进程
- 发现旧进程 PID 701929 (identify-life-stages-1, 零产出) → 已清理
- 发现 tmux session `gemma-all` 运行旧脚本 → 已清理

## Step 2: 三个问题修复

### 问题 1: Task List ✅

从 `results/plan_c/` (Llama 成功实验) 确认 11 个精确 task name:
```
identify-life-stages-1, freeze, grow-fruit, identify-life-stages-2,
measure-melting-point-unknown-substance, lifespan-longest-lived,
lifespan-longest-lived-then-shortest-lived, chemistry-mix,
inclined-plane-determine-angle, find-animal, find-non-living-thing
```
`scripts/run_gemma_all_gpu1.sh` 中的 TASKS 数组已包含这 11 个 task。

### 问题 2: System Role 修复 ✅ (已修复)

`sanitize_messages_for_template()` 函数已存在于 `src/llm_agent.py` (约 line 92)，在 `_generate_vllm()` 和 `_generate_hf()` 中都有调用。无需额外修改。

### 问题 3: vLLM 内存配置 ✅

**修改文件**: `src/llm_agent.py`, `_load_vllm()` 方法 (line ~220)

**最终配置** (经三轮 dry-run 迭代):
```python
self._llm = LLM(
    model=self.model_path,
    tensor_parallel_size=self.tensor_parallel_size,
    gpu_memory_utilization=0.85,
    enforce_eager=True,
    enable_prefix_caching=False,
    max_model_len=4096,
    trust_remote_code=True,
)
```

**关键发现 — vLLM prefix caching 导致 EngineCore 崩溃**:

| 配置 | 结果 |
|------|------|
| gpu_memory=0.85, 默认设置 | EngineCore 在 ~37 prompts 后崩溃 |
| gpu_memory=0.70, enforce_eager=True | EngineCore 在 ~56 prompts 后崩溃 |
| gpu_memory=0.85, enforce_eager=True, prefix_caching=False | ✅ 全 60 prompts 完成 |

根因: vLLM v0.18.1 的 prefix caching 与 Gemma-2 的 Sliding Window Attention 交互导致内存泄漏，EngineCore 进程最终 OOM 被杀。禁用 prefix caching 后 KV cache 正常回收。

## Step 3: Dry-Run 结果

```
Task: find-non-living-thing, 1 episode
Internal episode:      score=0.0, 50s
Deterministic episode: score=58.0, 179s
Total prompts: 60 (30 internal + 30 deterministic)
```

输出文件:
- `results/gemma_dryrun_v3/find-non-living-thing/episodes.jsonl` — 1 行
- `results/gemma_dryrun_v3/find-non-living-thing/labeled_steps.jsonl` — 30 行
- `results/gemma_dryrun_v3/find-non-living-thing/episode_summary.jsonl` — 1 行

Episode summary: `{"episode": 0, "variation": 0, "internal_final": 0.0, "det_final": 58.0, "label": "det-preferred", "signal_source": "score_comparison", "reason": "both_alive_det_wins", "score_gap": 58.0}`

## Step 4: 全量启动

- tmux session: `gemma-11tasks`
- 脚本: `scripts/run_gemma_all_gpu1.sh`
- 输出目录: `results/gemma_scienceworld_counterfactual/`
- 日志: `results/gemma_scienceworld_counterfactual/gemma_all_gpu1.log`
- 启动时间: 2026-05-20 16:44:30
- 预计总时长: ~11 tasks × 20 episodes × ~4min/episode ≈ 15 小时

启动验证:
- GPU 1: 27979MiB/32607MiB, 93% GPU-Util
- KV cache: 8.19 GiB, 25,552 tokens
- 首个 task (identify-life-stages-1) internal episode 完成 (score=0.0)
- GPU 0 未受影响 (0MiB)

## Step 5: Registry

`gemma-scienceworld-counterfactual` 实验 spec 已更新，包含新的 11 task list、vLLM 配置和修复记录。

## 保留数据

- `results/gemma_scienceworld_counterfactual/boil/` — 保留 (旧实验数据)
- `results/gemma_scienceworld_counterfactual/melt/` — 保留 (旧实验数据)
- 旧的损坏目录 (freeze, grow-fruit, identify-life-stages-1/2) — 已清理
