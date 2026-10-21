import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import timm
import json
import numpy as np
import os
from datetime import datetime

# Previous D215a results (from GN32-contaminated checkpoints)
PREVIOUS_RESULTS = {
    'muon_r50_bn':    0.006498,
    'adamw_r50_bn':   0.002771,
    'soap_r50_bn':    0.009288,
    'sgd_r50_bn':     0.001266,
    'shampoo_r50_bn': 1.160000,
}

def get_gradient_norms(model, dataloader, device, num_batches=10):
    model.train()
    criterion = nn.CrossEntropyLoss()
    layer_grad_norms = {}
    for i, (images, labels) in enumerate(dataloader):
        if i >= num_batches:
            break
        images, labels = images.to(device), labels.to(device)
        model.zero_grad()
        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        for name, param in model.named_parameters():
            if param.grad is not None:
                norm = param.grad.norm().item()
                if name not in layer_grad_norms:
                    layer_grad_norms[name] = []
                layer_grad_norms[name].append(norm)
    return {k: float(np.mean(v)) for k, v in layer_grad_norms.items()}

def classify_depth(layer_name):
    if layer_name.startswith('conv1') or layer_name.startswith('bn1'):
        return 'stem'
    for i in range(1, 5):
        if layer_name.startswith(f'layer{i}'):
            return f'layer{i}'
    if layer_name.startswith('fc'):
        return 'fc'
    return 'other'

