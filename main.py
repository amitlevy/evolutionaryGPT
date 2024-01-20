import logging
import yaml
from tqdm import tqdm
from evaluate import evaluate, reflect, gen_sample, get_initial_context

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

if __name__ == "__main__":
    with open("config.yaml",'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    
    T = cfg['iterations']
    N = cfg['samples']

    best_loss = float('inf')
    best_sol = None

    # the initial context is just the list of examples
    context = get_initial_context()
    
    for i in range(T):
        for j in tqdm(range(N)):
            sample_code = gen_sample(context, temperature=cfg['temperature'], model_name=cfg['model_name'])
            loss = evaluate(sample_code)

            if loss <= best_loss:
                best_sol = sample_code
                best_loss = loss
        
        # pick the best sample of the previous iteration to evolve in the next
        context += reflect(best_sol)
        logging.info(f"Finished iteration {i}, current loss is {best_loss} for:\n\n{best_sol}\n")
        if best_loss == 0:
            break
            

