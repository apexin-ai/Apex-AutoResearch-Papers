"""
KG-3: SDF Gradient → Action Token Projection 梯度回传 Toy Test
验证 SDF 梯度能稳定反向传播到 action tokens
"""
import torch
import torch.nn as nn


class SDFDecoder(nn.Module):
    """
    4 层 MLP，输入 [action_feature (1024d), xyz (3d)]，输出 scalar SDF
    Skip connection at layer 2（重新注入 xyz）
    """
    def __init__(self, feature_dim=1024, hidden_dim=256):
        super().__init__()
        input_dim = feature_dim + 3
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, hidden_dim)
        self.layer3 = nn.Linear(hidden_dim + 3, hidden_dim)
        self.layer4 = nn.Linear(hidden_dim, 1)
        self.softplus = nn.Softplus(beta=5)

    def forward(self, features, xyz):
        x = torch.cat([features, xyz], dim=-1)
        x = self.softplus(self.layer1(x))
        x = self.softplus(self.layer2(x))
        x = torch.cat([x, xyz], dim=-1)
        x = self.softplus(self.layer3(x))
        sdf = self.layer4(x)
        return sdf.squeeze(-1)


class ActionProjection(nn.Module):
    """模拟 VLA 的 action_in_proj: action_dim → feature_dim"""
    def __init__(self, action_dim=7, feature_dim=1024):
        super().__init__()
        self.proj = nn.Linear(action_dim, feature_dim)

    def forward(self, actions):
        return self.proj(actions)


