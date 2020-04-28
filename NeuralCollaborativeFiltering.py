"""
    It needs Python 3.6+

"""
import pickle
import torch
import pandas as pd
from fastai.collab import CollabDataBunch, collab_learner


if __name__ == "__main__":

    print("Loading data ...")
    ratings_df = pd.read_csv('ratings.csv')
    min_range = 0
    max_range = max(ratings_df['rating']) + 1

    data = CollabDataBunch.from_df(ratings_df, valid_pct=0.1)
    algo = collab_learner(data, n_factors=100, y_range=(min_range, max_range), wd=0.1)

    #algo.lr_find()
    #algo.recorder.plot(skip_end = 15)

    print("Training model ...")
    algo.fit_one_cycle(5, 0.01)

    print("Making predictions ...")
    user = [534, 1274, 210]
    item = [551, 405, 869]

    tensor_user = torch.LongTensor(user)
    tensor_item = torch.LongTensor(item)

    preds = algo.model(tensor_user, tensor_item).tolist()
    print(preds)

    model_filename = "ncf.model"
    algo.export(model_filename)

    




