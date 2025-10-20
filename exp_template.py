from core.experiment import Experiment
from typing import Dict, Any

class MyExperiment(Experiment):
    def __init__(self):
        hyperparams = {
            #variable : (start, stop, step_size)
            
        }

        super().__init__(hyperparams,
                         csv_name="output.csv")
    

    def process_trial(self, data : Dict[str:Any]) -> Dict[str:Any]:
        # your defined function here
        # e.g. compute f(x, y, z)
        pass
    
    def graph_result(self, data : Dict[str:Any], save_path : str) -> None:
        # your defined graph function here
        pass


def main():
    new_exp = MyExperiment() 
    new_exp.doExperiment()
            
if __name__ == "__main__":
    main()