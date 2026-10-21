# RSA image_mean Validation — Claim 2

## 核心数值

| Condition | last_preaction | image_mean | delta |
|-----------|---------------|------------|-------|
| **Trained** (peak, layer 23) | 0.4876 | **0.5014** | +0.0138 |
| **Untrained** (peak, layer 23) | 0.4846 | **0.4847** | +0.0001 |
| **SigLIP projector** | — | **0.6153** | — |

## 关键发现

### image_mean RSA = 0.5014（trained peak），远低于 SigLIP 0.6153

- **image_mean trained peak RSA: 0.5014** (layer 23)
- **image_mean untrained peak RSA: 0.4847** (layer 23)
- **SigLIP projector RSA: 0.6153**
- **Gap: 0.6153 → 0.5014 = -0.1139**

### Claim 2 判定: **HOLDS — LLM 确实降解 action alignment**

image_mean RSA (0.5014) ≈ 0.50，远低于 SigLIP (0.6153)，与 last_preaction (0.4876) 在同一量级。
这排除了"聚合伪影"假说——即使使用与 SigLIP 相同的 mean pooling 策略，VLA 的 action alignment 仍然显著低于 SigLIP projector。

### 补充观察

- image_mean 比 last_preaction 略高 (+0.0138 for trained)，说明 mean pooling 确实比单 token 聚合稍好
- 但这个提升很小，不改变 0.61→0.50 的主结论
- trained vs untrained delta (0.5014 - 0.4847 = +0.0167) 也与 last_preaction 的 delta (0.4876 - 0.4846 = +0.003) 方向一致，且更大

## 判断标准对照

- image_mean RSA ≈ 0.61 → 聚合伪影 → **未发生**
- image_mean RSA ≈ 0.49 → LLM 确实降解 → **✓ 发生 (0.5014)**
- 中间值 → 需要讨论 → **不适用**

## 可复现命令

```bash
# 服务器: westd-19183
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/vla-ssd
python3 rsa_image_mean.py
# 结果: /root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json
```

## 脚本路径

- `/root/vla-ssd/rsa_image_mean.py` (已有，无需修改)
