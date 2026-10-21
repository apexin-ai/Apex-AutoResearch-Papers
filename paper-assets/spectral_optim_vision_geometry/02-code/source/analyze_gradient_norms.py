import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import timm
import json
import numpy as np

def replace_bn_with_gn(module, num_groups=1):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(num_groups, child.num_features))
        else:
            replace_bn_with_gn(child, num_groups)
    return module

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

def main():
    device = torch.device('cuda:0')
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize([0.5071, 0.4867, 0.4408], [0.2675, 0.2565, 0.2761])
    ])
    valset = torchvision.datasets.CIFAR100(root='/root/autodl-tmp/data', train=False, transform=transform, download=True)
    valloader = torch.utils.data.DataLoader(valset, batch_size=32, shuffle=False, num_workers=4)

    D = '/root/autodl-tmp/checkpoints/spectral_optim'
    configs = [
        ('muon_r50_bn',    'resnet50', 'bn', f'{D}/resnet50_muon_s42_best.pt'),
        ('adamw_r50_bn',   'resnet50', 'bn', f'{D}/resnet50_adamw_s42_lr1e-3_best.pt'),
        ('soap_r50_bn',    'resnet50', 'bn', f'{D}/resnet50_soap_s42_lr1e-2_best.pt'),
        ('sgd_r50_bn',     'resnet50', 'bn', f'{D}/resnet50_sgd_s42_lr1e-1_best.pt'),
        ('shampoo_r50_bn', 'resnet50', 'bn', f'{D}/resnet50_shampoo_s42_lr7e-3_best.pt'),
        ('muon_r50_ln',    'resnet50', 'ln', f'{D}/resnet50_ln_muon_s42_best.pt'),
        ('adamw_r50_ln',   'resnet50', 'ln', f'{D}/resnet50_ln_adamw_s42_lr1e-3_best.pt'),
        ('sgd_r50_ln',     'resnet50', 'ln', f'{D}/resnet50_ln_sgd_s42_lr1e-1_best.pt'),
    ]

    results = {}
    for name, model_type, norm_type, ckpt_path in configs:
        import os
        if not os.path.exists(ckpt_path):
            print(f'SKIP {name}: {ckpt_path}')
            continue
        print(f'Processing {name}...')
        model = timm.create_model(model_type, pretrained=False, num_classes=100)
        if norm_type == 'ln':
            replace_bn_with_gn(model, num_groups=1)
        state = torch.load(ckpt_path, map_location='cpu', weights_only=False)
        if 'model_state_dict' in state:
            model.load_state_dict(state["model_state_dict"], strict=False)
        elif 'state_dict' in state:
            model.load_state_dict(state['state_dict'], strict=False)
        else:
            model.load_state_dict(state, strict=False)
        model = model.to(device)
        norms = get_gradient_norms(model, valloader, device)
        results[name] = norms
        print(f'  {len(norms)} layers, mean grad norm = {np.mean(list(norms.values())):.6f}')
        del model
        torch.cuda.empty_cache()

    output_path = '/root/spectral_optim_vision_geometry/gradient_norm_analysis.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nSaved to {output_path}')

    # Ratio analysis
    print('\n=== Per-layer Gradient Norm Ratio Analysis ===')
    for norm_type in ['bn', 'ln']:
        adamw_key = f'adamw_r50_{norm_type}'
        sgd_key = f'sgd_r50_{norm_type}'
        if adamw_key not in results:
            continue
        print(f'\n--- {norm_type.upper()} ---')
        for opt in ['muon', 'soap', 'shampoo', 'sgd']:
            opt_key = f'{opt}_r50_{norm_type}'
            if opt_key not in results or opt_key == adamw_key:
                continue
            ratios = []
            layer_names = []
            for layer in results[adamw_key]:
                if layer in results[opt_key] and results[adamw_key][layer] > 1e-10:
                    ratio = results[opt_key][layer] / results[adamw_key][layer]
                    ratios.append(ratio)
                    layer_names.append(layer)
            if ratios:
                n = len(ratios)
                early = ratios[:n//3]
                mid = ratios[n//3:2*n//3]
                late = ratios[2*n//3:]
                print(f'  {opt}/adamw: mean={np.mean(ratios):.4f} std={np.std(ratios):.4f} | early={np.mean(early):.4f} mid={np.mean(mid):.4f} late={np.mean(late):.4f}')

    # Cross-norm comparison: how does the ratio change BN→LN?
    print('\n=== BN→LN Ratio Change (spectral benefit amplification) ===')
    for opt in ['muon', 'soap', 'shampoo']:
        bn_adamw = f'adamw_r50_bn'
        bn_opt = f'{opt}_r50_bn'
        ln_adamw = f'adamw_r50_ln'
        ln_opt = f'{opt}_r50_ln'
        if not all(k in results for k in [bn_adamw, bn_opt, ln_adamw, ln_opt]):
            print(f'  {opt}: missing checkpoints, skip')
            continue
        bn_ratios = []
        ln_ratios = []
        for layer in results[bn_adamw]:
            if layer in results[bn_opt] and results[bn_adamw][layer] > 1e-10:
                bn_ratios.append(results[bn_opt][layer] / results[bn_adamw][layer])
        for layer in results[ln_adamw]:
            if layer in results[ln_opt] and results[ln_adamw][layer] > 1e-10:
                ln_ratios.append(results[ln_opt][layer] / results[ln_adamw][layer])
        if bn_ratios and ln_ratios:
            print(f'  {opt}: BN ratio mean={np.mean(bn_ratios):.4f}, LN ratio mean={np.mean(ln_ratios):.4f}, amplification={np.mean(ln_ratios)/np.mean(bn_ratios):.4f}x')

    # Per-layer detail for muon (top-10 highest ratio layers)
    print('\n=== Top-10 layers by muon/adamw ratio (LN) ===')
    if 'muon_r50_ln' in results and 'adamw_r50_ln' in results:
        layer_ratios = []
        for layer in results['adamw_r50_ln']:
            if layer in results['muon_r50_ln'] and results['adamw_r50_ln'][layer] > 1e-10:
                r = results['muon_r50_ln'][layer] / results['adamw_r50_ln'][layer]
                layer_ratios.append((layer, r, results['muon_r50_ln'][layer], results['adamw_r50_ln'][layer]))
        layer_ratios.sort(key=lambda x: x[1], reverse=True)
        for layer, r, mn, an in layer_ratios[:10]:
            print(f'  {layer}: ratio={r:.4f} (muon={mn:.6f}, adamw={an:.6f})')
        print('  ...')
        print(f'  Bottom 3:')
        for layer, r, mn, an in layer_ratios[-3:]:
            print(f'  {layer}: ratio={r:.4f} (muon={mn:.6f}, adamw={an:.6f})')

if __name__ == '__main__':
    main()
