# 状态检查报告 — 2026-05-22 14:48 UTC

## 1. XNLI MLP vs Linear 探针对照实验

**状态：结果文件已生成，进程仍在运行**

两个 MLP 进程（CPU-only）在 13:52 启动，结果文件已写入。

### Qwen3 MLP 探针 (36 layers)

| 方向 | Best Layer | Balanced Acc | F1 |
|------|-----------|-------------|-----|
| EN→EN | 23 | **0.9658** | 0.9665 |
| ZH→ZH | 26 | **0.9099** | 0.9118 |
| EN→ZH | 30 | **0.8843** | 0.8930 |
| ZH→EN | 22 | **0.9746** | 0.9765 |

### Llama31 MLP 探针 (32 layers)

| 方向 | Best Layer | Balanced Acc | F1 |
|------|-----------|-------------|-----|
| EN→EN | 15 | **0.9303** | 0.9333 |
| ZH→ZH | 15 | **0.8847** | 0.8889 |
| EN→ZH | 19 | **0.8848** | 0.8878 |
| ZH→EN | 13 | **0.9469** | 0.9463 |

MLP 进程（PID 112489, 132700）仍在运行。日志显示 Qwen 在 ZH→ZH layer 18，Llama 在 ZH→EN layer 2。结果 JSON 已包含全部 4 方向——可能写了中间结果、进程仍在继续。

---

## 2. Gemma translate ZH 进度

**状态：进行中 — 520/1274 (40.8%)**

- tmux session: `gemma_translate_zh`（创建于 13:06）
- 当前进度：520/1274 已翻译，最近 checkpoint 在 500
- .partial 文件：481KB
- 最终 `zh_conflict_train.jsonl` 尚未生成
- GPU 1 (PID 85171)，模型 Qwen3-8B，batch_size=4
- 从 checkpoint 150 恢复
- 翻译速率：~370 条/小时，预计还需 ~2 小时

---

## 3. Bootstrap n=2000 (plan_111)

**状态：目标文件不存在**

以下文件均不存在：
- `data/qwen3/probe_results_bootstrap_n2000.json`
- `data/llama31/probe_results_bootstrap_n2000.json`
- `data/qwen3/bootstrap_asymmetry_n2000.json`
- `data/llama31/bootstrap_asymmetry_n2000.json`

无 train_probe 进程在运行。

XNLI 目录下存在 bootstrap_asymmetry.json（n=2000），这是 XNLI 线性探针的 bootstrap，非 conflict 任务：
- Qwen3 (XNLI): ZH→EN=0.9717, EN→ZH=0.9045, diff=0.0672, 95%CI=[0.024, 0.117], 显著
- Llama31 (XNLI): ZH→EN=0.9492, EN→ZH=0.8895, diff=0.0597, 95%CI=[0.009, 0.113], 显著

---

## 4. COMET 验证进度

**状态：进行中 — train split 反向翻译阶段**

两个 validate_translation 进程自 07:15 运行（~7.5 小时）。

### 已完成：test split 验证

| 模型 | Total | Passed | Filtered | Pass Rate | Mean COMET | Threshold |
|------|-------|--------|----------|-----------|------------|-----------|
| Qwen3 | 168 | 31 | 137 | **18.5%** | 0.7016 | 0.80 |
| Llama31 | 272 | 76 | 196 | **27.9%** | 0.7160 | 0.80 |

### 进行中：train split 反向翻译

| 模型 | GPU | PID | 进度 | 总数 |
|------|-----|-----|------|------|
| Qwen3 | GPU 0 | 59412 | 660/798 back-translated | 798 (82.7%) |
| Llama31 | GPU 2 | 59571 | 660/1096 back-translated | 1096 (60.2%) |

反向翻译完成后还需 COMET 打分和过滤。

**关注**：test split 通过率很低（Qwen 18.5%，Llama 27.9%），threshold=0.8 可能过严。mean_comet ~0.70-0.72。

---

## 5. GPU 利用率

| GPU | 型号 | Util | VRAM | 进程 |
|-----|------|------|------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 14% | 16.5/98GB | COMET Qwen (PID 59412) |
| 1 | RTX PRO 6000 Blackwell (98GB) | 9% | 16.5/98GB | Gemma translate (PID 85171) |
| 2 | RTX PRO 6000 Blackwell (98GB) | 18% | 16.5/98GB | COMET Llama (PID 59571) |
| 3 | RTX PRO 6000 Blackwell (98GB) | **0%** | **0/98GB** | **空闲** |

MLP 探针在 CPU 上运行，不占 GPU。

---

## 综合概览

| 任务 | 状态 | 关键指标 |
|------|------|---------|
| XNLI MLP 探针 | 结果已生成 | Qwen best=0.9746 (ZH→EN), Llama best=0.9469 (ZH→EN) |
| Gemma 翻译 | 进行中 40.8% | 520/1274, ~2h remaining |
| Bootstrap n=2000 | 未启动 | conflict 任务的 bootstrap 文件不存在 |
| COMET 验证 | 反向翻译中 | Qwen 82.7%, Llama 60.2%; test pass rate 低 |
| GPU | 3/4 使用中 | GPU 3 空闲, 总体利用率低 (~10-18%) |
