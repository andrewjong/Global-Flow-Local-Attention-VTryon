import time
from tqdm import tqdm
from options.train_options import TrainOptions
import data as Dataset
from model import create_model
from util.visualizer import Visualizer


if __name__ == '__main__':
    # get training options
    opt = TrainOptions().parse()
    opt.serial_batches = True
    opt.nThreads = 0
    # create a dataset
    dataset = Dataset.create_dataloader(opt)
    dataset_size = len(dataset) * opt.batchSize
    print('training images = %d' % dataset_size)

    for epoch in range(10):
        print("epoch", epoch)
        for i, data in tqdm(enumerate(dataset), total=len(dataset)):
            pass

