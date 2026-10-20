# Gemma GPU1 清理 + 排查 + Dry-run + 重启报告

**日期**: 2026-05-20 16:27 CST
**服务器**: westb-13313

---

## Step 1: 清理 cuda:1

- **清理前**: GPU 1 有 VLLM::EngineCore (PID 547990), 占用 28466MiB
- **操作**: `kill -9 547990`
- **清理后**: GPU 1 显存 0MiB, 无进程
- **GPU 0 未受影响**: Llama ALFWorld (PID 547473, 28008MiB) 正常运行

## Step 2: 排查 system role 修复

- `sanitize_messages_for_template()` 已在 `src/llm_agent.py:87` 实现
- 在两处 `apply_chat_template` 调用前正确使用:
  - `_generate_vllm()` (line 262)
  - `_generate_hf()` (line 277)
- `episode_level_collection.py` 通过 `LLMAgent` 间接调用, 不直接使用 `apply_chat_template`
- **结论: 无需代码修改, sanitize 已就位**

## Step 3: Dry-run

- **命令**: `CUDA_VISIBLE_DEVICES=1 python src/episode_level_collection.py --task_types "find-non-living-thing" --episodes 1 --gpu_id 1 ...`
- **结果**: 成功
  - Episode 0: internal_final=50.0, det_final=58.0, label=det-preferred
  - 30 labeled steps
  - 输出文件: episodes.jsonl (1行), episode_summary.jsonl (1行), labeled_steps.jsonl (30行), collection_meta.json
  - vLLM 引擎正常加载和关闭
  - 无 system role 错误

## Step 4: 全量启动

- **脚本**: `scripts/run_gemma_all_gpu1.sh`
- **tmux session**: `gemma-all`
- **任务列表 (11 tasks × 20 episodes)**:
  1. identify-life-stages-1
  2. freeze
  3. grow-fruit
  4. identify-life-stages-2
  5. measure-melting-point-unknown-substance
  6. lifespan-longest-lived
  7. lifespan-longest-lived-then-shortest-lived
  8. chemistry-mix
  9. inclined-plane-determine-angle
  10. find-animal
  11. find-non-living-thing
- **参数**: `--episodes 20 --gpu_id 1 --seed 42 --max_steps 30 --model_path /root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it`
- **输出**: `results/gemma_scienceworld_counterfactual/`
- **日志**: `results/gemma_scienceworld_counterfactual/gemma_all_gpu1.log`

### 启动验证
- GPU 1: VLLM::EngineCore (PID 702359), 模型加载中
- 第一个 task `identify-life-stages-1` Episode 0 已开始
- GPU 0 (Llama ALFWorld) 未受影响

### 预估
- Dry-run 1 episode ≈ 3 min (含模型加载), 推理本身 ≈ 2.5 min
- 每 task 20 episodes + 模型加载 ≈ ~50-60 min
- 11 tasks 串行 ≈ ~9-11 hours

### 已有数据(保留)
- `boil/` 和 `melt/` 有之前的有效数据, 未清理

### 监控命令
```bash
# 查看 tmux
ssh connect.westb.seetacloud.com tmux attach -t gemma-all

# 查看日志
tail -f results/gemma_scienceworld_counterfactual/gemma_all_gpu1.log

# 查看 GPU
nvidia-smi -i 1

# 查看进度
grep "Done in\|FAILED" results/gemma_scienceworld_counterfactual/gemma_all_gpu1.log
```
