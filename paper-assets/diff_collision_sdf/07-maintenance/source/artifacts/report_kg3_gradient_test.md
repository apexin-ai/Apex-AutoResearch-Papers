# KG-3: SDF Gradient → Action Token 梯度回传 Toy Test 报告

**日期**: 2026-05-19  
**结论**: **KG-3 PASS**

---

## 测试配置

| Config | batch | action_dim | feature_dim | n_query | 结果 |
|--------|-------|-----------|-------------|---------|------|
| 1 | 1 | 7 | 1024 | 16 | PASS |
| 2 | 16 | 7 | 1024 | 16 | PASS |
| 3 | 64 | 7 | 1024 | 16 | PASS |
| 4 | 16 | 32 | 1024 | 16 | PASS |
| 5 | 16 | 7 | 1024 | 64 | PASS |

SDF Decoder: 4 层 MLP, hidden=256, Softplus(beta=5) activation, skip connection at layer 3。  
ActionProjection: Linear(action_dim → 1024)。

---

## 完整输出

```
============================================================
Test: batch=1, action_dim=7, feature_dim=1024, n_query=16
============================================================
  [1] Gradient has NaN: False PASS
  [2] Gradient norm (mean): 0.981800
      Gradient max abs:     0.710773
      Exploded: False PASS
  [3] Gradient vanished: False PASS
  [4] Eikonal |nabla SDF| mean: 0.1216 (target ~1.0)
  [5] SDF: mean=-0.2309, std=0.0362, min=-0.3034, max=-0.1742
      Colliding points (SDF<0): 16/16
      Collision cost: 0.250865
      Eikonal loss:   0.771572
      Total loss:     0.328022
  [6] Cost original:         0.250865
      Cost after -grad step: 0.250768
      Cost after +grad step: 0.250960
      -grad reduces cost: True PASS
  [7] Per-layer gradient norms in SDF Decoder:
      layer1.weight         grad_norm=58.178455
      layer1.bias           grad_norm=1.006274
      layer2.weight         grad_norm=30.090782
      layer2.bias           grad_norm=1.034298
      layer3.weight         grad_norm=34.023861
      layer3.bias           grad_norm=1.010455
      layer4.weight         grad_norm=34.061989
      layer4.bias           grad_norm=1.000000
      action_grad_norm:       0.987289
  Result: PASS

============================================================
Test: batch=16, action_dim=7, feature_dim=1024, n_query=16
============================================================
  [1] Gradient has NaN: False PASS
  [2] Gradient norm (mean): 0.057819
      Gradient max abs:     0.096626
      Exploded: False PASS
  [3] Gradient vanished: False PASS
  [4] Eikonal |nabla SDF| mean: 0.1529 (target ~1.0)
  [5] SDF: mean=-0.2811, std=1.0380, min=-2.7915, max=1.4987
      Colliding points (SDF<0): 144/256
      Collision cost: 0.569651
      Eikonal loss:   0.720026
      Total loss:     0.641654
  [6] Cost original:         0.569651
      Cost after -grad step: 0.569641
      Cost after +grad step: 0.569662
      -grad reduces cost: True PASS
  [7] Per-layer gradient norms in SDF Decoder:
      layer1.weight         grad_norm=10.944869
      layer1.bias           grad_norm=0.311640
      layer2.weight         grad_norm=7.767018
      layer2.bias           grad_norm=0.408957
      layer3.weight         grad_norm=11.239902
      layer3.bias           grad_norm=0.485747
      layer4.weight         grad_norm=13.111344
      layer4.bias           grad_norm=0.562500
      action_grad_norm:       0.320028
  Result: PASS

============================================================
Test: batch=64, action_dim=7, feature_dim=1024, n_query=16
============================================================
  [1] Gradient has NaN: False PASS
  [2] Gradient norm (mean): 0.016073
      Gradient max abs:     0.028373
      Exploded: False PASS
  [3] Gradient vanished: False PASS
  [4] Eikonal |nabla SDF| mean: 0.1442 (target ~1.0)
  [5] SDF: mean=-0.3192, std=0.9338, min=-2.7588, max=2.0541
      Colliding points (SDF<0): 636/1024
      Collision cost: 0.567100
      Eikonal loss:   0.735171
      Total loss:     0.640617
  [6] Cost original:         0.567100
      Cost after -grad step: 0.567097
      Cost after +grad step: 0.567103
      -grad reduces cost: True PASS
  [7] Per-layer gradient norms in SDF Decoder:
      layer1.weight         grad_norm=7.278909
      layer1.bias           grad_norm=0.324912
      layer2.weight         grad_norm=6.643936
      layer2.bias           grad_norm=0.448646
      layer3.weight         grad_norm=10.283916
      layer3.bias           grad_norm=0.548403
      layer4.weight         grad_norm=12.602468
      layer4.bias           grad_norm=0.640625
      action_grad_norm:       0.166773
  Result: PASS

============================================================
Test: batch=16, action_dim=32, feature_dim=1024, n_query=16
============================================================
  [1] Gradient has NaN: False PASS
  [2] Gradient norm (mean): 0.018909
      Gradient max abs:     0.042922
      Exploded: False PASS
  [3] Gradient vanished: False PASS
  [4] Eikonal |nabla SDF| mean: 0.1523 (target ~1.0)
  [5] SDF: mean=0.9907, std=1.2778, min=-1.1680, max=4.0657
      Colliding points (SDF<0): 50/256
      Collision cost: 0.127597
      Eikonal loss:   0.720224
      Total loss:     0.199619
  [6] Cost original:         0.127597
      Cost after -grad step: 0.127594
      Cost after +grad step: 0.127600
      -grad reduces cost: True PASS
  [7] Per-layer gradient norms in SDF Decoder:
      layer1.weight         grad_norm=3.155388
      layer1.bias           grad_norm=0.104820
      layer2.weight         grad_norm=2.089531
      layer2.bias           grad_norm=0.131599
      layer3.weight         grad_norm=2.602096
      layer3.bias           grad_norm=0.147696
      layer4.weight         grad_norm=3.190187
      layer4.bias           grad_norm=0.187500
      action_grad_norm:       0.167396
  Result: PASS

============================================================
Test: batch=16, action_dim=7, feature_dim=1024, n_query=64
============================================================
  [1] Gradient has NaN: False PASS
  [2] Gradient norm (mean): 0.057941
      Gradient max abs:     0.096747
      Exploded: False PASS
  [3] Gradient vanished: False PASS
  [4] Eikonal |nabla SDF| mean: 0.1528 (target ~1.0)
  [5] SDF: mean=-0.2804, std=1.0331, min=-2.7890, max=1.5329
      Colliding points (SDF<0): 576/1024
      Collision cost: 0.569123
      Eikonal loss:   0.719823
      Total loss:     0.641105
  [6] Cost original:         0.569123
      Cost after -grad step: 0.569113
      Cost after +grad step: 0.569133
      -grad reduces cost: True PASS
  [7] Per-layer gradient norms in SDF Decoder:
      layer1.weight         grad_norm=10.953660
      layer1.bias           grad_norm=0.312323
      layer2.weight         grad_norm=7.769152
      layer2.bias           grad_norm=0.409365
      layer3.weight         grad_norm=11.245345
      layer3.bias           grad_norm=0.486001
      layer4.weight         grad_norm=13.108138
      layer4.bias           grad_norm=0.562500
      action_grad_norm:       0.317302
  Result: PASS

============================================================
SUMMARY
============================================================
  Config (1, 7): PASS
  Config (16, 7): PASS
  Config (64, 7): PASS
  Config (16, 32): PASS
  Config (16, 7, 1024, 64): PASS

KG-3 Overall: PASS
```

