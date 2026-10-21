# check eval scripts precheck

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_scripts_precheck_20260523T144055_result.json`
- **Structured JSON:** [`046aba6d20e62d59e847.json`](../../sessions/04/046aba6d20e62d59e847.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇报如下：

---

## GPU Chain 预检查结果（7 步）

### Step 1: SS s123 eval (`d048_eval_ss_s123.sh`) — ✅ 就绪

- **Checkpoint**: `runs/d048_ss_s123/` — epoch_0 和 epoch_1 都有完整的 `lora/` + `gate_params.pt`
- 脚本会从 epoch_2 → 1 → 0 搜索最优，**当前会选中 epoch_1**
- ⚠️ **注意**：SS s123 训练是 3 epochs，目前只到 epoch_1。如果训练还在跑 epoch_2，等训练完再启动链；如果训练已完成且只产出了 2 个 epoch，则 epoch_1 就是最终 checkpoint，无问题
- Eval 模式：TF（4 组）+ AR N=50（2 组）+ Bootstrap CI ✅
- 数据文件 `data/eval_200/eval_200.json` ✅
- 输出目录 `results/d048_final_ar/` ✅
- Python 脚本 `src/eval_phase2_gar.py`、`src/eval_attention_steering.py` ✅

### Step 2: SS s456 resume (`d048_ss_s456_resume.sh`) — ✅ 就绪

- `--resume runs/d048_ss_s456/epoch_0` — 存在，包含 `lora/` + `gate_params.pt` (3.3MB)
- 模型路径 `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct` ✅
- 训练数据 `data/ultrachat_8k` ✅
- 超参正确：lr=2e-4, batch=1, grad-accum=8, epochs=3, seed=456, SS max-ratio=0.3
- 训练脚本 `src/train_phase2_v8b.py` ✅

### Step 3: SS s456 eval (`d048_eval_ss_s456.sh`) — ✅ 就绪（依赖 Step 2）

- Checkpoint 将由 Step 2 生成于 `runs/d048_ss_s456/`
- 脚本结构与 s123 eval 一致，参数正确
- 输出到 `results/d048_final_ar/`，子目录 `tf_ss_s456_ours` / `tf_ss_s456_dongre`

### Step 4: Qwen-1.5B Phase 1 diag (`qwen15b_phase1_diag.sh`) — ✅ 就绪

- 模型路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct/` ✅
- Python 脚本 `src/run_phase1_gar_llama.py` ✅
- 输出到 `results/qwen15b_phase1/`

### Step 5: Qwen-1.5B TG train (`qwen15b_tg_train.sh`) — ✅ 就绪

- 模型路径 ✅
- 训练数据 `data/ultrachat_8k` ✅
- 超参：lr=2e-4, **batch=4**, grad-accum=2, epochs=3, seed=42
- 训练脚本 `src/train_phase2.py` ✅（注意：用的是 v7 train_phase2.py 而非 v8b）
- 输出到 `runs/qwen15b_tg_v7_s42`

### Step 6: Qwen-1.5B eval (`qwen15b_eval.sh`) — ✅ 就绪（依赖 Step 5）

- Checkpoint 将由 Step 5 生成于 `runs/qwen15b_tg_v7_s42`
- 2 个条件：Base + TG，N=50, beta=0 3 5
- 含 Bootstrap CI + Wilcoxon 统计检验

### Step 7: MMLU eval (`mmlu_eval_all.sh`) — ✅ 就绪

- `lm-evaluation-harness` 已安装 ✅（`/root/miniconda3/bin/lm_eval`）
- `mmlu_eval_single.sh` ✅
- 6 个 checkpoint 全部验证通过（`adapter_config.json` 存在）：
  - `base_qwen`: none ✅
  - `lo_s42`: `runs/phase2_lora_only_s42/lora` ✅
  - `tg_v7_s42`: `runs/phase2_tg_s42_v7/lora` ✅
  - `ug_s42`: `runs/phase2_ug_s42/lora` ✅
  - `pcgrad_v9_s42`: `checkpoints/tg_v9_pcgrad_s42/lora` ✅
  - `ss_v8b_s42`: `runs/d048_ss_s42/lora` ✅
- Base model `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct` ✅

---

### 唯一需要确认的点

**SS s123 是否还在训练 epoch_2？** 当前只有 epoch_0 和 epoch_1。如果 3 epoch 训练仍在进行中，需等 epoch_2 完成后再启动链。如果训练已结束（只产出 2 个 checkpoint），则可以直接启动。

---
