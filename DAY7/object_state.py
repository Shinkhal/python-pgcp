import pickle


class ExperimentSnapshot:

    def __init__(self,experiment_id,model_type,hyperparameters,metrics,timestamp):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        return self.metrics[metric_name]


def save_experiment(snapshot, file_path):

    with open(file_path, "wb") as file:
        pickle.dump(snapshot, file)


def load_experiment(file_path):

    with open(file_path, "rb") as file:
        return pickle.load(file)
