my best complete final answer to the task.

The pre-training hyper-parameters for different variants of OpenELM are given in Tab. 9.
We finetune all the models with BFloat16 as a data type. We use activation checkpointing along with gradient accu-
mulation with a step size of two. We use the AdamW op-timizer with default beta values. We use the cosine learn-ing rate scheduler with a warm-up ratio of 0.1, and we set the weight decay to 0 and loss temperature beta to 0.01.
We set the maximum context length to 1024 and maximum prompt length to 512. Other hyper-parameters are included in Tab. 10.270M 450M 1.1B 3B
Batch size 8
Training epochs 5 8 5 10
Learning rate 2e-5 3e-5 5e-5 1e-4
Loss function hinge hinge sigmoid hinge
DeepSpeed Zero3 [38] ✗ ✓ ✓ ✓
GPUs 8
GPU Type A100 A100 A100 A100
GPU Memory 40 GB 40 GB 40 GB 80 GB