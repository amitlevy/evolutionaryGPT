# Evolutionary GPT: Expert-Level Performance on Tasks with Environmental Feedback

There have recently been a slew of papers achieving expert-level performance on different tasks, including [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5) from DeepMind, [Eureka](https://arxiv.org/abs/2310.12931), and [Hypothesis Refinement](https://openreview.net/pdf?id=bNt7oajl2a).
They all use the same idea: some variant of evolutionary search, and reward reflection.

**Evolutionary Search:** sampling N independent sample solutions for the task from an LLM, evaluating them all in the "environment" for the task, picking the best one, and generating N variations of it, repeating that for T iterations.

**Reward Reflection:** giving the model some sort of feedback on why the current best solution failed to get zero loss on the task. For instance, if you wanted to generate a maximally efficient algorithm for a problem, the feedback could be the output of a profiler.

The repositories that currently exist have all been engineered to solve a very specific task, or are unnecessarily complex, so I've decided to create evolutionaryGPT as a simple and generic version of this method that can be easily modified to work for any task.

## Demo Task
The current demo task (seen below) is taken from the Hypothesis Refinement paper, another simple example is solving a LeetCode problem with the test cases as the feedback mechanism.


```
Find the rule mapping X to Y in the following examples and express it as a Python function:

[97, 97, 97, 97] -> [97, 97, 97]

[4, 4, 4] -> [4, 4]

[33, 0, 4, 1, 2, 24, 66] -> []

[76, 42, 17, 76, 17] -> [76, 17]

...
```


It is consistently solved by evolutionaryGPT with T=3 and N=5 (the hyperparameters used in the paper).
More difficult tasks should use higher T, N, for instance, Eureka used T=5 and N=16.

## Running the demo

1. Git clone the repository

2. Install the requirements
```
pip3 install -r requirements.txt
```
The python version I tested it on is 3.10.

3. Export your API key as an environment variable
```
export OPENAI_API_KEY='yourkey'
```

4. Run the command (**Careful**! It'll run **exec()** on GPT-4 generated code, and cost about 10 cents)
```
python3 main.py
```

## Changing the task
I believe the code is relatively well organized and commented. To change the task you need to modify evaluate.py and system_prompt.txt. To change the hyperparameters look inside config.yaml.

## 🛡 Disclaimer
This project, evolutionaryGPT, is an experimental application and is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise.