def main():
    device = torch.device('cuda:1')
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize([0.5071, 0.4867, 0.4408], [0.2675, 0.2565, 0.2761])
    ])
    valset = torchvision.datasets.CIFAR100(root='/root/autodl-tmp/data', train=False, transform=transform, download=True)
    valloader = torch.utils.data.DataLoader(valset, batch_size=32, shuffle=False, num_workers=4)

    D = '/root/autodl-tmp/checkpoints/spectral_optim'
    configs = [
        ('muon_r50_bn',    f'{D}/resnet50_muon_s42_best.pt'),
        ('adamw_r50_bn',   f'{D}/resnet50_adamw_s42_lr1e-3_best.pt'),
        ('soap_r50_bn',    f'{D}/resnet50_soap_s42_lr1e-2_best.pt'),
        ('shampoo_r50_bn', f'{D}/resnet50_shampoo_s42_lr5e-2_best.pt'),
        # SGD BN: permanently lost, skipped
    ]

    print("=" * 70)
    print("D215a CORRECTED: R50-BN Gradient Norm Analysis")
    print("Using verified BN checkpoints (Shampoo/SGD corrected)")
    print("Best checkpoint = highest val acc epoch")
    print("=" * 70)

    results = {}
    for name, ckpt_path in configs:
        if not os.path.exists(ckpt_path):
            print(f'\nSKIP {name}: {ckpt_path} not found')
            continue

        stat = os.stat(ckpt_path)
        mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        size_mb = stat.st_size / (1024 * 1024)

        print(f'\n--- {name} ---')
        print(f'  File: {ckpt_path}')
        print(f'  Modified: {mtime}, Size: {size_mb:.1f} MB')

        model = timm.create_model('resnet50', pretrained=False, num_classes=100)
        state = torch.load(ckpt_path, map_location='cpu', weights_only=False)

        if 'model_state_dict' in state:
            sd = state['model_state_dict']
        elif 'state_dict' in state:
            sd = state['state_dict']
        else:
            sd = state

        # Validate BN identity
        has_bn = any('bn1.running_mean' in k for k in sd.keys())
        has_gn = any('gn' in k.lower() or 'group_norm' in k.lower() for k in sd.keys())
        bn_keys = [k for k in sd.keys() if 'running_mean' in k]
        print(f'  BN validation: has_running_mean={has_bn} ({len(bn_keys)} keys), has_gn_keys={has_gn}')
        if not has_bn:
            print(f'  ERROR: No bn1.running_mean found! This is NOT a BN checkpoint!')
            continue

        # Print epoch info if available
        if isinstance(state, dict):
            for key in ['epoch', 'best_acc', 'best_val_acc', 'val_acc']:
                if key in state:
                    print(f'  {key}: {state[key]}')

        model.load_state_dict(sd, strict=False)
        model = model.to(device)
        norms = get_gradient_norms(model, valloader, device)
        mean_norm = np.mean(list(norms.values()))
        results[name] = norms

        print(f'  Layers: {len(norms)}, Mean grad norm: {mean_norm:.6f}')

        # Compare with previous
        if name in PREVIOUS_RESULTS:
            old = PREVIOUS_RESULTS[name]
            delta_pct = (mean_norm - old) / old * 100
            print(f'  Previous (D215a): {old:.6f}, Delta: {delta_pct:+.1f}%')
            if name == 'shampoo_r50_bn':
                print(f'  ** SHAMPOO KEY CORRECTION: old={old:.6f} (was GN32!), new={mean_norm:.6f} (true BN) **')

        # Per-depth breakdown
        depth_norms = {}
        for layer, norm in norms.items():
            depth = classify_depth(layer)
            if depth not in depth_norms:
                depth_norms[depth] = []
            depth_norms[depth].append(norm)
        depth_means = {d: float(np.mean(v)) for d, v in depth_norms.items()}
        depth_order = ['stem', 'layer1', 'layer2', 'layer3', 'layer4', 'fc']
        depth_str = ', '.join(f'{d}={depth_means.get(d, 0):.6f}' for d in depth_order if d in depth_means)
        print(f'  By depth: {depth_str}')

        del model
        torch.cuda.empty_cache()

    # Summary comparison table
    print('\n' + '=' * 70)
    print('SUMMARY: Old (D215a) vs Corrected')
    print(f'{"Config":<20} {"Old":>12} {"New":>12} {"Delta%":>10} {"Note"}')
    print('-' * 70)
    for name in ['muon_r50_bn', 'adamw_r50_bn', 'soap_r50_bn', 'shampoo_r50_bn', 'sgd_r50_bn']:
        old = PREVIOUS_RESULTS.get(name, None)
        if name in results:
            new = np.mean(list(results[name].values()))
            delta = (new - old) / old * 100 if old else 0
            note = ''
            if name == 'shampoo_r50_bn':
                note = 'CORRECTED (was GN32)'
            elif name in ['muon_r50_bn', 'adamw_r50_bn', 'soap_r50_bn']:
                note = 'same ckpt'
            print(f'{name:<20} {old:>12.6f} {new:>12.6f} {delta:>+9.1f}% {note}')
        else:
            print(f'{name:<20} {old if old else "N/A":>12} {"SKIPPED":>12} {"":>10} lost')

    # Cross-layer CV
    print('\n=== Cross-layer Coefficient of Variation ===')
    for name in results:
        vals = list(results[name].values())
        cv = np.std(vals) / np.mean(vals) if np.mean(vals) > 0 else 0
        print(f'  {name}: CV={cv:.4f} (mean={np.mean(vals):.6f}, std={np.std(vals):.6f})')

    # Ratio analysis: each optimizer / adamw by depth
    print('\n=== Optimizer/AdamW Ratio by Depth ===')
    if 'adamw_r50_bn' in results:
        adamw_norms = results['adamw_r50_bn']
        for opt in ['muon', 'soap', 'shampoo']:
            opt_key = f'{opt}_r50_bn'
            if opt_key not in results:
                continue
            opt_norms = results[opt_key]
            depth_ratios = {}
            for layer in adamw_norms:
                if layer in opt_norms and adamw_norms[layer] > 1e-10:
                    depth = classify_depth(layer)
                    if depth not in depth_ratios:
                        depth_ratios[depth] = []
                    depth_ratios[depth].append(opt_norms[layer] / adamw_norms[layer])
            depth_order = ['stem', 'layer1', 'layer2', 'layer3', 'layer4', 'fc']
            parts = []
            for d in depth_order:
                if d in depth_ratios:
                    parts.append(f'{d}={np.mean(depth_ratios[d]):.4f}')
            all_ratios = [r for v in depth_ratios.values() for r in v]
            print(f'  {opt}/adamw: overall={np.mean(all_ratios):.4f} | {", ".join(parts)}')

    # Save results
    output_path = '/root/spectral_optim_vision_geometry/gradient_norm_analysis_bn_corrected.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nResults saved to {output_path}')

if __name__ == '__main__':
    main()