---

## 分析

### 梯度数值稳定性
所有配置下梯度无 NaN、无 explode（max abs 均 < 1）、无 vanish。使用 Softplus(beta=5) 替代 ReLU 作为激活函数，避免了 ReLU 的零梯度区域，保证梯度信号完整传播。

### 梯度方向正确性
所有配置的有限差分验证均 PASS：沿梯度负方向微调 action 后 collision cost 下降，确认梯度方向能正确引导 action 远离碰撞区域。

### 逐层梯度传播
梯度从 SDF decoder 的 layer4 稳定传播到 layer1，再通过 ActionProjection 到达 action tokens。各层梯度范数在合理范围内，无明显衰减断层。

### Batch size 缩放
随 batch size 增大（1→16→64），action 梯度范数按 ~1/B 缩放（0.98→0.058→0.016），符合 mean reduction 的预期。信号稳定，不因 batch 增大而消失。

### Eikonal 正则化
初始化时 |∇SDF| ≈ 0.12-0.15，远低于目标值 1.0。这在未经训练的随机初始化网络上是正常的——Eikonal loss 的梯度方向正确（推动 |∇SDF| → 1），训练后会收敛。此项不影响 KG-3 的 PASS 判定。

### action_dim=32（openpi 配置）
与 action_dim=7 表现一致，梯度稳定、方向正确。维度增大未引入额外不稳定性。
