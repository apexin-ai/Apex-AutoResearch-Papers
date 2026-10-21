# 14B Cross-Scorer Contingency Plan

## Trigger Condition
exp_14b_c4 完成后，如果 K*=1（而非预期 K*=2），启动此 contingency 排除 "1.5B scorer 能力不足" confound。

## 前提状态（已验证 2026-05-18）

| 项目 | 状态 | 路径 |
|------|------|------|
| Qwen2.5-14B-Instruct-AWQ | 存在 (9.4GB, 4-bit) | `/root/autodl-tmp/.hf_cache/Qwen2.5-14B-Instruct-AWQ/` |
| score_14b_confound.py | 存在 (4599B) | `scripts/score_14b_confound.py` |
| exp_14b_scorer_confound.sh | 存在 (677B, +x) | `scripts/exp_14b_scorer_confound.sh` |
| fetch_14b_data.sh | 已创建 | `scripts/fetch_14b_data.sh` |
| cqa1 -> westd SSH | 已通 | ed25519 key, port 42896 |

## 执行步骤

### Step 1: 拉取数据（~2 min）

```bash
# 在 cqa1-22115 上执行
cd /root/autodl-tmp/gen-depth-contamination
bash scripts/fetch_14b_data.sh
```

验证：确认 depth_0.jsonl 到 depth_5.jsonl 全部到位，每个文件行数一致。

### Step 2: 启动 14B scorer（~1-2h，取决于数据量）

```bash
# 在 cqa1-22115 上执行
cd /root/autodl-tmp/gen-depth-contamination
nohup bash scripts/exp_14b_scorer_confound.sh > logs/14b_scorer_confound.log 2>&1 &
echo $! > /tmp/14b_scorer_pid.txt
```

监控：
```bash
tail -f logs/14b_scorer_confound.log
```

### Step 3: 验证结果

结果输出到 `results_14b_scorer_confound/`，包含：
- `data_14b_scored/features.csv` -- 14B scorer 提取的特征
- 分析报告（K* 值、统计检验结果）

关键对比：
- 14B scorer 的 K* vs 1.5B scorer 的 K*
- 如果 14B scorer 也给出 K*=1，则排除 scorer 能力不足的 confound
- 如果 14B scorer 给出 K*=2，则 1.5B scorer 确实能力不足，需重新评估

## 注意事项

- cqa1 有 4x GPU，脚本默认用 CUDA_VISIBLE_DEVICES=0，单卡即可运行 AWQ 14B
- 数据传输只拉 depth_*.jsonl，不拉 seed_docs.jsonl（~539MB，scoring 不需要）
- 如果 westd 在 exp 完成前关机，需先确保数据已保存
