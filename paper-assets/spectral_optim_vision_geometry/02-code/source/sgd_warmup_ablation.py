#!/usr/bin/env python3
"""
SGD warmup ablation for ConvNeXt-T on CIFAR-100.
Tests whether linear warmup + cosine decay prevents SGD divergence.
W-EXP-5: Reviewer Q5 warmup ablation experiment.

Input: --warmup_epochs (0, 1, 2), --lr, --epochs, --seed, --gpu
Output: per-epoch train/val accuracy, final checkpoint
"""
import argparse, os, random, time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as T
import timm

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True

def main():
    p = argparse.ArgumentParser(description='SGD Warmup Ablation - ConvNeXt-T CIFAR-100')
    p.add_argument('--model', default='convnext_tiny')
    p.add_argument('--epochs', type=int, default=5)
    p.add_argument('--warmup-epochs', type=int, default=0,
                   help='Number of linear warmup epochs (0=no warmup)')
    p.add_argument('--lr', type=float, default=0.1)
    p.add_argument('--momentum', type=float, default=0.9)
    p.add_argument('--weight-decay', type=float, default=5e-4)
    p.add_argument('--batch-size', type=int, default=128)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--gpu', type=int, default=0)
    p.add_argument('--output-dir', default='/root/runs/spectral_optim_vision_geometry/')
    args = p.parse_args()

    set_seed(args.seed)
    device = torch.device(f'cuda:{args.gpu}')

    # CIFAR-100 resized to 224 for ConvNeXt (matches project baseline_train.py)
    norm = T.Normalize((0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761))
    train_tf = T.Compose([
        T.Resize(224), T.RandomHorizontalFlip(), T.ToTensor(), norm
    ])
    test_tf = T.Compose([T.Resize(224), T.ToTensor(), norm])

    train_ds = torchvision.datasets.CIFAR100(
        './data', train=True, download=True, transform=train_tf)
    test_ds = torchvision.datasets.CIFAR100(
        './data', train=False, download=True, transform=test_tf)
    train_dl = torch.utils.data.DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True,
        num_workers=4, pin_memory=True)
    test_dl = torch.utils.data.DataLoader(
        test_ds, batch_size=args.batch_size, shuffle=False,
        num_workers=4, pin_memory=True)

    model = timm.create_model(args.model, pretrained=False, num_classes=100)
    model = model.to(device)

    optimizer = optim.SGD(model.parameters(), lr=args.lr,
                          momentum=args.momentum,
                          weight_decay=args.weight_decay)

    # Linear warmup from lr*1e-4 to lr, then cosine decay
    we = args.warmup_epochs
    if we > 0 and we < args.epochs:
        warmup_s = optim.lr_scheduler.LinearLR(
            optimizer, start_factor=1e-4, total_iters=we)
        cosine_s = optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=args.epochs - we)
        scheduler = optim.lr_scheduler.SequentialLR(
            optimizer, [warmup_s, cosine_s], milestones=[we])
    else:
        scheduler = optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=args.epochs)

    criterion = nn.CrossEntropyLoss()
    best_vacc = 0

    for epoch in range(args.epochs):
        model.train()
        tloss, tcorr, ttot = 0.0, 0, 0
        for x, y in train_dl:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            out = model(x)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            tloss += loss.item() * y.size(0)
            tcorr += out.argmax(1).eq(y).sum().item()
            ttot += y.size(0)

        model.eval()
        vcorr, vtot = 0, 0
        with torch.no_grad():
            for x, y in test_dl:
                x, y = x.to(device), y.to(device)
                out = model(x)
                vcorr += out.argmax(1).eq(y).sum().item()
                vtot += y.size(0)

        scheduler.step()
        tacc = 100.0 * tcorr / ttot
        vacc = 100.0 * vcorr / vtot
        best_vacc = max(best_vacc, vacc)
        lr_now = optimizer.param_groups[0]['lr']
        print(f'Epoch {epoch+1}/{args.epochs} | '
              f'LR: {lr_now:.6f} | '
              f'Train: {tacc:.2f}% ({tloss/ttot:.4f}) | '
              f'Val: {vacc:.2f}%')

    print(f'BEST_VAL_ACC={best_vacc:.2f}')
    print(f'FINAL_VAL_ACC={vacc:.2f}')

    os.makedirs(args.output_dir, exist_ok=True)
    tag = f'sgd_warmup{we}ep_{args.model}_c100_seed{args.seed}'
    ckpt = os.path.join(args.output_dir, f'{tag}.pt')
    torch.save({
        'state_dict': model.state_dict(),
        'best_val_acc': best_vacc,
        'final_val_acc': vacc,
        'args': vars(args)
    }, ckpt)
    print(f'Checkpoint: {ckpt}')

if __name__ == '__main__':
    main()
