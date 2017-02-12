import kimports
from kimports import *

def get_paths(base_path):
    """get_paths returns the train_path, valid_path, and test_path give a base path"""
    train_path = base_path + '/train'
    valid_path = base_path + '/valid'
    test_path = base_path + '/test'
    resource_path = base_path + '/resources'

    return train_path, valid_path, test_path, resource_path

def plot_images(imgs, figsize=(12,6), per_row=4, titles=None):
    if type(imgs[0]) is np.ndarray:
        imgs = np.array(imgs).astype(np.uint8)
        if (imgs.shape[-1] != 3):
            imgs = imgs.transpose((0,2,3,1))
    num_rows = math.ceil(len(imgs) / float(per_row))
    fig = plt.figure(figsize=figsize)
    for i, img in enumerate(imgs):
        sp = fig.add_subplot(num_rows, per_row, i+1)
        if titles != None:
            sp.set_title(titles[i], fontsize=18)
        plt.imshow(img)

def onehot(batches):
    num_classes = len(batches.class_indices)
    return np.equal(batches.classes, np.matrix(np.arange(num_classes)).T).T.astype(int)

def onehot(batches):
    num_classes = len(batches.class_indices)
    return np.equal(batches.classes, np.matrix(np.arange(num_classes)).T).T.astype(int)
def multiclass_logloss_rowscaled(batches, preds):
    preds = np.clip(preds, 0.0001, 0.9999)
    sums = np.matrix(np.sum(preds, axis=1)).T
    preds = np.divide(preds, sums)
    oh = onehot(batches)
    return (-1.0/batches.N) * np.sum(np.multiply(oh, np.log(preds)))
