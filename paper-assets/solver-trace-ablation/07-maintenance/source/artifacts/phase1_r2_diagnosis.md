# Phase 1 GRPO 实验失败诊断报告

**日期**: 2026-05-13  
**服务器**: westd-39279  

## 1. 错误摘要

| 实验 | 轮次 | EXIT_CODE | 根因 |
|------|------|-----------|------|
| exec-only | R1 | 2 | argparse required 参数未传 |
| exec+STA | R1 | 2 | 同上 |
| exec-only | R2 | 1 | wandb API key 未配置 |
| exec+STA | R2 | 1 | 同上 |

## 2. R1 根因：argparse 参数解析失败 (EXIT_CODE=2)

**错误信息**:
```
train_grpo.py: error: the following arguments are required: --model_path, --data_path, --reward_mode, --output_dir
```

**分析**: R1 版本的 `train_grpo.py` 中，4 个核心参数设置为 `required=True`。启动命令仅传了 `--config`，argparse 在 `parse_args()` 阶段就报错退出，config 文件根本没被读取。

**R1→R2 之间的修复**: 已将参数改为 `default=None`，config 加载后手动检查缺失参数。R2 不再出现此错误。

## 3. R2 根因：wandb API key 未配置 (EXIT_CODE=1)

**错误信息**:
```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

**崩溃位置**: `train_grpo.py:211` → `wandb.init()`

**分析**: 
- 两个 YAML 配置都设了 `wandb_project: solver-trace-ablation`，且未设 `no_wandb: true`
- 服务器上 `wandb.api.api_key` 返回 `None`，从未执行过 `wandb login`
- `wandb.init()` 未被 try/except 保护，直接抛出异常终止进程

## 4. 已执行的修复

### 修复 wandb 崩溃（train_grpo.py:211-216）

将裸的 `wandb.init()` 调用包裹在 try/except 中，失败时优雅降级：

```python
# 修改前
wandb.init(project=args.wandb_project, name=run_name, config=vars(args))

# 修改后
try:
    wandb.init(project=args.wandb_project, name=run_name, config=vars(args))
except wandb.errors.UsageError as e:
    logger.warning(f"wandb init failed ({e}), falling back to no_wandb")
    report_to = "none"
    args.no_wandb = True
```

**验证结果**: import + parse_args 测试通过。

## 5. 环境信息

```
torch==2.10.0+cu128
transformers==4.57.6
trl==1.1.0
peft==0.19.0
accelerate==1.13.0
wandb==0.26.0
vllm==0.18.1 (TRL 警告: 支持 0.11.0-0.17.1)
```

数据文件: `data/proofwriter_fol_500.jsonl` (485KB) OK  
模型目录: `/root/autodl-tmp/models/Qwen3-4B` OK

## 6. 后续建议

1. **配置 wandb API key**: 在服务器上执行 `wandb login` 以启用实验追踪
2. **vLLM 版本警告**: TRL 1.1.0 仅支持 vLLM <=0.17.1，当前 0.18.1。目前仅是警告，如果训练中出现 generation 相关错误需降级
3. **可以启动 R3**: wandb 崩溃已修复，训练将在无 wandb 模式下继续（或配好 API key 后正常追踪）
