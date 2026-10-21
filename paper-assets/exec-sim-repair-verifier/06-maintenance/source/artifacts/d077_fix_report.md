# D077 Truncation Fix Report

## Val Set Token Length Distribution

| Statistic | Value |
|-----------|-------|
| n | 9335 |
| mean | 1252 |
| median | 397 |
| p75 | 1268 |
| p90 | 4865 |
| p95 | 4957 |
| p99 | 5406 |
| max | 8768 |

### Truncation Rate by max_seq_length

| max_seq_length | Truncated | Rate |
|---------------|-----------|------|
| 2048 | 1883 | 20.2% |
| 4096 | 1406 | 15.1% |
| 6144 | 36 | 0.4% |
| **8192** | **9** | **0.1%** |
| 12288 | 0 | 0.0% |

分布呈双峰特征：大量短样本 (median=397) 和一个 ~5000 token 的集中区 (p90-p95)。2048 截断了长尾，4096 仍落在集中区内部，6144+ 才突破。

## 修改内容

### eval_repo_verifier.py (line 114-127)

- `--max_seq_length` 默认值改为 `None`，根据 split 自动设置：
  - `test` -> 2048 (与原行为一致)
  - `val` -> 8192 (truncation 0.1%)
- `--batch_size` 默认值改为 `None`，自动适配：
  - `max_seq_length > 2048` -> batch_size=2
  - 否则 -> batch_size=16 (原默认值)
- 用户显式指定 `--max_seq_length` 或 `--batch_size` 时使用用户值

### eval_repo_cwm.py (line 276-291)

同样的修改，test 默认 batch_size=8 (原默认值)，val 默认 batch_size=2。

## 选择 max_seq_length=8192 的理由

1. 覆盖 99.9% 的 val 样本 (仅 9/9335 截断)
2. Qwen3-4B 支持 32768 context length，8192 在模型能力范围内
3. 5090 32GB 显存，bf16 4B 模型 + 8192 input + flash_attention_2，batch_size=2 可行
4. 12288 可消除全部截断，但边际收益极小 (仅多覆盖 9 个样本)，显存开销更大

## Dry-Run 验证结果

```
# val split: 自动 max_seq_length=8192, batch_size=2
$ python eval_repo_cwm.py --dry_run --split val --max_samples 5
split=val  max_seq_length=8192  batch_size=2
Dry run OK: 5 instances, labels={1: 5}

# test split: 保持原默认值
$ python eval_repo_cwm.py --dry_run --split test --max_samples 3
split=test  max_seq_length=2048  batch_size=8
Dry run OK: 3 instances, labels={1: 2, 0: 1}

# 用户显式指定值优先
$ python eval_repo_cwm.py --dry_run --split val --max_seq_length 4096 --batch_size 4
split=val  max_seq_length=4096  batch_size=4

# verifier --help 确认新参数可见
$ python eval_repo_verifier.py --help
--max_seq_length  Max input tokens (default: 2048 for test, 8192 for val)
```

## 下一步：Val Checkpoint Sweep

用修改后的脚本对所有 checkpoint 做 val eval：

```bash
# CLS verifier
for ckpt in /home/sonny/exec-sim-repair-verifier/outputs/repo_cls_*/checkpoint-*; do
  python eval_repo_verifier.py \
    --checkpoint_dir "$ckpt" \
    --split val \
    --output "eval_val_cls_$(basename $(dirname $ckpt))_$(basename $ckpt).json" \
    --save_predictions \
    --device cuda:X
done

# CWM
for ckpt in /home/sonny/exec-sim-repair-verifier/outputs/repo_cwm_*/checkpoint-*; do
  python eval_repo_cwm.py \
    --checkpoint_dir "$ckpt" \
    --split val \
    --output "eval_val_cwm_$(basename $(dirname $ckpt))_$(basename $ckpt).json" \
    --device cuda:X
done
```

预期效果：val truncation rate 从 20.2% 降到 ~0.1%，unparseable rate 应同步大幅下降，val accuracy 更真实反映模型能力。
