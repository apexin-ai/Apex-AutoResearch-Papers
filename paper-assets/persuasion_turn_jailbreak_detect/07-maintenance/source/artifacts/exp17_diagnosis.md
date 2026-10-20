# exp17_dataset_scale 诊断报告

**诊断时间**: 2026-05-19 ~07:50 CST
**服务器**: westd-33183

## 根本原因

**Checkpoint 格式不匹配**：`train_deberta_mlm.py` 保存为 HuggingFace safetensors 格式 (`model.safetensors`)，但 `train_classifier.py --mode treatment` 的 `load_encoder()` 调用 `torch.load()` 期望 `model.pt`。导致所有 MLM Stage2 均 crash：

```
FileNotFoundError: [Errno 2] No such file or directory: 'checkpoints/exp17/mlm_seed42/deberta_mlm/best/model.pt'
```

实际文件为 `model.safetensors`（735MB），路径正确但格式不对。

## 各任务状态

### Vanilla (GPU2) — ✅ 全部完成
| Seed | Val Loss | Val Acc | 状态 |
|------|----------|---------|------|
| 42   | 0.0679   | 0.9733  | ✅ |
| 123  | 0.0594   | 0.9933  | ✅ |
| 456  | (见 results/) | ✅ | ✅ |

Checkpoints: `checkpoints/exp17/vanilla_seed{42,123,456}/baseline/best.pt`

### 9-class (GPU3) — ✅ 完成但有异常

原始脚本在 Stage1 seed=42 时进程中断（仅记录到 model loading）。Resume 脚本补完了全部 3 seeds。

| Seed | Stage1 | Stage2 Val Acc | 备注 |
|------|--------|----------------|------|
| 42   | ✅ | 1.0000（degenerate） | ⚠️ Val Loss=0.0000，所有 epoch 均为 0.0/1.0 |
| 123  | ✅ (Persuasion Acc=0.82, Intent Acc=0.99) | 需确认 | 正常 |
| 456  | ✅ | 0.9933 | Val Loss 0.0004→0.0076 稳定 |

⚠️ **seed=42 Stage2 结果退化**：train_loss 从 0.0453 骤降到 0.0000，val_loss 始终 0.0000。可能原因：
1. 原始 Stage1 进程中断，checkpoint 可能不完整（但文件存在）
2. 9-class multitask embeddings 对 binary 任务过于 informative，GRU 直接 memorize

Checkpoints: `checkpoints/exp17/9class_seed{42,123,456}/` (multitask + treatment)

### MLM (GPU0/1) — 🔄 修复中

原始 MLM Stage2 全部因 model.pt/safetensors 不匹配而 crash。修复脚本已启动在 GPU 0/1：

| Seed | Stage1 | Stage2 | 当前状态 |
|------|--------|--------|----------|
| 42   | ✅ (val_loss=4.0762) | 🔄 running on GPU0 | fix 脚本 Stage2 val_acc=0.9800 (epoch 19) |
| 123  | 🔄 running on GPU0 | pending | fix 脚本 Stage1 epoch 4/4 进行中 |
| 456  | 🔄 running on GPU1 | pending | fix 脚本 Stage1 epoch 4/4 进行中 |

修复方式：改用 `--mode baseline --model_name <hf_checkpoint_dir>` 替代 `--mode treatment --deberta_checkpoint`，绕过 `torch.load()` 直接用 `from_pretrained()` 加载 safetensors。

**注意**：fix 脚本用 `--mode baseline` 而非原始的 `--mode treatment`，这意味着 MLM embeddings 的提取方式可能与 vanilla baseline 完全相同（仅模型权重不同），而非通过 treatment mode 加载 fine-tuned encoder。需确认 baseline mode 下传入 MLM checkpoint 路径是否等价于 treatment mode 的行为。

## 可 Salvage 的结果

1. **Vanilla 3 seeds**: 全部可用，结果正常
2. **9-class seed 123/456**: 结果可用（seed=42 需要人工审查退化原因）
3. **MLM**: 修复脚本正在运行，预计 ~30min 内完成

## W&B

所有脚本 `WANDB_MODE=disabled`，无任何 W&B metrics。这是 cron 判定 failed 的直接原因（cron 检查 W&B runs 发现为空）。

## 进程和 GPU 状态

- GPU 0: exp17_mlm_gpu0_fix (tmux session `exp17_mlm_gpu0`) — ~20GB VRAM, 67% util
- GPU 1: exp17_mlm_gpu1_fix (tmux session `exp17_mlm_gpu1`) — ~20GB VRAM, 69% util
- GPU 2/3: idle（原始 exp17 进程已退出）

## 数据完整性

`data/expanded_1000/`: ✅
- train.jsonl: 700 conversations (15MB)
- val.jsonl: 150 conversations (3.2MB)
- test.jsonl: 150 conversations (3.2MB)

## 时间线

1. **07:13** — 原始 exp17_gpu2.sh (vanilla+MLM) 和 exp17_gpu3.sh (9-class) 启动
2. **07:14** — GPU2: vanilla 3 seeds 完成，MLM Stage1 seed=42 开始；GPU3: 9-class Stage1 seed=42 开始后中断
3. **~07:15** — GPU3 进程异常退出（日志仅 22 行）
4. **07:29** — Resume 脚本启动：GPU2 跑 MLM Stage1+2 seed=42，GPU3 跑 9-class 全部 seeds
5. **07:34** — GPU2 MLM Stage2 crash（FileNotFoundError: model.pt）
6. **07:35** — GPU3 9-class 全部完成
7. **07:44** — Fix 脚本在 GPU0/1 启动，修复 MLM 全 3 seeds

## 修复建议

1. **等待 fix 脚本完成**：GPU0/1 上的 MLM fix 正在正常运行，不要中断
2. **修复 train_classifier.py**：`load_encoder()` (line 57) 应支持 safetensors 格式——使用 `safetensors.torch.load_file()` 或 `AutoModel.from_pretrained()` 替代 `torch.load()`，从根源修复 treatment mode 加载逻辑
3. **审查 9-class seed=42**：检查 Stage1 checkpoint 完整性，确认退化是否因 checkpoint 损坏或 embedding 过拟合
4. **确认 fix 脚本语义等价性**：验证 `--mode baseline --model_name <mlm_ckpt>` 与 `--mode treatment --deberta_checkpoint <mlm_ckpt>` 在 embedding 提取上是否等价
5. **启用 W&B**：下次实验移除 `WANDB_MODE=disabled`
6. **完成后跑评估**：所有 seeds 完成后统一在 test set 上评估，生成 exp17 summary table
