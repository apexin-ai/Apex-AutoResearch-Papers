# w5_lora_scierc_training 失败诊断

- **实验**: w5_lora_scierc_training
- **服务器**: westd-16980 (GPU: 2× RTX PRO 6000 Black, 97 GB each, idle)
- **退出**: EXIT_CODE=1，运行 133 s
- **诊断时间**: 2026-05-15

## 错误类型
**配置错误 / 缺凭据**：wandb 未登录。训练在 `trainer.train()` 调用刚开始的 `on_train_begin` 回调里抛出 `UsageError: No API key configured`。

## 关键日志（尾部）
```
Starting training
The tokenizer has new PAD/BOS/EOS tokens that differ from the model config ...
Traceback (most recent call last):
  File "scripts/train_lora_scierc.py", line 227, in <module>
    main()
  ...
  File ".../transformers/integrations/integration_utils.py", line 893, in setup
    self._wandb.init(...)
  ...
  File ".../wandb/sdk/lib/wbauth/authenticate.py", line 139, in authenticate_session
    raise UsageError(...)
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
EXIT_CODE=1
```

前置阶段一切正常：
- tokenizer / 数据集 / 模型加载全部成功（train=1762, val=260；checkpoint 5 shards 全部载入）
- LoRA + SFTTrainer 构造完成
- 失败发生在第一个 optimizer step 之前的 wandb init

## 根本原因
1. `train_lora_scierc.py` 默认 `report_to = "wandb"`（只有 `--dry_run` 才改为 `"none"`）。
2. 服务器上未配置 wandb 凭据：
   - 环境变量无 `WANDB_API_KEY`（env 输出无 wandb 相关项）
   - `/root/.netrc` 不存在
   - `/root/.config/wandb` 不存在
3. wandb 在 noninteractive 模式下无法 prompt 输入 key，直接抛错并终止训练。

## 排除项
- **不是 OOM**：失败时进程已退出，nvidia-smi 显示 0 MiB 占用；且训练根本没跑到 forward。两张卡 97 GB × 2，Qwen3-8B + LoRA 远远够。
- **不是数据/模型路径错误**：日志确认 train/val/base model 全部加载成功。
- **不是依赖缺失**：torch/transformers/peft/trl 全部 import 成功并完成 trainer 构造。
- **不是代码 bug**：训练脚本本身逻辑正确，问题在外部凭据缺失。

## 修复建议（任选其一）

### 方案 A（推荐保留 W&B 追踪）：配置 wandb 凭据
```bash
# 一次性写入 ~/.netrc（持久）
WANDB_API_KEY=[REDACTED] wandb login --relogin
# 或仅当前 session：
export WANDB_API_KEY=[REDACTED]
```
key 取自 https://wandb.ai/authorize。之后用原命令重跑即可。

### 方案 B（最快）：禁用 wandb，跑离线训练
注入环境变量，无需改代码：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
         cd /root/schema_semantic_constrained_ie && \
         WANDB_MODE=disabled python3 scripts/train_lora_scierc.py"
```
`WANDB_MODE=disabled` 让 `wandb.init` 走 no-op 路径，不要求 key。

### 方案 C：W&B 离线模式（保留日志，事后同步）
```bash
WANDB_MODE=offline python3 scripts/train_lora_scierc.py
# 训练完后再 wandb sync ./wandb/offline-run-*
```

## 是否需要代码修改
**不需要立即改代码。** 推荐先用方案 A 或 B 重跑：
- 想保留实验追踪 → 方案 A（配 `WANDB_API_KEY`）
- 想立刻拿到 LoRA checkpoint、不在意 wandb → 方案 B（`WANDB_MODE=disabled`）

若后续多个训练脚本都会遇到同样问题，可考虑在 `parse_args` 里加 `--no_wandb` flag 做永久解决（在 `if args.dry_run` 等价的分支里把 `report_to` 置为 `"none"`）。

## 重跑命令示例（方案 B）
```bash
ssh connect.westd.seetacloud.com
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie
WANDB_MODE=disabled nohup python3 scripts/train_lora_scierc.py \
  > /root/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log 2>&1 &
```