def run_test(batch_size, action_dim, feature_dim=1024, n_query_points=16, margin=0.02):
    print(f"\n{'='*60}")
    print(f"Test: batch={batch_size}, action_dim={action_dim}, "
          f"feature_dim={feature_dim}, n_query={n_query_points}")
    print(f"{'='*60}")

    torch.manual_seed(42)

    action_proj = ActionProjection(action_dim, feature_dim)
    sdf_decoder = SDFDecoder(feature_dim, hidden_dim=256)

    # 用 Kaiming init 确保初始化合理
    for m in [action_proj, sdf_decoder]:
        for name, param in m.named_parameters():
            if 'weight' in name:
                nn.init.kaiming_normal_(param, nonlinearity='relu')
            elif 'bias' in name:
                nn.init.zeros_(param)

    actions = torch.randn(batch_size, action_dim, requires_grad=True)
    query_points = torch.randn(batch_size, n_query_points, 3) * 0.3

    # Forward
    action_features = action_proj(actions)

    sdf_values = []
    for i in range(n_query_points):
        xyz = query_points[:, i, :]
        sdf = sdf_decoder(action_features, xyz)
        sdf_values.append(sdf)
    sdf_all = torch.stack(sdf_values, dim=1)

    # Collision cost
    collision_cost = torch.relu(-sdf_all + margin)
    total_cost = collision_cost.mean()

    # Eikonal regularization — 需要对 xyz 求梯度
    xyz_eik = query_points[:, 0, :].clone().detach().requires_grad_(True)
    sdf_eik = sdf_decoder(action_features.detach(), xyz_eik)
    grad_sdf = torch.autograd.grad(
        sdf_eik.sum(), xyz_eik, create_graph=True
    )[0]
    eikonal_loss = ((grad_sdf.norm(dim=-1) - 1.0) ** 2).mean()

    loss = total_cost + 0.1 * eikonal_loss
    loss.backward()

    # === 检查结果 ===
    grad = actions.grad
    checks = {}

    # Check 1: 无 NaN
    has_nan = torch.isnan(grad).any().item()
    checks['no_nan'] = not has_nan
    print(f"  [1] Gradient has NaN: {has_nan} "
          f"{'FAIL' if has_nan else 'PASS'}")

    # Check 2: 无 explode
    grad_norm = grad.norm(dim=-1).mean().item()
    grad_max = grad.abs().max().item()
    is_exploded = grad_max > 1e6
    checks['no_explode'] = not is_exploded
    print(f"  [2] Gradient norm (mean): {grad_norm:.6f}")
    print(f"      Gradient max abs:     {grad_max:.6f}")
    print(f"      Exploded: {is_exploded} "
          f"{'FAIL' if is_exploded else 'PASS'}")

    # Check 3: 梯度非零
    is_zero = grad_norm < 1e-10
    checks['non_zero'] = not is_zero
    print(f"  [3] Gradient vanished: {is_zero} "
          f"{'FAIL' if is_zero else 'PASS'}")

    # Check 4: Eikonal |∇SDF|
    eikonal_grad_norm = grad_sdf.norm(dim=-1).mean().item()
    print(f"  [4] Eikonal |nabla SDF| mean: {eikonal_grad_norm:.4f} (target ~1.0)")

    # Check 5: SDF 统计
    print(f"  [5] SDF: mean={sdf_all.mean().item():.4f}, "
          f"std={sdf_all.std().item():.4f}, "
          f"min={sdf_all.min().item():.4f}, max={sdf_all.max().item():.4f}")
    n_colliding = (sdf_all < 0).sum().item()
    print(f"      Colliding points (SDF<0): {n_colliding}/{sdf_all.numel()}")
    print(f"      Collision cost: {total_cost.item():.6f}")
    print(f"      Eikonal loss:   {eikonal_loss.item():.6f}")
    print(f"      Total loss:     {loss.item():.6f}")

    # Check 6: 梯度方向一致性（有限差分验证）
    with torch.no_grad():
        eps = 1e-4
        # 沿梯度负方向（梯度下降）应该减小 cost
        actions_minus = actions - eps * grad
        features_minus = action_proj(actions_minus)
        sdf_minus = []
        for i in range(n_query_points):
            xyz = query_points[:, i, :]
            sdf_minus.append(sdf_decoder(features_minus, xyz))
        sdf_minus_all = torch.stack(sdf_minus, dim=1)
        cost_minus = torch.relu(-sdf_minus_all + margin).mean().item()

        actions_plus = actions + eps * grad
        features_plus = action_proj(actions_plus)
        sdf_plus = []
        for i in range(n_query_points):
            xyz = query_points[:, i, :]
            sdf_plus.append(sdf_decoder(features_plus, xyz))
        sdf_plus_all = torch.stack(sdf_plus, dim=1)
        cost_plus = torch.relu(-sdf_plus_all + margin).mean().item()

    cost_orig = total_cost.item()
    direction_ok = cost_minus <= cost_orig + 1e-6
    checks['direction'] = direction_ok
    print(f"  [6] Cost original:         {cost_orig:.6f}")
    print(f"      Cost after -grad step: {cost_minus:.6f}")
    print(f"      Cost after +grad step: {cost_plus:.6f}")
    print(f"      -grad reduces cost: {direction_ok} "
          f"{'PASS' if direction_ok else 'CHECK'}")

    # Check 7: 逐层梯度范数（检查梯度在 MLP 各层的传播）
    print(f"  [7] Per-layer gradient norms in SDF Decoder:")
    sdf_decoder.zero_grad()
    action_proj.zero_grad()
    actions2 = actions.detach().clone().requires_grad_(True)
    af2 = action_proj(actions2)
    sdf2 = sdf_decoder(af2, query_points[:, 0, :])
    cost2 = torch.relu(-sdf2 + margin).mean()
    cost2.backward()
    for name, param in sdf_decoder.named_parameters():
        if param.grad is not None:
            gn = param.grad.norm().item()
            print(f"      {name:20s}  grad_norm={gn:.6f}")
    proj_grad_norm = actions2.grad.norm().item() if actions2.grad is not None else 0
    print(f"      action_grad_norm:       {proj_grad_norm:.6f}")
    grad_reaches_action = proj_grad_norm > 1e-10
    checks['per_layer'] = grad_reaches_action

    all_pass = all(checks.values())
    print(f"\n  Result: {'PASS' if all_pass else 'FAIL'}")
    return all_pass, checks


if __name__ == "__main__":
    configs = [
        (1, 7),
        (16, 7),
        (64, 7),
        (16, 32),
        (16, 7, 1024, 64),
    ]

    all_results = []
    for cfg in configs:
        result, checks = run_test(*cfg)
        all_results.append((cfg, result, checks))

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for cfg, result, checks in all_results:
        status = "PASS" if result else "FAIL"
        failed = [k for k, v in checks.items() if not v]
        detail = f" (failed: {failed})" if failed else ""
        print(f"  Config {cfg}: {status}{detail}")

    overall = all(r for _, r, _ in all_results)
    print(f"\nKG-3 Overall: {'PASS' if overall else 'FAIL'}")
