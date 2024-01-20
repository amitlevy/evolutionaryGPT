# EvolGPT: Expert-Level Performance on Tasks with Fast Feedback

There has recently been a slew of papers achieving expert level performance on different tasks using an LLM:
* AlphaGeometry by DeepMind
* Eureka: Human-Level Reward Design
* Phenomenal Yet Puzzling: Testing Inductive Reasoning
And many others. 

In my opinion, it should be emphasized that they all use the same core idea: evolutionary search, and reward reflection.

**Evol**utionary search: sampling N indepdent sample solutions for the task from an LLM, evaluating them all in the "environment" for the task, picking the best one, and generating N variations of it, repeating that for some amount T iterations.

Reward Reflection: giving the model some sort of feedback on why the current best solution failed to get zero loss on the task. For instance, if you wanted to generate a maximally efficient algorithm for a problem, the feedback could be the output of a profiler. The loss could be the runtime, or failed test cases if there are any.

The repositories I saw so far have (in my opinion) all been engineered to solve a very specific task and difficult to extend, or unnecessarily complex, so I've decided to create EvolGPT as a simple and generic version of this method. The current demo task is taken from the Inductive Reasoning paper:

> Find the rule mapping X -> Y in the following examples and express it as a Python function:
[97, 97, 97, 97] -> [97, 97, 97]
[4, 4, 4] -> [4, 4]
[33, 0, 4, 1, 2, 24, 66] -> []
[76, 42, 17, 76, 17] -> [76, 17]

And I've verified it can indeed be solved consistantly with T=3 and N=5 (the hyperparameters used in the paper).
More difficult tasks should use higher T,N, for instance Eureka used T=5 and N=16.

## Usage:

1. Git clone the repository

2. Install the requirements:
```
pip3 install -r requirements.txt
```
The python version I tested it on is 3.10.

3. Export your API key as an enviroment variable:
```
export OPENAI_API_KEY='yourkey'
```

5. Run the command (**Careful**! It'll run exec() on GPT-4 generated code, and cost about 10 cents):
```
python3 main.py
```

## 🛡 Disclaimer

Disclaimer
This project, EvolGPT, is an experimental application and is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise.
